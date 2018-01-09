from operator import itemgetter
from fractions import *

f = open("lstm_net_output/generate_audio_text.txt", "r")
d = f.readlines()
s = d[0].split("][")

new_l = []
for item in s:
    if "[" in item or "]" in item:
        item = item.replace('[', '')
        item = item.replace(']', '')
    item = item.split(", ")

    if len(item) == 5 and "]" not in item:
        new_l.append(item)

count = 0
d = []
for item in new_l:
    print(item, "P")
    new_l = []
    item[0] = float(item[0])
    item[1] = float(item[1])
    item[3] = float(item[3])
    item[4] = float(item[4])

    count += item[0]
    item[0] = count
    item[1] += item[0]

    new_l.append(round(item[0] * 480, 2)) # Elapsed Time
    new_l.append(round(float(item[1] * 480), 2)) # Note Duration
    new_l.append(item[2]) # Note
    new_l.append(item[3]) # Velocity
    new_l.append(item[4]) # Tempo


    d.append(new_l)

final_orderd = []
for item1 in d:

    start = [item1[0], item1[2], item1[3]]
    end = [item1[1], item1[2], 0]
    final_orderd.append(start)
    final_orderd.append(end)


final_orderd = sorted(final_orderd, key=itemgetter(0))

tempo_list = []

previous_item = None
for item in d:
    if previous_item is None or item[4] != previous_item:
        tempo_l = [item[0], int((1 / (item[4] / 60000000)))]
        tempo_list.append(tempo_l)
        previous_item = item[4]

csv_file = "0, 0, Header, 1, 2, 480\n"
csv_file += "1, 0, Start_track\n"
csv_file += '1, 0, Title_t, "Classical Generated Song"\n'
csv_file += "1, 0, Time_signature, 4, 2, 24, 8\n"

for item in tempo_list:
    new_line = "1, {}, Tempo, {}\n".format(item[0], item[1])
    csv_file += new_line

csv_file += "1, {}, End_track\n".format(item[0])
csv_file += "2, 0, Start_track\n"
csv_file += "2, 0, Program_c, 1, 19\n"

end = None
for sitem in final_orderd:
    try:
        new_line = "2, {}, Note_on_c, 0, {}, {} \n".format("{0:.2f}".format(sitem[0]), int(sitem[1]), sitem[-1])
        csv_file += new_line
        end = "{0:.3f}".format(float(sitem[1]) + float(sitem[0]))
    except:
        pass

csv_file += "2, " + str(end) + ", " + "End_track\n"
csv_file += "0, 0, End_of_file"

print csv_file

csv_output = open("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/lstm_net_output/generated_csv.csv", "w")
csv_output.write(csv_file)
