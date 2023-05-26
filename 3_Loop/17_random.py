import random
ct_h = 0
ct_t = 0
for i in range(76):
    int = random.randint(0,1)
    if int == 1:
        print("H",end = ' ')
        ct_h = ct_h + 1
    if int == 0:
        print("T",end = ' ')
        ct_t = ct_t + 1
print()
print("Probability of head = ", ct_h/(ct_h + ct_t))
print("Probability of tail = ", ct_t/(ct_h + ct_t))
