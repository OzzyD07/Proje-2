import components.getDirectory as get

def editPerson():
    searchedName = input("Düzenlemek istediğiniz kişinin ismini girin: ")
    directory = get.readDirectory()
    
    found = False
    for person in directory:
        if searchedName.upper() == person["isim"].upper():
            found = True
            print(f"Mevcut bilgiler: {person['isim']}: {person['numara']}")
            
            new_name = input("Yeni ismi girin (değiştirmek istemiyorsanız boş bırakın): ")
            new_number = input("Yeni numarayı girin (değiştirmek istemiyorsanız boş bırakın): ")
            
            if new_name:
                person["isim"] = new_name
            if new_number:
                try:
                    person["numara"] = int(new_number)
                except ValueError:
                    print("Geçersiz numara. Numara değiştirilmedi.")
            
            print(f"Güncellenmiş bilgiler: {person['isim']}: {person['numara']}")
            break
    
    if not found:
        print("Bu isimde bir kişi bulunamadı.")

    try:
        with open("rehber.txt", "w") as file:
            for person in directory:
                newList = {
                    "isim" : person["isim"],
                    "numara" : person["numara"]
                }
                file.write(str(newList)+ ",")
        print("Değişiklikler kaydedildi.")
    except IOError:
        print("Dosya yazma hatası oluştu. Değişiklikler kaydedilemedi.")