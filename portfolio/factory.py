# -*- coding: utf-8 -*-

from flask import Flask

from . import db
from . import register_blueprints
from .core import lm


def create_app(package_name, package_path, settings_override=None):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the Overholt platform.

    :param package_name: application package name
    :param package_path: application package path
    :param settings_override: a dictionary of settings to override
    """
    app = Flask(package_name, instance_relative_config=True)

    app.config.from_object('portfolio.settings')
    app.config.from_pyfile(app.root_path + '/settings.cfg', silent=True)
    app.config.from_object(settings_override)

    db.init_app(app)

    lm.init_app(app)

    register_blueprints(app, package_name, package_path)

    return app



