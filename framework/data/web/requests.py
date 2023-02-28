import rich
from rich.panel import Panel
import bs4
import requests
from requests import Response
import threading
import asyncio
import queue
from enum import Enum

   
class Request:
    """
    Request class

    Return a Response.

    Usage: 
    req = Request(url)
    res = req.run()

    or 

    req = Request()
    req.url = url 
    res = req.run()

    or 

    res = Request(url).run()
    

    """

    _url: str = None

    def __init__(self, url: str|None = None):
        self._url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, *args):
        self._url, *_ = args

    def _check_url(self):
        # if url is not set
        # raise ValueError
        if not self._url:
            raise ValueError("url is None")

    def _request(self) -> Response:
        self._check_url()
        return requests.get(self._url)

    def _main(self) -> Response:
        self._check_url()
        return self._request()

    
    def run(self) -> Response:
        return self._main()

   
class AsyncRequest:
    """
    Async Request class

    Return a Response.

    Usage: 
    req = Request(url)
    res = await req.run()

    or 

    req = Request()
    req.url = url 
    res = await req.run()

    or 

    res = await Request(url).run()
    

    """

    _url: str = None

    def __init__(self, url: str|None = None):
        self._url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, *args):
        self._url, *_ = args

    async def _check_url(self):
        # if url is not set
        # raise ValueError
        if not self._url:
            raise ValueError("url is None")

    async def _request(self) -> Response:
        await self._check_url()
        return requests.get(self._url)

    async def _main(self) -> Response:
        await self._check_url()
        return await self._request()

    
    async def run(self) -> Response:
        return await self._main()


class RequestOnThread:
    def __init__(self, urls: list[str]|None = None ):
        
        if isinstance(self._urls, list):
            self._urls = urls
        else:
            self._urls = urls

        self._q = queue.Queue()
        self._qlock = threading.Lock()

    @property
    def url(self):
        return self._url
    @url.setter
    def url(self, value):
        self._url = value

    def _ret_request(self, url: str):
        while self._ql.locked():
            continue 
        else:
            res = requests.get(self._url)
            self._q.put(res)

    def run(self) -> queue.Queue:
        threads = []
        for url in self._urls:
            threads.append(
                threading.Thread(target=self._ret_request, args=(url, ))
            )
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        
        return self._q