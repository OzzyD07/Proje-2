import components.getDirectory as get

def searchWithName():
    searchedName = input("Aramak istediğiniz ismi girin: ")
    directory = get.readDirectory()
    for i in directory:
        if searchedName.upper() == i["isim"].upper(): 
            print(f"{i['isim']}:\t{i['numara']}")

def searchWithNo():
    searchedNo = int(input("Aramak istediğiniz numarayı girin: "))
    directory = get.readDirectory()
    for i in directory:
        if searchedNo == i["numara"]: 
            print(f"{i['isim']}:\t{i['numara']}")
