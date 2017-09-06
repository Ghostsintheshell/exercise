# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:56:03 2017

@author: Yew
"""

import openpyxl as xl

#创建一个EXCEL对象，打开文件
wb = xl.load_workbook('ETF_analysis.xlsx')
print('表单名称：',wb.sheetnames)