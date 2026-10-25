import os
import sys

from filesystem import FileSystem   # <-- File Management module

fs = FileSystem()                    # <-- one shared file system for the session

# STUDENT 5 ADDITION: User management and system information
import platform
import users

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_help():
    print("\nAvailable Commands:")
    print(" help                -Show available commands")
    print(" clear               -Clear the terminal screen")
    print(" exit                -Shut down MiniOS")

    # Under File Management
    print("")
    print(" dir [folder]        -List files and folders")
    print(" mkdir <folder>      -Create a new directory")
    print(" create <file> [text]-Create a new file")
    print(" read <file>         -Display the contents of a file")
    print(" delete <name>       -Delete a file or an empty folder")
    print(" write <file> <text> -Write text to a file")
    print(" rename <old> <new>  -Rename a file or folder")
    print(" cd <folder>         -Change directory (cd .. goes up)")
    print(" pwd                 -Show the current directory")

    # Under Process Management
    print("")
    print("")
    print("")
    print("")

    # Under Memory Management
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")


def exit_os():
    print("\nMiniOSMTB is shutting down... \nBye, I'll miss you")
    sys.exit(0)

def show(result):
    """Print a file system result (skips empty strings, e.g. after cd)."""
    if result:
        print("\n" + result + "\n")


# STUDENT 5 ADDITION: System information command
def show_systeminfo():
    print("\n========================================")
    print("           SYSTEM INFORMATION")
    print("========================================")
    print("OS Name: MiniOS MTB")
    print("Version: 1.0")
    print(f"Architecture: {platform.architecture()[0]}")
    print("CPU: Virtual CPU (simulated)")
    print("Memory: 1024 MB (simulated)")
    print(f"User: {users.get_current_user()}")
    print("========================================\n")


# Brain of our code, means your logic is supposed to be inserted under defmain()
def main():
    clear_screen()
    print("========================================================================================================================")
    print("                                                       MINIOS MTB                                                                                            ")
    print("========================================================================================================================")
    print("\nWelcome to MiniOSMTB!\n")

# STUDENT 5 ADDITION: Require a successful login before using MiniOS
    if users.login() is None:
        return

    while True:
        try:
            user_input = input("MiniOSMTB>").strip()
            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]

            if command == "exit":
                exit_os()
            elif command == "help":
                display_help()
            elif command == "clear":
                clear_screen()
            # ---------------- File Management ----------------
            elif command == "dir":
                show(fs.dir(args[0] if args else None))
            elif command == "mkdir":
                show(fs.mkdir(args[0] if args else ""))
            elif command == "create":
                show(fs.create(args[0] if args else "", " ".join(args[1:])))
            elif command == "read":
                show(fs.read(args[0] if args else ""))
            elif command == "delete":
                show(fs.delete(args[0] if args else ""))
            elif command == "write":
                if len(args) < 2:
                    show("Usage: write <file> <text>")
                else:
                    show(fs.write(args[0], " ".join(args[1:])))
            elif command == "rename":
                if len(args) < 2:
                    show("Usage: rename <old> <new>")
                else:
                    show(fs.rename(args[0], args[1]))
            elif command == "cd":
                show(fs.cd(args[0] if args else None))
            elif command == "pwd":
                show(fs.pwd())

            # ---------------- Process Management (teammate) ----------------

            # ---------------- Memory Management (teammate) -----------------

            # STUDENT 5 ADDITION: User and system commands
            elif command == "whoami":
                users.whoami()
            elif command == "systeminfo":
                show_systeminfo()
            else:
                print(f"\nUnknown command: '{command}'.")
                print("Type 'help' to see the available commands\n")

        except KeyboardInterrupt:
            exit_os()

        # STUDENT 5 ADDITION: Catch unexpected errors so the CLI can continue
        except Exception as error:
            print(f"\nError: The command could not be completed: {error}")

if __name__ == "__main__":
    main()
