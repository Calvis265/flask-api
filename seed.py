from models import db
from models.hero import Hero
from models.power import Power
from models.hero_power import HeroPower
from app import app   

with app.app_context():
    db.drop_all()
    db.create_all()

    
    hero1 = Hero(name='calvi onyango', super_name='legend')
    power1 = Power(name='Stealth', description='Can move without being seen.')
    hero_power1 = HeroPower(strength='Strong', hero=hero1, power=power1)

    db.session.add_all([hero1, power1, hero_power1])
    db.session.commit()
