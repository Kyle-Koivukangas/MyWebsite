"""
This script is meant to be run at server startup, it will pull the HTML from each project template on the projects page and save it as a JSON file that is
meant to be called via AJAX request so that the projects page can be interactive and loaded in the background.

This script should be placed in mywebsite/startup_scripts folder
"""

from bs4 import BeautifulSoup
import json
import os

def build_projects_json():
    builder = Builder()
    builder.make_json()


class Builder():
    def __init__(self):
        self.projects_html = {}
        self.projects_folder = "{}\\mywebsite\\templates\\projects".format(os.getcwd())
        self.projects_json = "{}\\projects.json".format(self.projects_folder)

        #get list of template file paths

    def parse_templates(self):
        "parses project_name.pt file for the main content for each project template and saves them to a dictionary"
        project_template_paths = []
        for folder, subs, files in os.walk(self.projects_folder):
            for filename in files:
                if filename.endswith('.pt'):
                    project_template_paths.append(os.path.abspath(os.path.join(folder, filename)))

        #extract the projects-content div and save to dictionary
        for file in project_template_paths:
            with open(file) as template:
                soup = BeautifulSoup(template, "html.parser")
                template_name = os.path.splitext(os.path.basename(file))[0]
                html = soup.find(id="projects-content")
                self.projects_html[template_name] = str(html)

    def make_json(self):
        self.parse_templates()
        json_data = json.dumps(self.projects_html, default=lambda o: o.__dict__, sort_keys=True, indent=4)

        with open(self.projects_json, 'w') as outfile:
            json.dump(json_data, outfile)
        
        print("\nProjects JSON created successfully\n")


if __name__ == '__main__':
    build_projects_json()
