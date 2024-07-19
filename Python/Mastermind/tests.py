import subprocess
import time
import numpy

#subprocess.Popen('cd C:\Users\fitch\Desktop\Uni-Coding\Uni-Coding\Python\Mastermind')

Tests = open("calls.txt","r")
i = 1
for test in Tests:
    subprocess.Popen(test)
    time.sleep(0.25)
    Output = open(fr"outputexample{i}.txt")
    Sol = open(fr"C:\Users\fitch\Downloads\MastermindTests\outputexample{i}.txt")
    out = []
    sol1 = []
    for j in Output:
        out.append(j)
    for l in Sol:
        sol1.append(l)
    
    print("test " + str(i))
    try:
        for k in range(0,len(out)):
            numpy.array_equalS
            if(numpy.array_equal( out[k].split(), sol1[k].split())):
                print("line " + str(k) + " wrong")
                print(out[k].split())
                print(sol1[k].split())
    except:
        print("sol is longer")
    print(" ")
    i+=1
