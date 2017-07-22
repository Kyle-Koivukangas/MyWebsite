from mywebsite.viewmodels.base_viewmodel import BaseViewModel


class LoginViewModel(BaseViewModel):
    def __init__(self):
        self.email = None
        self.password = None
        self.error = None

    def from_dict(self, data_dict):
        self.email = data_dict.get('email')
        self.password = data_dict.get('password')
        self.confirm_password = data_dict.get('confirm_password')

    def validate(self):
        self.error = None

        if not self.password:
            self.error = "You must input your password"
            return

        if not self.email:
            self.error = "You must input your email address"
            return

        # if self.password != loginDB[self.email[password]]:
        #     self.error = "incorrect email address or password"
        #     return
