# Haar_Cascade_Detection
This repo contains a trained dataset for object detection utilizing OpenCV's cascade detection feature and associated scripts to identify the object given a realtime video feed, a saved mp4, or an image. 

# Getting Started With Identification
The only dependicies needed for this project are OpenCV and Numpy, so if this is your first time running any Python scripts in the terminal you should run these commands(assuming you have Python installed):

```sh
$ sudo apt-get install python-opencv
$ sudo apt-get install numpy
```
Then we will clone the project to a directory: 
```sh
git clone https://github.com/OceanDL/Haar_Cascade_Detection/
```

Once these two dependcies are installed and the project has been cloned to the associated directory we are ready to begin using the object detection scripts, there are three object detection scripts you can utilize in the repository, RunPictureIdentifier.py RunRealTimeVideoIdentifier.py, and RunSavedVideoIdentifier.py

To utilize these scripts, CD to the cloned directory and execute the python script (with the path name to the file you wish to identify if using RunPictureIdentifier.py or RunSavedVideoIdentifier.py)

```sh
~/Haar_Cascade_Detection/$ python RunSavedVideoIdentifier.py grenade.mp4
```

The realtime identification by default uses the default webcam of the computer (whatever that device may be). 

# Getting Started With Training
Training only requires one dependecy(OpenCV) which can be fetched with the following command:
```sh
$  sudo apt-get install libopencv-dev
```
From here, you will need to gather positive and negative images for your dataset. For positive images you want only the object in the picture and a varied background as to not have any binary features from the background of the positive images. For negative images, you can use the ones in this repository or substitute any pictures that do not include the object you are trying to detect. 

Once you have gathered the image dataset, you put them into the two respective folders, positive_images and negative_images(while deleting the current positive images if training a different object).

Then from there you will create two .txt files that will be used for atrifically creating samples to be used while training. These two commands are:
```sh
$  find ./positive_images -iname "*.jpg" > positives.txt
$  find ./negative_images -iname "*.jpg" > negatives.txt
```
Now we will create the samples to be utilized during training, we will be using a perl script for this and you can look at the arguments in the official OpenCV documentation for more info on each argument. One major argument to look at is -h and -w which must match the aspect ration of your positive dataset. In our case, since the dataset was 1:1 we used 80x80 for training(this number can be lowered or raised however training time will increase with higher resolutions and this resoultion seemed fine for the intended camera resolution).
```sh
$  perl bin/createsamples.pl positives.txt negatives.txt samples 1500\
  "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1\
  -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 80 -h 40"
 ```

Now that the samples have been created and placed in the samples folder, we must combine them into a single .vec file to be used in training:
```sh
$  python mergevec.py -v samples -o output.vec
```

From this point we are ready to begin training, depending on the resolution size and stages this can take a long time especially on non -tbb instalations of OpenCV. You will normally only train around 20 stages as to not overtrain your model(official OpenCV docs reccomend to only train until 10e-5)
```sh
$  opencv_traincascade -data classifier -vec output.vec -bg negatives.txt\
  -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000\
  -numNeg 600 -w 80 -h 80 -mode ALL -precalcValBufSize 1024\
  -precalcIdxBufSize 1024
```

The arguments can be looked at more closely here: 
https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html#positive-samples


And that's it, once training has been completed a cascade.xml file will be generated in the classifier folder to be used for identification. 


# Credit
Thanks to Thorston Ball and Harriosn Kinsley for their Haar Training walkthroughs and scripts. The training section of this walkthrough is heavily adapted from Ball's walkthrough, additionally thanks to Naotoshi Seo for his createsamples.pl script and Blake Wulfe for his mergevec.py script. 
