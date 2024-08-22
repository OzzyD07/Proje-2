import keyboard, os 
import components.addPerson as add
import components.getDirectory as get
import components.search as search
import components.editPerson as edit

class Menu:
    def __init__(self, options):
        self.options = options
        self.max_width = max(len(option) for option in self.options)
        self.cursor_position = 0

    def print_options(self):
        for index, option in enumerate(self.options):
            padding = " " * (self.max_width - len(option))
            prefix = ">" if index == self.cursor_position else " "
            print(f"║  {prefix}{option}{padding} ║")

    def draw_frame(self):
        title = "PROJELER"
        print(f"{' ' * (self.max_width // 2 - len(title) // 2)}{title}")
        top_bottom = "═" * (self.max_width + 4)
        print(f"╔{top_bottom}╗")
        print(f"║ {' ' * (self.max_width + 2)} ║")
        self.print_options()
        print(f"║ {' ' * (self.max_width + 2)} ║")
        print(f"╚{top_bottom}╝")

    def run(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.draw_frame() 
            event = keyboard.read_event(suppress=True)
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == "up":
                    self.cursor_position = (self.cursor_position - 1) % len(self.options)
                elif event.name == "down":
                    self.cursor_position = (self.cursor_position + 1) % len(self.options)
                elif event.name == "enter":
                    self.select_option()
                    if self.cursor_position == len(self.options) - 1:
                        break

    def select_option(self):
        option = self.options[self.cursor_position]
        os.system('cls' if os.name == 'nt' else 'clear')
        if option.startswith("1"):
            get.printDirectory()
        elif option.startswith("2"):
            add.addPerson()
        elif option.startswith("3"):
            search.searchWithName()
        elif option.startswith("4"):
            search.searchWithNo()
        elif option.startswith("5"):
            edit.editPerson()
        elif option.startswith("0"):
            print("Çıkış yapılıyor...")
            return
        
        input("Devam etmek için bir tuşa basın...")

if __name__ == '__main__':
    options = [
        "1-Rehberi Görüntüle",
        "2-Kişi Ekle",
        "3-İsme Göre Arama",
        "4-Numaraya Göre Arama",
        "5-Kişi Düzenle Veya Sil",
        "0-Çıkış",
    ]
    menu = Menu(options)
    menu.run()