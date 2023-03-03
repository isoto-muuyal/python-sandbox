datosA = {0,1, 2, 4, 6};
datosB = {1, 2, 3 ,4 ,5 ,6 ,9};

print("original set A is: ",datosA,"\n")
print("original set B is: ",datosB,"\n")

datosA.add(input("please enter your first Name to set A: "))
datosA.add(input("please enter your age to add to set A: "))
datosA.add(input("please enter your group number to add to set A: "))

datosC = datosA
datosC.update(datosB)
print("union between A and B :\n", datosC)
datosD = datosA.intersection(datosB)
print("intersection between A and B :\n", datosD)
datosE = datosA.difference(datosB)
print("difference betwen A and B :\n", datosE)
print("symetric difference between A and B :\n", datosA ^ datosB)