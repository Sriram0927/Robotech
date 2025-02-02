# finding the maximum score using for loop
score = [22,11,32,53,56,23,98,76,54,23,65]
maximum = 0
for scores in score:
    if scores > maximum:
        maximum = scores
print(maximum)
