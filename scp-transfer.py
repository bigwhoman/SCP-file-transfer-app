import tkinter as tk
from tkinter import filedialog
import paramiko
from scp import SCPClient

def browse_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def create_ssh_client(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def transfer_file():
    host = host_entry.get()
    port = int(port_entry.get())
    user = user_entry.get()
    password = password_entry.get()
    file_path = file_entry.get()

    ssh = create_ssh_client(host, port, user, password)
    scp = SCPClient(ssh.get_transport())
    scp.put(file_path)
    scp.close()
    ssh.close()

root = tk.Tk()
root.title("SCP File Transfer")

host_label = tk.Label(root, text="Host:")
host_label.grid(row=0, column=0)
host_entry = tk.Entry(root)
host_entry.grid(row=0, column=1)

port_label = tk.Label(root, text="Port:")
port_label.grid(row=1, column=0)
port_entry = tk.Entry(root)
port_entry.grid(row=1, column=1)

user_label = tk.Label(root, text="Username:")
user_label.grid(row=2, column=0)
user_entry = tk.Entry(root)
user_entry.grid(row=2, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1)

file_label = tk.Label(root, text="File:")
file_label.grid(row=4, column=0)
file_entry = tk.Entry(root)
file_entry.grid(row=4, column=1)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=4, column=2)
transfer_button = tk.Button(root, text="Transfer", command=transfer_file)
transfer_button.grid(row=5, column=1)
root.mainloop()






