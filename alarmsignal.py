from phue import Bridge, Light
import time

b = Bridge('192.168.7.214')  # Enter bridge IP here.

# If running for the first time, press button on bridge and run with b.connect() uncommented
# b.connect()


def alarmsignal(bridge, light_id, color_xy=[0.675, 0.305]):
    light = Light(bridge, light_id)

    old_brightness = light.brightness
    old_xy = light.xy
    print(old_xy)

    light.xy = color_xy
    for i in range(0, 5):
        light.brightness = 254
        time.sleep(0.3)
        light.brightness = 1
        time.sleep(0.5)

    light.brightness = old_brightness
    light.xy = old_xy


pink = [0.3936, 0.1778]
alarmsignal(b, 1)
