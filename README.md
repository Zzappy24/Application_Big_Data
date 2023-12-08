# Application_Big_Data

Use a model.h5 to predict the weather based on images.

# 2 solution, one with a script shell (bash)
for Mac and linux user :
open Docker
Download the file script_docker_mac_linux.sh
Copy the path 
Open a terminal and paste : {path_of/script_docker_mac_linux.sh}

You will have nothin to do, all the command line, are in the .sh

results will be put in the output file, in the same folder


# BUT you can also define :
- your images from you compute
- where you want to put the file output
- and even which model.h5 you want to use




## 1) Install Docker dekstop

## 2) FirstOpen a terminal 

## 3)  git clone the project : 
git clone https://github.com/Zzappy24/Application_Big_Data.git

## 4) locate your terminal in Application_Big_Data/BigDataProject :
cd Application_Big_Data/BigDataProject

## Install gdown to download the model.h5 from a google drive folder
pip install gdown



## Build the images named big_data_image using : 
docker build -t big_data_image .

## locate in Application_Big_Data
cd ../

## Run the big_data_image. You need to put the path of the input image and the output : 
docker run -v "/Users/{username}/{path to your input folder with image}:/app/input" -v "/Users/{username}/{choose the path of the output folder}:/app/output" -v "/Users/username/{path to your model.h5}:/app/model" big_data_image

If your model folder model is empty, it will automatically download a default model stored our public google drive.

for path_to_the_output_folder, you could put it directly in the desktop. no need to create the folder manually, it will be created during the run

exemple of output for windows : "C:\Users\{username}\Desktop\output"
exemple of output for Mac : "/Users/{username}/Desktop/output"
