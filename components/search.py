import components.getDirectory as get

def searchWithName():
    try:
        searchedName = input("Aramak istediğiniz ismi girin: ")
        directory = get.readDirectory()
        for i in directory:
            if searchedName.upper() == i["isim"].upper(): 
                print(f"{i['isim']}:\t{i['numara']}")
    except:
        print("Lütfen geçerli bir isim girin")
        searchWithName()


def searchWithNo():
    try:
        searchedNo = int(input("Aramak istediğiniz numarayı girin: "))
        directory = get.readDirectory()
        for i in directory:
            if searchedNo == i["numara"]: 
                print(f"{i['isim']}:\t{i['numara']}")
    except:
        print("Lütfen geçerli bir numara girin")
        searchWithNo()