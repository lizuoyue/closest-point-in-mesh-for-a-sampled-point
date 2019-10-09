g++ -std=c++11 sample_points.cpp -o sample_points -lpthread
MESH_ROOT="../Replica-Dataset/replica_v1/"
for SCENE_NAME in $(ls ${MESH_ROOT})
do
	MESH_FILE=${MESH_ROOT}${SCENE_NAME}"/mesh.ply"
	mkdir -p ${SCENE_NAME}
	echo ${SCENE_NAME}
	echo ${MESH_FILE}
	./sample_points -f ${MESH_FILE} -d 5000 -o ${SCENE_NAME} -p 0.05 -v 10
done
