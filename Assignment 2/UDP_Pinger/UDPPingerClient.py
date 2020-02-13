import socket
import time

msgFromClient       = "Hello UDP Server"
serverAddressPort   = ("127.0.0.1", 8700)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(2)

while True:
    message = input("Enter yoour message in lowevercase: ")
    send_time = time.monotonic_ns()
    # Send to server using created UDP socket
    UDPClientSocket.sendto(message.encode(), serverAddressPort)
    try:
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "Message from Server {}".format(msgFromServer[0])
        received_time = time.monotonic_ns()
        time_diff = received_time - send_time
        print(msg, "RTT Time: ", time_diff, "ns")
    except socket.timeout as e:
        received_time = time.monotonic_ns()
        time_diff = received_time - send_time
        print(msg, "RTT Time: ", time_diff, "ns")
        print(e)

    