# Face-Recognition-Attendence-System
# Attendance Management System based on Face Recognition using Python and OpenCv
<h2>Code Requirements</h2>

.🔲Opencv(pip install opencv-python)
..🔲Tkinter(Available in python)
..🔲PIL (pip install Pillow)
.🔲.Pandas(pip install pandas)
.🔲.What steps you have to follow??
.🔲Download my Repository
.🔲Create a TrainingImage folder in a project.

.🔲Project Structure
.🔲After run you need to give your face data to system so enter your ID and name in box than click on Take Images button.
.🔲It will collect 200 images of your faces, it save a images in TrainingImage folder
.🔲After that we need to train a model(for train a model click on Train Image button.
.🔲It will take 5-10 minutes for training(for 10 person data).
.🔲After training click on Automatic Attendance ,it can fill attendance by your face using our trained model (model will save in TrainingImageLabel )
.🔲it will create .csv file of attendance according to time & subject.
.🔲You can store data in database (install wampserver),change the DB name according to your in AMS_Run.py.
.🔲Manually Fill Attendance Button in UI is for fill a manually attendance (without facce recognition),it's also create a .csv and store in a database.
# Screenshots
Basic UI
# Login Section
![image](https://user-images.githubusercontent.com/95865069/212906822-3e0387e1-a351-488e-9235-c72e8db794eb.png)
# Main Section
![Screenshot_20230117_184031](https://user-images.githubusercontent.com/95865069/212909948-db61e2d5-75c3-41f0-ab50-bfcba6caad84.png)
# Student Management Section
![Screenshot_20230117_184046](https://user-images.githubusercontent.com/95865069/212909989-9908d511-495f-4fcc-aa59-b9c28a24e8be.png)
# Face Recognition Section

![Screenshot_20230117_184106](https://user-images.githubusercontent.com/95865069/212910010-e2271352-fb69-4fdf-806a-8ac28f8a53e3.png)
# Attendence Section

![image](https://user-images.githubusercontent.com/95865069/212915883-a4bee010-8339-428b-9fbe-3cd4df096f70.png)
 When it recognise me it will automatically or manually fill the atttendence with date,time and subject
# Notes

<h4>🔲It will require high processing power(I have 8 GB RAM) </br></h4>
🔲Noisy image can reduce the accuracy, so quality of images should be good.



