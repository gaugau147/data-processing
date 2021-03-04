### Install requirements
```bash
pip install -r requirements.txt
```

### Flow
 - Specify image path

 - Look for similar image and list to a csv file:
```bash
python find_similar.py -image=<path_to_image> -dataset=<path_to_data> -threshold=<threshold>
```
 
 - Also copy similar image to another folder:
```bash
python find_similar.py -image=<path_to_image> -dataset=<path_to_data> -isSave -save_path=<path_to_save_dir> -threshold=5
```
 - `threshold = 5` is a good start, smaller threshold means stricter threshold.
 - `dataset` should be `0-normal` etc., not `dataset/`.

### Algorithm
Imagehash is used for a fast transformation and comparision.

