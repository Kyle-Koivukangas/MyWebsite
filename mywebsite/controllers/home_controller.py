import pyramid_handlers

from mywebsite.controllers.base_controller import BaseController

class HomeController(BaseController):

    @pyramid_handlers.action(renderer='templates/home/index.pt')
    def index(self):
        return {'value': 'HOME'}

    @pyramid_handlers.action(renderer='templates/home/about.pt')    
    def about(self):
        return {'value': 'ABOUT'}

    @pyramid_handlers.action(renderer='templates/home/contact.pt')
    def contact(self):
        return {'value': 'CONTACT'}
