# AirBnb Clone Website
This project is for deploying a simple copy of the **AirBnB Website** by bulding a full web application. The application will be composed of:

- A **Command Interpreter** to manipulate data without a visual interface, like in a Shell(Perfect for development and debugging)
- A website **(the front-end)** that shows the final product to everybody: **static** and **dynamic**
- A **database** or filed that stores data (data = objects)
- An **API** that provides a communication interface between the front-end and your data(retrieve, create, delete, update them)

## 1.The Console
The first step of this project is to create a console which is a simple
command interpreter shell for
1. Creating a data model
2. Manage (create, update, destroy, etc) objects via the console / command
interpreter
3. Store and persist objects to a file (JSON file)

## How to use the command Interpreter(Console)
- The command Interpreter is started by running the `console.py` script.
- After starting the interpreter, you can write the command `help` to see the
available commands and if you want to know what each command does you just type 
the command `help command`.
Example:
```console
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit
$
```
