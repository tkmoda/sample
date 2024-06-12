# import laspy
import open3d, laspy, pdal
import os
import numpy as np
import matplotlib.pyplot as plt
# import open3d.visualization

inputPath = os.path.join(os.getcwd(), r"data\ShibuyaUnderground_resample.pcd")
outputPath =  os.path.join(os.getcwd(), r"data\ShibuyaUnderground.las")
path = os.path.join(os.getcwd(), r"data\autzen.laz")

# pc = open3d.io.read_point_cloud(path)
pc = open3d.io.read_point_cloud(inputPath)
# open3d.visualization.draw_geometries([pc],width=900,height=600)
pc_downsample = pc.uniform_down_sample(every_k_points=1)
# pc_downsample = pc
pc_downsample.estimate_normals(search_param=open3d.geometry.KDTreeSearchParamHybrid(radius=0.5, max_nn=20))

pc_downsample.colors = pc_downsample.normals

## DBSCANクラスタリング
labels = np.array(pc_downsample.cluster_dbscan(eps=0.5, min_points=10, print_progress=True))

# max_label = labels.max()
# print(f"point cloud has {max_label + 1} clusters")
# colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
# colors[labels < 0] = 0
# pc_downsample.colors = open3d.utility.Vector3dVector(colors[:, :3])

print(labels)


## DBSCAN改良
## 一定距離以内の法線ベクトルの内積を求め、平行に近い点群が一定以上あること

open3d.visualization.draw_geometries([pc_downsample],width=900,height=600)
# open3d.visualization.draw_geometries([pc,pc_downsample],width=900,height=600,point_show_normal=True)


