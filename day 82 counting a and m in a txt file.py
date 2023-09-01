def AMCount():
    f = open("story1.txt")
    data = f.read()
    print(data)
    cnta = 0
    cntm = 0
    for i in data:
        if i in 'aA':
            cnta += 1
        elif i in 'mM':
            cntm += 1
    print("A Occurs : ",cnta," times")
    print("M Occurs : ",cntm," times")
AMCount()
