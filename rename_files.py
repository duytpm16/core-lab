import glob
import itertools
import os
import re
import shutil


def main():
    jpgs = [(jpg.split(sep="_")[0], jpg) for jpg in glob.glob("*.jpg")]
    iter = itertools.groupby(jpgs, lambda x : x[0])
  
    for prefix, group in iter:
        os.mkdir(prefix)
        image_prefix = prefix.split(sep="-")[-1]
        image_prefix = re.sub("P", ".", image_prefix)

        i = 1
        for file in group:
            shutil.copy(file[1], prefix)
            os.rename(prefix + "/" + file[1], prefix + "/" + image_prefix + "-" + str(i).zfill(4) + ".jpg")
            i += 1

if __name__ == "__main__":
    main()