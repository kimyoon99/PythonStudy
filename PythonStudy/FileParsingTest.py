'''
Created on 2013. 12. 1.

@author: devsik
'''

import codecs
# pymongo : https://pypi.python.org/pypi/pymongo/
import pymongo
import sys
print sys.getdefaultencoding()

conn = pymongo.Connection("mongodb://localhost:27017");
db = conn['testDB'];

nameList = [];

#encoding
#utf8_file = codecs.open('encoding.txt', 'r', 'utf-8', 'strict', 1);
#
#for line in utf8_file.readlines():
#    nameList.append(line);
#
#utf8_file.close();

f = open("encoding.txt", 'r');
lines = f.readlines();

for line in lines:
    print line;
    nameList.append(line);
    
f.close();

#for name in nameList:
#    doc = {'name' : name};
#    db.user.insert(doc);
#
#for user in db.user.find():
#    print user['name'];
    
    
