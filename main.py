from game import Game
from menu import MainMenu, OptionsMenu, CreditsMenu

#def main():

g = Game()

#state_dict = { menu.MainMenu, menu.OptionsMenu, menu.CreditsMenu, farm.FarmMenu}
   # g.setup_states(state_dict)
    #g.main()
while g.running:
    if MainMenu.check_input == ['Options'] or ['Credits']:
        g.curr_menu.display_menu()
    elif MainMenu.check_input == ['Start']:
        g.event_menu.display_menu()
    #g.gameLoop()
    #if MainMenu.check_input.actions['start']:
       # g.event_menu.display_menu()



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
