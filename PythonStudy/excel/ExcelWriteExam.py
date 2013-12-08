'''
Created on 2013. 12. 8.

@author: devsik
'''
import xlwt
import datetime

font = xlwt.Font();
font.name = 'Times New Roman';
font.colour_index = 2;
font.bold = True;

style = xlwt.XFStyle();
style.font = font;

style1 = xlwt.XFStyle()
style1.num_format_str = 'D-MMM-YY';

wb = xlwt.Workbook();
ws = wb.add_sheet('A Test Sheet');

ws.write(0, 0, 'Test', style);
ws.write(1, 0, datetime.datetime.now(), style1);
ws.write(2, 0, 1);
ws.write(2, 1, 1);
ws.write(2, 2, xlwt.Formula("A3+B3"));

wb.save("example.xls");