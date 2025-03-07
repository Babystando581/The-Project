import time
import asyncio
import tracemalloc

tracemalloc.start()

on_ground = False

jump_start = 0


def air_time(timer):
    global jump_start
    if on_ground is True:
        jump_start = timer

    return timer - jump_start


def jumping_bodge(x):
    global on_ground
    on_ground = x

# async def wait(s):
#    await asyncio.sleep(s)
#    print(s)

# print(y := 2 * (a := 5 * (c := 5)))
