import os
import subprocess

# Define the server commands
windows_commands = ["net", "start", "w3svc"]
linux_commands = ["service", "apache2", "start"]

# Start the server on Windows
if os.name == "nt":
    subprocess.run(windows_commands)

# Start the server on Linux
else:
    subprocess.run(linux_commands)

# Create the chatbox interface for configuring permissions
while True:
    command = input("Enter a command: ")
    if command == "exit":
        break
    elif command == "permissions on":
        # Enable permissions
        subprocess.run(["chmod", "755", "/var/www"])
    elif command == "permissions off":
        # Disable permissions
        subprocess.run(["chmod", "700", "/var/www"])
    else:
        print("Invalid command")

# Stop the server on Windows
if os.name == "nt":
    subprocess.run(["net", "stop", "w3svc"])

# Stop the server on Linux
else:
    subprocess.run(["service", "apache2", "stop"])
