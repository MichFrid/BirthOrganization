from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from datetime import date
import json

#from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

@require_http_methods(['POST', 'GET'])
def serve_home(request):
    x = 50
    #import IPython
    #IPython.embed()
    print("hi")
    return HttpResponse("<h1>Hello World,br/> world</h1>")


def serve_html(request):
    #print(request.GET)
    x = request.GET.get("name", "no name found")
    my_dict = {"age":30, "city":"Jerusalem"}
    return render(request=request, template_name="homepage.html",
                  context={'x':x,
                  'dict': my_dict,
                   'list': list(range(100))})

def ex2(request):
    return render(request=request,
                  template_name="show_params.html",
                  context={
                      'dict': request.GET,
                  })

def today_date(request):
    d = date.today()
    current_date = f"{d.day}-{d.month}-{d.year}"
    return render(request=request,
                  template_name="homepage.html",
                  context={
                      'current_date': current_date,
                  })

# def today_coins(request):
#     res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#     if response.status_code == 200:
#         # data = response.json()
#         # current_price = data['bpi']['USD']['rate']
#         res =
#         return render(request, 'homepage.html', {'current_price': current_price})
#     else:
#         # Handle error if API request fails
#         error_message = 'Failed to retrieve coin data'
#         return render(request, 'error.html', {'error_message': error_message})

def hello_view(request):
    return HttpResponse("Hello from Django")

def bye_view(request):
    if request.method == 'POST':
        return HttpResponse("This is a POST response")
    else:
        return HttpResponse("Method not allowed")

# url = 'http://localhost/bye'
# response = requests.post(url)
#
# print(response.text)  # Print the response content

def my_view(request):
    image_names = [
        "image1.jpg",
        "image2.jpg",
        "image3.jpg",
        "image4.jpg",
        "image5.jpg",
    ]
    image_urls = [static(f'images/{name}') for name in image_names]
    return render(request, 'my_template.html', {'image_urls': image_urls})
