---
tags: 学习笔记
---
# curl十连发

来源：
日期：2026-09-19

## 学了什么

1. 最简单的get
```
curl https://httpbin.org/get
```
**作用：** 发一次最普通的 **GET** 请求，拿回服务器响应。  
**练什么：** 认识「请求 → 响应」的最小闭环；返回 JSON 里的 `headers`、`url`、`args` 就是服务器看到的你这次请求的摘要。  
**以后用在哪：** 调任何「查询类」API（查列表、查详情）都是 GET。

2. 带参数查询
```
curl "https://httpbin.org/get?course=security&week=1"
```
**作用：** 在 URL 里用 `?k=v&k2=v2` 传**查询参数**。  
**练什么：** 看返回的 `args` 里变成了 `{"course":"security","week":"1"}`——参数是 URL 的一部分，服务器从 query string 里读。  
**以后用在哪：** 搜索、分页 `?page=1&size=10`、筛选，全是这个格式。

3. 自定义请求头
```
curl -H "X-Practice:day2" https://httpbin.org/get
```
**作用：** 往请求里加一个**自定义 Header**。  
**练什么：** Header 是「随请求一起带上的元信息」，服务器能在 `headers` 里读到 `X-Practice`。  
**以后用在哪：** 业务自定义头（如 `X-Request-Id`）、后面要学的 `Authorization`、`User-Agent`、`Content-Type` 都是 Header。

4. User-Agent
```
curl -A "MyStudyBot/1.0" https://httpbin.org/get
```
**作用：** `-A` 就是专门改 **`User-Agent`** 这个头，表明「我是谁（客户端是什么）」。  
**练什么：** 看返回里 `User-Agent` 变成了你写的值。爬虫、接口风控经常看这个字段。  
**以后用在哪：** 写爬虫要伪装浏览器 UA；服务端日志/限流也会按 UA 识别客户端。

5. POST JSON
```
curl -X POST https://httpbin.org/post -H "Content-Type:application/json" -d "{\"title\":\"book1\",\"page\":100}" 
```


6. POST表单
```
curl -X POST https://httpbin.org/post -d "username=demo&password=123"
```
**作用：** 用 **POST** 提交**表单格式**的请求体（`key=value&key2=value2`）。  
**练什么：** GET 和 POST 的分工——GET 用来「读」，POST 用来「交数据、创建资源」；`-d` 里的内容进 **body**，不进 URL。  
**以后用在哪：** 传统网页登录表单、部分后端接收 `application/x-www-form-urlencoded`。

7. 查看状态码
```
curl -o nul -s -w "%{http_code}\n" https://httpbin.org/status/200
curl -o nul -s -w "%{http_code}\n" https://httpbin.org/status/404
curl -o nul -s -w "%{http_code}\n" https://httpbin.org/status/503
```
**作用：** 不打印响应正文，**只打印 HTTP 状态码**。  
**练什么：**

|码|含义|记法|
|---|---|---|
|200|成功|OK|
|404|资源不存在|客户端路径问题|
|503|服务暂不可用|服务端/依赖挂了|

**以后用在哪：** 写脚本/测试时靠状态码判断成败（后面 pytest 测 API 全靠它）；排错先看码再看 body。

8. 带Cookie
```
curl -c cookies.txt -b cookies.txt https://httpbin.org/cookies/set/session/demo1
curl -b cookies.txt https://httpbin.org/cookies
```
**作用：**

- `-c cookies.txt`：把服务器**下发的 Cookie 存进文件**
- `-b cookies.txt`：再请求时**自动带上**该文件里的 Cookie

**练什么：** Cookie 是「服务器发给你的小票，下次请求你再出示」——**跨请求保持状态**。  
**以后用在哪：** 浏览器登录态、Session 的载体；你后端课里 JWT vs Session 对比，Cookie 就是 Session 常见的存放处。

9. 看完整响应头
```
curl -I https://httpbin.org/get
```
**作用：** 只看（或额外打印）**响应头**：`Content-Type`、`Server`、`Set-Cookie` 等。  
**练什么：** 响应头和请求头一样重要——正文是什么类型、有没有重定向、有没有下 Cookie，都在头里。  
**以后用在哪：** 调接口时先看 `Content-Type` 是不是 JSON；排查 CORS、缓存、压缩等问题都看响应头。

10. Bearer Token模拟登录后请求
```
curl -H "Authorization:Bearer fake-token-day2" https://httpbin.org/bearer
```
**作用：** 用标准方式携带**登录凭证**；不带则应 **401 Unauthorized**。  
**练什么：**

- 带了 `Authorization: Bearer xxx` → 认证通过的形状
- 不带 → 401 = 「你没登录/凭证无效」  
    **以后用在哪：** 你第 3~4 周 FastAPI 登录后，前端每次请求都会长这个样子；和 ⑧ 的 Cookie 登录是**两条流派**（Cookie 会话 vs Token 无状态）

## 怎么用

①② 方法+参数 → GET 怎么读数据 
⑥ POST body → 怎么提交数据 
③④⑩ 各种 Header → 元信息 / UA / 鉴权 
⑧ Cookie → 有状态的登录 
⑦⑨ 状态码+响应头 → 怎么判断成功、服务器告诉你什么
对照 ⑥：同样是 POST，**body 形状和 Header** 不同——⑥ 是表单，⑤ 是 JSON，这是 Day 3 写 API 前最有用的一组对比。
## 报错与坑
（没有就删掉这栏）

## 相关