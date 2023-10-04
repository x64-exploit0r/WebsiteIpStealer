#VERSION 4.10.2023
#MOST SHIT PROGRAM I HAVE EVER WRITTEN BUT ALSO MOST USEFULL.
import socket

input = input("Enter the website(example www.etc.com)")
Ip = socket.gethostbyname(input)
print(f"Ip of {input} is {Ip}")
