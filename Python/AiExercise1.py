
def multiply(x, y):
    if y > 0:
        return x + multiply(x, y-1)
    elif y<0:
        return -multiply(x,0-y)
    else:
        return 0
    
def divide(x, y):
    if x < 0 and y < 0:
        return divide(0 - x, 0 - y)
    elif x < 0:
        return 0 - divide(0 - x, y)
    elif y<0:
        return 0 - divide (x, 0 - y)
    else:
        return divide_helper(x, y, 0)

def divide_helper(x, y, temp):
    if y > x:
        return temp
    else:
        return divide_helper(x - y, y, temp + 1)
a = input()
b = input()
print(multiply(int(a),int(b)))
print(divide(int(a),int(b)))