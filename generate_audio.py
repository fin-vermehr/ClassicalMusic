import numpy as np
from scipy.io.wavfile import write
import sample

sample_ = sample.main()

f = open("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/lstm_net_output/generate_audio_text.txt", "w")

f.write(sample_)

print(sample_)
print "Writing was succesful..."
