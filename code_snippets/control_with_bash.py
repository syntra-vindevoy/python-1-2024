import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: qpy <command>")
        return

    command = sys.argv[1]

    if command == "test":
        print("test")
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()


''' bash
alias qpy='python3 /path/to/control_with_bash.py'
source ~/.bashrc  # or source ~/.bash_profile
qpy test
'''

