import os

list_anim_tiles = os.listdir()
list_anim_tiles = sorted([ele for ele in list_anim_tiles if ele[-4:] in ['.txt', '.png']])

id_tile = input('> Enter number for the animated tiles after renaming (or press enter to check parent folder for auto increment):\n')

try:
    id_tile = int(id_tile)
except:
    list_anim_tiles_bef = os.listdir('../')
    list_anim_tiles_bef = [int(ele.split('.')[0]) for ele in list_anim_tiles_bef if ele[-4:] in ['.txt']]

    id_tile = max(list_anim_tiles_bef) + 1

orig = list_anim_tiles[0].split('.')[0]

for lvl in list_anim_tiles:
    num = lvl.split('.')[0]

    if num != orig:
        id_tile += 1
        orig = num

    ext = lvl.split('.')[-1]
    ext = '.' + ext
    
    os.rename(lvl, str(id_tile) + ext)
    