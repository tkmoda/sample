# import laspy
import open3d, laspy
# import open3d.visualization

path = r"C:\Users\takumi\Documents\pointcloud\ShibuyaUnderground.pts"

pc = open3d.io.read_point_cloud(path)
pc_downsample = pc.uniform_down_sample(every_k_points=100)
pc_downsample.estimate_normals(search_param=open3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
open3d.visualization.draw_geometries([pc,pc_downsample],point_show_normal=True)
