from PIL import Image
import numpy as np
from time import sleep

width = 212
pixel_size = (9,20)

def list_to_bw(img_list):
    new_list = [[0]*len(img_list[0]) for _ in range(len(img_list))]
    for i in range(len(img_list)):
        for j in range(len(img_list[i])):
            new_list[i][j] = sum(img_list[i][j][:3])//3
    # print(img_list[0])
    return new_list

img = Image.open('symbols.png')
img_arr = np.copy(np.asarray(img))
img_arr = list_to_bw(img_arr.tolist())

pixel_size = (8,18)

d = dict()
s = """~!@#$%^&*()_+=<>"№;:?,./1234567890 qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"""
for i in range(len(img_arr[0])//pixel_size[0]):
    sm = 0
    for x in range(pixel_size[0]):
        for y in range(pixel_size[1]):
            sm += img_arr[y][x+pixel_size[0]*i]
    if 255 - (sm/(pixel_size[0]*pixel_size[1])*100)//100 in d.keys():
        d[255 - (sm/(pixel_size[0]*pixel_size[1])*100)//100] += s[i]
    else: d[255 - (sm/(pixel_size[0]*pixel_size[1])*100)//100] = s[i]
    # d[s[i]] = 255 - (sm/180*100)//100
lst = sorted([[key,d[key]] for key in d.keys()])
print(tuple([tuple(i) for i in lst]))
#" .:~+?168%№@"
    