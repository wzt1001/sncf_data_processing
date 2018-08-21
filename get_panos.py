import numpy as np
import psycopg2
import cv2
import csv
import PIL
import os
import random
from PIL import Image
import argparse
import pickle
from sklearn.utils import shuffle
from shutil import copyfile

path = '../data/images/lazare_225'
output_dir = '../data/panos/lazare_225'
print(os.walk(path))

if not os.path.exists(output_dir):
	os.makedirs(output_dir)

for item in os.walk(path):
	if item[0][-4:] == 'pano':
		file = os.listdir(item[0])[0]
		print(file)
		copyfile(os.path.join(item[0], file), os.path.join(output_dir, item[0].split('/')[-2] + '.png'))


