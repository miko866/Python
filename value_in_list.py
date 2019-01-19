# most frequent value in a list
test = [1, 2, 3, 4, 1, 6, 7, 6, 2, 2, 2]

print(max(set(test), key = test.count))

