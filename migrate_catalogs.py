
import requests


# BASE = 'http://proxy.docker:8004'

BASE = 'https://dome-marketplace.eu'
TOKEN = 'eyJraWQiOiJkaWQ6a2V5OnpEbmFlVlluV1RadTVuYnJIMXFtQlZNdk53U3J0S25rUmJDWjR4SDVoMkxRUG56ZHIiLCJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJhdWQiOiJkaWQ6a2V5OnpEbmFlVFUzOVd4OUtYZ21Fd21mWHNaU3lFVnhnQ3F3Q1Ztb1B5VlFVVEQ4YmhXOGEiLCJzdWIiOiJkaWQ6a2V5OnpEbmFlcnRtQ0RhR055ekZQdkNlNmtWSFNLYVFkcHV5RGVyMU5TWTVBSFI0UWNKMlciLCJzY29wZSI6Im9wZW5pZCBsZWFyY3JlZGVudGlhbCIsImlzcyI6Imh0dHBzOi8vdmVyaWZpZXIuZG9tZS1tYXJrZXRwbGFjZS5ldSIsImV4cCI6MTc1MTk3NzgwOCwiaWF0IjoxNzUxOTc0MjA4LCJ2YyI6eyJAY29udGV4dCI6WyJodHRwczovL3d3dy53My5vcmcvbnMvY3JlZGVudGlhbHMvdjIiLCJodHRwczovL3RydXN0LWZyYW1ld29yay5kb21lLW1hcmtldHBsYWNlLmV1L2NyZWRlbnRpYWxzL2xlYXJjcmVkZW50aWFsZW1wbG95ZWUvdjEiXSwiY3JlZGVudGlhbFN1YmplY3QiOnsibWFuZGF0ZSI6eyJpZCI6IjNhOGRhNDZlLThmZTAtNDI4ZS04MWY1LWZlZWY2OTc1ZDZkNiIsImxpZmVfc3BhbiI6eyJlbmRfZGF0ZV90aW1lIjoiMjAyNS0xMS0yN1QxMDo0MjoyMy44OTcyNjcyNDRaIiwic3RhcnRfZGF0ZV90aW1lIjoiMjAyNC0xMS0yN1QxMDo0MjoyMy44OTcyNjcyNDRaIn0sIm1hbmRhdGVlIjp7ImVtYWlsIjoiZmRlbGF2ZWdhQGZpY29kZXMuY29tIiwiZmlyc3RfbmFtZSI6IkZyYW5jaXNjbyIsImlkIjoiZGlkOmtleTp6RG5hZXJ0bUNEYUdOeXpGUHZDZTZrVkhTS2FRZHB1eURlcjFOU1k1QUhSNFFjSjJXIiwibGFzdF9uYW1lIjoiZGUgbGEgVmVnYSIsIm1vYmlsZV9waG9uZSI6IiJ9LCJtYW5kYXRvciI6eyJjb21tb25OYW1lIjoiRnJhbmNpc2NvIGRlIGxhIFZlZ2EiLCJjb3VudHJ5IjoiRVMiLCJlbWFpbEFkZHJlc3MiOiJmZGVsYXZlZ2FAZmljb2Rlcy5jb20iLCJvcmdhbml6YXRpb24iOiJGVVRVUkUgSU5URVJORVQgQ09OU1VMVElORyBBTkQgREVWRUxPUE1FTlQgU09MVVRJT05TIFNMIiwib3JnYW5pemF0aW9uSWRlbnRpZmllciI6IlZBVEVTLUI4Nzc5ODYxNyIsInNlcmlhbE51bWJlciI6IjAyMjkzMzQ3ViJ9LCJwb3dlciI6W3siaWQiOiI5OThlMjhiZi1jY2YxLTRkNzMtOTI4My03YzM4YjI3NDlhMzIiLCJ0bWZfYWN0aW9uIjoiRXhlY3V0ZSIsInRtZl9kb21haW4iOiJET01FIiwidG1mX2Z1bmN0aW9uIjoiT25ib2FyZGluZyIsInRtZl90eXBlIjoiRG9tYWluIn0seyJpZCI6IjFhMmMwN2M1LWY0MzYtNDhkYS1iNTJmLTQzODJkZmM5YzY1ZiIsInRtZl9hY3Rpb24iOlsiQ3JlYXRlIiwiVXBkYXRlIiwiRGVsZXRlIl0sInRtZl9kb21haW4iOiJET01FIiwidG1mX2Z1bmN0aW9uIjoiUHJvZHVjdE9mZmVyaW5nIiwidG1mX3R5cGUiOiJEb21haW4ifV0sInNpZ25lciI6eyJjb21tb25OYW1lIjoiNTY1NjU2NTZQIEplc3VzIFJ1aXoiLCJjb3VudHJ5IjoiRVMiLCJlbWFpbEFkZHJlc3MiOiJqZXN1cy5ydWl6QGluMi5lcyIsIm9yZ2FuaXphdGlvbiI6IkRPTUUgQ3JlZGVudGlhbCBJc3N1ZXIiLCJvcmdhbml6YXRpb25JZGVudGlmaWVyIjoiVkFURVMtUTAwMDAwMDBKIiwic2VyaWFsTnVtYmVyIjoiSURDRVMtNTY1NjU2NTZQIn19fSwiaWQiOiIwZTA5MTIwOS1hNjdiLTQzODQtOWFiMy1mNTVmNzc1ZjQ2YmEiLCJpc3N1ZXIiOiJkaWQ6ZWxzaTpWQVRFUy1RMDAwMDAwMEoiLCJ0eXBlIjpbIkxFQVJDcmVkZW50aWFsRW1wbG95ZWUiLCJWZXJpZmlhYmxlQ3JlZGVudGlhbCJdLCJ2YWxpZEZyb20iOiIyMDI0LTExLTI3VDEwOjQyOjIzLjg5NzI2NzI0NFoiLCJ2YWxpZFVudGlsIjoiMjAyNS0xMS0yN1QxMDo0MjoyMy44OTcyNjcyNDRaIn0sImp0aSI6IjdhZmNiNjFlLWYwZmItNGE0Ny05NmYyLWYwODMwZDQ2ZjM5MiIsImNsaWVudF9pZCI6Imh0dHBzOi8vdmVyaWZpZXIuZG9tZS1tYXJrZXRwbGFjZS5ldSJ9.GglplFROPEE1IRUc73W6TIPa64kK244y7rLlmni0Kx9vXtM4k8AyDhLgK_3s0axIdf2xEA8D3iadJIKmrTqzMA'

PAGE_SIZE = 50

PARTIES = {}


def fetch_all(url):
    all_items = []
    page = 0

    while True:
        params = {
            "offset": page * PAGE_SIZE,
            "limit": PAGE_SIZE
        }
        print(f"Fetching page {page + 1}...")

        response = requests.get(url, headers={
            "Accept": "application/json"
        }, params=params)

        response.raise_for_status()

        data = response.json()
        if not data:
            print("No more data.")
            break

        all_items.extend(data)
        page += 1

    return all_items


def get_product_spec(spec_id):
    url = f"{BASE}/catalog/productSpecification/{spec_id}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()


def create_category(name, party):
    url = f'{BASE}/admin/catalog/category'
    cat = {
        "isRoot": True,
        "lifecycleStatus": "Launched",
        "name": name
        # "relatedParty": [{
        #     "id": party,
        #     "href": party,
        #     "role": "Owner"
        # }]
    }

    resp = requests.post(url, json=cat, headers={
        'Authorization': 'Bearer ' + TOKEN
    })
    resp.raise_for_status()

    return resp.json()


def update_catalog(catalog_id, category_id, category_name):
    url = f'{BASE}/admin/catalog/catalog/{catalog_id}'
    catalog = {
        "category": [
            {
                "id": category_id,
                "href": category_id,
                "name": category_name
            }
        ]
    }

    resp = requests.patch(url, json=catalog, headers={
        'Authorization': 'Bearer ' + TOKEN
    })
    resp.raise_for_status()

    return resp.json()


def update_offering(offer, category_id, category_name):
    url = f'{BASE}/admin/catalog/productOffering/{offer["id"]}'

    categories = offer.get('category', [])
    categories.append({
        'id': category_id,
        'href': category_id,
        'name': category_name
    })

    resp = requests.patch(url, json={
        'category': categories
    }, headers={
        'Authorization': 'Bearer ' + TOKEN
    })
    resp.raise_for_status()


if __name__ == "__main__":
    catalog_url = f"{BASE}/catalog/catalog"
    catalogs = fetch_all(catalog_url)

    for catalog in catalogs:
        if 'name' not in catalog:
            continue

        if 'relatedParty' not in catalog or len(catalog['relatedParty']) == 0:
            continue

        catalog_id = catalog['id']
        catalog_name = catalog['name']
        party_id = catalog['relatedParty'][0]['id']

        if party_id not in PARTIES:
            PARTIES[catalog['relatedParty'][0]['id']] = {
                'migrated': [],
                'pending': []
            }

        if 'category' in catalog and len(catalog['category']) > 0:
            category = catalog['category'][0]['id']
            print(f'-----> Found catalog {catalog_name} ({catalog_id}) with category {category} and status {catalog["lifecycleStatus"]}')

            PARTIES[party_id]['migrated'].append({
                'id': catalog_id,
                'name': catalog_name,
                'status': catalog["lifecycleStatus"],
                'categoryId': category
            })
        else:
            print(f'No category found for catalog {catalog_name} ({catalog_id}) with status {catalog["lifecycleStatus"]}')
            PARTIES[party_id]['pending'].append({
                'id': catalog_id,
                'name': catalog_name,
                'status': catalog["lifecycleStatus"]
            })

    print('=========================================================================')
    print('=========================================================================')

    for party_id, data in PARTIES.items():
        print('--------------------------------------------------------------')
        print(f'Party {party_id} has {len(data["migrated"])} migrated catalogs and {len(data["pending"])} pending catalogs')
        print('Migrated catalogs: ' + ', '.join([f'{c["name"]} ({c["id"]})' for c in data['migrated']]))
        print('Pending catalogs: ' + ', '.join([f'{c["name"]} ({c["id"]})' for c in data['pending']]))

        for catalog in data['pending']:
            try:
                # Create a new catalog category
                category = create_category(catalog['name'], party_id)
                # Update the catalog with the new category
                update_catalog(catalog['id'], category['id'], category['name'])
                catalog['categoryId'] = category['id']

                data['migrated'].append(catalog)
            except Exception as e:
                print(f'Error creating category for catalog {catalog["name"]}: {e}')
                continue

            print(f'Created category {category["name"]} ({category["id"]}) for catalog {catalog["name"]} ({catalog["id"]})')


    print('=========================================================================')
    print('=========================================================================')

    offerings_url = f'{BASE}/catalog/productOffering'
    offers = fetch_all(offerings_url)

    for offer in offers:
        try:
            spec = get_product_spec(offer['productSpecification']['id'])
            provider = spec['relatedParty'][0]['id']

            # Get the category ID to be included
            category_id = None
            category_name = None
            for cat in PARTIES[provider]['migrated']:
                if cat['status'].lower() == 'launched':
                    category_id = cat['categoryId']
                    category_name = cat['name']
                    print(f'Found Launched catalog {cat["name"]}')
                    break
            else:
                print(f'Not Found any Launched catalog for offer {offer["name"]}')

            if category_id is None:
                for cat in PARTIES[provider]['migrated']:
                    if cat['status'].lower() == 'active':
                        category_id = cat['categoryId']
                        category_name = cat['name']
                        print(f'Found Active catalog {cat["name"]}')
                        break
                else:
                    print(f'Not Found any Active catalog for offer {offer["name"]}')
            
            if category_id is None:
                cat = PARTIES[provider]['migrated'][0]
                category_id = cat['categoryId']
                category_name = cat['name']
                print(f'Using catalog {cat["name"]} with status {cat["status"]}')

            update_offering(offer, category_id, category_name)
            print(f'Updated product offer {offer["id"]} - {offer["name"]}')

        except Exception as e:
            print(f'Error updating product offer {offer["id"]} - {offer["name"]}: {e}')
            continue




# Get all the catalogs
# Check if the same provider has more than 1 catalog


# Create a category for each catalog
# Update catalog with the category information
# Save category info for later use


# Get all the product offerings
# Get the provider info


# Choose a catalog from the provider
# Add the catalog category to the product offering
