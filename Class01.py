# Stateless  --> It means no client information is stored between get requests and each request is separate and unconnected.
# It consumes fewer resources because systems do not need to keep track of information to connect numerous transmissions.


##-- HTTP status codes --##

# 301 - Moved Permanently - The requested page has moved to a new url.
# 403 - Forbidden - Access is forbidden to the requested page.
# 503 - Service Unavailable	- The server is temporarily overloading or down.


import requests


# Get()

base_url1 = "https://reqres.in/api/users"

response = requests.get(base_url1)

print(response)

print("Get function --",response.json())


# Post()

base_url2 = "https://reqres.in/api/users"

to_post = {"name":"Ronak Pal Singh Bali","Age":25,"place":"INDIA"}

response = requests.post(base_url2, to_post)

print(response)

print("Post function --",response.json())


# Put ()

base_url3 = "https://reqres.in/api/users/5"

to_put = {"name":"Bali Singh Pal Ronak", "age":52,"place":"AIDNI"}

response = requests.put(base_url3, to_put)

print(response)

print("Put function --",response.json())



# Patch ()

base_url4 = "https://reqres.in/api/users/4"

to_patch = {"name":"Nobody"}

response = requests.put(base_url4, to_patch)

print(response)

print("Patch function --",response.json())


# Delete ()


base_url5 = "https://reqres.in/api/users/1"


response = requests.delete(base_url5)

print(response)

print("Delete function --",response.status_code)


