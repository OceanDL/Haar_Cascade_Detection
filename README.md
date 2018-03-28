# Haar_Cascade_Detection
This repo contains a trained dataset for object detection utilizing OpenCV's cascade detection feature and associated scripts to identify the object given a realtime video feed, a saved mp4, or an image. 

# Getting Started With Identification
The only dependicies needed for this project are OpenCV and Numpy, so if this is your first time running any Python scripts in the terminal you should run these commands(assuming you have Python installed):

'''sh
$ sudo apt-get install python-opencv
$ sudo apt-get install numpy
'''
Then we will clone the project to a directory: 
'''sh
git clone https://github.com/OceanDL/Haar_Cascade_Detection/
'''

Once these two dependcies are installed and the project has been cloned to the associated directory we are ready to begin using the object detection scripts, there are three object detection scripts you can utilize in the repository, RunPictureIdentifier.py RunRealTimeVideoIdentifier.py, and RunSavedVideoIdentifier.py

To utilize these scripts, CD to the cloned directory and execute the python script (with the path name to the file you wish to identify if using RunPictureIdentifier.py or RunSavedVideoIdentifier.py)

'''sh
~/Haar_Cascade_Detection/$ python RunSavedVideoIdentifier.py grenade.mp4
'''

The realtime identification by default uses the default webcam of the computer (whatever that device may be). 

# Getting Started With Training
TBD
