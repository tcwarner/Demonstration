# -*- coding: utf-8 -*-

import os
import numpy
import skimage.io
import string

import matplotlib.pyplot as plt
import matplotlib.image as mpimg



image_directory = 'Lab 9'

image_files = os.listdir(image_directory)



image_channel_paths = {}

calculated_features = {}

for image_file_name in image_files:
    # Row 1 = insulin treated
    # Row 2 = untreated (negative control)
    # Row 3 = oleic acid treated (positive control)
    parsed_fn = image_file_name[:-4].split('_')
    field_id = tuple([parsed_fn[0], int(parsed_fn[2])])
    
    calculated_features[parsed_fn[0]] = []
    
        
    if field_id not in image_channel_paths:
        image_channel_paths[field_id] = [None,None]
    if parsed_fn[1] == 'gfp':
        image_channel_paths[field_id][0] = image_file_name
    elif parsed_fn[1] == 'dapi':
        image_channel_paths[field_id][1] = image_file_name
    else:
        1/0 # something is wrong




# load the images into numpy matrix
images = {}

for image_id in image_channel_paths:
    images[image_id] = numpy.zeros([960,1280,3])
    for i in range(2):
        #print (image_id,i)        
        image_matrix = skimage.io.imread(image_directory+'/'+image_channel_paths[image_id][i])
        image_matrix[image_matrix[:,:,0] > 50,:] =0
        channel_max=numpy.max(image_matrix[:,:,i+1])
        channel_min=numpy.min(image_matrix[:,:,i+1])
        image_matrix[:,:,i+1]=255.0*(image_matrix[:,:,i+1-channel_min])/(channel_max-channel_min)
        #print(image_matrix.shape)  
        # these images are of the dimension 960 x 1280 x 3 (height x width x color) 
        
        images[image_id][:,:,i+1] = (numpy.max(image_matrix,axis=2))/255.0
    
    imgplot = plt.imshow(images[image_id])
    #plt.show()    
    
    plt.imsave("%s_%d.jpg" %(image_id[0],image_id[1]), images[image_id])
    # saves RGB image
    

# Calculating features
for image_id in images:
    blueAve=numpy.median(images[image_id][:,:,2])
    greenAve=numpy.median(images[image_id][:,:,1])
    green_array=images[image_id][:,:,1]
    blue_array=images[image_id][:,:,2]
    bin_green=green_array>40/255
    bin_blue=blue_array>40/255
    a=numpy.mean(bin_green)
    b=numpy.mean(bin_blue)
    feature_value = images[image_id][100,1000,1]*images[image_id][800,100,2]
    #print (feature_value)
    calculated_features[image_id[0]].append(b/a)
    
#print (calculated_features)
    
averages = [numpy.mean(calculated_features['field1']), numpy.mean(calculated_features['field2']), numpy.mean(calculated_features['field3'])]


#print (averages)

fig, ax = plt.subplots()
x = numpy.arange(3)
plt.bar(x, averages)
plt.xticks(x, ('Insulin', 'Untreated', 'Oleic Acid'))
plt.ylabel('Ratio of GFP fluorescence (lipids) to DAPI fluorescence (DNA)')
plt.show()