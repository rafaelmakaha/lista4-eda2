import matplotlib.pyplot as plt

avlTime = []
with open("./avl_time", "r") as f:
    content = f.readlines()
    for line in content:
        avlTime.append(line[:-1])
f.close

rbTime = []
with open("./rb_time", "r") as f:
    content = f.readlines()
    for line in content:
        rbTime.append(line[:-1])
f.close

print(avlTime)
print(rbTime)