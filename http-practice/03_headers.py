# 实现自定义头+User-Agent

import requests

headers= {
    "X-Practice":"daty4",
    "User-Agent":"MyStudyNot/1.0",
}

resp = requests.get("https://httpbin.org/get",headers=headers,timeout=10)

got = resp.json().get("headers",{})
print("服务器看到X-Practice：",got.get("X-Practice"))
print("服务器看到User-Agent",got.get("User-Agent"))