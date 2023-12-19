import requests
import os
from PIL import Image
from IPython.display import IFrame

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r = requests.get(url)
path = os.path.join(os.getcwd(),  'image.png')

with open(path,'wb') as f:
    f.write(r.content)

Image.open(path)


# Question 1: write wget
"""
In the previous section, we used the wget function to retrieve content from the web server as shown below. Write the python code to perform the same task. The code should be the same as the one used to download the image, but the file name should be 'Example1.txt'.
"""

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
response = requests.get(url)
path = os.path.join(os.getcwd(), "example1.txt")
with open(path, "wb") as f:
    f.write(response.content)


# Get Request with URL Parameters

url_get='http://httpbin.org/get'

payload={"name":"Joseph","ID":"123"}
r = requests.get(url_get,params=payload)

print(r.text)
print(r.headers['Content-Type'])
print(r.json())
print(r.json()['args'])


# POST Request
url_post='http://httpbin.org/post'

r_post=requests.post(url_post,data=payload)
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

print(r_post.json()['form'])



