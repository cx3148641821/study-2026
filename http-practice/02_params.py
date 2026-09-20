# 实现查询参数 curl "https://httpbin.org/get?course=security&week=1"

import requests

resp= requests.get(
    "https://httpbin.org/get",
    params={"course":"security","week":1},
    timeout = 10,
)

print("完整的url",resp.url)
print("服务器最终看到的args:",resp.json().get("args"))
