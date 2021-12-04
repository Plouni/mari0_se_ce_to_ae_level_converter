import os

for mus in os.listdir():
    if '.mp3.ogg' in mus:
        os.rename(mus, mus.replace('.mp3.ogg', '.ogg'))