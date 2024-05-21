import argparse
import dataio.load_image as load_image
import processing.crop as crop
import processing.rotate as rotate
import processing.resize as resize

def main():
    # create parser object
    parser = argparse.ArgumentParser(description="Basic command line interface for the ultimage package.")

    # required arguments
    parser.add_argument("image_path", type=str, help="The path to the image file.")
    parser.add_argument("operation", type=str, help="The operation to be performed", choices=["rotate", "crop", "resize"])

    # optional arguments for operation
    parser.add_argument("-n", "--noshow", action="store_true", help="Stops the display of the image.")
    parser.add_argument("--angle", type=int, help="The angle of rotation in degrees (only for rotate operation).")
    parser.add_argument("--coords", nargs=4, type=list, help="The coordinates of the crop region in the form [x_start, x_end, y_start, y_end] (only for crop operation).")
    parser.add_argument("--scale", type=float, help="The scaling factor (only for resize operation).")    

    # parse arguments
    args = parser.parse_args()

    # load image
    image = load_image.load_image(args.image_path)

    # perform operation
    if args.operation == "rotate":
        new_image = rotate.rotate_image(image, args.angle)
    elif args.operation == "crop":
        if len(args.coords) != 4:
            raise ValueError("Crop argument must have 4 values.")
        else:
            new_image = crop.image_crop(image, args.coords[0], args.coords[1], args.coords[2], args.coords[3])
    elif args.operation == "resize":
        if args.scale <= 0:
            raise ValueError("Scale factor must be greater than 0.")
        elif args.scale > 1:
            new_image = resize.enlarge(image, args.scale)
        else:
            new_image = resize.shrink(image, 1/args.scale)

    # show image
    if not args.noshow:
        load_image.show_image(image)
        load_image.show_image(new_image)

if __name__ == "__main__":
    main()
