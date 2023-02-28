import time 
import asyncio
import rich
from rich.panel import Panel

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        rich.print(
            Panel.fit(f"[yellow]Time: {func.__name__}, {end_time - start_time}", style="yellow")
        )
        return result
    return wrapper 

def async_time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = asyncio.run(func(*args, **kwargs))
        end_time = time.time()
        rich.print(
            Panel.fit(
                f"[yellow]Time: {func.__name__}, {end_time - start_time}",
                 style="yellow"
            )
        )
        return result
    return wrapper

