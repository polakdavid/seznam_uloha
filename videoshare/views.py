from requests import get
import os
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from .models import Videos
from .filters import Filters


def home(request):
    """
    Function responsible for render main web page and visualize list of movies
    """
    order_btn = {}

    # Make request to main source if response status is other than 200 use local database
    response = get(os.environ["SYNC_URL"])

    # Create context dictionary for represent data
    # I choose this method because main data source is from SYNC_URL it needs fewer data parse to get result
    raw_data = Filters()

    if response.status_code == 200:
        raw_data.append_list_items(response.json())
    else:
        raw_data.convert_queryset_dictlist(Videos.objects.all())

    # Handle the list ordering this is fixed on "name" column
    if 'order-btn' in request.POST:
        if request.POST['order-btn'] == 'False':
            order_btn['text'] = "Order: Z-A"
            order_btn['value'] = "True"
            raw_data.order_desc()
        else:
            order_btn['text'] = "Order: A-Z"
            order_btn['value'] = "False"
            raw_data.order_asc()

    # After init set default status for ordering
    if "value" not in order_btn:
        order_btn.update({"text": "Order: A-Z",
                          "value": False})
        raw_data.order_asc()

    # filter by name or source. Filtering is case-sensitive
    if 'select' in request.GET and 'filter_input' in request.GET:
        filter_text = request.GET['filter_input']
        filter_key = request.GET['select']
        context = raw_data.filter_by_key(filter_text, filter_key)
    else:
        context = raw_data.to_list()

    return render(request, 'home.html', {"context": context, "order": order_btn})

def videoplayer(request):
    """
    Function for render video player site if data id exists else redirect back to home page
    """
    if 'video' not in request.GET:
        return redirect('home')

    # Get Id for database searching
    video_id = request.GET['video']
    try:
        video = model_to_dict(Videos.objects.get(pk=video_id))
    except:
        return redirect('home')

    return render(request, 'videoplayer.html', {"movie": video})

