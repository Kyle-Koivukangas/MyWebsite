from pyramid.config import Configurator
import os

import mywebsite
import mywebsite.controllers.home_controller as home
import mywebsite.controllers.account_controller as account
import mywebsite.controllers.projects_controller as projects
import mywebsite.controllers.blog_controller as blog
import mywebsite.controllers.admin_controller as admin
from mywebsite.data.dbsession import DbSessionFactory
import mywebsite.startup_scripts.projects_json_builder as projects_json_builder


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    run_startup_scripts()

    init_includes(config)  
    init_routing(config)
    init_db(config)

    config.scan()
    return config.make_wsgi_app()

def init_db(config):
    top_folder = os.path.dirname(mywebsite.__file__)
    rel_folder = os.path.join('db', 'mywebsite.sqlite')

    db_file = os.path.join(top_folder, rel_folder)
    DbSessionFactory.global_init(db_file)

def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_handler('root', '/', handler=home.HomeController, action='index')

    add_controller_routes(config, home.HomeController, 'home')
    add_controller_routes(config, account.AccountController, 'account')
    add_controller_routes(config, projects.ProjectsController, 'projects')
    add_controller_routes(config, blog.BlogController, 'blog')
    add_controller_routes(config, admin.AdminController, 'admin')

def add_controller_routes(config, ctrl, prefix):
    config.add_handler(prefix + "ctrl_index", '/' + prefix, handler=ctrl, action='index')
    config.add_handler(prefix + "ctrl_index/", '/' + prefix + '/', handler=ctrl, action='index')
    config.add_handler(prefix + "ctrl", '/' + prefix + "/{action}", handler=ctrl)
    config.add_handler(prefix + "ctrl/", '/' + prefix + "/{action}/", handler=ctrl)
    config.add_handler(prefix + "ctrl_id", '/' + prefix + "/{action}/{id}", handler=ctrl)
    


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')

def run_startup_scripts():
    projects_json_builder.build_projects_json()
