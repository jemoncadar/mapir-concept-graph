export REPLICA_ROOT=/home/ubuntu/tfg_jesus_moncada_ramirez/Datasets/Replica/
export CG_FOLDER=/home/ubuntu/tfg_jesus_moncada_ramirez/Repos/concept-graphs/

export PKL_FILENAME=full_pcd_none_overlap_maskconf0.95_simsum1.2_dbscan.1_merge20_masksub_post.pkl.gz

export SCENE_NAME=room0

python  $CG_FOLDER/conceptgraph/scenegraph/build_scenegraph_cfslam.py \
    --mode build-scenegraph \
    --cachedir ${REPLICA_ROOT}/${SCENE_NAME}/sg_cache \
    --mapfile ${REPLICA_ROOT}/${SCENE_NAME}/pcd_saves/${PKL_FILENAME} \
    --class_names_file ${REPLICA_ROOT}/${SCENE_NAME}/gsa_classes_ram_withbg_allclasses.json