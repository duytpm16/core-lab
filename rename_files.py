import glob
import itertools
import os
import re
import shutil


def main():
    jpgs = glob.glob("*.jpg")
    prefixes = set([jpg.split(sep="_")[0] for jpg in jpgs])

    for prefix in prefixes:
        os.mkdir(prefix)
        for image in glob.glob(prefix + "*.jpg"):
            shutil.copy(image, prefix)

        os.chdir(prefix)

        image_names  = glob.glob(prefix + "*.jpg")
        image_prefix = prefix.split(sep="-")[-1]
        image_prefix = re.sub("P", ".", image_prefix)
        
        new_names  = [image_prefix + "-" + str(i).zfill(4) + ".jpg" for i in range(1, len(image_names) + 1)]
        for i, j in zip(image_names, new_names):
            os.rename(i, j)

        os.chdir("../")

if __name__ == "__main__":
    main()