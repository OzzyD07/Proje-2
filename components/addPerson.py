def addPerson():
    name = input("İsim girin: ")
    no = int(input("Numara girin: "))
    file = open("rehber.txt", "a")
    person = {
        "isim": name,
        "numara": no
    }
    file.write(str(person)+ ",")
    file.close()
