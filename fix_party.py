
import requests


TOKEN = ''

party_id = 'urn:ngsi-ld:organization:d817c6a0-5b5e-4cbc-b1b9-786396c69f49'
new_party_id = 'urn:ngsi-ld:organization:57404b83-d1ac-445c-a2f6-3f64310191ea'

organization_id = 'VATES-A48283964'

# Get organization
resp = requests.get('https://dome-marketplace.org/party/organization/{}'.format(party_id))

data = resp.json()
print(data)

# Update organization id
body = {
    'externalReference': [{'externalReferenceType': 'idm_id', 'name': organization_id}]
}
url = 'https://dome-marketplace.org/admin/party/organization/{}'.format(party_id)

resp = requests.patch(url, json=body, headers={
    'Authorization': 'Bearer {}'.format(TOKEN)
})
resp.raise_for_status()

# Delete new party object
new_body = {
    'externalReference': [{'externalReferenceType': 'idm_id', 'name': organization_id + '-dep'}]
}
new_url = 'https://dome-marketplace.org/admin/party/organization/{}'.format(new_party_id)

new_resp = requests.patch(new_url, json=new_body, headers={
    'Authorization': 'Bearer {}'.format(TOKEN)
})
new_resp.raise_for_status()
