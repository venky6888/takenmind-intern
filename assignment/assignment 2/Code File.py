import pandas as pd
exf=pd.ExcelFile("Input File.xlsx")
sheet1=exf.parse('Sheet1')
sheet2=exf.parse('Sheet2')
sheet3=exf.parse('Sheet3')
sheet4=exf.parse('Sheet4')
sheet5=exf.parse('Sheet5')
sheet6=exf.parse('Sheet6')
sheet7=exf.parse('Sheet7')
sheet8=exf.parse('Sheet8')
sheet9=exf.parse('Sheet9')
sheet10=exf.parse('Sheet10')

print(sheet1)

sheet1.to_csv('Sheet1_convert.csv')
sheet2.to_csv('Sheet2_convert.csv')
sheet3.to_csv('Sheet3_convert.csv')
sheet4.to_csv('Sheet4_convert.csv')
sheet5.to_csv('Sheet5_convert.csv')
sheet6.to_csv('Sheet6_convert.csv')
sheet7.to_csv('Sheet7_convert.csv')
sheet8.to_csv('Sheet8_convert.csv')
sheet9.to_csv('Sheet9_convert.csv')
sheet10.to_csv('Sheet10_convert.csv')