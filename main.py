# -*- coding: utf-8-*-
import numpy as np
import cv2
import os
import shutil
# termination criteria

# Arrays to store object points and image points from all the images.
def on_mouse(event, x, y, flags, param):
    # global img, points
    # img2 = img.copy()
    if event == cv2.EVENT_MBUTTONDOWN:
        param[0]=[]
        param[1] = param[2].copy()
        cv2.imshow(f"{filename}", param[1])
        print('[INFO] Contours is cleaned')
        # cv2.imshow(f"78", param[1])
        #
        # cv2.waitKey()
        # point1 = (x, y)
        # param[0].append(point1)
        # param[0] = []
        # print("???")
        # point1 = (x, y)
        # param[0].append(point1)
        # cv2.circle(img2, point1, 10, (0,255,0), 5)
        # cv2.imshow('hsv', img2)
    if event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        # 按住左键拖曳
        param[0].append((x, y))
        if len(param[0]) > 2:
            for i in range(len(param[0]) - 1):
                cv2.line(param[1], param[0][i], param[0][i + 1], (0, 0, 255), 10)
                # cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
            cv2.imshow(f"{filename}", param[1])
            # if cv2.waitKey(1) & 0xFF == ord("q"):
            #     print("ih")
            #     cv2.destroyWindow(f"{filename}")
    if event == cv2.EVENT_LBUTTONUP:  # 左键释放
        print("length of points",len( param[0]))
        # flags=False
        # cv2.destroy+Window('hsv')



def get_file(path):
    voll_path=[]
    name=[]
    roott=''
    saved=0
    for root,dir,files in os.walk(path):
        for d in dir:
            inhalt =os.listdir(os.path.join(root,d))
            length=len(inhalt)-1
            step=length//3
            inhalt=inhalt[1:-1:step]
            for file in inhalt :
                print(file)
                if file.endswith('.jpg') or file.endswith('.JPG'):

                    voll_path.append(os.path.join(root,d,file))
                    name.append(file)


    return name,voll_path
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path=r'C:\Users\z00461wk\Downloads\Cam77-88'
    save_path='mask/'

    name, voll_path=get_file(path)
    print(len(name))
    for singleimage,filename in zip (voll_path,name):
        img = cv2.imread(singleimage)
        img_copy=img.copy()
        points=[]
        h1, w1 = img_copy.shape[:2]
        area = h1 * w1 / 384
        cv2.namedWindow(f"{filename}", 0)
        cv2.resizeWindow(f"{filename}", int(w1 / 4), int(h1 / 4))
        cv2.setMouseCallback(f"{filename}", on_mouse, [points, img_copy,img])
        cv2.imshow(f"{filename}", img_copy)
        cv2.waitKey()
        if cv2.waitKey(1) & 0xFF == ord("q"):

            cv2.destroyWindow(f"{filename}")

        if len(points):
            mask = np.zeros((img.shape[0], img.shape[1]))
            fillpst = np.array(points)
            aa = cv2.fillPoly(mask, [fillpst], (255, 255, 255)).astype(np.uint8)
            cv2.namedWindow(f"mask_+{filename}", 0)
            cv2.resizeWindow(f"mask_+{filename}", int(h1 / 2), int(w1 / 2))
            while True:
                cv2.imshow(f"mask_+{filename}", aa)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

            cv2.destroyAllWindows()

            # cv2.destroyWindow(f"mask_+{filename}")
            # aa /= 255
            shutil.copy(singleimage, save_path)
            print('[INFO] copy completed')
            cv2.imwrite(os.path.join(save_path,filename[:-4]+'_mask'+filename[-4:]),aa)
        else:
            print(f'No Mask on {singleimage}')
            # cv2.destroyWindow(f"{filename}")
            cv2.destroyAllWindows()
            continue
    print('[INFO] end')

