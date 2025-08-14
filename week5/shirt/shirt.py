from PIL import Image, ImageOps
import sys
import os


def main():
    if len(sys.argv) >3:
        print("Too many command-line arguments")
        sys.exit(1)

    if len(sys.argv) <3:
        print("Too few command-line arguments")
        sys.exit(1)

    infile, outfile = sys.argv[1], sys.argv[2]

    valid_exts = {".jpg", ".jpeg", ".png"}

    in_root, in_ext = os.path.splitext(infile.lower())
    out_root, out_ext = os.path.splitext(outfile.lower())

    if in_ext not in valid_exts:
        print("Invalid input")
        sys.exit(1)


    if out_ext not in valid_exts:
        print("Invalid output")
        sys.exit(1)

    if in_ext != out_ext:
        print("Input and output have different extensions")
        sys.exit(1)

    if not os.path.isfile(infile):
        print("Input does not exist")
        sys.exit(1)

    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        print("shirt.png not found")
        sys.exit(1)


    photo = Image.open(infile)
    photo = ImageOps.fit(photo, shirt.size)
    photo.paste(shirt, (0, 0), shirt)
    photo.save(outfile)





if __name__ == "__main__":
    main()