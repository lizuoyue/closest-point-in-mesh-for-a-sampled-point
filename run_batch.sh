g++ -std=c++11 sample_points.cpp -o sample_points -lpthread
for MESH_FOLDER in $(ls '../Replica-Dataset/replica_v1/')
do
	MESH_FILE=${MESH_FOLDER}"/mesh.ply"
	SCENE_NAME="scene_"$(basename ${MESH_FOLDER})
	mkdir ${SCENE_NAME}
	echo ${MESH_FILE}
	echo ${SCENE_NAME}
	./sample_points -f ${MESH_FILE} -d 5000 -o ${SCENE_NAME} -p 0.05 -v 10
done
