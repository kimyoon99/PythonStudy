
'''
Created on 2013. 11. 25.

@author: devsik
'''
from Service import Service

aaa = Service();
aaa.setname("김윤식");
aaa.sum("가", "나");

bbb = Service();
bbb.setname("임성연");
bbb.sum("다", "나");

print(type(bbb));
