import os
import json
import logging

cwd = os.getcwd()

list_enemy = [file for file in os.listdir(cwd) if '.json' in file[-5:]]


for enemy in list_enemy:

    try:
        with open(cwd + '\\' + enemy, 'r') as f:
            enemy_txt = f.read()
            
        enemy_txt = enemy_txt.replace('offsetx','offsetX').replace('offsety','offsetY').replace('quadcenterx','quadcenterX').replace('quadcentery','quadcenterY').replace('quadcount','quadCount')

        
        with open(cwd + '\\' + enemy, 'w+') as f:
            f.write(enemy_txt)
    except:
        print("Error for enemy: ", enemy_txt)
