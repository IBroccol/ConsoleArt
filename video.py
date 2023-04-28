from PIL import Image
import numpy as np
from time import sleep, time
from math import floor
from random import choice
import os
import sys
import cv2
from functools import lru_cache
from moviepy.editor import *
import pygame

def list_to_bw(img_list, contrast=1):
    new_arr = (np.sum(img_list, axis=2)//3)**contrast
    mxindex = np.unravel_index(new_arr.argmax(), new_arr.shape)
    mx = new_arr[mxindex[0], mxindex[1]]
    mnindex = np.unravel_index(new_arr.argmin(), new_arr.shape)
    mn = new_arr[mnindex[0], mnindex[1]]

    if mn == mx: return [[mn]*len(img_list[0]) for _ in range(len(img_list))]
    new_list = (new_arr[:,:] - mn)/(mx-mn)
    return new_list.tolist()



@lru_cache(None)
def find_nearest(symbols, value):
    value = value*(symbols[-1][0]-symbols[0][0]) + symbols[0][0]
    mn_delta = 256
    for i in range(len(symbols)):
        delta = abs(value-symbols[i][0])
        if delta > mn_delta:
            return symbols[i-1][1]
        else: mn_delta = delta

    return symbols[-1][1]

def bw_list_to_png(img_list, name):
    size = (len(img_list[0]), len(img_list))
    img_list = np.asarray(img_list)
    image_out = Image.new("L",size)
    image_out.putdata(img_list.flatten())
    image_out.save(f'{name}.png')
    return image_out
        
#settings for 14 text size
width = 237
height = 55
pixel_size = (8,18)

t0 = time()

file = './videos/rickroll.mp4'
framerate = 25


video = cv2.VideoCapture(file)

v = VideoFileClip(os.path.join(file))
v.audio.write_audiofile(os.path.join("sound.mp3"))


pygame.mixer.init()
pygame.mixer.music.load('sound.mp3')
pygame.mixer.music.set_volume(0.3)



try:  
	if not os.path.exists('pet'): 
		os.makedirs('pet')
except OSError: 
	print ('Error') 
symbols = ((12.0, ' '), (18.0, '.'), (23.0, '_:'), (26.0, '",'), (28.0, '~^'), (30.0, '='), (31.0, '!<'), (32.0, '>;'), (33.0, '*+/'), (34.0, 'rc'), (35.0, '?L'), (36.0, 'zv'), (37.0, 's'), (38.0, ')'), (39.0, '(7TJ'), (40.0, 'tuiflnF'), (41.0, 'xC'), (42.0, '13oY'), (43.0, 'yIZ'), (44.0, 'eaj'), (45.0, '5h'), (46.0, '2wES'), (47.0, 'P'), (48.0, 'k'), (49.0, '4pb'), (50.0, '69qdUV'), (51.0, 'GH'), (52.0, 'AK'), (53.0, 'O'), (54.0, 'X'), (55.0, 'mRD'), (56.0, '8'), (57.0, 'B'), (58.0, '#%'), (59.0, '$0'), (60.0, 'g'), (61.0, 'NM'), (62.0, '&W'), (64.0, '№'), (65.0, 'Q'), (76.0, '@'))
i = 0
fr = 0
try:
    t0 = time()
    #os.system('cls')
    pygame.mixer.music.play()
    while (True):
        ret,frame = video.read()
        i+=1
        if ret:
            if i/framerate - (time()-t0) < 0:
                continue
            img = Image.fromarray(frame)
            k = width/img.width
            img = img.resize((int(img.width*k), height))
            img_arr = np.copy(np.asarray(img))
            
            img_arr = list_to_bw(img_arr,1.5)
            
            ans = list()

            for y in range(height):
                for x in range(len(img_arr[y])):
                    ans.append(choice(find_nearest(symbols,int(img_arr[y][x]*10)/10)))
            sys.stdout.write(''.join(ans))
            fr+=1
            sleep(max(0,(i/framerate - (time()-t0))-0.05))  
            #if time()-t0 > 30: break
        else: 
            break
    video.release()
    pygame.mixer.music.stop()
    cv2.destroyAllWindows()
except KeyboardInterrupt:
    video.release()
    pygame.mixer.music.stop()
print(i/(time()-t0), 'fps')
