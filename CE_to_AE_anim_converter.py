import os
import json
import logging

cwd = os.getcwd()

list_anim = [file for file in os.listdir(cwd) if '.json' in file[-5:]]

convert_mp3 = 'ogg'

for anim in list_anim:

    try:
        with open(cwd + '\\' + anim, 'r') as f:
            dic_anim = json.load(f)
            
        list_new_action = []
        list_current_action = dic_anim["actions"]
        
        for action in list_current_action:
            action_name = action[0]
            
            if action_name in ["enablexscroll", "disablexscroll", "enableyscroll", "disableyscroll"]:
                action_name = [action[0].replace("blex", "blehor").replace("bley", "blever")]
            
            elif action_name == 'dialogbox':
                action = action + ["orange"]
            
            elif action_name in ["setcamerax", "setcameray"]:
                action = ["pancameratox", action[1], "0.001"]
            
            elif action_name == "playmusic":
                action = [action[0], "music/" + action[1].replace("mp3", convert_mp3)]

            list_new_action.append(action)
            
        dic_anim["actions"] = list_new_action
            

        with open(cwd + '\\' + anim, 'w+') as f:
            json.dump(dic_anim, f, indent=4)
    except:
        print("Error for animation: ", anim)
