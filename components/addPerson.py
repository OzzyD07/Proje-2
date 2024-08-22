def addPerson():
    try:
        name = input("İsim girin: ")
        no = int(input("Numara girin: "))
        file = open("rehber.txt", "a")
        person = {
            "isim": name,
            "numara": no
        }
        file.write(str(person)+ ",")
        file.close()
    except: 
        print("Lütfen bir geçerli bir isim veya numara girin")
        addPerson()
