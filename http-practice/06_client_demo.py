# 06_client_demo.py —— 用统一客户端发请求

from http_client import get,raise_for_status

resp=get("https://httpbin.org/get",params={"day":"4"})

raise_for_status(resp)
print("status",resp.status_code)
print("UA回显",resp.json().get("headers",{}).get("User-Agent"))


# # Day 4 HTTP / requests 笔记

# ## 1. 方法
# - GET：读数据，参数在 URL
# - POST：提交数据，参数在 body

# ## 2. 状态码
# - 2xx 成功；4xx 客户端问题；5xx 服务端问题
# - 404 路径不存在；401 未认证；403 无权限；422 参数校验失败（FastAPI 常见）

# ## 3. data= vs json=
# - data={"a":1}  → 表单 urlencoded → httpbin 看 form
# - json={"a":1}  → application/json → httpbin 看 json
# - 后端联调优先 json=

# ## 4. Header 要点
# - User-Agent：客户端身份
# - Authorization: Bearer xxx：Token 登录（Day 2 curl ⑩）
# - Content-Type：告诉服务器 body 是什么格式

# ## 5. curl ↔ requests 对照
# | curl | requests |
# |------|----------|
# | curl URL | requests.get(url) |
# | -H "K: V" | headers={"K": "V"} |
# | "?a=1" | params={"a": 1} |
# | -d "a=1" | data={"a": 1} |
# | -X POST + JSON | json={...} |
# | -w "%{http_code}" | resp.status_code |
# | -c/-b cookies | requests.Session() |