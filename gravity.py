on_ground = False

jump_start = 0


def air_time(timer):
    global jump_start
    if on_ground is True:
        jump_start = timer
        # print('not holding ', timer, jump_start)
    # else:
    # print('holding ',timer, jump_start)

    return timer - jump_start


def jumping_bodge(x):
    global on_ground
    on_ground = x


print(y := 2 * (a := 5 * (c := 5)))
