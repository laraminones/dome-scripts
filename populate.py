import json
import requests

REMOTE_URL = 'https://dome-marketplace.eu'

LOCAL_URL = 'http://proxy.docker:8004'
LOCAL_TOKEN = ''

PAGE_SIZE = 50

PARTIES = {}
CATALOGS = {}
PRICES = {}

RESOURCES = {}
SERVICES = {}
PRODUCTS = {}


CATEGORIES = {}


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


def create_party(party_data):
    url = f"{LOCAL_URL}/admin/party/organization"

    del party_data['id']
    del party_data['href']

    response = requests.post(url, headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {LOCAL_TOKEN}"
    }, json=party_data)
    response.raise_for_status()

    return response.json()['id']


def create_catalog(catalog_data):
    url = f"{LOCAL_URL}/admin/catalog/catalog"

    del catalog_data['id']
    del catalog_data['href']

    # Update the party IDs in the catalog
    for party in catalog_data.get('relatedParty', []):
        remote_id = party.get('id')
        if remote_id in PARTIES:
            party['id'] = PARTIES[remote_id]
            party['href'] = PARTIES[remote_id]

    response = requests.post(url, headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {LOCAL_TOKEN}"
    }, json=catalog_data)
    response.raise_for_status()

    return response.json()['id']


def create_service(service_data):
    url = f"{LOCAL_URL}/admin/service/serviceSpecification"

    del service_data['id']
    del service_data['href']

    # Update the party IDs in the catalog
    for party in service_data.get('relatedParty', []):
        remote_id = party.get('id')
        if remote_id in PARTIES:
            party['id'] = PARTIES[remote_id]
            party['href'] = PARTIES[remote_id]

    response = requests.post(url, headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {LOCAL_TOKEN}"
    }, json=service_data)
    response.raise_for_status()

    return response.json()['id']


def create_resource(resource_data):
    import ipdb; ipdb.sset_trace()
    url = f"{LOCAL_URL}/admin/resource/resourceSpecification"

    del resource_data['id']
    del resource_data['href']

    # Update the party IDs in the catalog
    for party in resource_data.get('relatedParty', []):
        remote_id = party.get('id')
        if remote_id in PARTIES:
            party['id'] = PARTIES[remote_id]
            party['href'] = PARTIES[remote_id]

    response = requests.post(url, headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {LOCAL_TOKEN}"
    }, json=resource_data)
    response.raise_for_status()

    return response.json()['id']


def create_product(product_data):
    url = f"{LOCAL_URL}/admin/catalog/productSpecification"

    del product_data['id']
    del product_data['href']

    # Update the party IDs in the catalog
    for party in product_data.get('relatedParty', []):
        remote_id = party.get('id')
        if remote_id in PARTIES:
            party['id'] = PARTIES[remote_id]
            party['href'] = PARTIES[remote_id]

    for service in product_data.get('serviceSpecification', []):
        remote_id = service.get('id')
        if remote_id in SERVICES:
            service['id'] = SERVICES[remote_id]
            service['href'] = SERVICES[remote_id]

    for resource in product_data.get('resourceSpecification', []):
        remote_id = resource.get('id')
        if remote_id in RESOURCES:
            resource['id'] = RESOURCES[remote_id]
            resource['href'] = RESOURCES[remote_id]

    if "productSpecificationRelationship" in product_data:
        product_data["productSpecificationRelationship"] = []

    response = requests.post(url, headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {LOCAL_TOKEN}"
    }, json=product_data)
    response.raise_for_status()

    return response.json()['id']

def create_pop(price_data):
    url = f"{LOCAL_URL}/admin/catalog/productOfferingPrice"

    del price_data['id']
    del price_data['href']

    response = requests.post(url, headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {LOCAL_TOKEN}"
    }, json=price_data)
    response.raise_for_status()

    return response.json()['id']


def create_offering(offering_data):
    url = f"{LOCAL_URL}/admin/catalog/productOffering"

    del offering_data['id']
    del offering_data['href']

    for price in offering_data.get('productOfferingPrice', []):
        remote_id = price.get('id')
        if remote_id in PRICES:
            price['id'] = PRICES[remote_id]
            price['href'] = PRICES[remote_id]

    for category in offering_data.get('category', []):
        remote_id = category.get('id')
        if remote_id in CATEGORIES:
            category['id'] = CATEGORIES[remote_id]
            category['href'] = CATEGORIES[remote_id]

    if 'productSpecification' in offering_data:
        remote_id = offering_data['productSpecification']['id']

        offering_data['productSpecification']['id'] = PRODUCTS[remote_id]
        offering_data['productSpecification']['href'] = PRODUCTS[remote_id]

    response = requests.post(url, headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {LOCAL_TOKEN}"
    }, json=offering_data)
    response.raise_for_status()

    return response.json()['id']


def create_category(category_data):
    url = f"{LOCAL_URL}/admin/catalog/category"

    del category_data['id']
    del category_data['href']

    if not category_data["isRoot"]:
        category_data["parentId"] = CATEGORIES[category_data["parentId"]]

    response = requests.post(url, headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {LOCAL_TOKEN}"
    }, json=category_data)
    response.raise_for_status()

    return response.json()['id']


if __name__ == "__main__":
    # Get all the parties
    party_url = f"{REMOTE_URL}/party/organization"
    parties = fetch_all(party_url)
    print(f"Fetched {len(parties)} parties from remote.")

    # Create a map with the party IDs
    for party in parties:
        remote_id = party.get('id')
        try:
            if remote_id:
                # Create new parties in the local environment
                local_id = create_party(party)
                PARTIES[remote_id] = local_id
                print(f"Created party {remote_id} with local ID {local_id}")
        except Exception as e:
            print(f"Error creating party {remote_id}")

    # Get all the root categories
    category_url = f"{REMOTE_URL}/catalog/category?isRoot=true"
    categories = fetch_all(category_url)
    print(f"Fetched {len(categories)} root categories from remote.")

    for category in categories:
        remote_id = category.get('id')
        try:
            if remote_id:
                # Create new parties in the local environment
                local_id = create_category(category)
                CATEGORIES[remote_id] = local_id
                print(f"Created category {remote_id} with local ID {local_id}")
        except Exception as e:
            print(f"Error creating category {remote_id}")

    # Get all the child categories
    category_url = f"{REMOTE_URL}/catalog/category?isRoot=false"
    categories = fetch_all(category_url)
    print(f"Fetched {len(categories)} child categories from remote.")

    for category in categories:
        remote_id = category.get('id')
        try:
            if remote_id:
                # Create new parties in the local environment
                local_id = create_category(category)
                CATEGORIES[remote_id] = local_id
                print(f"Created category {remote_id} with local ID {local_id}")
        except Exception as e:
            print(f"Error creating category {remote_id}")

    # Get all the catalogs
    catalog_url = f"{REMOTE_URL}/catalog/catalog"
    catalogs = fetch_all(catalog_url)
    print(f"Fetched {len(catalogs)} catalogs from remote.")

    # Update the catalog with the new IDs
    for catalog in catalogs:
        remote_id = catalog.get('id')
        try:
            if remote_id:
                # Create new catalogs in the local environment
                local_id = create_catalog(catalog)
                CATALOGS[remote_id] = local_id
                print(f"Created catalog {remote_id} with local ID {local_id}")
        except Exception as e:
            print(f"Error creating catalog {remote_id}")


    # Get all the service specs
    service_url = f"{REMOTE_URL}/service/serviceSpecification"
    services = fetch_all(service_url)
    print(f"Fetched {len(services)} services from remote.")

    # Update the product specs with the new party IDs
    # Create a map with the product spec IDs
    for service in services:
        remote_id = service.get('id')
        try:
            if remote_id:
                # Create new catalogs in the local environment
                local_id = create_service(service)
                SERVICES[remote_id] = local_id
                print(f"Created service {remote_id} with local ID {local_id}")
        except Exception as e:
            print(f"Error creating service {remote_id}")


    # Get all the resource specs
    resource_url = f"{REMOTE_URL}/resource/resourceSpecification"
    resources = fetch_all(resource_url)
    print(f"Fetched {len(resources)} resources from remote.")

    # Update the product specs with the new party IDs
    # Create a map with the product spec IDs
    for resource in resources:
        remote_id = resource.get('id')
        try:
            if remote_id:
                # Create new catalogs in the local environment
                local_id = create_resource(resource)
                RESOURCES[remote_id] = local_id
                print(f"Created resource {remote_id} with local ID {local_id}")
        except Exception as e:
            print(f"Error creating resource {remote_id}")


    # Get all the product specs
    product_url = f"{REMOTE_URL}/catalog/productSpecification"
    products = fetch_all(product_url)
    print(f"Fetched {len(products)} products from remote.")

    # Update the product specs with the new party IDs
    # Create a map with the product spec IDs
    for product in products:
        remote_id = product.get('id')
        try:
            if remote_id:
                # Create new catalogs in the local environment
                local_id = create_product(product)
                PRODUCTS[remote_id] = local_id
                print(f"Created product {remote_id} with local ID {local_id}")
        except Exception as e:
            print(f"Error creating product {remote_id}")

    # Get all the product offering prices
    price_url = f"{REMOTE_URL}/catalog/productOfferingPrice"
    pops = fetch_all(price_url)
    print(f"Fetched {len(pops)} prices from remote.")

    # Create a map with the product offering prices IDs
    for pop in pops:
        remote_id = pop.get('id')
        try:
            if remote_id:
                # Create new catalogs in the local environment
                local_id = create_pop(pop)
                PRICES[remote_id] = local_id
                print(f"Created price {remote_id} with local ID {local_id}")
        except Exception as e:
            print(f"Error creating price {remote_id}")

    print('============')
    print(PRICES)
    print('============')

    # Get all the product offerings
    offering_url = f"{REMOTE_URL}/catalog/productOffering"
    offerings = fetch_all(offering_url)
    print(f"Fetched {len(offerings)} offerings from remote.")

    # Create prodict offerings
    for offering in offerings:
        remote_id = offering.get('id')
        try:
            if remote_id:
                local_id = create_offering(offering)
                print(f"Created offering {remote_id} with local ID {local_id}")
        except Exception as e:
            print(f"Error creating offering {remote_id}")
            print(str(e))
