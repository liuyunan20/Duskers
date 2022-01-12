class Robot:
    def __init__(self):
        self.robot = '''
  ╬   ╬╬╬╬╬╬╬   ╬     ╬   ╬╬╬╬╬╬╬   ╬     ╬   ╬╬╬╬╬╬╬   ╬   
  ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬     ╬╬╬╬╬   
      ╬╬╬╬╬╬╬             ╬╬╬╬╬╬╬             ╬╬╬╬╬╬╬       
     ╬╬╬   ╬╬╬           ╬╬╬   ╬╬╬           ╬╬╬   ╬╬╬      
     ╬       ╬           ╬       ╬           ╬       ╬      
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

    def print_log(self, robot):
        print("║════════════════════════════════════════════════════════════════════════════════║")
        print(robot.robot)
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

    def game_menu(self, robot):
        self.print_game_menu()
        while True:
            print("\nYour command:")
            game_menu_option = input()
            if game_menu_option.lower() == "exit":
                self.exit()
                break
            elif game_menu_option.lower() == "save":
                self.save()
                break
            elif game_menu_option.lower() == "back":
                self.play(robot)
                break
            elif game_menu_option.lower() == "main":
                self.main_menu(robot)
                break

    def play(self, robot):
        print("Enter your name:")
        name = input()
        print(f"\nGreetings, commander {name}!")
        while True:
            print('''Are you ready to begin?
[Yes] [No] Return to Main[Menu]

Your command:''')
            begin_option = input()
            if begin_option.lower() == "yes":
                self.print_log(robot)
                print("\nYour command:")
                play_option = input()
                if play_option.lower() == "m":
                    self.game_menu(robot)
                    break
                elif play_option.lower() == "save":
                    self.save()
                    break
                elif play_option.lower() == "up":
                    self.upgrade()
                    break
                elif play_option.lower() == "ex":
                    self.explore()
                    break
                else:
                    print("Invalid input")
            elif begin_option.lower() == "no":
                print("How about now.")
            elif begin_option.lower() == "main":
                self.main_menu(robot)
                break
            else:
                print("Invalid input")

    def high(self, robot):
        while True:
            print('''No scores to display.
[Back]

Your command:''')
            back = input()
            if back.lower() == "back":
                self.main_menu(robot)
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

    def main_menu(self, robot):
        self.print_title()
        while True:
            print("\nYour command:")
            self.start_option = input()
            print()
            if self.start_option.lower() == "play":
                self.play(robot)
                break
            elif self.start_option.lower() == "high":
                self.high(robot)
                break
            elif self.start_option.lower() == "exit":
                self.exit()
                break
            elif self.start_option.lower() == "help":
                self.help()
                break
            else:
                print("Invalid input")


my_robot = Robot()
my_menu = Menu()
my_menu.main_menu(my_robot)




