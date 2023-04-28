from PIL import Image
import numpy as np
from time import sleep, time
from math import floor
from random import choice
import os
import sys

def list_to_bw(img_list, contrast=1):
    mx = 0
    mn = 256
    for i in range(len(img_list)):
        for j in range(len(img_list[i])):
            mx = max(mx,sum(img_list[i][j][:3])//3)
            mn = min(mn,sum(img_list[i][j][:3])//3)
    new_list = [[0]*len(img_list[0]) for _ in range(len(img_list))]
    for i in range(len(img_list)):
        for j in range(len(img_list[i])):
            new_list[i][j] = (((sum(img_list[i][j][:3])//3 - mn)/(mx-mn))**contrast)
    # print(img_list[0])
    return new_list

def find_nearest(symbols, value):
    value = value*(symbols[-1][0]-symbols[0][0]) + symbols[0][0]
    mn_delta = 256
    for i in range(len(symbols)):
        delta = abs(value-symbols[i][0])
        if delta > mn_delta: return choice(symbols[i-1][1])
        else: mn_delta = delta
    return choice(symbols[-1][1])

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

img = Image.open('./images/cat.png')
k = width/img.width
img = img.resize((width, int(pixel_size[0]*img.height*k/pixel_size[1])))
img_arr = np.copy(np.asarray(img))
img_arr = list_to_bw(img_arr.tolist(),1)
# bw_list_to_png(img_arr,'result')



symbols = ((12.0, ' '), (18.0, '.'), (23.0, '_:'), (26.0, '",'), (28.0, '~^'), (30.0, '='), (31.0, '!<'), (32.0, '>;'), (33.0, '*+/'), (34.0, 'rc'), (35.0, '?L'), (36.0, 'zv'), (37.0, 's'), (38.0, ')'), (39.0, '(7TJ'), (40.0, 'tuiflnF'), (41.0, 'xC'), (42.0, '13oY'), (43.0, 'yIZ'), (44.0, 'eaj'), (45.0, '5h'), (46.0, '2wES'), (47.0, 'P'), (48.0, 'k'), (49.0, '4pb'), (50.0, '69qdUV'), (51.0, 'GH'), (52.0, 'AK'), (53.0, 'O'), (54.0, 'X'), (55.0, 'mRD'), (56.0, '8'), (57.0, 'B'), (58.0, '#%'), (59.0, '$0'), (60.0, 'g'), (61.0, 'NM'), (62.0, '&W'), (64.0, '№'), (65.0, 'Q'), (76.0, '@'))


os.system('cls')
ans = ''
for y in range(len(img_arr)):
    for x in range(len(img_arr[y])):
        ans += find_nearest(symbols,img_arr[y][x])
sys.stdout.write(ans)

