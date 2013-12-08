'''
Created on 2013. 12. 8.

@author: devsik
'''
import io
f = io.StringIO();
f.write("life is too short");
value = f.getvalue();
print(value);
f.close();