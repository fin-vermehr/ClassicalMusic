import matplotlib.pyplot as plt

f = open("history.txt", 'r')

f = f.readlines()
print(f)
train_loss_history = []
step_history = []

for line in f:
    train_loss = line[:line.index("/")]
    step = line[line.index("/") + 1:]
    step_history.append(step)
    train_loss_history.append(train_loss)

plt.plot(step_history, train_loss_history)
plt.ylabel("Train Loss")
plt.xlabel("Step")
plt.show()
