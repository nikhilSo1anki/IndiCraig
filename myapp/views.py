import requests
import urllib
from urllib.parse import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models

BASE_CRAGLIST_URL ='https://ahmedabad.craigslist.org/search/sss?query='
BASE_IMAGE_URL = 'https://images.craigslist.org/'

# Create your views here.
def home(request):
    return render(request,'base.html')

def newSearch(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    
    #encoding url
    encoded_search = urllib.parse.quote_plus(search)
    final_search = BASE_CRAGLIST_URL + encoded_search

    #getting page directly with requests

    response = requests.get(final_search)
    data = response.text
    soup = BeautifulSoup(data,features='html.parser')

    #fetching all <li> tags with class name in url
    post_listing = soup.find_all('li',{'class':'result-row'}) 

    final_posting = []

    for post in post_listing:
        post_title = post.find(class_="result-title").text    
        post_url = post.find('a').get('href')

        if post.find(class_="result-price"):
            post_price = post.find(class_="result-price").text
        else:
            post_price = "Not Available"

        
        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL + post_image_id + '_300x300.jpg'
           
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        

        final_posting.append((post_title,post_url,post_price,post_image_url))

        
       
    stuff_for_frontend = {
        'search' : search,
        'final_posting' : final_posting,
    }

    return render(request,'new_search.html',stuff_for_frontend)