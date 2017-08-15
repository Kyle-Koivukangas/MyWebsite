import pyramid_handlers
import json


from mywebsite.controllers.base_controller import BaseController


class ProjectsController(BaseController):

    @pyramid_handlers.action(renderer='templates/projects/index.pt')
    def index(self):
        return {'value': 'PROJECTS/INDEX'}

    @pyramid_handlers.action(renderer='json')
    def projectsJSON(self):
        """serves JSON file for the projects page, this file will contain the HTML for each project which will be inserted in to
        the page via javascript"""
        response_data = {}

        # the following will need to be tweaked, I need to first write a script that pulls the HTML from the project templates 
        # and packs it in to a properly formatted JSON file rather than doing that in the controller.
        with open('mywebsite/templates/projects.json', 'r') as f:
            projects = [line.rstrip('\n') for line in f]
            try:
                response_data['result'] = 'success'
                response_data['message'] = ''.join(projects)
            except:
                response_data['result'] = 'oops!'
                response_data['message'] = 'error reading file'
                
        return json.dumps(response_data, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


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

