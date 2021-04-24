import math
import matplotlib.pyplot as plt


def fun1(x) :
    return 1/x

def fun2(x) :
    return math.sqrt(6-x**2)

def fun1_neg(x) :
    return -fun1(x)

def fun2_neg(x) :
    return -fun2(x)

def draw_fun(fn,x_lo,x_hi, y_lo, y_hi, step=1, color=None):
    f1x = []
    f1y = []

    x=x_lo
    while x < x_hi :
        try :
            y = fn(x)
            if y < y_lo or y > y_hi:
                raise Exception("y is too big")
            f1x.append(x)
            f1y.append(y)
        except :
            plt.plot(f1x, f1y, color=color)
            f1x.clear()
            f1y.clear()
        x += step
        x = round(x, 2)
        #print(x)
    plt.plot(f1x, f1y, color=color)

x_lo = -10.0
x_hi = 10.0
x_step = 0.1
y_lo = -10.0
y_hi = 10.0
# axis X
plt.plot([x_lo, x_hi], [0.0, 0.0], color='red')
# axis y
plt.plot([0.0, 0.0], [y_lo, y_hi], color='red')

colors = ['green', 'blue', 'orange', 'purple']
funcs = [[fun1], [fun2, fun2_neg]] #, [math.sqrt], [math.sin], [math.tan]]
color_index = 0
for fn_parts in funcs :
    color = colors[color_index]
    color_index += 1
    if color_index == len(colors) :
        color_index = 0
        
    for fn in fn_parts :
        draw_fun(fn,x_lo,x_hi,y_lo, y_hi, x_step, color=color)
        


    


plt.show()
