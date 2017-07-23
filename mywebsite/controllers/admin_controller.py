import pyramid_handlers
from mywebsite.controllers.base_controller import BaseController
from mywebsite.viewmodels.register_viewmodel import RegisterViewModel
from mywebsite.services.account_service import AccountService


class AdminController(BaseController):

    @pyramid_handlers.action(renderer="templates/admin/accounts.pt")
    def accounts(self):
        all_accounts = AccountService.get_accounts()

        return {'accounts': all_accounts}


    # GET /admin/new_album
    @pyramid_handlers.action(renderer='templates/admin/new_account.pt',
                             request_method='GET',
                             name='new_account')
    def new_account_get(self):
        vm = RegisterViewModel()
        print(vm)
        return vm.to_dict()

    # POST /account/register
    @pyramid_handlers.action(renderer='templates/admin/new_account.pt',
                             request_method='POST',
                             name='new_account')
    def new_account_post(self):
        vm = RegisterViewModel()
        vm.from_dict(self.request.POST)

        # if not vm.validate():
        #     return vm.to_dict()

        
        new_account = AccountService.create_account(email=vm.email, password=vm.password, superuser=vm.superuser)
        # log new album
        print("Created a new account with email {}".format(new_account.email))

        # redirect
        self.redirect('/admin/accounts')
