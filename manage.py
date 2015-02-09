# -*- encoding:utf-8 -*-

from flask.ext import script
import commands

if __name__ == "__main__":
    from main import app_factory
    # from zip_address import app
    import config
    manager = script.Manager(app_factory)
    manager.add_option("-n", "--name", dest="app_name",
                       required=False, default=config.project_name)
    manager.add_option("-c", "--config", dest="config",
                       required=False, default=config.Dev)
    manager.add_command("test", commands.Test())
    manager.add_command("test_travis", commands.TestTravis())
    manager.add_command("create_db", commands.CreateDB())
    manager.add_command("drop_db", commands.DropDB())
    manager.add_command("gunicorn", commands.GunicornServer())
    manager.run()
