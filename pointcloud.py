# import laspy
import open3d, laspy, pdal
# import open3d.visualization

inputPath = r"C:\Users\takumi\Documents\pointcloud\ShibuyaUnderground.pts"
outputPath = r"C:\Users\takumi\Documents\pointcloud\ShibuyaUnderground.las"
# path = r"C:\Users\takumi\Documents\pointcloud\autzen.laz"


# pc = open3d.io.read_point_cloud(path)
# pc_downsample = pc.uniform_down_sample(every_k_points=100)
# pc_downsample.estimate_normals(search_param=open3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
# open3d.visualization.draw_geometries([pc,pc_downsample],point_show_normal=True)

json = r"""{
    "pipeline": [
        "ShibuyaUnderground.pts",
        {
            "type": "filters.reprojection",
            "out_srs": "EPSG:6677"
        },
        {
            "type": "filters.faceraster",
            "resolution": 1
        },
        {
            "type": "writers.gdal",
            "gdaldriver": "GTiff",
            "output_type": "all",
            "resolution": "1.0"
            "filename":"ShibuyaUnderground-gtiff.tif"
        }    
        ]
}"""

# json = r"""{
#     "pipeline": [
#         "ShibuyaUnderground.pts",
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
#             "filename":"ShibuyaUnderground.tif"
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