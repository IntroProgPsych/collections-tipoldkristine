# https://www.w3schools.com/python/python_match.asp

# Write a function handle_command(cmd) that uses a match expression:
#   - if cmd == "start": print "Starting..."
#   - if cmd == "stop": print "Stopping..."
#   - if cmd == "save": print "Saving..."
#   - otherwise: print "Unknown command"
#
# Ask the user for a command and call the function once.
#
# 
# Write your code here:

def handle_command(cmd):
    match cmd:
        case "start":
            print("Starting...")
        case "stop":
            print("Stopping...")
        case "save":
            print("Saving...")
        case _:
            print("Unknown command")

command = input("Enter a command: ")
handle_command(command)
