'''réaliser application qui détecte les visages

option 1 : sur une photo venant d'un fichier

       2 : capture video de la webcam

       3 : vidéo venant d'un fichier

et les met en flou'''

import matplotlib.pyplot as plt
import numpy as np
import cv2

def image_visage_floutée(image):
    img = cv2.imread(image)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    haar_file = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + haar_file)

    grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey_image)
    print("Nombre de visages détecté dans l'image: {0}".format(len(faces)))

    position_list = faces.tolist()
    for face in faces:
        print(face)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), color=255)
        roi = img[y:y+h, x:x+w]
        roi = cv2.GaussianBlur(roi, (23, 23), 30)
        img[y:y+roi.shape[0], x:x+roi.shape[1]] = roi
    
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def video_visage_floutée(img):
    haar_file = 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + haar_file)

    grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey_image)
    print("Nombre de visages détecté dans l'image: {0}".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), color=255)
        roi = img[y:y+h, x:x+w]
        roi = cv2.GaussianBlur(roi, (23, 23), 30)
        img[y:y+roi.shape[0], x:x+roi.shape[1]] = roi
    return img

from PIL import ImageFilter
from PIL import Image
import numpy as np

def capture_cam_video_floutée(source):
    '''
    cam = cv2.VideoCapture(0) #source webcam
    cam = cv2.VideoCapture("dossier/ficher.mp4") #source video
    '''
    cam = cv2.VideoCapture(source)

    nom_fenetre = "video_cam"

    largeur_image = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    hauteur_image = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cv2.namedWindow(nom_fenetre, cv2.WND_PROP_FULLSCREEN)

    nouvelle_video = []

    while True :
        ret, image = cam.read()
        if ret:
            image = video_visage_floutée(image)

            cv2.imshow(nom_fenetre, image)

            nouvelle_video.append(image)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter('video.mp4', fourcc, 24, (largeur_image, hauteur_image))

    for image in nouvelle_video:
        video.write(image)

    cv2.destroyAllWindows()
    video.release()

def capture_cam_video_stylisée(source):
    '''
    cam = cv2.VideoCapture(0) #source webcam
    cam = cv2.VideoCapture("dossier/ficher.mp4") #source video
    '''
    cam = cv2.VideoCapture(source)

    nom_fenetre = "video_cam"

    largeur_image = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    hauteur_image = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    cv2.namedWindow(nom_fenetre, cv2.WND_PROP_FULLSCREEN)

    nouvelle_video = []

    while True :
        ret, image = cam.read()
        if ret:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)

            image = image.filter(ImageFilter.EDGE_ENHANCE)
            image = image.filter(ImageFilter.ModeFilter(15))

            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            cv2.imshow(nom_fenetre, image)

            nouvelle_video.append(image)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter('video.mp4', fourcc, 24, (largeur_image, hauteur_image))

    for image in nouvelle_video:
        video.write(image)

    cv2.destroyAllWindows()
    video.release()

capture_cam_video_floutée(0)

