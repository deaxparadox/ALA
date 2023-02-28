import asyncio
import threading
import time 
from time import sleep
import requests
from requests import Response 
from bs4 import BeautifulSoup
import warnings
from queue import Queue 

from data.web.requests import AsyncRequest
from data.web.scrape import Parser, Domains, HTMLElements
from data.core import async_to_sync 

async def _filter_valid_link(links: list[str]):
    valids = []
    for link in links:
        link = link.split("/")
        for tld in Domains.TLD:
            if f".{tld}" in link:
                valids.append(link)
    
    for i in valids:
        yield i 





@async_to_sync 
async def _main(url):
    req = AsyncRequest(url)
    res: Response = await req.run()
    parsed: BeautifulSoup = await Parser(res).run()
    links_element = parsed.findall(HTMLElement.a)
    links = 


class Threaded(type):
    _q: Queue = Queue()
    _pause: bool = False 
    _qlock = threading.Lock()

    def __init__(self, workers: int|None = 0):
        if workers:
            self.__workers = worker
        warnings.warn("Worker requirement not found. Default to 1")

    def _check_queue_size(self):
        if self._q.qsize() > 100:
            self._pause = True
            print(
                f"Queue is full. Waiting for {self._q.qsize() - 100} more requests"
            )
        else:
            self._pause = False
    
    @classmethod
    def _filter(cls):
        while True:
            # check queue is empty
            # sleep 1 and try again
            if cls._q.empty():
                sleep(1)
                continue 
            
            # check queue size exceed 100 
            # _pause threads 
            # sleep 1 and try again
            if cls._pause:
                sleep(1)
                continue
            
            else:
                try:
                    cls._qlock.acquire()
                    url = q.get()
                    _main(url)
                except:
                    print(
                        "Unable to acquire lock\n"\
                            "trying again"
                    )
                finally:
                    cls._qlock.release()
            
            break 

    def _run(self):
        threads = list()
        for i in range(self.__workers):
            threads.append(
                threading.Thread(target=self._filter)
            )
        
        for t in threads:
            t.start()

        for t in threads:
            t.join()


def main():
    _main()


if __name__ == "__main__":
    main()