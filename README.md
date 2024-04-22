# cpre436x_final_project

> **NOTICE:** <br>
> Any reference to an individual or organization is purely coincidental. The information contained in this document is for educational purposes only. The "personal information" was randomly generated and does not represent any real person or organization.


## ExifTools
### Add Exif data to images
`exiftool -config ../config.config -XMP-xmp:SpreadSheetName="employee-2024" -SellRows=20 IMAGE_NAME`
`exiftool -config ../config.config -XMP-xmp:BuyerId="000000000 IMAGE_NAME`

### Read Exif data from images
`exiftool IMAGE_NAME`


## Image_steo.py
- Written to make the images used in the scenario
- Use --image to specify the image to hide the text in (REQUIRED)
- Can hide either a text file or typed text in the cli using -f:--file or -t:--text respectively
- Can write to new file name using the -o:--out_file flag (NOTE: If not provide the image will be written to the same file name)
- Can retrieve the hidden message using the -r:--retrieve flag

### Writing To Image
- `python image_steo.py --image START_IMAGE -f TEXT_FILE_TO_HIDE -o IMAGE_OUT_NAME`
- `python image_steo.py --image START_IMAGE -t "TEXT_TO_HIDE"`

# Setup
1. Clone repo
2. Create new Volume on VM
3. Add minium of the 4 provided image
   1. More images can be added to increase difficulty
4. Remove the drive letter from the volume

## Option Breadcrumbs
- Adding the `image_steo_breadcrumb.py` script to the desktop
  - Rename to fix scenario (Recommended: `work_script.py`)
- Images have exif metadata, so providing exiftool (Included) is a way to find the hidden message if there are more than the 4 provided images
