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

path = '../../data/panos/lazare_225'
output_dir = './cluster'
csv_path = './cluster.csv'
print(os.walk(path))

cluster_result = []

with open(csv_path, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
    	cluster_result.append(row)
    	# print(row)

for i in cluster_result:

	if not os.path.exists(os.path.join(output_dir, i[0])):
		os.makedirs(os.path.join(output_dir, i[0]))
	copyfile(os.path.join(path, i[1] + '.png'), os.path.join(output_dir, i[0], i[1] + '.png'))

# for item in os.walk(path):
# 	if item[0][-4:] == 'pano':
# 		file = os.listdir(item[0])[0]
# 		print(file)
# 		copyfile(os.path.join(item[0], file), os.path.join(output_dir, item[0].split('/')[-2] + '.png'))


