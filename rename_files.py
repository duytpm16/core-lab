import argparse
import glob
import itertools
import os
import re
import shutil


class Rename():
    def __init__(self, source, image_type, n_replace):
        os.chdir(source)
        if (image_type == "SEMP"):
            self.semp_images(n_replace)

    def semp_images(self, n):
        jpgs = glob.glob("*.jpg")
        pre  = [jpg.replace("_", "-", n).split(sep="_")[0] for jpg in jpgs]
        jpgs = [(pre[i], jpgs[i]) for i in range(0, len(jpgs))]
        
        for prefix, group in itertools.groupby(jpgs, lambda x : x[0]):
            os.mkdir(prefix)
            image_prefix = prefix.split(sep="-")[-1]
            image_prefix = re.sub("P", ".", image_prefix)

            files = list(group)
            for file, i in zip(files, range(1, len(files) + 1)):
                shutil.copy(file[1], prefix)
                os.rename(prefix + "/" + file[1], prefix + "/" + image_prefix + "-" + str(i).zfill(4) + ".jpg")

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image-type', type=str, required=True, metavar="", choices=["SEMP"], help="Type of images in the source directory. Currently available: 'SEMP'")
    parser.add_argument('--n-replace', type=int, required=False, default=0, metavar="", help="The number of times '_' needs to be replaced by '-' starting from the first occurence.")
    parser.add_argument('--source', type=str, required=True, metavar="", help="Path to the source directory.")

    args = parser.parse_args()
    Rename(args.source, args.image_type, args.n_replace)