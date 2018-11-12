import random 
f = open('training_data.txt', 'w+')
for x in range(0, 100):
    a = random.randint(0,1)
    b = random.randint(0,1)
    if a == b:
        c = 0
    else:
        c = 1
    inputs = str(a)+str(b)+str(c)+"\n"
    f.write(inputs)

f.close()