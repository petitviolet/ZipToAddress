# -*- encoding:utf-8 -*-
'''
# Reference
https://github.com/italomaia/flask-empty/blob/master/examples/blog_example/main.py
'''
from flask import Flask
# from flask import render_template


def config_str_to_obj(cfg):
    if isinstance(cfg, str):
        module = __import__('config', fromlist=[cfg])
        return getattr(module, cfg)
    return cfg


def app_factory(config, app_name, blueprints=None):
    ''' app configuration
    '''
    configure_logger()
    app = Flask(app_name)

    config = config_str_to_obj(config)
    configure_app(app, config)
    configure_blueprints(app, blueprints or config.BLUEPRINTS)
    configure_error_handlers(app)

    return app


def configure_app(app, config):
    ''' load and apply configuration written in config.py
    '''
    app.config.from_object(config)
    app.config.from_envvar("APP_CONFIG", silent=True)


def __import_variable(blueprint_path, module, variable_name):
    path = '.'.join(blueprint_path.split('.') + [module])
    mod = __import__(path, fromlist=[variable_name])
    return getattr(mod, variable_name)


def configure_blueprints(app, blueprints):
    ''' '''
    for blueprint_config in blueprints:
        blueprint = None
        kw = {}

        if (isinstance(blueprint_config, str)):
            blueprint = blueprint_config
        elif (isinstance(blueprint_config, dict)):
            blueprint = blueprint_config[0]
            kw = blueprint_config[1]

        blueprint = __import_variable(blueprint, 'apis', 'blueprint')
        app.register_blueprint(blueprint, **kw)

def configure_logger():
    from logger import logging
    # logger = logging.getLogger(app_name)
    # app.logger = logger

def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        pass
        # return render_template("access_forbidden.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        pass
        # return render_template("page_not_found.html"), 404

    @app.errorhandler(405)
    def method_not_allowed_page(error):
        pass
        # return render_template("method_not_allowed.html"), 405

    @app.errorhandler(500)
    def server_error_page(error):
        pass
        # return render_template("server_error.html"), 500
