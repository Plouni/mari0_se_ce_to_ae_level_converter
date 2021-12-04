import os

for lvl in os.listdir():
    if '_' not in lvl:
        os.rename(lvl, "levelscreen.".join(lvl.split('.')))