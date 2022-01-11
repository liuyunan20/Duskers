class Robot:
    def __init__(self):
        self.robot = '''
   ┼
 ▄█ █▄
▐█▄▄▄█▌
 █ █ █ 
 ║ ║ ║
 
 '''


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

    def print_log(self,robot):
        print("║════════════════════════════════════════════════════════════════════════════════║")
        print(robot.robot * 3, sep=" "*5)
        print('''║════════════════════════════════════════════════════════════════════════════════║
║                  [Ex]plore                          [Up]grade                  ║
║                  [Save]                             [M]enu                     ║
║════════════════════════════════════════════════════════════════════════════════║''')

    def print_game_menu(self):
        print('''                             ║════════════════════════║
                             ║           MENU         ║
                             ║                        ║
                             ║[Back] to game          ║
                             ║ Return to [Main] Menu  ║
                             ║[Save] and exit         ║
                             ║[Exit] game             ║
                             ║════════════════════════║''')

    def game_menu(self):
        self.print_game_menu()
        while True:
            print("\nYour command:")
            game_menu_option = input()
            if game_menu_option.lower() == "exit":
                self.exit()
            elif game_menu_option.lower() == "save":
                self.save()
            elif game_menu_option.lower() == "back":
                return self.play()
            elif game_menu_option.lower() == "main":
                return self.main_menu()

    def play(self):
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
                print("\nYour command:")
                play_option = input()
                if play_option.lower() == "m":
                    self.game_menu()
                elif play_option.lower() == "save":
                    self.save()
                elif play_option.lower() == "up":
                    return self.upgrade()
                elif play_option.lower() == "ex":
                    return self.explore()
                else:
                    print("Invalid input")
            elif begin_option.lower() == "no":
                print("How about now.")
            elif begin_option.lower() == "main":
                return self.main_menu()
            else:
                print("Invalid input")

    def high(self):
        while True:
            print('''No scores to display.
[Back]

Your command:''')
            back = input()
            if back.lower() == "back":
                self.main_menu()
                break
            else:
                print("Invalid input")

    def help(self):
        print("Coming SOON! Thanks for playing!")

    def exit(self):
        print("Thanks for playing, bye!")

    def save(self):
        print("Coming SOON! Thanks for playing!")

    def upgrade(self):
        print("Coming SOON! Thanks for playing!")

    def explore(self):
        print("Coming SOON! Thanks for playing!")

    def main_menu(self):
        self.print_title()
        while True:
            print("Your command:")
            self.start_option = input()
            print()
            if self.start_option.lower() == "play":
                self.play()
            elif self.start_option.lower() == "high":
                self.high()
            elif self.start_option.lower() == "exit":
                self.exit()
                break
            elif self.start_option.lower() == "help":
                self.help()
                break
            else:
                print("Invalid input")


my_menu = Menu()
my_menu.main_menu()




