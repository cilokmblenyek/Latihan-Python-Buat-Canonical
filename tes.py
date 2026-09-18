# 12. enumerate / zip
names = ["a", "b", "c"]
scores = [10, 20, 30]
for i, (n, s) in enumerate(zip(names, scores)):
    print(i, n, s)