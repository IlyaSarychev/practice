from django.views.generic.base import TemplateView
from django.views.decorators.http import require_POST
from django.shortcuts import redirect

from .forms import NewsfeedSearchForm, PhotosSearchForm
from .services import requests, database
from prnu_service import get_fingerprint_from_images


class IndexView(TemplateView):
    '''Главная страница'''

    template_name = 'parser/index.html'
    extra_context = {
        'news_form': NewsfeedSearchForm(),
        'photos_form': PhotosSearchForm(),
        'page': 'main'
    }


class SearchResultView(TemplateView):
    '''Результат запроса vk api любым из двух методов'''

    template_name = 'parser/result.html'
    extra_context = {'page': 'search_result'}

    def post(self, request, *args, **kwargs):
        json, res = requests.execute_vk_api_request(request)
        self.extra_context.update({'json': json, 'response': res, 'method': request.POST.get('form_name')})
        return super().get(request, *args, **kwargs)


@require_POST
def post_items_view(request):
    '''Обработка сохранения результирующих записей после api запроса'''

    database.post_items_except_for_deleted(request)
    return redirect('database')


class DataListView(TemplateView):
    '''Список сохраненных записей'''

    template_name = 'parser/data_list.html'
    extra_context = {'page': 'database'}

    def dispatch(self, request, *args, **kwargs):
        data = database.retrieve_all_data()
        self.extra_context.update(data)
            
        return super().dispatch(request, *args, **kwargs)

def delete_item_view(request, collection, id):
    '''Удалить запись'''

    database.delete_item(collection, id)

    return redirect('database')


class PRNUExtractionView(TemplateView):
    '''Извлечение признака из записи'''

    template_name = 'prnu/extracted.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        image_urls = database.retrieve_image_urls(kwargs['collection'], int(kwargs['id']))
        images = []

        for url in image_urls:
            fingerprint = get_fingerprint_from_images([url])
            images.append((url, fingerprint))

        database.save_fingerprints(kwargs['collection'], int(kwargs['id']), images)

        self.extra_context['images'] = images
        self.extra_context['id'] = kwargs['id']

        return super().get(request, *args, **kwargs)