#Using a while loop, write a function that continuously asks the user for input until they type the word "exit".
def ask_until_exit():
    while True:
        user_input = input("Enter a word (type 'exit' to stop): ")
        if user_input.lower() == "exit":
            break
        print(user_input)

# Call the function
ask_until_exit()
