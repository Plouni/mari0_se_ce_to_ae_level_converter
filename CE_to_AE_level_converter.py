import os

dic_id_entity_replace = {
    9: 186,
    86: 273,
    87: 274,
    82: 185,
    26: 27,
    29: 196,
    37: 197,
    38: 198,
    7: 271,
    19: 200,
    39: 275,
    18: 309,
    110: 199,
    4: 210,
    101: 257,
    105: 231,
    42: 270,
    # flip flop from CE
    10: 272
}

# Replace if using ogg for example
convert_mp3 = 'mp3'
# Replace if you want to convert cube to an enemy for example
replace_box = None

dic_id_entity_replace = {k: str(dic_id_entity_replace[k]) for k in dic_id_entity_replace}

def get_new_id(id):
    if id not in dic_id_entity_replace:
        return str(id)
    return dic_id_entity_replace[id]

def get_new_sub(string):
    return str(int(string)-1)

def get_coor_region(elem_split):
    region = [ele for ele in elem_split if ':' in ele][0].split(':')
    x0 = region[1].replace('m', 'n')
    y0 = region[2].replace('m', 'n')
    x1 = region[3].replace('m', 'n')
    y1 = region[4].replace('m', 'n')
    return x0, y0, x1, y1
    
def check_if_invalid(new_body_table, x, y, length, height):
    if x+1 > length or y+1> height or x < 0 or y< 0:
        return True
    return '-' in new_body_table[y][x]

cwd = os.getcwd()

##### You can change the variable if you want #####
path = cwd

try:
    list_in = [file for file in os.listdir(path + '\\in') if file[-4:] == '.txt']
except:
    input("No folder 'in' found! Press enter to quit")
    raise


for txt_level in list_in:

    with open(path + '\\in\\' + txt_level) as f:
        level = f.read()

    CE=False
    # Convert CE to SE
    if '¤' in level:
        level = level.replace('¸', ';')
        level = level.replace('·', '*')
        level = level.replace('¤', ',')
        level = level.replace('×', '-')
        level = level.replace('¨', '=')
        CE=True
        
    split_level = level.split(';')
    
    height = int(split_level[0])

    body = split_level[1].split(',')
    new_body = []

    for elem in body:
        elem_split = elem.split('-')
        elem2 = elem_split[0]

        coin_prefix = ''
        metadata_tile = ''
        if len(elem_split)>1:
            elem3 = elem_split[1]
            # if enemy
            if any(c.isalpha() for c in elem3):
                metadata_tile = elem3
            # spawnr
            elif elem3 == '6':
                enemy = elem_split[2]
                speedx = elem_split[3]
                speedy = elem_split[4]
                
                param1 = ''
                if 'link' in elem_split[2:]:
                    param1 = '-link-{}-{}'.format(elem_split[-2].replace('m', 'n'), elem_split[-1].replace('m', 'n'))
                
                metadata_tile = '{}-{}|{}|{}|true|none'.format(205, enemy, speedx.replace('m', 'n'), speedy.replace('m', 'n')) + param1
                
            # and/or gate
            elif int(elem3) in [86, 87]:
                links = ''
                if 'link' in elem_split[2:]:               
                    list_param = elem_split[3:]
                    i = 0
                    dic_link = {}
                    for sub_param in list_param:
                        if sub_param == 'link':
                            i = i+1
                            dic_link[i] = []
                        else:
                            dic_link[i].append(sub_param)
                            
                    for key_link in dic_link:
                        links = links + '-link-{}-{}-{}'.format(dic_link[key_link][-2].replace('m', 'n'), dic_link[key_link][-1].replace('m', 'n'), key_link)                    
                    
                metadata_tile = '{}-{}{}'.format(get_new_id(int(elem3)), elem_split[2], links)
                
            # Various entities
            elif int(elem3) in [14, 21, 31, 41, 32, 52, 36, 68, 40, 28, 74, 93, 5, 30, 49, 9, 84, 82, 26, 67, 85, 2, 61, 37, 38, 39, 18, 4, 81, 35, 101, 89, 95, 96, 60, 91, 90, 80, 105, 10] or (int(elem3)==42 and CE):
                id_link = len(elem_split)
                param1 = ''
                if 'link' in elem_split[2:] and int(elem3) not in [105]:
                    id_link = elem_split.index('link')
                    param1 = '-link-{}-{}'.format(elem_split[-2].replace('m', 'n'), elem_split[-1].replace('m', 'n'))
                                
                # all parameters before link
                list_param = elem_split[2:id_link]
                
                # music
                if int(elem3) in [4]:
                    param0 = 'music/' + list_param[2].replace('.', 'º').replace("mp3", convert_mp3) + '|1|false'
                # funnel
                elif int(elem3) in [105]:
                    links = ''
                    if 'link' in elem_split[2:]:               
                        list_param2 = elem_split[6:]
                        i = 0
                        dic_link = {}
                        for sub_param in list_param2:
                            if sub_param == 'link':
                                i = i+1
                                dic_link[i] = []
                            else:
                                dic_link[i].append(sub_param)
                            
                        for key_link in dic_link:
                            links = links + '-link-{}-{}-{}'.format(dic_link[key_link][-2].replace('m', 'n'), dic_link[key_link][-1].replace('m', 'n'), dic_link[key_link][0])         
                        
                    param0 = list_param[1] + '|' + list_param[2] + '|' + list_param[0] + '|' + list_param[3] + links
                    
                # flipflop
                elif int(elem3) in [10]:
                    links = ''
                    if 'link' in elem_split[2:]:               
                        list_param2 = elem_split[3:]
                        i = 0
                        dic_link = {}
                        for sub_param in list_param2:
                            if sub_param == 'link':
                                i = i+1
                                dic_link[i] = []
                            else:
                                dic_link[i].append(sub_param)
                            
                        for key_link in dic_link:
                            links = links + '-link-{}-{}-{}'.format(dic_link[key_link][-2].replace('m', 'n'), dic_link[key_link][-1].replace('m', 'n'), dic_link[key_link][0])         
                        
                    param0 = elem_split[2] + links
                    
                # door
                elif int(elem3) in [28]:
                    param0 = list_param[2] + '|' + list_param[0] + '|' + list_param[1]
                # x/v wall indicator
                elif int(elem3) in [30]:
                    param0 = ''
                # delay
                elif int(elem3) in [9]:
                    param0 = list_param[1] + '|' + list_param[0]
                # sinus
                elif int(elem3) in [82]:
                    param0 = list_param[0] + '|' + list_param[1] + '|' + list_param[3] + '|' + list_param[2]
                # gel
                elif int(elem3) in [85]:
                    if CE:
                        param0 = list_param[0] + '|' + list_param[2] + '|' + list_param[1] + '|' + list_param[4] + '|' + list_param[3]
                    else:
                        param0 = list_param[0] + '|' + list_param[2] + '|' + list_param[1] + '|' + list_param[3] + '|' + list_param[4]
                # spawnr platform
                elif int(elem3) in [41]:
                    param0 = list_param[1] + '|' + list_param[2] + '|' + list_param[3] + '|' + list_param[0]
                
                # Vine, sublevel, exit and warp
                elif int(elem3) in [14]:
                    param0 = get_new_sub(list_param[0])
                elif int(elem3) in [21]:
                    param0 = get_new_sub(list_param[0]) + '|1|down|big'
                elif int(elem3) in [31]:
                    param0 = get_new_sub(list_param[0]) + '|1|up|big'
                elif int(elem3) in [81]:
                    param0 = '{}|{}|down|big'.format(elem_split[2], elem_split[3])
                # bowser    
                elif int(elem3) in [81]:
                    param0 = 'boss'
                # faith plate  
                elif int(elem3) in [49]:
                    param0 = '{}|{}|true|{}'.format(elem_split[2].replace('m', 'n'), elem_split[3].replace('m', 'n'), elem_split[4])
                    
                else:
                    # cube dispenser
                    if int(elem3) in [67] and (str(list_param[-1]) == '1' or str(list_param[-1]) == 'box') :
                        list_param[-1] = 'cube'
                        
                    param0 = '|'.join(list_param)
                
                param0 = param0.replace('|m', '|n')
                
                # timer
                if int(elem3) in [74]:
                    param0 = param0 + '|true'
                
                # if empty
                if len(param0) == 0:
                    metadata_tile = get_new_id(int(elem3)) + param1
                else:
                    metadata_tile = '{}-{}'.format(get_new_id(int(elem3)), param0 + param1)
                
            elif int(elem3) in [26]:
                param = '|'.join(elem_split[2:])
                metadata_tile = '{}-{}'.format(27, param)
                
            # if animation trigger and not CE
            elif int(elem3) == 42 and not CE:
                metadata_tile = str(get_new_id(int(elem3))) + '-' + elem_split[2] + '-' + elem_split[3] + '-link-anim___to___replace-' + elem_split[4].split('region:')[1]
                
            # Region trigger
            elif int(elem3) == 19:
                category = elem_split[2]
                if category == 'true':
                    category = 'player'
                else:
                    category = "everything"
                    
                x0, y0, x1, y1 = get_coor_region(elem_split)
                
                metadata_tile = '{}-{}|{}|{}|{}|{}'.format(get_new_id(int(elem3)), x1, y1, x0, y0, category)
                
            # animated tiles
            elif int(elem3) == 7:
                visible = elem_split[2]
                    
                x0, y0, x1, y1 = get_coor_region(elem_split)
                
                param1 = ''
                if 'link' in elem_split[2:]:
                    param1 = '-link-{}-{}'.format(elem_split[-2].replace('m', 'n'), elem_split[-1].replace('m', 'n'))
                
                metadata_tile = '{}-{}|{}|{}|{}|{}'.format(get_new_id(int(elem3)), visible, x1, y1, x0, y0 + param1)
              
            # cloud
            elif int(elem3) == 92:
                metadata_tile = '{}-3'.format(get_new_id(int(elem3)))
            # firebar
            elif int(elem3) == 79:
                if elem_split[4] == 'false':
                    cw_param = 'cw'
                else:
                    cw_param = 'ccw'
                
                metadata_tile = '{}-{}|{}|0|{}|true'.format(get_new_id(int(elem3)), elem_split[2], elem_split[3], cw_param)
            # text
            elif int(elem3) == 110:
                param1 = ''
                if 'link' in elem_split[2:]:
                    param1 = '-link-{}-{}'.format(elem_split[-2].replace('m', 'n'), elem_split[-1].replace('m', 'n'))
                    
                metadata_tile = '{}-{}|white|true|{}|false|false{}'.format(get_new_id(int(elem3)), elem_split[2], elem_split[3], param1)
            # portalgun
            elif int(elem3) == 29:
                if elem_split[2] == 'true' and elem_split[3] == 'false':
                    portal_type = "1 only"
                elif elem_split[2] == 'false' and elem_split[3] == 'true':
                    portal_type = "2 only"
                else:
                    portal_type = "both"
                metadata_tile = '{}-{}'.format(get_new_id(int(elem3)), portal_type)
                
            # laser detector
            elif int(elem3) == 56:
                metadata_tile = '56-{}|true|false'.format(elem_split[2])
            # Mario spawnpoint
            elif int(elem3) == 8:
                metadata_tile = '8-false'
            # Mario spawnpoint
            elif int(elem3) == 11:
                metadata_tile = '11-true|true'
            # Checkpoint
            elif int(elem3) == 100:
                if 'region' in elem_split[-1]:
                    metadata_tile = '100-link-check___to___replace-' + elem_split[-1].split('region:')[1]
                else:
                    metadata_tile = '100'
                    
            # Box
            elif int(elem3) == 20 
                if replace_box is not None:
                    metadata_tile = replace_box
                else:
                    metadata_tile = 20
                
            # antlines
            elif int(elem3) in [43, 44, 45, 46, 47, 48]:
                metadata_tile = elem3
                if 'link' in elem_split[2:]:
                    metadata_tile += '-link-{}-{}'.format(elem_split[-2].replace('m', 'n'), elem_split[-1].replace('m', 'n'))
            else:
                metadata_tile = '205|false|0'

            metadata_tile = '-' + metadata_tile
            

        sub_elem = elem2.split('*')

        sub_tile = sub_elem[0]

        if 'c' in sub_tile:
            coin_prefix = '116~'
            sub_tile = sub_tile[:-1]
        
        # For animated tiles
        if int(sub_tile) >= 10000:
            sub_tile = str(int(sub_tile) + 80000)

        sub_tile = coin_prefix + sub_tile  
            
        # To multiply tiles
        if len(sub_elem)>1:
            sub_tile = sub_tile + ','
            multiply = int(sub_elem[1])

            sub_str = sub_tile * multiply
            sub_str = sub_str[:-1]
        else:
            sub_str = sub_tile

        new_body.append(sub_str + metadata_tile)

    # Separate each tile
    new_body_str = ','.join(new_body)
    new_body_list = new_body_str.split(',')
    
    new_body_line = []
    new_body_table = []
    length = len(new_body_list) / height
    
    cpt = 0
    
    # Creates a list of list (for each line of the level)
    for i in new_body_list:
        
        new_body_line.append(i)
        cpt += 1
        
        if cpt == length:
            new_body_table.append(new_body_line)
            new_body_line = []
            cpt = 0
            
    
    dic_anim_check = {}
    # Initialize dictionnary of animation and checkpoint that will need a region trigger
    for y, line in enumerate(new_body_table):
        for x, elem in enumerate(line):
            # Animations
            if "-link-anim___to___replace" in elem:
                elems = elem.split('-')
                dic_anim_check[elems[2] + '_' + str(x) + '_' + str(y)] = {'type':"animation", 'x':x, "y": y, 'player_only': elems[3], 'region': elems[-1]}
            # Checkpoint
            elif "-link-check___to___replace" in elem:
                elems = elem.split('-')
                dic_anim_check["checkpoint_entity_" + str(x) + '_' + str(y)] = {'type':"checkpoint", 'x':x, "y": y, 'region': elems[-1]}
                

    # print(dic_anim_check)
    for key in dic_anim_check:
        dic_prop_anim = dic_anim_check[key]
        
        # Radius in which the animation trigger can be placed (if no entity and not out of borders)
        for radius in range(1, 3):
            coor_check_x = [1, -1, 0, 0, 1, 1, -1,  -1]
            coor_check_y = [0, 0, 1, -1, 1, -1, 1,  -1]
            
            for x_coor, y_coor in zip(coor_check_x, coor_check_y):
                x_trigger, y_trigger = int(dic_prop_anim["x"]) + int(x_coor)*radius, int(dic_prop_anim["y"]) + int(y_coor)*radius
                
                # Check next coordinates if not valid
                if check_if_invalid(new_body_table, x_trigger, y_trigger, length, height):
                    continue
                # Coordinates valid, so we add region trigger and update animation/checkpoint to be linked to region
                else:
                    # Initial offset of the region
                    offset_x = int(dic_prop_anim["region"].split(':')[0].replace('m', '-'))
                    offset_y = int(dic_prop_anim["region"].split(':')[1].replace('m', '-'))
                    
                    # Preparing region trigger
                    region = "-200-{}|{}".format(dic_prop_anim["region"].split(':')[-2].replace('m', 'n'), dic_prop_anim["region"].split(':')[-1].replace('m', 'n'))
                    region = region  + "|{}|{}|"
                    if dic_prop_anim["type"] == "checkpoint" or dic_prop_anim["player_only"] == 'true':
                        region += "player"
                    else : 
                        region += "everything" 
                        
                    if dic_prop_anim["type"] == "checkpoint":
                        # Checkpoint trigger is linked to region trigger
                        new_body_table[dic_prop_anim["y"]][dic_prop_anim["x"]] = "-".join(new_body_table[dic_prop_anim["y"]][dic_prop_anim["x"]].split("-")[0:2]) + '-link-' + str(x_trigger+1) + '-' + str(y_trigger+1)
                    else:
                        # Animation trigger is linked to region trigger
                        new_body_table[dic_prop_anim["y"]][dic_prop_anim["x"]] = "-".join(new_body_table[dic_prop_anim["y"]][dic_prop_anim["x"]].split("-")[0:3]) + '-link-' + str(x_trigger+1) + '-' + str(y_trigger+1)
                    
                    # Region trigger area set
                    new_body_table[y_trigger][x_trigger] = new_body_table[y_trigger][x_trigger] + region.format(str(offset_x - x_trigger+dic_prop_anim["x"]).replace('-', 'n'), str(offset_y - y_trigger+dic_prop_anim["y"]).replace('-', 'n'))
                    # print(new_body_table[dic_prop_anim["y"]][dic_prop_anim["x"]])
                    # print(new_body_table[y_trigger][x_trigger])    
                    break
            break
    
    # new_body_table is list of list so we flatten it
    new_body_flat = [item for sublist in new_body_table for item in sublist]
    new_body_str = ','.join(new_body_flat)
    
    dic_properties = {ele.split('=')[0]: ele.split('=')[1] for ele in split_level[2:] if '=' in ele}

    # End of level metadata
    new_properties = []
    new_properties.append('height=' + str(height))
    new_properties.append('background={},{},{}'.format(int(float(dic_properties["backgroundr"])), int(float(dic_properties["backgroundg"])), int(float(dic_properties["backgroundb"]))))
    new_properties.append("spriteset=" + dic_properties["spriteset"])
    new_properties.append('music=music/' + dic_properties["music"].replace("mp3", convert_mp3))
    # Timelimit
    new_properties.append('timelimit=' + dic_properties["timelimit"])
    
    # background
    if 'custombackground' in dic_properties:
        new_properties.append('custombackground=' + dic_properties["custombackground"])
    # foreground
    if 'customforeground' in dic_properties:
        new_properties.append('customforeground=' + dic_properties["customforeground"])
        
    # scrollfactor background
    new_properties.append('scrollfactor=' + dic_properties["scrollfactor"])
    new_properties.append('scrollfactory=0')
    # scrollfactor foreground
    new_properties.append('scrollfactor2=' + dic_properties["fscrollfactor"])
    new_properties.append('scrollfactor2y=0')
    
    # portalgun
    if 'portalgun' in dic_properties:
        if dic_properties['portalgun']=='none':
            new_properties.append('noportalgun')
        elif dic_properties['portalgun']=='blue':
            new_properties.append('portalguni=3')
        else:
            new_properties.append('portalguni=4')
    else:
        new_properties.append('portalguni=1')

    # version?
    new_properties.append('vs=13.0122')

    new_properties_str = ';'.join(new_properties)

    # Saving level
    lvl_ae = new_body_str + ';' + new_properties_str

    if 'out' not in os.listdir(path) or not os.path.isdir('out'):
        os.mkdir(path + '\\' + 'out')

    path_out = 'out\\' + txt_level

    with open(path_out, 'w+') as f:
        f.write(lvl_ae)
        
    print(txt_level, "done!")