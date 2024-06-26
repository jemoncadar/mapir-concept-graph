export RAVH_ROOT=/home/ubuntu/tfg_jesus_moncada_ramirez/Datasets/RobotAtVirtualHome
export CG_FOLDER=/home/ubuntu/tfg_jesus_moncada_ramirez/Repos/concept-graphs/
export RAVH_CONFIG_PATH=${CG_FOLDER}/conceptgraph/dataset/dataconfigs/robotatvirtualhome/robotatvirtualhome.yaml

export SCENE_NAME=living_room_home30

python $CG_FOLDER/conceptgraph/scripts/run_slam_rgb.py \
  --dataset_root $RAVH_ROOT \
  --dataset_config $RAVH_CONFIG_PATH \
  --scene_id $SCENE_NAME \
  --image_height 480 \
  --image_width 640 \
  --stride 5 \
  --device cuda:1 \
  --save_pcd \
  --end 100 \
  --visualize
