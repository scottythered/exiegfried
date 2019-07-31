# exiegfried

**exiegfried** is a simple Python script to auto-generate parts of an Archival Information Package (AIP).

## What it Does
1. Give exiegfried a path to a folder of AIPs.
2. For each AIP, exigfried runs your installed versions of [ExifTool](https://www.sno.phy.queensu.ca/~phil/exiftool/) and [Siegfried](https://www.itforarchivists.com/siegfried/), a signature-based file format identification tool, on two of the AIP folders: "original content" and "fixity content."
3. CSV outputs from these two tools are saved in new folders: "original_fixty-content" and "processed_fixty-content."
4. ARCHIVAL PROFIT!

## NEW!
Two versions of exiegfried are now available: a standalone command-line script (*/script_version/*) and a GUI version built using the Gooey library (*/gui_version/*).

## Requirements
If you're running the standalone command-line script, make sure Pandas is installed; everything else is standard.

If you're running the GUI version, install the reqs provided in the GUI directory: ```pip install -r requirements.txt ```

In either case, you should have ExifTool and Siegfried installed and on your local PATH; if not, at least have them in the same directory as your exiegfried version.
