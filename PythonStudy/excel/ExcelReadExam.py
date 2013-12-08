'''
Created on 2013. 12. 8.

@author: devsik
'''
import xlrd
import datetime;

workbook = xlrd.open_workbook("example.xls");
sh = workbook.sheet_by_name('A Test Sheet');
print sh.cell(0, 0).value;
print xlrd.xldate_as_tuple(sh.cell(1, 0).value, 0)[0];
print sh.cell(2, 0).value;
print sh.cell(2, 1).value;
print sh.cell(2, 2).value;
print datetime.datetime.now();