import tkinter as tk
import subprocess

class ServiceControl:
    def __init__(self, master):
        self.master = master
        master.title("Service Control")

        # Create the input box and buttons
        self.input_label = tk.Label(master, text="Enter service name:")
        self.input_box = tk.Entry(master)
        self.start_button = tk.Button(master, text="Start", command=self.start_service)
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_service)

        # Place the input box and buttons in the window
        self.input_label.pack()
        self.input_box.pack()
        self.start_button.pack()
        self.stop_button.pack()

    def start_service(self):
        # Get the service name from the input box
        service_name = self.input_box.get()

        # Start the service using the subprocess module
        subprocess.run(["net", "start", service_name])

    def stop_service(self):
        # Get the service name from the input box
        service_name = self.input_box.get()

        # Stop the service using the subprocess module
        subprocess.run(["net", "stop", service_name])

root = tk.Tk()
my_gui = ServiceControl(root)
root.mainloop()
