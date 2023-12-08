# Application_Big_Data

Use a model.h5 to predict the weather based on images.


### 1) Install Docker dekstop

### 2) FirstOpen a terminal 

### 3)  git clone the project : 
git clone https://github.com/Zzappy24/Application_Big_Data.git


### locate in BigDataProject
cd ./BigDataProject


### Build the images named big_data_image using : 
docker build -t big_data_image .

### locate in Application_Big_Data
cd ../

### Run the big_data_image. You need to put the path of the input image and the output : 
docker run -v {path_to_the_input_folder_with_images}:/app/input -v {path_to_the_output_folder}:/app/output big_data_image

for path_to_the_output_folder, you could put it directly in the desktop. no need to create the folder manually, it will be created during the run

exemple of output for windows : "C:\Users\{username}\Desktop\output"
exemple of output for Mac : "/Users/{username}/Desktop/output"
