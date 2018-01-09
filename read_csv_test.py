import glob
from pprint import pprint
from operator import itemgetter

def convert(filename):

    f = open(filename, 'r')
    lines = f.readlines()

    line_dict = {}

    for line in lines:
        line = line.split(",")
        for i in range(len(line)):
            line[i] = line[i].strip(" ")
            line[i] = line[i].strip("\n")
            line[i] = line[i].strip("'")
            line[i] = line[i].strip('"')

            if line[i].isdigit():
                line[i] = float(line[i])

            if line[i] == "Note_off_c":
                line[i] = "Note_on_c"

        if line[2] not in line_dict:
            line_dict[line[2]] = []

        line_dict[line[2]].append(line)

    key_signature_stamp = 0

    division = line_dict["Header"][0][5]

    channel_dict = {}

    if "Key_signature" in line_dict:
        for note_on in line_dict["Note_on_c"]:
            for key_signature in line_dict["Key_signature"]:

                if key_signature[1] <= note_on[1]:
                    key_signature_stamp = int(key_signature[3])

            note_on[4] -= key_signature_stamp

            if note_on[0] not in channel_dict:
                channel_dict[note_on[0]] = []

            channel_dict[note_on[0]].append(note_on)

    combined_channels = []

    for channel in channel_dict:
        for note in channel_dict[channel]:
            if note[5] != 0:
                single_note = [note[1], note[4], note[5]]
                combined_channels.append(single_note)

            elif note[5] == 0:
                for i in range(len(combined_channels)):
                    if len(combined_channels[i]) == 3 and combined_channels[i][1] == note[4]:

                        combined_channels[i].append(note[1] - combined_channels[i][0])
                        single_note = combined_channels[i]
                        combined_channels[i] = single_note

    if "Tempo" in line_dict:
        if len(line_dict["Tempo"]) == 1:
            for note_on in combined_channels:
                note_on.append(60000000 / line_dict["Tempo"][0][3])
        else:
            for tempo in line_dict["Tempo"]:
                for i in range(len(combined_channels)):
                    if combined_channels[i][0] <= tempo[1]:
                        if len(combined_channels[i]) < 5:
                            combined_channels[i].append(60000000 / tempo[3])
                        single_note = combined_channels[i]
                        combined_channels[i] = single_note

    combined_channels = sorted(combined_channels, key=itemgetter(0))

    for i in range(len(combined_channels)):
        quotient = (combined_channels[i][0]) / division
        combined_channels[i][0] = round(quotient, 2)
        combined_channels[i][1] = int(combined_channels[i][1])
        combined_channels[i][2] = int(combined_channels[i][2])
        combined_channels[i][3] = round(int(combined_channels[i][3]) / division, 3)

        try:
            combined_channels[i][4] = int(combined_channels[i][4])
        except:
            pass

    final_list = []
    previous_time = 0

    for note_on in combined_channels:
        if len(note_on) == 5:
            current_time = note_on[0]
            single_note = [round(note_on[0] - previous_time, 3),
                           note_on[1], note_on[2], note_on[3], note_on[4]]
            previous_time = current_time
            final_list.append(single_note)

    p = open("/Users/finvermehr/Documents/coding/Python/machine-learning/classical/data/input_np.txt", "a")

    if len(final_list) > 20:

        p.write(str(final_list))


    return final_list

for filename in glob.iglob('outputs/beethoven*.csv'):
    print(filename)
    s = convert(filename)
    print(s)
