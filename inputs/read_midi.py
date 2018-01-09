import glob
f = open("convert.txt", "w")

for filename in glob.iglob('*.mid'):
    print(filename)
    print(filename)
    s =filename[:-4]
    d = "midicsv /Users/finvermehr/Documents/Coding/Python/machine-learning/classical/inputs/{}.mid /Users/finvermehr/Documents/Coding/Python/machine-learning/classical/outputs/{}.csv \n".format(filename[:-4], filename[:-4])
    print(d)
    f.write(d)
