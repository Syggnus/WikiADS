from JSONHandler import JSONHandler
from menu import Menu

menu = Menu()
json_handler = JSONHandler('data.json')

while True:
    menu.print_menu()
    option = menu.get_input()

    if not menu.is_valid_option(option):
        print("Opção inválida! Tente novamente.")
        continue

    if option == 3:
        print("Finalizando Aplicação.")
        break

    data = json_handler.read()
    selected_option = menu.options[option]
    selected_text = data[selected_option]
    print(f"Wiki: {selected_text}")
