# POST表单+POST JSON

import requests

resp_from = requests.post(
    "https://httpbin.org/post",
    data={"username":"demo","password":"123"},
    timeout=10,
)
form_json = resp_from.json()
print("表单 status:",resp_from.status_code)
print("服务器读到form",form_json.get("form"))
print("Content-Type请求头:",form_json.get("headers",{}).get("Content-Type"))

resp_json = requests.post(
    "https://httpbin.org/post",
    json={"title":"bool1","pages":100},
    timeout=10,
)

data_json = resp_json.json()
print("JSON status:",resp_json.status_code)
print("服务器读到 json:",data_json.get("json"))
print("Content-Type 请求头:",data_json.get("headers",{}).get("Content-Type"))