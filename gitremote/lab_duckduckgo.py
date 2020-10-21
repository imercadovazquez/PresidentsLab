import requests


url_ddg = "https://api.duckduckgo.com/?q=presidents of the united states&format=json&pretty=1"
resp = requests.get(url_ddg)
rsp_data = resp.json()

for item in rsp_data:
    print("item: ", item)
    print("value:", rsp_data[item])
    pres_list = rsp_data[item]
print("\n*********************************************************************************\n")
for x in rsp_data['RelatedTopics']:
    print("entries: ", x)
