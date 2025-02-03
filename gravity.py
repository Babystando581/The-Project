jumping = False

jump_start = 0


def air_time(timer):
    global jump_start
    if jumping is False:
        jump_start = timer
        print('not holding ', timer, jump_start)
    else:
        print('holding ',timer, jump_start)

    return timer - jump_start


def jumping_bodge(x):
    global jumping
    jumping = x
