import requests
from pprint import pprint
r = requests.get("https://jsonplaceholder.typicode.com/posts", ).json()
d = {}
for dic in r:
    if dic["userId"] in d:
        d[dic["userId"]].append(dic)
    else:
        d[dic["userId"]] = [dic]
pprint(d)