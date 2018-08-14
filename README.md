sncf_data_processing
===========================

What is this project for?
------------
People get confused with station spaces. We are trying to computer vision, specificly deep convolutional neural networks to train a model that could tell the location of a given image. Taking advantage of this model, we could do an spatial legibility evaluation based on the model. 

What is contained in this repo?
------------
The raw data contains LiDar and videos from a specially design device, which we deploy in Gare de Lyon and Gare St Lazare. The scripts here are to extract, clean and sort out data from this device for further training purpose.

How-to
------------

**video_capture.ipynb**
    - frame extraction and cubic projection, saves all images in */top_9/left/*.png form
    - usage
        '-f', '--framelist', default='lazare_frame_list', help='frame list table name'
        '-s', '--schema', default='gare_st_lazare', help='schema for the station'
        '-i', '--imagelist', default='images_225', help='image list table name'
        '-v', '--video', default='../data/videos/lazare.mp4', help='video path'
        '-o', '--output', default='../data/images/lazare_225', help='output image path'
        '-d', '--direction', default=22.5, type=float, help='direction as degree'
        
        python video_capture.py -f lazare_frame_list -s gare_st_lazare -i images_225 -v 
        ../data/videos/lazare.mp4 -o ../data/images/lazare_225 -d 0

**video_spliting.ipynb**
    - dividing as regenerate video samples as different categories
    - usage
        '-f', '--framelist', default='lazare_frame_list', help='frame list table name'
        '-s', '--schema', default='gare_st_lazare', help='schema for the station'
        '-i', '--imagelist', default='images_225', help='image list table name'
        '-v', '--video', default='../data/videos/lazare.mp4', help='video path'
        '-o', '--output', default='../data/videos/split', help='output image path'
        
        python video_spliting.py -f lazare_frame_list -s gare_st_lazare -i images_225 -v 
        ../data/videos/lazare.mp4 -o ../data/videos/split
        

        
        
        
        