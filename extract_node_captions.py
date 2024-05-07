import argparse
import gzip
import pickle
from pathlib import Path

import numpy as np
from PIL import Image
from tqdm import tqdm

import slam.slam_classes
from utils.image_utils import crop_image_and_mask

MAP_FILE = "/home/ubuntu/tfg_jesus_moncada_ramirez/"


def load_scene_map(map_file_path: str):
    """
    TODO
    """
    scene_map = slam.slam_classes.MapObjectList()
    with gzip.open(Path(map_file_path), "rb") as file:

        loaded_data = pickle.load(file)

        if not isinstance(loaded_data, dict):
            raise ValueError("Map file is not a dictionary")
        if not "objects" in loaded_data:
            raise ValueError("Map file does not contain 'objects' key")

        scene_map.load_serializable(loaded_data["objects"])

        print(f"Loaded {len(scene_map)} objects from map file")

    return scene_map


def main(args):

    # Load the scene map
    scene_map = load_scene_map(map_file_path=args.map_file)

    for obj_idx, obj in tqdm(
        enumerate(scene_map), total=len(scene_map), desc="Iterating over objects..."
    ):  # for each object

        # Get images confidence
        conf = np.array(obj["conf"])

        # Get (first args.max_detections_per_object) most reliable detections
        det_idx_most_conf = np.argsort(conf)[::-1][: args.max_detections_per_object]

        # If less than two reliable detections, skip object
        if (len(det_idx_most_conf)) < 2:
            continue

        # Result variables
        # One caption per detection
        captions = list()
        # One low (True) or high (False) confidence per detection
        low_confidences = list()

        for det_idx in tqdm(det_idx_most_conf, desc="Iterating over detections..."):

            image = Image.open(obj["color_path"][det_idx]).convert("RGB")  # image
            xyxy = obj["xyxy"][det_idx]  # bounding box
            class_id = obj["class_id"][det_idx]  # object class
            # TODO: get class name
            mask = obj["mask"][det_idx]  # mask # TODO: what is the mask?

            cropped_image, cropped_mask = crop_image_and_mask(image, mask)
            # TODO: modify cropped_image!

            if cropped_image.size[0] * cropped_image.size[1] < 70 * 70:
                low_confidences.append(True)
                print(
                    f"Small object ({cropped_image.size[0] * cropped_image.size[1]}), low confidence"
                )
            else:
                low_confidences.append(False)

            # TODO: Gemini call, save result to "captions"
            captions.append("TODO")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="TODO: program description")

    parser.add_argument(
        "--map-file", "-m", type=str, required=True, help="Path to the map file"
    )

    parser.add_argument(  # TODO: help
        "--max-detections-per-object", "-d", type=int, default=10, help=""
    )

    args = parser.parse_args()

    main(args)
