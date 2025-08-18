import os

def dele(whatt):
    if os.path.exists(whatt):
     os.remove(whatt)

def writee(whatt, too):
    with open(whatt,"r") as ds:
        con=ds.read()

    with open(whatt,"w") as de:
        de.write(con)
        de.write(too)

def ridd(whatt): 
    with open(whatt,"r") as de: 
        print(de.read())
        dataa = de.read()

file = 'hello'
writee(file, '\n yo')
ridd(file)
