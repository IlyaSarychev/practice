import json
import os

from dotenv import load_dotenv
from pymongo import MongoClient
from bson import json_util


load_dotenv()

client = MongoClient(os.getenv('MONGO_HOST_NAME'), int(os.getenv('MONGO_PORT')))
db = client[os.getenv('MONGO_DATABASE_NAME')]

def post_items_except_for_deleted(request):
    data = json.loads(request.POST.get('json'))
    method_name = request.POST.get('method')
    item_keys = [int(key.lstrip('item-')) for key in request.POST.keys() if key.startswith('item-')]
    items_to_insert = [item for item in data['response']['items'] if item['id'] in item_keys]

    collection_name = method_name.split('_')[0]
    collection = db[collection_name]
    
    return collection.insert_many(items_to_insert)

def retrieve_all_data():
    data = {}
    for collection in ('photos', 'news'):
        items = list(db[collection].find({}))
        if len(items):
            items = [(item['id'], collection, json_util.dumps(item, indent=4)) for item in items]
            data.update({(collection + '_list'): items})

    return data

def delete_item(collection, id):
    collection = db[collection]
    return collection.delete_one({'id': id})


def retrieve_image_urls(collection_name, id):
    collection = db[collection_name]
    item = collection.find_one({'id': id})

    image_urls = []

    if collection_name == 'news':
        for attachment in item['attachments']:
            if attachment['type'] == 'photo':
                image_urls.append(attachment['photo']['sizes'][-1]['url'])

    if collection_name == 'photos':
        image_urls.append(item['sizes'][-1]['url'])

    return image_urls


def save_fingerprints(collection_name, id, data):
    collection = db[collection_name]
    data = list(map(lambda item: (item[0], str(item[1])), data))
    return collection.update_one({'id': id}, {'$set': {'fingerprint': data}})