from blocks import Block, solid_group
from globals import a_g
floor = Block((0, a_g['size'][1] - 30), (a_g['size'][0], 30), None, (255, 255, 255))

solid_group.add(floor)

test_platform_1 = Block((0.2 * a_g['size'][0], 0.85 * a_g['size'][1]), (200, 50), None, (100, 100, 100), None)

solid_group.add(test_platform_1)

test_platform_2 = Block((0.4 * a_g['size'][0], 0.8 * a_g['size'][1]), (200, 50), None, (100, 100, 100), None)

solid_group.add(test_platform_2)

test_platform_3 = Block((0.6 * a_g['size'][0], 0.75 * a_g['size'][1]), (200, 50), None, (100, 100, 100), None)

solid_group.add(test_platform_3)

goal = Block((a_g['size'][0] - 50, a_g['size'][1] - (50 + floor.dimensions[1])), (50, 50), None, (250, 0, 0), 'end')

solid_group.add(goal)