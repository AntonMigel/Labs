[![License CC BY-NC-SA 4.0](https://img.shields.io/badge/license-CC4.0-blue.svg)](https://raw.githubusercontent.com/AlexanderSoroka/CNN-XRay.git/master/LICENSE.md)

# X-Ray chest images classification

The goal of that lab is to create CNN that classifies x-ray chest images

Pre-requisites:
1. TensorFlow 1.14 environment

Steps to reproduce results:
1. Clone the repository:
```
git clone git@github.com:AlexanderSoroka/CNN-XRay.git
```
2. Download [Kaggle chest xray pneumonia](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) and unpack it
3. Generate TFRecords with build_image_data.py script:

```
python build_image_data.py --input /work/datasets/chest_xray/ --output /tmp/xray
```

Validate that total size of generated tfrecord files is close ot original dataset size

4. Run train.py to train pre-defined CNN:
```
python train.py --train '/tmp/xray/train*' --test '/tmp/xray/test*
```

5. Modify model and have fun

### [License](https://raw.githubusercontent.com/AlexanderSoroka/CNN-ArtWorks/master/LICENSE.md)

Copyright (C) 2020 Alexander Soroka.

All rights reserved.
Licensed under the [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) (**Attribution-NonCommercial-ShareAlike 4.0 International**)

The code is released for academic research use only. For commercial use, please contact [soroka.a.m@gmail.com](soroka.a.m@gmail.com).
