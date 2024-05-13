# import laspy
import open3d, laspy

path = r"C:\Users\takumi\Documents\pointcloud\ShibuyaUnderground.pts"

pc = open3d.io.read_point_cloud(path)

