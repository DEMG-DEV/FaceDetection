from Muct import Muct
import cv2
import sys
import logging as log
import datetime as dt

sub_paths = ["a", "b", "c", "d", "e"]
total_count = 0

for sub_path in sub_paths:
    try:
        muct = Muct("Data/muct", sub_path)
        data = muct.get_all_image_path()
        log.basicConfig(filename='File_Database.log', level=log.INFO)
        count = 0

        log.info("=> Start a new Face Detection on 'Data/muct/"+sub_path+"' at " +
                 str(dt.datetime.now()))
        print("=> Start a new Face Detection on 'Data/muct/"+sub_path+"' at " +
              str(dt.datetime.now()))
        for imagePath in data:
            cascPath = "Data/haarcascade_frontalface_default.xml"

            # Create the haar cascade
            faceCascade = cv2.CascadeClassifier(cascPath)

            # Read the image
            image = cv2.imread("Data/muct/" + sub_path + "/" + imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            log.info("File: "+imagePath+",faces: " +
                     str(len(faces))+" at "+str(dt.datetime.now()))
            count += 1

        total_count += count
        log.info("The total number of faces is: "+str(count))
        log.info("=> End Face Detection on 'Data/muct/" +
                 sub_path+"' at "+str(dt.datetime.now()))
        print("The total number of faces is: "+str(count))
        print("=> End Face Detection on 'Data/muct/" +
              sub_path+"' at "+str(dt.datetime.now()))
    except:
        log.info("Error read the directory "+sub_path)

    print("Total count of faces => "+str(total_count))
    log.info("Total count of faces => "+str(total_count))
