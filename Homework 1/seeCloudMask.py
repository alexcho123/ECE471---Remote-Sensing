import os
import sys
import numpy as np
from osgeo import gdal

# Defining relative PATHs
GeoTIF_dir = "s2_santafe_spatially_aligned"
masked_dir = "cloudMasked"

images = []
labels = []
geoTransform = None
projection = None
for GeoTIF in os.listdir(GeoTIF_dir):
    labels.append(GeoTIF)
    dataset = gdal.Open(GeoTIF_dir + '\\' + GeoTIF)
    geoTransform = dataset.GetGeoTransform()
    projection = dataset.GetProjection()
    img = dataset.ReadAsArray()
    images.append(img)

output = []
print("Adding Cloud Mask...")
for image in images:
    bands, height, width = image.shape
    newImage = np.full((bands + 1, height, width), 65535)
    NDSI = np.zeros((height, width))
    ratio1 = np.zeros((height, width))
    ratio2 = np.zeros((height, width))
    ratio3 = np.zeros((height, width))
    newImage[:bands, :, :] = image
    for j in range(height):
        for k in range(width):
            if newImage[6, j, k] > 0:
                NDSI[j, k] = (newImage[1, j, k] - newImage[4, j, k]) / (newImage[1, j, k] + newImage[4, j, k])
                ratio1[j, k] = (newImage[2, j, k] - newImage[4, j, k]) / (newImage[2, j, k] + newImage[4, j, k])
                ratio2[j, k] = (newImage[2, j, k] - newImage[5, j, k]) / (newImage[2, j, k] + newImage[5, j, k])
                ratio3[j, k] = (newImage[3, j, k] - newImage[5, j, k]) / (newImage[3, j, k] + newImage[5, j, k])
                if -.15 <= ratio1[j, k] and -.15 <= ratio2[j, k] and ratio3[j, k] < .2 and NDSI[j, k] <= .4:
                    newImage[7, j, k] = 0
    output.append(newImage)

for image in output:
    _, height, width = image.shape
    for j in range(height):
        for k in range(width):
            image[6, j, k] = min(image[6, j, k], image[7, j, k])

try:
    os.mkdir(masked_dir)
except:
    sys.exit("Cloud Masked Data already exists")

print("Creating GeoTIFFs...")
for image, name in zip(output, labels):
    bands, height, width = image.shape
    bands -= 1
    driver = gdal.GetDriverByName('GTiff')
    tif = driver.Create(masked_dir + '\\' + name, width, height, bands, gdal.GDT_UInt16)
    tif.SetGeoTransform(geoTransform)
    tif.SetProjection(projection)
    for band in range(bands):
        tif.GetRasterBand(band + 1).WriteArray(image[band, :, :])
    tif.FlushCache()
    tif = None

print("Done")