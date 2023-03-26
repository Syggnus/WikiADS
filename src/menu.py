class Menu:
    def __init__(self):
        self.options = {
            1: "Sistemas Operacionais",
            2: "Arquitetura e Organização de Computadores",
            3: "Sair"
        }
    
    def print_menu(self):
        print("Menu Principal:")
        for key, value in self.options.items():
            print(f"{key} - {value}")
    
    def get_input(self):
        return int(input("Digite uma opção: "))
    
    def is_valid_option(self, option):
        return option in self.options.keys()