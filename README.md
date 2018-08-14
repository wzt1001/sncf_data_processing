SNCF Data Processing
===========================

What is this project for?
------------
People get confused with station spaces. We are trying to use computer vision, specificly deep convolutional neural networks to train a model that could tell the location of a given image. Taking advantage of this model, we could do an spatial legibility evaluation based on the model. 

What is contained in this repo?
------------
The raw data contains LiDar and videos from a specially design device, which we deployed in Gare de Lyon and Gare St Lazare. The scripts here are to extract, clean and sort out data from this device for further training purpose.

How-to
------------

**video_capture.py**
frame extraction and cubic projection, saves all images in */top_9/left/*.png form
* usage
    1. '-f', '--framelist', default='lazare_frame_list', help='frame list table name'
    2. '-s', '--schema', default='gare_st_lazare', help='schema for the station'
    3. '-i', '--imagelist', default='images_225', help='image list table name'
    4. '-v', '--video', default='../data/videos/lazare.mp4', help='video path'
    5. '-o', '--output', default='../data/images/lazare_225', help='output image path'
    6. '-d', '--direction', default=22.5, type=float, help='direction as degree'
        
    ~~~~
    python video_capture.py -f lazare_frame_list -s gare_st_lazare -i images_225 -v ../data/videos/lazare.mp4 -o ../data/images/lazare_225 -d 0
    ~~~~

**video_spliting.py**
dividing as regenerate video samples as different categories
* usage
    1. '-f', '--framelist', default='lazare_frame_list', help='frame list table name'
    2. '-s', '--schema', default='gare_st_lazare', help='schema for the station'
    3. '-i', '--imagelist', default='images_225', help='image list table name'
    4. '-v', '--video', default='../data/videos/lazare.mp4', help='video path'
    5. '-o', '--output', default='../data/videos/split', help='output image path'
        
    ~~~~
    python video_spliting.py -f lazare_frame_list -s gare_st_lazare -i images_225 -v ../data/videos/lazare.mp4 -o ../data/videos/split
    ~~~~
        
**reorder_folder.py**
separating images into three categories
* usage
    1. '-s', '--schema', default='gare_st_lazare', help='schema for the station')
    2. '-i', '--imagelist', default='images_225', help='image list table name')
    3. '-tp', '--trainpath', default='../data/train_lazare', help='training data path')
    4. '-vp', '--valpath', default='../data/val_lazare', help='validation data path')
    5. '-ep', '--testpath', default='../data/test_lazare', help='testing data path')
    6. '-p', '--percentagetrain', default=0.8, type=float, help='train data percentage in all data')
    
    ~~~~
    python reorder_folder.py -s gare_st_lazare -i images_225 -tp ../data/train_lazare -vp ../data/val_lazare -ep ../data/test_lazare -p 0.8
    ~~~~
    
**reorder_folder.py**




