import open3d as o3d
import numpy as np


def custom_draw_geometry(pcd):
    # The following code achieves the same effect as:
    # o3d.visualization.draw_geometries([pcd])
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()
    vis.destroy_window()


print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("../Open3D-master/examples/test_data/fragment.ply")
print(pcd)
custom_draw_geometry(pcd)
