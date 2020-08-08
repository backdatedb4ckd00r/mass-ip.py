import socket
#socket.gethostbyname(domain)
file = open('site.txt', 'r')
domain_list = []
for x in file.readlines():
	domain_list.append(x.rstrip())
for y in domain_list:
	print(y + '-> ' + socket.gethostbyname(y))