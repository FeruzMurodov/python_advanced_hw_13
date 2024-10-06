from datetime import datetime
from os.path import exists
class Chat:
    def __init__(self, filename='chat.txt'):
        self.filename = filename

    def display_messages(self):
        try:
            with open(self.filename, 'r', encoding="utf-8") as fr:
                messages = fr.readlines()
                print("".join(messages))
        except FileNotFoundError:
            print("There is no messages for now.")
    def add_message(self, name, message):
        with open(self.filename, 'a') as fa:
            fa.write(f"{name}:{message}. Time:{datetime.now()}\n")

    def run(self):
        name = input("What's your name? ... ")
        while True:
            command = input("Type 1 to see chat or 2 to send message or 'x' to exit: ")
            if command == '1':
                self.display_messages()
            elif command == '2':
                message = input("Type message: ")
                self.add_message(name, message)
            elif command == 'x':
                break
            else:
                print("Unknown command.")

if __name__ == '__main__':
    chat = Chat()
    chat.run()