from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .hero import Hero
from .power import Power
from .hero_power import HeroPower
