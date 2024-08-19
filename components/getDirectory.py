import ast

def readDirectory(): 
    try:
        file = open("rehber.txt", "r")
        readed = ast.literal_eval(file.read())
        file.close()
        return readed
    except:
        print("!!Dosya Okuma Hatası!!")

def printDirectory():
    directory = readDirectory()
    print("İsim\tNumara\n"+"="*18)
    for i in directory:
        print(f"{i["isim"]}:\t{i["numara"]}")
