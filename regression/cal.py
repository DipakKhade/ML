x = [5,7,8,7,2,17,2,9,4,11,12,9,6]


sum = 0

for index, xi in enumerate(x):
    sum += xi

xbar = sum / len(x)

print(xbar)