### Install requirements
```bash
pip install -r requirements.txt
```

### Find similar images
 - Look for similar image and list to a csv file:
```bash
python find_similar.py -image=<path_to_image> -dataset=<path_to_data> -threshold=<threshold>
```
 
 - Also copy similar image to another folder:
```bash
python find_similar.py -image=<path_to_image> -dataset=<path_to_data> -isSave -save_path=<path_to_save_dir> -threshold=5
```

 - `threshold = 5` is a good start, smaller threshold means stricter threshold.
 - `dataset` should be `0-normal` etc., not the whole dataset.

`Algorithm`: `Imagehash` is used for a fast transformation and comparision.


### Make small dataset
```bash
python make_dataset.py -dataset=<path_to_big_dataset> -num_img=<num_imgs_of_small_dataset>
```

This script create a small dataset with the following degradation types:
 - `1-camera`: soil, dirt, tape, water
 - `2-environment`: glare, fog, rain

The below flags can be used to specify degradation types:
```bash
-dtypes_1='soil dirt tape water' -dtypes_2='glare fog rain'
```
`Note`: This algorithm uses filename to distingush between degradation types. Please make sure you named the images right.