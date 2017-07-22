import pyramid_handlers

from mywebsite.controllers.base_controller import BaseController
from mywebsite.viewmodels.register_viewmodel import RegisterViewModel


class AccountController(BaseController):
    @pyramid_handlers.action(renderer="templates/account/index.pt")
    def index(self):
        return {'value': 'ACCOUNT'}

    @pyramid_handlers.action(renderer="templates/account/signin.pt")
    def signin(self):
        return {'value': 'SIGNIN'}

    # GET /ACCOUNT/REGISTER
    @pyramid_handlers.action(renderer="templates/account/register.pt",
                            request_method='GET',
                            name='register')
    def register_get(self):
        print("Calling register via GET...")

        vm = RegisterViewModel()
        return vm.to_dict()

    # POST /ACCOUNT/REGISTER
    @pyramid_handlers.action(renderer="templates/account/register.pt",
                            request_method='POST',
                            name='register')
    def register_post(self):
        vm = RegisterViewModel()
        vm.from_dict(self.request.POST)

        print("Calling register via POST... email: {}, Password: {}, Confirm: {}".format(vm.email, vm.password, vm.confirm_password))
        
        vm.validate()
        if vm.error:
            vm.password = None
            vm.confirm_password = None
            return vm.to_dict()


        print('Redirecting..')
        self.redirect('/account')
        
        return {'value': 'REGISTER'}