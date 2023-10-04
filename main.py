#VERSION 4.10.2023

import socket

input = input("Enter the website(example www.etc.com)")
Ip = socket.gethostbyname(input)
print(f"Ip of {input} is {Ip}")