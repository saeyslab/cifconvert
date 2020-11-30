# This package has been deprecated. Please use [ifcimglib](https://github.ugent.be/mlippeve/ifcimglib)

# cifconvert
`cifconvert` is a package built on the [python-bioformats](https://github.com/CellProfiler/python-bioformats) package that saves images and masks from the proprietary Amnis CIF-file format to an HDF5 file.

# Installation
## Requirements
Python

## Install
Clone this repository:
```
git clone https://github.com/saeyslab
```
Install dependencies using the pip package manager:
```
pip install -r requirements.txt
```
# Usage
This package has two functions:
- `cifconvert` for converting CIF-files to HDF5-files,
- and `cifmerge` for creating Virtual HDF5 Datasets from existing HDF5-files.

## `cifconvert`
```
usage: cifconvert [-h] [--channels [CHANNELS [CHANNELS ...]]] [--debug]
                  cif output width height

positional arguments:
  cif                   Input cif containing images.
  output                Output filename for h5.
  width                 Width to crop or padd images to.
  height                Height to crop or pad images to.

optional arguments:
  -h, --help            show this help message and exit
  --channels [CHANNELS [CHANNELS ...]], -c [CHANNELS [CHANNELS ...]]
                        Images from these channels will be extracted. Default
                        is to extract all.
  --debug               Show debugging information.
```
## cifmerge
```
usage: cifconvert [-h] output [h5s [h5s ...]]

positional arguments:
  output      Output filename for h5.
  h5s         h5 datasets to concatenate in virtual dataset.

optional arguments:
  -h, --help  show this help message and exit
```
