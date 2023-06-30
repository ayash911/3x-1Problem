import matplotlib.pyplot as plt
#every number upto 2 to the 68th power has been checked by this method and all of them end at a loop of 4,2,1
x = int(input("Enter the number: "))
def plot():
    xc,yc,a = [],[]
    while x != 1: #stop loop at 1
        if x % 2 == 0:
            x /= 2 #if numebr is even divide by 2
        else:
            x = (x*3) + 1 #if number is odd multiply by 3 and add 1
        print(x)        
        yc.append(x)
        xc.append(a)
        a += 1

    plt.plot(xc,yc) #plot the graph of the points
    plt.show()
plot()
