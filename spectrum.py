from phue import Bridge, Light
from random import random
from time import sleep

b = Bridge('192.168.251.50')  # Enter bridge IP here.

# If running for the first time, press button on bridge and run with b.connect() uncommented
# b.connect()


def slowchange(bridge, new_color_xy, light_id=None):
    if light_id:
        lights = [Light(bridge, light_id)]
    else:
        lights = bridge.get_light_objects()

    if not lights:
        return False

    for light in lights:
        old_x, old_y = light.xy
        break

    new_x, new_y = new_color_xy
    step = 1
    if old_x > new_x:
        step = -1
    for x in range(int(old_x*1000), int(new_x*1000), step):
        for light in lights:
            sleep(0.001)
            light.xy = [x/1000, old_y]

    step = 1
    if old_y > new_y:
        step = -1
    for y in range(int(old_y*1000), int(new_y*1000), step):
        for light in lights:
            sleep(0.001)
            light.xy = [new_x, y/1000]

while True:
    newcolor = [random(), random()]
    print("Change color to %s" % newcolor)
    slowchange(b, newcolor, 1)
