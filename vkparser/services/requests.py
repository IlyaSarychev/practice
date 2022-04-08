import requests
import json

from django.conf import settings
from datetime import datetime


def execute_vk_api_request(request):
    form_name = request.POST.get('form_name')
    params = settings.VK_API_BASE_PARAMS
    params.update({key: value for key, value in request.POST.items() if len(value)})
    del params['form_name']
    del params['csrfmiddlewaretoken']

    if form_name == 'news_form':
        res = requests.get(settings.VK_API_REQUEST + 'newsfeed.search', params=params)
    if form_name == 'photos_form':
        res = requests.get(settings.VK_API_REQUEST + 'photos.search', params=params)

    items = json.loads(res.text)['response']['items']

    for item in items:
        item['date'] = datetime.fromtimestamp(item['date'])

        if form_name == 'news_form':
            # Получить фото из поста
            item['photos'] = None
            attachments = item.get('attachments', None)
            if attachments:
                photos = list(filter(lambda i: i['type'] == 'photo', attachments))
                if photos:
                    item['photos'] = [photo['photo']['sizes'][-1]['url'] for photo in photos]

        if form_name == 'photos_form':
            item['photos'] = [s['url'] for s in item['sizes']]

    # Исключить записи без фото
    items = [item for item in items if item['photos']]

    return json.dumps(json.loads(res.text), indent=4), items