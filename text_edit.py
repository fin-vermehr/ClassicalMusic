s = "/Users/finvermehr/Documents/Coding/Python/machine-learning/rapping/data/tinyshakespeare/input.txt"
f = open(s, "r")
lines = f.readlines()
f.close()

f = open(s, "w")

for line in lines:
    if "?" in line or "[" not in line or "]" not in line or "------" not in line:
        if "(x" in line:
            i = line.index("(x")
            for i in range(int(line[i + 2: i + 3])):
                f.write(line[:i])
        else:
            f.write(line)
    else:
        print(line)
f.close()
