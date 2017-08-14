import pyramid_handlers
import json


from mywebsite.controllers.base_controller import BaseController


class ProjectsController(BaseController):

    @pyramid_handlers.action(renderer='templates/projects/index.pt')
    def index(self):
        return {'value': 'PROJECTS/INDEX'}

    @pyramid_handlers.action(renderer='json')
    def pokerbot(self):
        response_data = {}

        with open('mywebsite/templates/projects/pokerbot.html', 'r') as f:
            pokerbot = [line.rstrip('\n') for line in f]
            try:
                response_data['result'] = 'success'
                response_data['message'] = ''.join(pokerbot)
            except:
                response_data['result'] = 'oops!'
                response_data['message'] = 'error reading file'
                
        return json.dumps(response_data, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
