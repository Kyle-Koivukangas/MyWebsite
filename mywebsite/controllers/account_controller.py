import pyramid_handlers
from mywebsite.controllers.base_controller import BaseController
from mywebsite.viewmodels.register_viewmodel import RegisterViewModel
from mywebsite.viewmodels.login_viewmodel import LoginViewModel
from mywebsite.services.account_service import AccountService
import mywebsite.infrastructure.cookie_auth as cookie_auth

class AccountController(BaseController):
    @pyramid_handlers.action(renderer="templates/account/index.pt")
    def index(self):
        user_id = self.logged_in_user_id
        if not user_id:
            print("Cannot view account page, must login (allow cookies as well)")
            self.redirect("/account/login")
        account = AccountService.find_account_by_id(user_id)
        account = {'email': account.email, 'created': account.created, 'id': account.id, 'is_super_user': account.is_super_user, 'email_confirmed': account.email_confirmed}
        return account

    @pyramid_handlers.action(renderer="templates/account/signin.pt")
    def login_get(self):
        return {'value': 'SIGNIN'}

    # GET /ACCOUNT/REGISTER
    @pyramid_handlers.action(renderer="templates/account/register.pt", request_method='GET', name='register')
    def register_get(self):
        print("Calling register via GET...")

        vm = RegisterViewModel()
        return vm.to_dict()

    # POST /ACCOUNT/REGISTER
    @pyramid_handlers.action(renderer="templates/account/register.pt", request_method='POST', name='register')
    def register_post(self):
        vm = RegisterViewModel()
        vm.from_dict(self.request.POST)

        print("Calling register via POST... email: {}, Password: {}, Confirm: {}".format(vm.email, vm.password, vm.confirm_password))
        
        vm.validate()
        if vm.error:
            vm.password = None
            vm.confirm_password = None
            return vm.to_dict()

        account = AccountService.find_account_by_email(vm.email)
        if account:
            vm.error = "An account with this email already exists. Please log in instead."
            return vm.to_dict()

        account = AccountService.create_account(vm.email, vm.password)
        print("Registered new user: " + account.email)

        print('Redirecting to account page...')
        self.redirect('/account')
        
        return {'value': 'REGISTER'}

    
    @pyramid_handlers.action(renderer="templates/account/login.pt", request_method='GET', name='login')
    def login_get(self):
        vm = LoginViewModel()
        return vm.to_dict()

    @pyramid_handlers.action(renderer="templates/account/login.pt", request_method='POST', name='login')
    def login_post(self):
        vm = LoginViewModel()
        vm.from_dict(self.request.POST)

        print("Calling Login view POST.. {} {}".format(vm.email, vm.password))

        account = AccountService.get_authenticated_account(vm.email, vm.password)
        if not account:
            vm.error = "Email address or password are incorrect."
            return vm.to_dict()

        cookie_auth.set_auth(self.request, account.id)

        print('Login success, Redirecting..')
        self.redirect('/account/index')

        return {'value': "LOGGED_IN"}

    @pyramid_handlers.action(renderer="templates/account/logout.pt")
    def logout(self):
        cookie_auth.logout(self.request)
        
        self.redirect("/home/index")
        return {}