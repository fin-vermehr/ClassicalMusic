import glob
from operator import itemgetter
import re
def convert(filename):

    f = open(filename, 'r')
    lines = f.readlines()

    final_list = []

    previous_channel = 1

    med_list = []

    divisor = None
    key_signature = 0

    n_list = []

    for club in lines:
        club = club.split(",")

        if "Header" in club[2]:
            divisor = float(club[5])

        if "Key_signature" in club[2]:
            key_signature = float(re.sub("\D", "", club[3]))

        if int(club[0]) == 3 or int(club[0]) == 2:
            n_list.append(club)
            if int(club[0]) != previous_channel:
                previous_channel = int(club[0])
                previous_channel = int(club[0])
            club[1] = int(club[1])

    n_list = sorted(n_list, key=itemgetter(1))


    for line in n_list:

        if "Note_on_c" in line[2]:
            if line[-1] != " 0\n":
                line[-1] = " 100\n"
                med_list.append(line)
            else:
                med_list.append(line)

        elif "Note_off_c" in line:
            line[2] = " Note_on_c"
            line[-1] = " 0\n"
            med_list.append(line)
        else:
            pass

    for line_ in med_list:
        line_[1] = float(line_[1]) / divisor


        if line_[-1] != " 0\n":

            line_list = []
            line_[4] = float(line_[4]) - key_signature
            line_list.append(float(str(round(line_[1], 4))))
            line_list.append(int(float(str(round(line_[4], 0)))))
            line_list.append(int(line_[0]))
            final_list.append(line_list)

        if line_[-1] == " 0\n":

            if float(line_[4]) == final_list[-1][1] and final_list[-1][-1] == int(line_[0]):
                s = line_[1] - round(final_list[-1][0], 3)
                s = float(str(round(float(s), 4)))
                final_list[-1].insert(1, float(str(round(s, 3))))

                print(line_, final_list[-1])

            else:
                for flist in final_list:
                    if len(flist) == 2 and int(line_[4]) == int(flist[1]) and int(line_[0]) == flist[-1]:
                        s = float(line_[1]) - flist[0]
                        flist.insert(1, float(str(round(s, 3))))

                    else:
                        pass


    of = open("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/input_data.txt", "a")

    new_final = []

    for x in final_list:
        x[0] = round(x[0], 2)
        if len(x) == 3:
            new_final.append(x)


    new_final = sorted(new_final, key=itemgetter(0))
    before = 0

    for spine in new_final:
        if before < spine[0]:
            spine_copy = spine[0]
            spine[0] = round(float(spine[0]) - float(before), 2)
            before = spine_copy

        elif before == spine[0]:
            spine[0] = 0

        elif before > spine[0]:
            before = 0

        else:
            of.write(str(new_final))

    print new_final

    return new_final, divisor

# for filename in glob.iglob('*.csv'):
#     s = convert(filename)
#     print filename, s
#
s = convert("/Users/finvermehr/Documents/Coding/Python/machine-learning/classical/outputs/bmw_988.csv")
