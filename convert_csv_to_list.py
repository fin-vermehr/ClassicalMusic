import glob
from operator import itemgetter

def convert(filename):

    f = open(filename, 'r')
    lines = f.readlines()

    flag = False

    for line in lines:
        if "Tempo" in line:
            flag = True

    divisor = None
    key_signature = 0
    last_channel = None

    sorted_notes = []

    final_list = []

    combined_list = []

    for line in lines:
        line = line.split(",")

        if "Header" in line[2]:
            divisor = int(line[5])
            print(divisor)

        if "Key_signature" in line[2]:
            key_signature = int(line[3])

        if ("Note_on_c" in line[2] or "Note_off_c" in line[2]):

            line[0] = int(line[0])  # channel
            line[1] = (float(line[1]) / divisor)  # time
            line[2] = line[2].strip()  # description
            line[3] = int(line[3])  # huh
            line[4] = int(line[4]) - key_signature  # midi key
            line[5] = int(line[5].strip("\n"))  # end or start

            if last_channel is None or last_channel < line[0]:
                combined_list.append([line])
                last_channel = line[0]

            if last_channel == line[0]:
                combined_list[-1].append(line)

    for channel in combined_list:

        sorted_notes.append(list())

        for note in channel:

            if note[5] != 0:
                sorted_notes[-1].append([note[1], note[4], note[5]])

            if note[5] == 0:
                if sorted_notes[-1][-1][1] == note[4] and len(sorted_notes[-1][-1]) == 3:
                    sorted_notes[-1][-1].insert(1, note[1])

                else:

                    for short_note in sorted_notes[-1]:
                        if len(short_note) == 3 and\
                           short_note[-2] == note[4]: #and note[1] - short_note[0] < 11:


                           short_note.insert(1, note[1])

    for li in sorted_notes:
        for pe in li:
            final_list.append(pe)

    final_list = sorted(final_list, key=itemgetter(0))

    tempo_list = []

    for line in lines:
        if ", Tempo" in line:
            i = line.index(", Tempo")
            tempo = [round(float(line[2:i]) / divisor, 2)]
            tempo.append(int(60000000 / float(line[i + 9: - 1])))
            tempo_list.append(tempo)



    actual_final = []
    for line_ in final_list:
        try:
            s = [line_[0],round(float(line_[1] - line_[0]), 2), line_[2], line_[3]]
            actual_final.append(s)

        except:
            pass


    for line in actual_final:
        for tempo in tempo_list:
            if tempo[0] >= line[0]:
                if len(line) == 4:
                    line.append(tempo[1])


    of = open("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/input.txt", "a")

    before = 0

    for spine in actual_final:
        if before < spine[0]:
            spine_copy = spine[0]
            spine[0] = round(float(spine[0]) - float(before), 2)
            before = spine_copy

        elif before == spine[0]:
            spine[0] = 0

        elif before > spine[0]:
            before = 0

    for note in actual_final:
        if note[3] % 5 == 0 or note[3] % 10 == 0:
            pass
        else:
            str_note_first = str(note[3])[:-1]
            str_note_last = str(note[3])[-1]

            if int(str_note_last) >= 7.5:
                try:
                    str_note_first = str(int(str_note_first) + 1)
                    str_note_last = str(0)
                except:
                    pass

            elif int(str_note_last) >= 2.5 and int(str_note_last) < 7.5:
                str_note_last = str(5)

            elif int(str_note_last) < 2.5:
                str_note_last = str(0)

            else:
                pass
            note[3] = int(str_note_first + str_note_last)

    if flag is True:
        for a in actual_final:
            of.write(str(a))

    else:
        print("FALSE FLAG")

    return actual_final


for filename in glob.iglob('outputs/*.csv'):
    s = convert(filename)
    print(s)
    print(filename)

#s = convert("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/bach_bmw.csv")
