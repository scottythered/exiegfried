#!/usr/bin/env python
# coding: utf-8

import subprocess as sb
import json
import pandas as pd
import sys
import os
import io
from gooey import Gooey, GooeyParser


@Gooey(program_name='Exiegfried', default_size=(610, 350),
       disable_stop_button=True)
def main():
    desc = 'a simple Python script to auto-generate fixity content of '\
           'Archival Information Packages.'
    file_help_msg = 'Select a directory of AIPs to process'
    exiegfried_parser = GooeyParser(description=desc)
    exiegfried_parser.add_argument('Directory', help=file_help_msg,
                                   widget='DirChooser')
    args = exiegfried_parser.parse_args()

    directory = args.Directory
    contents = list_dir(directory)
    for item in contents:
        processor(directory, item, "2_", "original")
        processor(directory, item, "5_", "processed")


def list_dir(b):
    c = os.listdir(b)
    return c


def processor(w, x, y, z):
    if z == "original":
        folder_number = "3"
        folder_type = "original_fixty-content"
    elif z == "processed":
        folder_number = "6"
        folder_type = "processed_fixty-content"
    else:
        print("Your folder type isn't recognized. Shutting down.")
        sys.exit()
    extended_path = os.path.join(w, x)
    for folder in os.listdir(extended_path):
        if folder.startswith(y):
            ident = (folder.split("_")[1])[:-3]
            ident_number = folder.split("_")[2]
            new_folder = os.path.join(
                extended_path,
                "{0}_{1}aip_{2}_{3}".format(folder_number, ident, ident_number,
                                            folder_type))
            os.mkdir(new_folder)
            print("\n\nFolder created at: {0}\n\n".format(new_folder))
            folder_to_be_checked = os.path.join(extended_path, folder)
            exif_doc = os.path.join(new_folder, "{0}-exiftool.csv".format(z))
            sigf_doc = os.path.join(new_folder, "{0}-fileformats.csv".format(z))
            try:
                raw_exif = sb.check_output(
                    ["exiftool", "-j", "-r", folder_to_be_checked]
                )
                exif = json.loads(raw_exif.decode("utf-8"))
                df = pd.DataFrame(exif)
                df.to_csv(exif_doc, encoding="utf-8")
                print("\n\nExif data written to: {0}\n\n".format(exif_doc))
            except:
                print(
                    "'{0}' is empty, so there's no Exif data to write. "
                    "Skipping...".format(folder)
                )
            try:
                sigf = (
                    sb.check_output(
                        ["sf", "-droid", "-hash", "md5", folder_to_be_checked]
                    )
                ).decode("utf-8")
                sigf2 = 'id' + sigf[2:]
                with open(sigf_doc, "w") as f:
                    f.write(sigf2)
                print("File-format data written to: {0}\n\n".format(sigf_doc))
            except:
                print(
                    "'{0}' is empty, so there's no File-format data to write. "
                    "Skipping...".format(folder)
                )
        else:
            pass


if __name__ == "__main__":
    main()
