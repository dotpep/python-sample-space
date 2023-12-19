import requests


# Requests module in Python for HTTP protocol
url = 'https://www.ibm.com'
response_get = requests.get(url)
status_code = response_get.status_code # 200
requests_headers = response_get.request.headers
requests_bode = response_get.request.body # None

header = response_get.headers
header_date = header['date']
header_server = header['Server']
header_content_type = header['Content-Type']

response_encoding = response_get.encoding
response_text = response_get.text[0:100]


# Get Request with URL Parameters

url_get = 'http://httpbin.org/get'
payload = {"name": "Jeseph", "ID": "123"}

response_get = requests.get(url_get, params=payload)
response_url = response_get.url
response_headers = response_get.headers['Content-Type']

response_txt = response_get.text
response_json = response_get.json()


# POST Request
url_post = 'http://httpbin.org/post'

payload = {"name": "Jeseph", "ID": "123"}
response_post = requests.post(url_post, data=payload)

# Compare POST and GET Request
# URL compare
print("POST Request URL:", response_post.url)
print("GET Request URL:", response_get.url)

# Body compare
print("POST Request Body:", response_post.request.body)
print("GET Request Body:", response_get.request.body)
