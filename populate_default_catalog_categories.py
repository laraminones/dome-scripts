import requests

BASE = 'http://proxy.docker:8004'
TOKEN = ''

#BASE = 'https://dome-marketplace-sbx.org'
#TOKEN = ''

REMOTE_URL = 'https://dome-marketplace.org'

root_cats = f'{BASE}/catalog/category?isRoot=true&limit=1000'
resp = requests.get(root_cats)

dome_cats_res = requests.get(f'{REMOTE_URL}/catalog/catalog/urn:ngsi-ld:catalog:48d10cb4-0d1a-4f72-8962-3e44668efe09')
print('retrieved')
dome_cats=dome_cats_res.json()['category']
print(dome_cats)
print(f"Total categories fetched: {len(dome_cats)}")

default_cats = []

for cat in dome_cats:
    children = []
    catid = cat["id"]
    cat_res = requests.get(f'{REMOTE_URL}/catalog/category/{catid}')
    cat_data = cat_res.json()
    children_res = requests.get(f"{REMOTE_URL}/catalog/category?parentId={catid}")
    children_data = children_res.json()

    print(cat_data)
    print('children: ')
    print(children_data)

    url = f"{BASE}/admin/catalog/category"

    del cat_data['id']
    del cat_data['href']

    response = requests.post(url, headers={
         "Accept": "application/json",
         "Authorization": f"Bearer {TOKEN}"
     }, json=cat_data)
    response.raise_for_status()

    created_cat = response.json()

    print(f"Created category: {created_cat}")


    default_cats.append(created_cat)

    for children in children_data:
        del children['id']
        del children['href']
        children['parentId'] = created_cat['id']

        print(f"Children to create: {children}")

        response = requests.post(url, headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        }, json=children)
        response.raise_for_status()

        print(f"Created children category: {response.json()}")


catalog = {
     "name": "DOME Catalog",
     "description": "Default DOME catalog",
     "category": [{
         "id": cat["id"],
         "href": cat["id"],
         "name": cat["name"]
     } for cat in default_cats]
}

catalog_url = f"{BASE}/admin/catalog/catalog"
resp = requests.post(catalog_url, json=catalog, headers={
     'Authorization': f'Bearer {TOKEN}'
})

catalog_id = resp.json()['id']

requests.post(f"{BASE}/admin/defaultcatalog", json={
     "catalogId": catalog_id
}, headers={
     'Authorization': f'Bearer {TOKEN}'
})