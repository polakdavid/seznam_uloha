import requests
from .models import Videos 

def sync_data():
    sync_url = "https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json"
    
    response = requests.get(sync_url)
    
    if response.status_code != 200:
        # This part need to handle properly in robust project... 
        print("___________ SYNC FAILED ___________")
    else:
        json_response = response.json()

        for item in json_response:
            check_video = Videos.objects.filter(name=item["name"], source=item["source"])

            if not check_video.exists():
                new_row = Videos()
                for k, v in item.items():
                    setattr(new_row, k, v)
                    print(k)
                print(new_row)
                #video.save()

                #new_row = Videos.objects.create(item)
                #new_row.save()
                #print(new_row)


            print(check_video)
            break

        print("___________ SYNC SUCCESS ___________")



        
