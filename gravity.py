on_ground = False

jump_start = 0

repeated = 0

def air_time(timer):
    global jump_start
    global repeated
    if on_ground is True:
        jump_start = timer
        print('grounded state toggled',repeated)
        repeated += 1
    return timer - jump_start


def grounded_check(x):
    global on_ground
    on_ground = x
