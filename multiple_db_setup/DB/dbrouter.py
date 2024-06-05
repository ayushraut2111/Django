from django.apps import apps
from django.conf import settings


class TestRouter:

    appointment_db = settings.APPOINTMENT_DB

    def db_for_read(self, model, **hints):
        if hasattr(model, "db_name"):
            model_name = getattr(model, "db_name")
            return model_name
        else:
            return "default"

    def db_for_write(self, model, **hints):
        if hasattr(model, "db_name"):
            model_name = getattr(model, "db_name")
            return model_name
        else:
            return "default"

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name is None:
            return False
        
        model = apps.get_registered_model(app_label, model_name)
        if hasattr(model, "db_name"):
            model_name = getattr(model, "db_name")
            return db == model_name
        else:
            return db == "default"
