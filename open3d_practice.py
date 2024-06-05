# import laspy
import open3d, laspy, pdal
import os
# import open3d.visualization

inputPath = os.path.join(os.getcwd(), r"data\ShibuyaUnderground_resample.pcd")
outputPath =  os.path.join(os.getcwd(), r"data\ShibuyaUnderground.las")
path = os.path.join(os.getcwd(), r"data\autzen.laz")

# pc = open3d.io.read_point_cloud(path)
pc = open3d.io.read_point_cloud(inputPath)
# open3d.visualization.draw_geometries([pc],width=900,height=600)
pc_downsample = pc.uniform_down_sample(every_k_points=1)
# pc_downsample = pc
pc_downsample.estimate_normals(search_param=open3d.geometry.KDTreeSearchParamHybrid(radius=1, max_nn=30))
open3d.visualization.draw_geometries([pc_downsample],width=900,height=600)
# open3d.visualization.draw_geometries([pc,pc_downsample],width=900,height=600,point_show_normal=True)

print(pc_downsample)
