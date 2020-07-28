import cv2
import numpy as np
#from keras.datasets import mnist
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.layers import Dropout
#from keras.layers import Flatten
#from keras.layers.convolutional import Conv2D
#from keras.layers.convolutional import MaxPooling2D
#from keras.utils import np_utils
from keras import backend as K
K.common.set_image_dim_ordering('th')
from keras.models import model_from_json
import pickle

def solve(img1):
    K.clear_session()
    global batch_index
    json_file = open('pickles/john.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
	# load weights into new model
    loaded_model.load_weights("pickles/john_final.h5")
    img1="test_images/"+img1
    img = cv2.imread(img1,cv2.IMREAD_GRAYSCALE)
	#erosion = cv2.erode(img,kernel,iterations = 3)
	#dilation = cv2.dilate(img,kernel,iterations = 1)
	#img=dilation
    if img is not None:
		#images.append(img)
        img=~img
        ret,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        ctrs,ret=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt=sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
        w=int(28)
        h=int(28)
        train_data=[]
		#print(len(cnt))
        rects=[]
        for c in cnt :
            x,y,w,h= cv2.boundingRect(c)
            rect=[x,y,w,h]
            rects.append(rect)
		#print(rects)
        bool_rect=[]
        for r in rects:
            l=[]
            for rec in rects:
                flag=0
                if rec!=r:
                    if r[0]<(rec[0]+rec[2]+10) and rec[0]<(r[0]+r[2]+10) and r[1]<(rec[1]+rec[3]+10) and rec[1]<(r[1]+r[3]+10):
                        flag=1
                    l.append(flag)
                if rec==r:
                    l.append(0)
            bool_rect.append(l)
		#print(bool_rect)
        dump_rect=[]
        for i in range(0,len(cnt)):
            for j in range(0,len(cnt)):
                if bool_rect[i][j]==1:
                    area1=rects[i][2]*rects[i][3]
                    area2=rects[j][2]*rects[j][3]
                    if(area1==min(area1,area2)):
                        dump_rect.append(rects[i])
		#print(len(dump_rect)) 
        final_rect=[i for i in rects if i not in dump_rect]
		#print(final_rect)
        for r in final_rect:
            x=r[0]
            y=r[1]
            w=r[2]
            h=r[3]
            im_crop =thresh[y:y+h+10,x:x+w+10]
            im_resize = cv2.resize(im_crop,(28,28))

            im_resize=np.reshape(im_resize,(28,28,1))
            train_data.append(im_resize)
			
    s=''
    for i in range(len(train_data)):
        train_data[i]=np.array(train_data[i])
        train_data[i]=train_data[i].reshape(1,28,28,1)
        result=loaded_model.predict_classes(train_data[i])
        if(result[0]==10):
            s=s+'-'
        if(result[0]==11):
            s=s+'+'
        if(result[0]==12):
            s=s+'*'
        if(result[0]==0):
            s=s+'0'
        if(result[0]==1):
            s=s+'1'
        if(result[0]==2):
            s=s+'2'
        if(result[0]==3):
            s=s+'3'
        if(result[0]==4):
            s=s+'4'
        if(result[0]==5):
            s=s+'5'
        if(result[0]==6):
            s=s+'6'
        if(result[0]==7):
            s=s+'7'
        if(result[0]==8):
            s=s+'8'
        if(result[0]==9):
            s=s+'9'
        if(result[0]==13):
            s=s+'A'
        if(result[0]==14):
            s=s+'B'
        if(result[0]==15):
            s=s+'C'
        if(result[0]==16):
            s=s+'D'
        if(result[0]==17):
            s=s+'E'
        if(result[0]==18):
            s=s+'F'
        if(result[0]==19):
            s=s+'G'
        if(result[0]==20):
            s=s+'H'
        if(result[0]==21):
            s=s+'I'
        if(result[0]==22):
            s=s+'J'
        if(result[0]==23):
            s=s+'K'
        if(result[0]==24):
            s=s+'L'
        if(result[0]==25):
            s=s+'M'
        if(result[0]==26):
            s=s+'N'
        if(result[0]==27):
            s=s+'O'
        if(result[0]==28):
            s=s+'P'
        if(result[0]==29):
            s=s+'Q'
        if(result[0]==30):
            s=s+'R'
        if(result[0]==31):
            s=s+'S'
        if(result[0]==32):
            s=s+'T'
        if(result[0]==33):
            s=s+'U'
        if(result[0]==34):
            s=s+'V'
        if(result[0]==35):
            s=s+'W'
        if(result[0]==36):
            s=s+'X'
        if(result[0]==37):
            s=s+'Y'
        if(result[0]==38):
            s=s+'Z'
			
    check=['A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    old_s=s
    for i in s:
        if i in check:
            s=s+'='+'0'
	#for increement operator
    if '++' in s:
        s=s.replace('++','+1')
	#for decreement operator
    elif '--' in s:
        s=s.replace('--','-1')
    resu=[]
    resu.append(old_s)
    resu.append(eval(s))
    return resu



