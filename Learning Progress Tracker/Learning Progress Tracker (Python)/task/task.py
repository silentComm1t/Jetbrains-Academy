EXIT_MESSAGE = 'Bye!'

def learning_progress_tracker():
    print('Learning Progress Tracker')

    while True:
        try:
            user_input = input().strip()
        except (EOFError, KeyboardInterrupt):
            print(EXIT_MESSAGE)
            return

        if not user_input:
            print('No input')
            continue
        elif user_input == 'exit':
            print(EXIT_MESSAGE)
            return
        else:
            print('Unknown command')

if __name__ == '__main__':
    learning_progress_tracker()
