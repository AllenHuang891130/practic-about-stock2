#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import locale
a = []
b = []
c = []
with open('T86_ALLBUT0999_20211208.csv', encoding='big5' , errors = 'ignore') as a1:
    rows = csv.reader(a1, delimiter=',')
    a += rows
    for j in range(3,121):
        errors = 'ignore'
        if a[j][4].replace(',','') =='----' or locale.atof(a[j][10].replace(',','')) =='----' :
            print('wrong')
        elif  float(a[j][14].replace(',',"")) >= 50000:
            print('第一日',a[j][0],a[j][1],a[j][14])
with open('T86_ALLBUT0999_20211209.csv', encoding='big5' , errors = 'ignore') as a2:
    rows1 = csv.reader(a2, delimiter=',')
    b += rows1
    for j in range(3,121):
        errors = 'ignore'
        if b[j][4].replace(',','') =='----' or locale.atof(b[j][10].replace(',','')) =='----' :
            print('wrong')
        elif  locale.atof(b[j][10].replace(',',"")) >= 50000:
            print('第二日',b[j][0],b[j][1],b[j][10])
with open('T86_ALLBUT0999_20211210.csv', encoding='big5' , errors = 'ignore') as a3:
    rows2 = csv.reader(a3, delimiter=',')
    c += rows2
    for j in range(3,121):
        errors = 'ignore'
        if c[j][4].replace(',','') =='----' or locale.atof(c[j][10].replace(',','')) =='----' :
            print('wrong')
        elif  locale.atof(c[j][10].replace(',',"")) >= 50000:
            print('第三日',c[j][0],c[j][1],c[j][10])


# In[ ]:





# In[ ]:





# In[ ]:




