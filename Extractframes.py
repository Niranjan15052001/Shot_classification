import cv2
import os
import numpy as np
import glob 

def craete_dir(pathname,directory):
    path=os.path.join(pathname,directory)
    try:
        
        mode=0o777
        os.mkdir(path,mode)
        return path
    except OSError as error:
        print(error)
    
def save_frame(video,parentdir,idx):
    try:
        name='Video' +str(idx)
        savepath=craete_dir(parentdir,name)

        cap = cv2.VideoCapture(video)
        id = 0
        while 1:
            ret,frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if ret==False:
                cap.release()
                break
            cv2.imwrite(f'{savepath}/{id}.png',gray);
            id+=1
    except:
        return


if __name__ == '__main__':
    videopath=glob.glob('video/*')
    parentdir="D:\\python programs\\frames"
    id=1
    for video in videopath:
        
        print(video)
        save_frame(video,parentdir,id)
        id+=1




