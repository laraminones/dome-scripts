import requests

# BASE = 'http://proxy.docker:8004'
# TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdhbml6YXRpb25zIjpbeyJpZCI6ImQ2NTcwNmEyLTUwMmMtNDY4OS05ZGFmLWQyZGY5MDRkYTU3YiIsIm5hbWUiOiJGSUNPREVTIFMuTCIsImRlc2NyaXB0aW9uIjoiRklDT0RFUyIsIndlYnNpdGUiOiIiLCJyb2xlcyI6W3siaWQiOiJkZGNiNWY5NS0yNzBmLTQ2YzUtODQ2Ny00YzIzOGQxMzVhYzgiLCJuYW1lIjoiYWRtaW4ifSx7ImlkIjoiMzgzMmQzMDktMDhmYi00MDNlLTk3YWQtYTkzY2Y5ZjAzZGYwIiwibmFtZSI6InNlbGxlciJ9LHsiaWQiOiI5MmNmYWJkYy02NzFiLTQzMGQtYjVhYi1mODg2NTI1YWYyYWMiLCJuYW1lIjoib3JnQWRtaW4ifV19XSwiZGlzcGxheU5hbWUiOiIiLCJyb2xlcyI6W3siaWQiOiJkZGNiNWY5NS0yNzBmLTQ2YzUtODQ2Ny00YzIzOGQxMzVhYzgiLCJuYW1lIjoiYWRtaW4ifSx7ImlkIjoiMzgzMmQzMDktMDhmYi00MDNlLTk3YWQtYTkzY2Y5ZjAzZGYwIiwibmFtZSI6InNlbGxlciJ9XSwiYXBwX2lkIjoiMTlkZDg1OGMtMzI4Yy00NjQyLTkzYWItZGE0NWU0ZDI1M2FlIiwidHJ1c3RlZF9hcHBzIjpbXSwiaXNHcmF2YXRhckVuYWJsZWQiOmZhbHNlLCJpZCI6ImUwZDMwZjBlLTY0ZDQtNGU4MC05YzM5LWE2YjI2ZGEyOGFjZiIsImF1dGhvcml6YXRpb25fZGVjaXNpb24iOiIiLCJhcHBfYXpmX2RvbWFpbiI6IiIsImVpZGFzX3Byb2ZpbGUiOnt9LCJhdHRyaWJ1dGVzIjp7fSwic2hhcmVkX2F0dHJpYnV0ZXMiOiIiLCJ1c2VybmFtZSI6ImZkZWxhdmVnYSIsImVtYWlsIjoiZmRlbGF2ZWdhQGZpY29kZXMuY29tIiwiaW1hZ2UiOiIiLCJncmF2YXRhciI6IiIsImV4dHJhIjoiIiwidHlwZSI6InVzZXIiLCJpYXQiOjE3NTE2NDQ1NDYsImV4cCI6MTc1MTY0ODE0Nn0.vNhduQvd8j2UsKWfFNJU7z3cutuWr0mwdmiplmBk9Q4'

BASE = 'https://dome-marketplace.eu'
TOKEN = ''


root_cats = f'{BASE}/catalog/category?isRoot=true&limit=1000'
resp = requests.get(root_cats)


catalog = {
    "name": "DOME Catalog",
    "description": "Default DOME catalog",
    "category": [{
        "id": cat["id"],
        "href": cat["id"],
        "name": cat["name"]
    } for cat in resp.json()]
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
