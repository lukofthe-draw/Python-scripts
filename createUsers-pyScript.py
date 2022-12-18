import os
import subprocess

# Define the username, password, and group for the new user
username = "newuser"
password = "newpassword"
group = "users"

# Create the user on Windows
if os.name == "nt":
    subprocess.run(["net", "user", username, password, "/add"])
    subprocess.run(["net", "localgroup", group, username, "/add"])

# Create the user on Linux
else:
    subprocess.run(["useradd", "-m", "-p", password, "-g", group, username])

# Set the user's permissions
subprocess.run(["chmod", "700", "/home/{}".format(username)])
