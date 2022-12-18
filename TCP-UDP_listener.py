import socket

# Create a socket to listen for TCP connections
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(("", 0))
tcp_socket.listen(5)

# Create a socket to listen for UDP packets
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", 0))

# Create a list to store the results
results = []

# Start listening for incoming connections and packets
while True:
    # Check for incoming TCP connections
    r, _, _ = select.select([tcp_socket], [], [], 0.5)
    for sock in r:
        conn, addr = sock.accept()
        results.append(f"TCP connection from {addr[0]}:{addr[1]}")
        conn.close()

    # Check for incoming UDP packets
    r, _, _ = select.select([udp_socket], [], [], 0.5)
    for sock in r:
        data, addr = sock.recvfrom(1024)
        results.append(f"UDP packet from {addr[0]}:{addr[1]}: {data}")

# Open a new text file for writing
with open("results.txt", "w") as f:
    # Write the results to the file
    for result in results:
        f.write(result + "\n")
