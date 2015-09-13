#!/usr/bin/env python

import os
from ..utils.common import read_list

datasets_root = os.path.join(os.path.dirname(__file__), '..')
imagenet_vdet_classes = read_list(os.path.join(datasets_root,
     'imagenet_vdet_classes.txt'))
imagenet_det_200_classes = read_list(os.path.join(datasets_root,
     'imagenet_det_200_classes.txt'))
