# Custom command storage
commands = {}

def create_command(name, code):
    commands[name] = code

def echo(message):
    print(message)

def show_commands():
    for cmd in commands:
        print(f"{cmd}: {commands[cmd]}")

def get_input(prompt):
    return input(prompt)

def help():
    print("""
Available commands:
$createcommand - Create a custom command.
$echo - Print a message.
$commands - Show all custom commands.
$input - Get user input.
$help - Show this help message.
""")

def execute_command(command):
    parts = command.split(' ', 1)
    cmd = parts[0]
    args = parts[1] if len(parts) > 1 else ""

    if cmd == "$createcommand":
        if ' ' in args:
            name, code = args.split(' ', 1)
            create_command(name, code)
        else:
            print("Usage: $createcommand [name] [code]")
    elif cmd == "$echo":
        echo(args)
    elif cmd == "$commands":
        show_commands()
    elif cmd == "$input":
        prompt = args
        user_input = get_input(prompt)
        print(f"You entered: {user_input}")
    elif cmd == "$help":
        help()
    else:
        if cmd in commands:
            try:
                exec(commands[cmd])
            except Exception as e:
                print(f"Error executing command '{cmd}': {e}")
        else:
            print("Unknown command. Type $help for a list of commands.")

def main():
    print("Welcome to CommandCraft!")
    print("Type $help for a list of commands.")

    while True:
        command = input("> ")
        execute_command(command)

if __name__ == "__main__":
    main()
