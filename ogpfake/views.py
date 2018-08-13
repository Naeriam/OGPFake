"""
    Views for OGPFake

    This view gathers all necessary tags from GET request,
    then gets information from enviromental variables and renders the final page.

    Noemi Escudero del Olmo, 2018, https://github.com/Naeriam
"""

import os
from django.shortcuts import render


def ogpfake(request):

    # Get all necessary tags of the GET request
    ga_tracking_id = None if 'ga_tracking_id' not in request.GET else os.getenv(request.GET.get('ga_tracking_id'))
    title = None if 'title' not in request.GET else os.getenv(request.GET.get('title'))
    description = None if 'description' not in request.GET else os.getenv(request.GET.get('description'))
    url = None if 'url' not in request.GET else os.getenv(request.GET.get('url'))
    image = None if 'image' not in request.GET else os.getenv(request.GET.get('image'))

    # Error control
    error_text = '{0} has not been especified. Ensure you have a KEY name in your GET request ' \
                 'and a VALUE in your Heroku Config Vars'
    errors = []
    if not ga_tracking_id:
        errors.append(error_text.format('Google Analytics ID'))
    if not title:
        errors.append(error_text.format('A title for your link'))
    if not description:
        errors.append(error_text.format('A description for your link'))
    if not url:
        errors.append(error_text.format('A destination URL'))
    if not image:
        errors.append(error_text.format('An image for your link'))

    # Render web page
    return render(request, 'ogpfake.html', {
        'ga_tracking_id': ga_tracking_id,
        'title': title,
        'description': description,
        'url': url,
        'image': image,
        'errors': errors,
    })
