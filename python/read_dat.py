import numpy as np

points = np.fromfile('../scene_hotel_0/point_coordinate.dat', np.float32)
c_points = np.fromfile('../scene_hotel_0/nearest_point_in_mesh.dat', np.float32)
dist = np.fromfile('../scene_hotel_0/distance_to_mesh.dat', np.float32)
fid = np.fromfile('../scene_hotel_0/nearest_face_index.dat', np.int32)
print(points)
print(c_points)
print(dist)
print(fid)