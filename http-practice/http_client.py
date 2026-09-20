# 只封装常用旋钮

import requests

DEFAULT_TIMEOUT = 10
DEFAULT_HEADERS = {"User_Agent":"MyStudyBot/1.0"}

def get(url,params=None,headers=None,timeout=DEFAULT_TIMEOUT):
    """GET，并带上默认 UA；出错时抛出异常给调用方。"""
    h = {**DEFAULT_HEADERS,**(headers or {})}
    resp = requests.get(url,params=params,headers=h,timeout=timeout)
    return resp

def post_json(url,payload,headers=None,timeout=DEFAULT_TIMEOUT):
    """POST JSON，返回 Response。"""
    h={**DEFAULT_HEADERS,"Content-type":"application/json",**(headers or {})}
    # 说明：用 json= 参数时 requests 会自己设 Content-Type；
    # 这里显式写一遍是为了让你看清楚实际发出的头。
    resp= requests.post(url,json=payload,headers=h,timeout=timeout)
    return resp

def raise_for_status(resp):
    """4xx/5xx 直接抛 HTTPError，避免静默失败。"""
    resp.raise_for_status()
    return resp

