import components.addPerson as add
import components.getDirectory as get
import components.search as search

class Menu:

    def __init__(self, options):
        self.options = options
        self.max_width = len(max(self.options, key=len))

    def print_options(self):
        for option in self.options:
            padding = " " * (self.max_width - len(option))
            print(f"║ {option}{padding} ║")

    def draw_frame(self):
        print(f"{' ' * (int(self.max_width / 2 - 2))}PROJELER")
        top_bottom = "═" * (self.max_width + 2)
        print(f"╔{top_bottom}╗")
        print(f"║ {' ' * self.max_width} ║")
        self.print_options()
        print(f"║ {' ' * self.max_width} ║")
        print(f"╚{top_bottom}╝")

    def get_selection(self):
        while True:
            try:
                selection = int(input("Bir seçenek seçin: "))
                if selection == 0:
                    print("Programdan çıkılıyor...")
                    return None
                elif selection > len(self.options) - 1:
                    print("Geçersiz seçenek!")
                else:
                    print(self.options[selection - 1], "seçildi.")
                    return selection
            except ValueError:
                print("Lütfen bir sayı girin.")

    def run(self):
        while True:
            self.draw_frame()
            selection = self.get_selection()
            if selection is None:
                break
            elif selection == 1:
                get.printDirectory()
            elif selection == 2:
                add.addPerson()
            elif selection == 3:
                search.searchWithName()
            elif selection == 4:
                search.searchWithNo()
    

if __name__ == '__main__':
    options = [
        "1-Rehberi Görüntüle",
        "2-Kişi Ekle",
        "3-İsme Göre Arama",
        "4-Numaraya Göre Arama",
        "0-Çıkış",
    ]
    menu = Menu(options)
    menu.run()
