import os
import glob

target = '../dataset/L2R_Bicycle'
os.makedirs(target, exist_ok = True)

for item in glob.glob('../Replica-Dataset/replica_v1/*'):
	print(item + '/mesh.ply')