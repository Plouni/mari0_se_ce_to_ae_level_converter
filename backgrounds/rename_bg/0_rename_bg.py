import os
import string

list_bg = os.listdir()
list_bg = sorted([ele for ele in list_bg if ele.split('.')[-1] in ['json', 'png']])
num = 1
orig_name = ".".join(list_bg[0].split('.')[:-1])

bg_name = input('> Enter new background name (or press enter if you just want to fix suffix number):\n')
if len(bg_name) == 0:
    bg_name = orig_name

bg_name_base = bg_name.rstrip(string.digits)

for bg in list_bg:
    current_name = ".".join(bg.split('.')[:-1])

    ext = bg.split('.')[-1]
    ext = '.' + ext

    if current_name != orig_name:
        num+=1
    
    os.rename(bg, bg_name_base + str(num) + ext)
    