# Print title
class Menu:
    def __init__(self):
        self.start_option = None

    def print_title(self):
        print('''
╱╱╭╮╱╱╱╱╱╱╱╱╭╮
╱╱┃┃╱╱╱╱╱╱╱╱┃┃
╭━╯┣╮╭┳━━┳━━┫┃╭┳━━┳━┳━━╮
┃╭╮┃┃┃┃━━┫╭━┫╰╯┫┃━┫╭┫━━┫
┃╰╯┃╰╯┣━━┃╰━┫╭╮┫┃━┫┃┣━━┃
╰━━┻━━┻━━┻━━┻╯╰┻━━┻╯╰━━╯
        ''')
        print("[Play]", "[High] Scores", "[Help]", "[Exit]", sep="\n")

    def print_log(self):
        print('''
 ────────────(LOG)─────────────────────────────(LOG)─────────────────────────────
║════════════════════════════════════════════════════════════════════════════════║
║────────────────────────────────────────────────────────────────────────────────║
║────────────(ROBOT IMAGES)──────────────────────────────────────────────────────║
║────────────────────────────────────────────────────────────────────────────────║
║────────────────────────────────────────────────────────────────────────────────║
║────────────────────────────────────────────────────────────────────────────────║
║────────────────────────────────────────────────────────────────────────────────║
║────────────────────────────────────────────────────────────────────────────────║
║════════════════════════════════════════════════════════════════════════════════║
║                  [Ex]plore                          [Up]grade                  ║
║                  [Save]                             [M]enu                     ║
║════════════════════════════════════════════════════════════════════════════════║''')

    def menu(self):
        self.print_title()
        while True:
            print("Your command:")
            self.start_option = input()
            print()
            if self.start_option.lower() == "play":
                print("Enter your name:")
                name = input()
                print(f"\nGreetings, commander {name}!")
                while True:
                    print('''Are you ready to begin?
[Yes] [No] Return to Main[Menu]
    
Your command:''')
                    begin_option = input()
                    if begin_option.lower() == "yes":
                        self.print_log()
                        return True
                    elif begin_option.lower() == "no":
                        print("\nHow about now.")
                    elif begin_option.lower() == "menu":
                        self.print_title()
                        break
                    else:
                        print("Invalid input")
            elif self.start_option.lower() == "high":
                while True:
                    print('''No scores to display.
    [Back]
    
Your command:''')
                    back = input()
                    if back.lower() == "back":
                        self.print_title()
                        break
                    else:
                        print("Invalid input")
            elif self.start_option.lower() == "exit":
                print("Thanks for playing, bye!")
                break
            elif self.start_option.lower() == "help":
                print("Coming SOON! Thanks for playing!")
                break
            else:
                print("Invalid input")


my_menu = Menu()
my_menu.menu()




