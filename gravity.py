jump_start = 0


def air_time(timer ,on_ground):
    global jump_start
    if on_ground is True:
        jump_start = timer
    return timer - jump_start

# def grounded_check(x):
#    global on_ground
#    on_ground = x