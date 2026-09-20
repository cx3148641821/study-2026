# 实现curl https://httpbin.org/get

import requests

url = "https://httpbin.org/get"

resp=requests.get(url,timeout=10)

print("状态码：",resp.status_code)
print("响应类型：",type(resp))
print("Content-Type:",resp.headers.get("Content-Type"))
print("---- JSON 正文 ----")
data = resp.json()
print(data)
print("你的地址（部分）：",data.get("origin"))
