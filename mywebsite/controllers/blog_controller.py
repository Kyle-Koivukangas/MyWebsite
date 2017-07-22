import pyramid_handlers

from mywebsite.controllers.base_controller import BaseController


class BlogController(BaseController):

    @pyramid_handlers.action(renderer='templates/blog/index.pt')
    def index(self):
        return {'value': 'BLOG/INDEX'}