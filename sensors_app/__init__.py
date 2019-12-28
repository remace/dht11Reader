#! /usr/bin/env python
from flask import Flask

from . import models
from .views import app


models.db.init_app(app)
