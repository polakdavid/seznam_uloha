import os
import requests
from .models import Videos


def sync_data():
    """
    Function for update local database.
    """
    # Parameter SYNC_URL stored in environment list
    response = requests.get(os.environ["SYNC_URL"])

    if response.status_code != 200:
        # This part need to handle properly in robust project...
        print("___________ SYNC FAILED ___________")
    else:
        json_response = response.json()

        # At this need to handle data changes but this not a scope of project...
        # Update existing row, Delete not existed movies and Create new record if there is a new video
        for item in json_response:
            # Filtering data if it exists in DB
            check_video = Videos.objects.filter(name=item["name"], source=item["source"])

            if not check_video.exists():
                new_row = Videos()
                for k, v in item.items():
                    setattr(new_row, k, v)
                new_row.save()
        print("___________ SYNC SUCCESS ___________")




