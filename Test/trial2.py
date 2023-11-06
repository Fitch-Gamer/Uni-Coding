RawSize = input().split(" ")
y = RawSize[0]
x = RawSize[1]
RawBox = []
LinearWeight = []

for i in range(1,y):
    RawBox.append(input().split(" "))

for i in range (0,x-1):
    mass = 0
    for j in RawBox:
        if j[i] != ".":
            mass +=1
    LinearWeight.append(mass)



