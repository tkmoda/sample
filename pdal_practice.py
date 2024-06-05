# import laspy
import open3d, laspy, pdal
# import open3d.visualization

##リサンプリング
json = r"""{
    "pipeline": [
        {
            "type": "readers.pts",
            "filename": "./data/ShibuyaUnderground.pts"
        },
        {
            "type": "filters.decimation",
            "step": 5
        },
        {
            "type": "writers.pcd",
            "filename":"./data/ShibuyaUnderground_resample.pcd"
        }    
        ]
}"""

##GeoTIFF化
# json = r"""{
#     "pipeline": [
#         "./data/ShibuyaUnderground.pts",
#         {
#             "type": "filters.reprojection",
#             "out_srs": "EPSG:6677"
#         },
#         {
#             "type": "filters.faceraster",
#             "resolution": 1
#         },
#         {
#             "type": "writers.gdal",
#             "gdaldriver": "GTiff",
#             "output_type": "all",
#             "resolution": "1.0"
#             "filename":"./data/ShibuyaUnderground-gtiff.tif"
#         }    
#         ]
# }"""

##TIFF化
# json = r"""{
#     "pipeline": [
#         "./data/ShibuyaUnderground.pts",
#         {
#             "type": "filters.reprojection",
#             "out_srs": "EPSG:6677"
#         },
#         {
#             "type": "filters.faceraster",
#             "resolution": 1
#         },
#         {
#             "type": "writers.raster",
#             "filename":"./data/ShibuyaUnderground.tif"
#         }    
#         ]
# }"""
pipeline = pdal.Pipeline(json)
count = pipeline.execute()
arrays = pipeline.arrays
metadata = pipeline.metadata
log = pipeline.log

print(count)
print(arrays)
print(metadata)
print(log)