import os
import shutil
import random
import argparse
from datetime import datetime
from tqdm import tqdm



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-dataset', type=str, required=True, help='path to dataset which includes all classes')
    parser.add_argument('-save_path', type=str, help='path to save similar images')
    parser.add_argument('-dtypes_1', type=str, default='soil dirt tape water', help='camera degradation types, please use spaces only')
    parser.add_argument('-dtypes_2', type=str, default='glare fog rain', help='environment degradation types, please use spaces only')
    parser.add_argument('-num_img', type=int, required=True, help='number of images in dataset')
    args = parser.parse_args()

    dataset = args.dataset
    folders = sorted([f for f in os.listdir(dataset) if os.path.isdir(os.path.join(dataset, f))])
    dtype_camera = args.dtypes_1.split()
    dtype_env = args.dtypes_2.split()
    num_imgs = int(args.num_img/3)

    if args.save_path == None:
        save_path = 'data' + datetime.now().strftime('%d-%b-%H-%M-%S')
    else:
        save_path = args.save_path
    
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
    os.makedirs(save_path, exist_ok=True)

    for folder in tqdm(folders):
        images_list = sorted([img for img in os.listdir(os.path.join(dataset, folder)) if os.path.isfile(os.path.join(dataset, folder, img))])
        
        os.makedirs(os.path.join(save_path, folder))

        if '0' in folder:
            imgs = random.sample(images_list, num_imgs)
            for img in imgs:
                shutil.copy(os.path.join(dataset, folder, img), os.path.join(save_path, folder))

        if '1' in folder:
            for dtype in dtype_camera:
                dtype_image_list = sorted([img for img in images_list if dtype in img])
                if len(dtype_image_list) > int(num_imgs/len(dtype_camera)):
                    imgs = random.sample(dtype_image_list, int(num_imgs/len(dtype_camera)))
                else:
                    imgs = dtype_image_list
                for img in imgs:
                    shutil.copy(os.path.join(dataset, folder, img), os.path.join(save_path, folder))
        if '2' in folder:
            for dtype in dtype_env:
                dtype_image_list = sorted([img for img in images_list if dtype in img])
                if len(dtype_image_list) > int(num_imgs/len(dtype_env)):
                    imgs = random.sample(dtype_image_list, int(num_imgs/len(dtype_env)))
                else:
                    imgs = dtype_image_list
                for img in imgs:
                    shutil.copy(os.path.join(dataset, folder, img), os.path.join(save_path, folder))
