import keyboard
import components.addPerson as add
import components.getDirectory as get
import components.search as search

class Menu:

    def __init__(self, options):
        self.options = options
        self.max_width = len(max(self.options, key=len))
        self.cursesPlace = 0 
            
    def print_options(self):
        for index, option in enumerate(self.options):
            padding = " " * (self.max_width - len(option))
            if index == self.cursesPlace:
                print(f"║>{option}{padding} ║")
            else: 
                print(f"║ {option}{padding} ║")


    def draw_frame(self):
        print(f"{' ' * (int(self.max_width / 2 - 2))}PROJELER")
        top_bottom = "═" * (self.max_width + 2)
        print(f"╔{top_bottom}╗")
        print(f"║ {' ' * self.max_width} ║")
        self.print_options()
        print(f"║ {' ' * self.max_width} ║")
        print(f"╚{top_bottom}╝")


    def run(self):
        while True:
            self.draw_frame()
            key = keyboard.read_event()
            if key.event_type == "down" and key.name == "up":
                self.cursesPlace = (self.cursesPlace - 1) % len(self.options)
            elif key.event_type == "down" and key.name == "down":
                self.cursesPlace = (self.cursesPlace + 1) % len(self.options)
            elif key.event_type == "down" and key.name == "enter":
                self.select_option()

 
    def select_option(self):
        option = self.options[self.cursesPlace]
        if option.startswith("1"):
            get.printDirectory()
        elif option.startswith("2"):
            add.addPerson()
        elif option.startswith("3"):
            search.searchWithName()
        elif option.startswith("4"):
            search.searchWithNo()
        elif option.startswith("0"):
            print("Çıkış yapılıyor...")
            exit()

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
