# Homework 1

## Task 1

In order to create a spatially aligned dataset, first the GeoJSON file was read, and a vector perimeter was extracted.
This vector was then sent to a function that cropped each GeoTIFF to fit within the given vector.
Then, a function was applied that iterated over the dataset, found the max absolute resolution (most granular resolution), and applied it to all the images in the dataset.
Resolution distributions were made, which indicated that roughly ~10% of the data existed around this most granular resolution, which is why it was used.
Data inferencing was avoided as much as possible.
A bilinear interpolation scheme was used so that surrounding "thrown-away" data was still incorporated.

## Task 2

#### Cloud Masking Algorithm

#### Finding the Greenest, Snowiest, Cloudiest, and Brightest Scenes

#### Creating Mean, Min, Max, Median, Greenest, and 85% Greenest Composites

#### Output

    Finding Greenest Scene...
    Greenest Scene: s2_santafe_spatially_aligned\sentinel-2_L1C_2018-09-04.tif
         Average NDVI: 0.23788154883969684
    Finding Snowiest Scene...
    Snowiest Scene: s2_santafe_spatially_aligned\sentinel-2_L1C_2018-12-30.tif
         Average NDSI: 0.7825624259627408
    Finding Cloudiest Scene...
    Cloudiest Scene: s2_santafe_spatially_aligned\sentinel-2_L1C_2018-11-10.tif
         Ratio of Cloud Masked Pixels: 0.8309104903140482
    Finding Brightest Scene...
    Brightest Scene: s2_santafe_spatially_aligned\sentinel-2_L1C_2018-12-30.tif
         Average Relative Luminance: 5766.51933394326
    Creating Mean Composite...
    Done, Output: composites\mean.tif
    Creating Min Composite...
    Done, Output: composites\min.tif
    Creating Max Composite...
    Done, Output: composites\max.tif
    Creating Median Composite...
    Done, Output: composites\median.tif
    Creating Greenest Composite...
    Done, Output: composites\greenest.tif
    Creating 85% Greenest Composite...
    Done, Output: composites\greenest85.tif