#!/usr/bin/python3
import json
from models import storage
from models.db_models.item import Item

items = storage.get('Item')
for item in items:
    storage.remove(item)

with open('storage.json', 'r') as f:
    d = json.loads(f.read())

for k, v in d.items():
    if "Item" in k:
        name = v['name']
        price = v['price']
        medias = v['medias']
        Item(name, price, medias)
