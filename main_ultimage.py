import argparse
import json
import dataio.load_image as load
import dataio.save_image as save
import processing.crop as crop
import processing.rotate as rotate
import processing.resize as resize
import processing.textover as text
import sys

def main():
    # create parser object
    parser = argparse.ArgumentParser(description="Basic command line interface for ultimage")
    # add basic arguments
    parser.add_argument('-v','--version', action='store_true', help='Show software version')
    parser.add_argument("-n", "--noshow", action="store_true", help="Stops the display of the image.")
    parser.add_argument("-s", "--save", action="store_true", help="Saves the image to the output directory.")
    # add arguments for the image and the operations
    parser.add_argument("-i", "--in_path", type=str, help="The path to the image file.")
    parser.add_argument("-o", "--out_path", type=str, help="The path to the output file.")
    parser.add_argument("-r", "--rotate", type=float, help="The angle of rotation in degrees.")
    parser.add_argument("-m", "--mirror", type=int, choices=[-1,1], help="The axis of mirroring (-1 for vertical, 1 for horizontal).")
    parser.add_argument("-c", "--crop", nargs=4, type=int, help="The coordinates of the crop region in the form [x_start, x_end, y_start, y_end].")
    parser.add_argument("-rs", "--scale", type=float, help="The factor to rescale the image by (out of 1).")
    parser.add_argument("-t", "--text", nargs=5, type=str, help="The text to overlay on the image, the coordinates, and font size and color in the form ['text' left top color size].")    

    # parse arguments
    args = parser.parse_args()

    # show version
    if args.version:
        with open('VERSION', 'r') as file:
            v = file.read()
            print(f"ultimage version {v}")
            sys.exit(0)
    else:
        # load image
        if args.in_path:
            image = load.load_image(args.in_path)
        else:
            print("No image path provided. Using demo data")
            demo_image = load.load_test_image_metadata()
            image = load.load_image(demo_image['path'])
        new_image = image.copy()

        # perform operations
        if args.rotate:
            new_image = rotate.rotate_image(new_image, args.rotate)
        if args.mirror:
            new_image = rotate.mirror_image(new_image, args.mirror)
        if args.crop:
            new_image = crop.image_crop(new_image, args.crop)
        if args.scale:
            if args.scale > 1:
                new_image = resize.enlarge(new_image, args.scale)
            else:
                new_image = resize.shrink(new_image, 1/args.scale)
        if args.text:
            new_image = text.textover(new_image, args.text[0], int(args.text[1]), int(args.text[2]), color=args.text[3], fsize=int(args.text[4]))
        # show image
        if not args.noshow:
            load.show_image(image)
            if new_image is not None:
                load.show_image(new_image)
        # save image
        if args.save:
            print(f"Saving image to: {args.out_path}")
            save.save_image(new_image, args.out_path)

if __name__ == "__main__":
    main()
