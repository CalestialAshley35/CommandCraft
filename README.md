# CommandCraft

CommandCraft is a text-based game that allows users to create and execute custom commands. It is a fun and interactive way to learn about command execution in a programming context. 

## How to Access CommandCraft

- **Replit**: [Play CommandCraft](https://replit.com/@calestialashley/CommandCraft?s=app)
- **GitHub**: [Source Code](https://github.com/CalestialAshley35/CommandCraft.git)

## License

CommandCraft is licensed under the MIT License. The source code is freely available, and you can modify and distribute it under the terms of the MIT License.

## Available Commands

1. **$createcommand [name] [code]**: Create a custom command with the given name and code.
   - Example: `$createcommand greet print("Hello, world!")`
2. **$echo [message]**: Print the given message.
   - Example: `$echo Hello, world!`
3. **$commands**: Show all custom commands.
   - Example: `$commands`
4. **$input [prompt]**: Prompt the user for input and display what they entered.
   - Example: `$input What is your name?`
5. **$help**: Show the help message.
   - Example: `$help`

## How to Play

1. **Starting the Game**:
   - Run the game on Replit: [Play CommandCraft](https://replit.com/@calestialashley/CommandCraft?s=app).
   - You’ll see a welcome message and can start typing commands.

2. **Creating a Command**:
   - Use `$createcommand` to define a new command.
   - Example: `$createcommand greet print("Hello, world!")`
   - This creates a command `greet` that, when executed, prints "Hello, world!".

3. **Executing Commands**:
   - Type the name of your custom command to execute it.
   - Example: `greet` (after creating it with the above example).

4. **Echoing Messages**:
   - Use `$echo` to print any message.
   - Example: `$echo Hello, world!`

5. **Listing Commands**:
   - Use `$commands` to view all custom commands you’ve created.

6. **Taking Input**:
   - Use `$input` to prompt the user for input.
   - Example: `$input What is your name?`
   - The input will be displayed after the prompt.

7. **Getting Help**:
   - Use `$help` to display the help message with a list of available commands.

## Error Handling

CommandCraft includes error handling to catch and display errors that occur during the execution of custom commands. If you attempt to execute an undefined command, you will see an error message prompting you to check the available commands using `$help`.

## Example Usage

```plaintext
> $createcommand greet print("Hello, world!")
> greet
Hello, world!
> $echo This is CommandCraft
This is CommandCraft
> $input What is your favorite color?
What is your favorite color?
You entered: Blue
> $commands
greet: print("Hello, world!")
```

## Feedback and Contributions

You can find the source code on GitHub: [Source Code](https://github.com/CalestialAshley35/CommandCraft.git).

Feel free to fork the repository, make improvements, and submit pull requests. Report any issues or bugs via the GitHub issues page.

## Created By

- **GitHub**: @calestial_ashley
- **Display Name**: Calestial Ashley

Enjoy playing CommandCraft and exploring the possibilities with custom commands!
```
