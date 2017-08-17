import pyramid_handlers
import json


from mywebsite.controllers.base_controller import BaseController


class ProjectsController(BaseController):

    @pyramid_handlers.action(renderer='templates/projects/index.pt')
    def index(self):
        return {'value': 'PROJECTS'}

    @pyramid_handlers.action(renderer='json')
    def projectsjson(self):
        """serves JSON file for the projects page, this file will contain the HTML for each project which will be inserted in to
        the page via javascript"""
        response_data = {}

        with open('mywebsite/templates/projects/projects.json', 'r') as f:
            projects = json.load(f)
            try:
                response_data['result'] = 'success'
                response_data['message'] = projects
            except:
                response_data['result'] = 'oops!'
                response_data['message'] = 'error reading file'
        
        return json.dumps(response_data, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
