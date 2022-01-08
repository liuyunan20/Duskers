# Print title
print('''
╱╱╭╮╱╱╱╱╱╱╱╱╭╮
╱╱┃┃╱╱╱╱╱╱╱╱┃┃
╭━╯┣╮╭┳━━┳━━┫┃╭┳━━┳━┳━━╮
┃╭╮┃┃┃┃━━┫╭━┫╰╯┫┃━┫╭┫━━┫
┃╰╯┃╰╯┣━━┃╰━┫╭╮┫┃━┫┃┣━━┃
╰━━┻━━┻━━┻━━┻╯╰┻━━┻╯╰━━╯
''')
while True:
    print('''[Play]
[Exit]
    
Your command:''')
    start_option = input()
    print()
    if start_option.lower() == "play":
        print("Enter your name:")
        name = input()
        print(f"\nGreetings, commander {name}!")
        while True:
            print('''Are you ready to begin?
    [Yes] [No]
    
Your command:''')
            begin_option = input()
            if begin_option.lower() == "yes":
                print("\nGreat, now let's go code some more ;)")
                break
            elif begin_option.lower() == "no":
                print("\nHow about now.")
            else:
                print("Invalid command! Please input yes or no.")
        break
    elif start_option.lower() == "exit":
        print("Thanks for playing, bye!")
        break
    else:
        print("Invalid command! Please input play or exit.")





