
import rich
from rich.panel import Panel
import bs4
import requests
from requests import Response
import asyncio
import queue
from enum import Enum

from .requests import Request
from ..core.error import ArgumentError



class Domains:
    TLD: list[str] = [
        "com",
        "in",
        "org",
        "io",
    ]

class HTMLElements:
    a: str = 'a'
    p: str = 'p'
    div: str = 'div'
    span: str ='span'
    img: str = 'img'
    li: str = 'li'
    ul: str = 'ul'
    ol: str = 'ol'
    h1: str = 'h1'
    h2: str = 'h2'
    h3: str = 'h3'
    h4: str = 'h4'
    h5: str = 'h5'
    h6: str = 'h6'
    hr: str = 'hr'
    table: str = 'table'
    tr: str = 'tr'
    td: str = 'td'
    th: str = 'th'
    form: str = 'form'
    input: str = 'input'
    textarea: str = 'textarea'
    select: str ='select'
    option: str = 'option'
    button: str = 'button'
    label: str = 'label'
    br: str = 'br'
    link: str = 'link'
    meta: str ='meta'
    style: str ='style'
    script: str ='script'
    noscript: str = 'noscript'
    iframe: str = 'iframe'
    embed: str = 'embed'


class Parser:
    """
    class Parse

    args: a[0]: markup or Repsonse object
    kwargs: {"markup": markup} or {"response": response}
    """

    _markup: str = None
    _response: Response  = None 
    _response_object: bool = False
    
    def __init__(self, *args, **kwargs):
        if len(args) == 0 and len(kwargs) == 0:
            raise ArgumentError("No argument found!")

        # if the argument is string then parser it
        
        # if the argument if requests.Response object 
        # then set the _response_object True 
        # extract reponse data 
        # and parse it 
        
        arg = args[0] 
        if isinstance(arg, str):
            self._markup = arg
        else:
            self._response = arg
            self._response_object = True

        try:
            _markup = kwargs.get('markup')
            if isinstance(_markup, str):
                self._markup = _markup
        except:
            _res = kwargs.get('response')
            if isinstance(_res, Response):
                self._response = _res
                self._response_object = True


    @property
    def markup(self):
        return self._markup

    @markup.setter
    def markup(self, *args, **kwargs):
        """
        :param args: (markup,)
        :param kwargs: {"markup": markup}
        """
        if len(args) > 0:
            self._markup, *_ = args
        else:
            _markup = kwargs.get('markup')
            if isinstance(_markup, str):
                self._markup = _markup
            else:
                raise ValueError("markup: required str")

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, *args, **kwargs):
        """
        :param args: (markup,)
        :param kwargs: {"markup": markup}
        """
        if len(args) > 0:
            self._response, *_ = args
        else:
            _response = kwargs.get('response')
            if isinstance(_response, Response):
                self._response = _response
            else:
                raise ValueError("response: required Response object")

    async def _check_markup(self):
        if not self._markup:
            raise ValueError("markup is None")

    async def parser(self) -> bs4.BeautifulSoup:
        """
        :return: bs4.BeautifulSoup
        """

        if self._response_object:
            soup: bs4.BeautifulSoup = bs4.BeautifulSoup(self._response.text, "html.parser")
            return soup    

        # parse the res markup
        soup: bs4.BeautifulSoup = bs4.BeautifulSoup(self._markup, "html.parser")
        return soup


    async def _main(self) -> bs4.BeautifulSoup:
        return await self.parser()

    
    async def run(self) -> bs4.BeautifulSoup:
        """
        :return: return the bs4.BeautifulSoup
        """
        return await self._main()


class Scrape(object):
    def __init__(self):
        pass 