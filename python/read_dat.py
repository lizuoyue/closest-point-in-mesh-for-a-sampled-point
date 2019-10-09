import numpy as np
from plyfile import PlyData, PlyElement

def l2dist(p1, p2):
	diff = p1 - p2
	return np.sqrt(diff.dot(diff))

points = np.fromfile('../scene_hotel_0/point_coordinate.dat', np.float32).reshape((-1, 3))
c_points = np.fromfile('../scene_hotel_0/nearest_point_in_mesh.dat', np.float32).reshape((-1, 3))
dist = np.fromfile('../scene_hotel_0/distance_to_mesh.dat', np.float32)
fid = np.fromfile('../scene_hotel_0/nearest_face_index.dat', np.int32)

print(points.shape)
print(c_points.shape)
print(dist.shape)
print(fid.shape)

plydata = PlyData.read('my_output_file.ply')
mesh_vertex = plydata.elements[0].data
mesh_face = plydata.elements[1].data

for i in range(5):
	print('points:   ', points[i])
	print('closest:  ', c_points[i])
	print('distance: ', dist[i])
	print('l2dist:   ', l2dist(points[i], c_points[i]))
	print('face id:  ', fid[i])
	for pid in mesh_face[fid[i]]:
		print(mesh_vertex[pid])
	print('============')