from django.apps import AppConfig
import sys
from dotenv import load_dotenv

class VideoshareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videoshare'

    def ready(self):
        """
        Override function what is run after init part for scripting
        """
        # Load .env file for own init files
        load_dotenv()
        # Run synchronization after init server and update local database
        if sys.argv[1] == 'runserver':
            from .loaddb import sync_data
            sync_data()

