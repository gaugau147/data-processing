import os
import shutil
import imagehash
import csv
import argparse
from tqdm import tqdm

from PIL import Image
from skimage.metrics import peak_signal_noise_ratio as psnr
from pathlib import Path




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-image', type=str, required=True, help='path to image')
    parser.add_argument('-dataset', type=str, required=True, help='path to dataset')
    parser.add_argument('-isSave', action='store_true', help='save similar image or just list out their name')
    parser.add_argument('-save_path', type=str, help='path to save similar images')
    parser.add_argument('-threshold', type=int, default=5, help='5 is a good threshold, lower score is a more strict threshold')
    args = parser.parse_args()

    original_img = imagehash.average_hash(Image.open(args.image))
    img_name = Path(args.image).name
    

    img_list = sorted([img for img in os.listdir(args.dataset) if os.path.splitext(img)[1] in ['.jpg', '.jpeg']])
    for img in img_list:
        if img_name[:9] not in img:
            img_list.remove(img)

    if args.isSave:
        if args.save_path == None:
            save_path = 'similar_' + img_name[:-5]
        else:
            save_path = args.save_path
        if os.path.exists(save_path):
            shutil.rmtree(save_path)
        os.makedirs(save_path, exist_ok=True)
        shutil.copy(args.image, save_path)

    with open('similar_' + img_name[:-5] + '.csv', 'w', newline='') as csvfile:
        fieldnames = ['path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for img in tqdm(img_list):
            image = imagehash.average_hash(Image.open(os.path.join(args.dataset, img)))
            score = original_img - image
            if score < args.threshold:
                writer.writerow({
                'path': os.path.join(args.dataset, img)
                })
                
                if args.isSave:
                    shutil.copy(os.path.join(args.dataset, img), save_path)