# exiegfried
**exiegfried** is a simple Python script to auto-generate parts of an Archival Information Package (AIP).

1. Give exiegfried a path to a folder of AIPs.
2. For each AIP, exigfried runs your installed versions of [ExifTool](https://www.sno.phy.queensu.ca/~phil/exiftool/) and [Siegfried](https://www.itforarchivists.com/siegfried/), a signature-based file format identification tool, on two of the AIP folders: "original content" and "fixity content."
3. CSV outputs from these two tools are saved in new folders: "original_fixty-content" and "processed_fixty-content."
4. ARCHIVAL PROFIT!

## Requirements
Have Pandas installed. Also, you should either have ExifTool and Siegfried installed and on your PATH; if not, at least have them in the same directory as exiegfried.

## Limitations
exiegfried was written for a group of Windows users, so you'll have to do some minor file-path editing to use it on a Unix-based system.
