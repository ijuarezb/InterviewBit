#!/usr/bin/env python3
import sys
import socket

def tryPort(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = False
    try:
        sock.bind((host, port))
        result = True
    except:
        print("Port is in use")
    sock.close()
    return result

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

if __name__ == '__main__':

	# Reading arguments from command line
	if len(sys.argv) > 1:
		for arg in sys.argv:
			print(arg)

	# Reading from STDIN
	print("start writing from STDIN")
	for line in sys.stdin:
		print(line, end='')
	print("end writing from STDIN")

	# import sys
	# data = sys.stdin.readlines()
	# print "Counted", len(data), "lines."

	# Reading a whole file of text
	with open("host.txt", mode='r') as data:
		lines = data.readlines()
		for line in lines:
			#print(line.strip())
			#tryPort(line.strip(), 81)
			if isOpen(line.strip(), 443):
				print(line.strip(), "port 443 is open")
			else:
				print(line.strip(), "port 443 is close")

	# file = open('fangraphs_leaderboard.csv', 'r', encoding='utf-8-sig');
	# fileL = file.readlines();
	# file.close();
	#
	# lenL = len(fileL);
	# i=0;
	#
	# str = fileL[0].replace('"','');
	# fields = str.split(',');
	#
	# D = {};
	#
	# while ( i < lenL ):
	# 	my_str = fileL[i].replace('"','').rstrip();
	# 	my_list = my_str.split(',');
	# 	D[my_list[0]] = my_list;
	# 	i = i + 1;

	A = [[4, 'rojo'], [7, 'verde'], [2, 'amarillo'], [1, 'naranja'], [10, 'azul']]
	D = {'rojo':4, 'verde':7, 'amarillo':2, 'naranja':1, 'azul':10}

	print(A)

	# Sort Dictionary by VAlUE
	for f in sorted(D, key=D.get, reverse=True):
		print(f, D[f])


