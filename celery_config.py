from celery import Celery
from celery.schedules import crontab
from models.product import Product
from db import session
import pytest
celery_app = Celery('product', broker="redis://redis:6379/0")

celery_app.conf.beat_schedule = {
    "change attribute every 12 hour": {
        "task": "celery_config.update_status",
        "schedule": crontab(hour="*/12")
    },
}

@celery_app.task
def update_status():
    session.query(Product).filter(Product.status == "pending").update({"status": "confirm"})
    session.commit()

@celery_app.task 
def run_tests():
    pytest.main(['-v', 'tests'])