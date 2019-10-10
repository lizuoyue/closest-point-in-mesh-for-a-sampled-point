import tqdm
import os, glob
import numpy as np
from plyfile import PlyData, PlyElement

def almost0(num, t=1e-3):
	print(num)
	if np.abs(num) <= t:
		return True
	else:
		return False

def l2dist(p1, p2):
	diff = p1 - p2
	return np.sqrt(diff.dot(diff))

def common(p, li):
	l = np.array([[item[0], item[1], item[2], 1] for item in li])
	assert(almost0(np.linalg.det(l)))
	for i in range(4):
		lc = l.copy()
		lc[i, :3] = p
		assert(almost0(np.linalg.det(lc)))
	return

folders = glob.glob('../scene_*')
for folder in folders:
	points = np.fromfile(folder + '/point_coordinate.dat', np.float32).reshape((-1, 3))
	c_points = np.fromfile(folder + '/nearest_point_in_mesh.dat', np.float32).reshape((-1, 3))
	dist = np.fromfile(folder + '/distance_to_mesh.dat', np.float32)
	fid = np.fromfile(folder + '/nearest_face_index.dat', np.int32)
	ins_id = fid.copy()

	assert(points.shape[0] == c_points.shape[0])
	assert(points.shape[0] == dist.shape[0])
	assert(points.shape[0] == fid.shape[0])

	scene_name = os.path.basename(folder).replace('scene_', '')

	plydata = PlyData.read('../../Replica-Dataset/replica_v1/%s/habitat/mesh_semantic.ply' % scene_name)
	mesh_vertex = plydata.elements[0].data
	mesh_face = plydata.elements[1].data

	for i in tqdm.tqdm(range(points.shape[0])):
		assert(almost0(dist[i] - l2dist(points[i], c_points[i])))
		common(c_points[i], mesh_vertex[mesh_face[fid[i]][0]])
		ins_id[i] = mesh_face[fid[i]][1]



