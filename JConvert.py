Temp = input()
if Temp[-3:] in ['cal']:
    J = eval(Temp[:-3])*4.186
    print("{:.3f}J".format(J))
elif Temp[-1::] in ['J']:
    CAL = eval(Temp[:-1])/4.186
    print("{:.3f}cal".format(CAL))

