import numpy as np
from scipy.io.wavfile import write, read
from pprint import pprint

tragicaller = read("04LM_-_Tragicaller.wav", mmap=False)
tragicaller_data = list()
tragicaller_data = tragicaller[1][::8]

dopplereffekt = read("Dopplereffekt_-_Tetrahymena.wav", mmap=False)
dopplereffekt_data = list()
dopplereffekt_data = dopplereffekt[1][::8]

marcel = read("Marcel_Dettmann_-_Radar.wav", mmap=False)
marcel_data = list()
marcel_data = marcel[1][::8]


final_list = []
#final_list.append(tragicaller_data)
#final_list.append(dopplereffekt_data)
final_list.append(marcel_data)

f = open('electro_data.txt', 'w')

for song in final_list:
    for i in song:
        f.write(' %s' % i)

f.close
