# Application_Big_Data

Use a model.h5 to predict the weather based on images.
 

## 1) Install Docker dekstop

## 2) FirstOpen a terminal 

## 3)  git clone the project : 
git clone https://github.com/Zzappy24/Application_Big_Data.git

## 4) locate your terminal in Application_Big_Data/BigDataProject :
cd Application_Big_Data/BigDataProject

## Install gdown to download the model.h5 from a google drive folder
pip install gdown

## locate in model
cd ../
cd ./model

## install ResNet152V2-Weather-Classification-03.h5 in the folder model
gdown --id 1hzfqu8t3T50nZ0h2WN3ayYZJ335_xGcH -O ResNet152V2-Weather-Classification-03.h5

## locate in BigDataProject
cd ../
cd ./BigDataProject


## Build the images named big_data_image using : 
docker build -t big_data_image .

## locate in Application_Big_Data
cd ../

Run the big_data_image. You need to put the path of the input image and the output : 
docker run -v {path_to_the_input_folder_with_images}:/app/input -v {path_to_the_output_folder}:/app/output big_data_image

for path_to_the_output_folder, you could put it directly in the desktop. no need to create the folder manually, it will be created during the run

exemple of output for windows : "C:\Users\{username}\Desktop\output"
exemple of output for Mac : "/Users/{username}/Desktop/output"
