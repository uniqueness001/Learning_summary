# -*- coding: UTF-8 -*-
import sys,os,dlib,glob,numpy
from skimage import io

if len(sys.argv) != 5:
    print( "请检查参数是否正确")
    exit()
predictor_path = sys.argv[1]
face_rec_model_path = sys.argv[2]
faces_folder_path = sys.argv[3]
img_path = sys.argv[4]
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)
descriptors = []

for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    print("Processing file: {}".format(f))
    img = io.imread(f)

    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))
    for k, d in enumerate(dets):  
        shape = sp(img, d)       
        face_descriptor = facerec.compute_face_descriptor(img, shape)
        v = numpy.array(face_descriptor)  
        descriptors.append(v)
img = io.imread(img_path)
dets = detector(img, 1)
dist = []
for k, d in enumerate(dets):
    shape = sp(img, d)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    d_test = numpy.array(face_descriptor) 
    for i in descriptors:
        dist_ = numpy.linalg.norm(i-d_test)
        dist.append(dist_)
candidate = ['Unknown1','Unknown2','Shishi','Unknown4','Bingbing','Feifei']

c_d = dict(zip(candidate,dist))
cd_sorted = sorted(c_d.iteritems(), key=lambda d:d[1])
print ("\n The person is: ",cd_sorted[0][0]) 
dlib.hit_enter_to_continue()