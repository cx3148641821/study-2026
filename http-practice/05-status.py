# 状态码

import requests

urls = {
    "200":"https://httpbin.org/status/200",
    "404":"https://httpbin.org/status/404",
    "503":"https://httpbin.org/status/503",
}

for expect , url in urls.items():
    resp = requests.get(url,timeout=10,allow_redirects=False)
    ok = "OK" if resp.status_code == int(expect) else "意外"
    print(f"期望{expect} ->实际{resp.status_code} {ok}")


# # 05_status.py —— 只关心状态码，学「怎么判断成败」
# import requests

# urls = {
#     "200": "https://httpbin.org/status/200",
#     "404": "https://httpbin.org/status/404",
#     "503": "https://httpbin.org/status/503",
# }

# for expect, url in urls.items():
#     # allow_redirects 默认行为先不管；这里只要状态码
#     resp = requests.get(url, timeout=10, allow_redirects=False)
#     ok = "OK" if resp.status_code == int(expect) else "意外"
#     print(f"期望 {expect} -> 实际 {resp.status_code}  {ok}")