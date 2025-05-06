old position = current position
move character according to its x speed and y speed
collision = (check for collision between actor and all solids) #collision contains all solids colliding with actor
grounded = false #resets grounded state every loop
for all solids in collision: #cycles through all solids colliding with actor and runs following logic on them
    current position = old position #The if statement is no longer necessary because this instruction will be skipped if there's no collision
    if horizontal edges of character sprite are between edges of solid and bottom of actor is above top of solid:
        grounded = True
        y speed = 0


fn air_time(timer ,on_ground):
    if player is grounded:
        jump_start = timer
    return timer – jump_start

if (grav_value * air_time(pygame.time.get_ticks(), self.grounded)) ** 1.6 >= 35:
    self.gravity) = 35
else:
    self.gravity = (grav_value * air_time(pygame.time.get_ticks(), self.grounded)) ** 1.6