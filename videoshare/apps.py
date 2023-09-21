from django.apps import AppConfig

class VideoshareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videoshare'

    def ready(self):
        from .loaddb import sync_data
        sync_data()

