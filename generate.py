#!/usr/bin/env python3
from subprocess import call
from shutil import which
import argparse
from os import path

config = [[512, "iTunesArtwork", "App list in iTunes"],
          [1024, "iTunesArtwork@2x", "App list in iTunes for devices with retina display"],
          [120, "Icon-60@2x.png", "Home screen on iPhone/iPod Touch with retina display"],
          [180, "Icon-60@3x.png", "Home screen on iPhone with retina HD display"],
          [76, "Icon-76.png", "Home screen on iPad"],
          [152, "Icon-76@2x.png", "Home screen on iPad with retina display"],
          [167, "Icon-83.5@2x.png", "Home screen on iPad Pro"],
          [20, "Icon-Small-20.png", "Notifications"],
          [40, "Icon-Small-20@2x.png", "Notifications on devices with retina display"],
          [60, "Icon-Small-20@3x.png", "Notifications on devices with retina display"],
          [40, "Icon-Small-40.png", "Spotlight"],
          [80, "Icon-Small-40@2x.png", "Spotlight on devices with retina display"],
          [120, "Icon-Small-40@3x.png", "Spotlight on devices with retina HD display"],
          [29, "Icon-Small.png", "Settings"],
          [58, "Icon-Small@2x.png", "Settings on devices with retina display"],
          [87, "Icon-Small@3x.png", "Settings on devices with retina HD display"]]

def resize(imagemagick, source, destination, size):
    return call([imagemagick, "-density", "400", "-background", "none", "-resize", "{0}x{0}".format(size), source, "png:"+destination])

def main():
    # Ensure imagemagick is in PATH
    imagemagick = which("convert")
    if imagemagick is None:
        print("Install imagemagick (e.g. `brew install imagemagick`) before running this script.")
        return
    epilog_format = "{0: <10} {1: <25} {2: <25}\n"
    epilog = "Will generate the following files: \n" + epilog_format.format("size", "filename", "description") + epilog_format.format("----", "--------", "-----------")
    for item in config:
        epilog = epilog + epilog_format.format("{0}x{0}".format(item[0]), item[1], item[2])
    parser = argparse.ArgumentParser(description="Generate icons for Xcode", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    parser.add_argument("source", type=str, help="source file")
    parser.add_argument("destination_dir", type=str, help="destination directory")
    args = parser.parse_args()
    print("Source = {0}".format(args.source))
    for item in config:
        destination = path.join(args.destination_dir, item[1])
        if resize(imagemagick, args.source, destination, item[0]) == 0:
            print("Created {0}".format(destination))

if __name__ == "__main__":
    main()
