import xlwt
from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(1, 0, 'ISBT DEHRADUN')
wb.save('xlwt example.csv')