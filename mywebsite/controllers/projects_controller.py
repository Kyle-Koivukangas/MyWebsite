import pyramid_handlers

from mywebsite.controllers.base_controller import BaseController


class ProjectsController(BaseController):

    @pyramid_handlers.action(renderer='templates/projects/index.pt')
    def index(self):
        return {'value': 'PROJECTS/INDEX'}