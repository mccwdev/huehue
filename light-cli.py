import argparse
from phue import Bridge, Light

b = Bridge('192.168.7.214')  # Enter bridge IP here.

# If running for the first time, press button on bridge and run with b.connect() uncommented
# b.connect()


def parse_args():
    parser = argparse.ArgumentParser(description='Command Line Control of Hue Lights')
    parser.add_argument('light_id', type=int, help='Light ID')
    parser.add_argument('command', nargs="?")
    parser.add_argument('argument', nargs="?")
    parser.add_argument('--quiet', nargs="?")
    return parser.parse_args()


def switchlight(bridge, light_id, lighton):
    light = Light(bridge, light_id)

    light.xy = [1, 1]
    if lighton:
        light.brightness = 255
    else:
        light.brightness = 0


if __name__ == '__main__':
    arg = parse_args()

    print("Light %d, command %s, argument %s" % (arg.light_id, arg.command, arg.argument))
    if not arg.argument:
        print(eval("b.get_light(%d, '%s')" % (arg.light_id, arg.command)))
    else:
        print(eval("b.set_light(%d, '%s', %s)" % (arg.light_id, arg.command, arg.argument)))
