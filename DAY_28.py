'''
from datetime import datetime
c = datetime.now()
print(c.strftime('%y'))
print(c.strftime('%m'))
print(c.strftime('%d'))
print(c.strftime('%H:%M:%S'))

from datetime import datetime
current = datetime.now().today()
now = datetime.now()
print(current.strftime('%d/%m/%y %I:%H:%M:%S %p'))

from datetime import datetime
current = datetime.now().today()
now = datetime.now()
print(current.strftime('%d/%m/%y %I:%M:%S %p'))

%d --> day in month
%m --> month in year
%y --> year
%H --> hours
%M --> minute 
%S --> Second
%I --> 12 hour clock
%p --> AM or PM

import calendar
print(calendar.calendar(2005))
print(calendar.month(2005, 6))
print(calendar.weekday(2005, 6, 12))
print(calendar.isleap(2005))

=> Data Analysis
- Data Analysis is the process of inspecting, cleaning, transform and modeling data to discover useful insights, supports decision-making,
  and identify patterns. It is widely used in industries such as finanace, healthcare, marketing, and technology.

- Types of Data Analysis :-
1.Descrptive analysis - summarizing data
EXAMPLE :- Average sales per month
2.Diagnostic Analysis - Understanding causes
EXAMPLE :- why sales dropped
3. Predictive Analysis - Forecasting future outcomes
EXAMPLE :- predicting customer churn
4.Prescriptive Analysis - Suggensting actions based on data
EXAMPLE :- best marketing strategies

=> Numpy:-
- It is a python library which is known as numerical python
- This numpy has different dimensional arrays such as 1D, 2D, 3D
- To use the numpy import library as "import numpy as np"

EXAMPLE :-
import numpy as np
a = np.array([[1,2,3],[4,5,6,],[7,8,9]])
print(a)

- 1D array
EXAMPLE :-
import numpy as np
a = np.array([1,2,3,4])
print(a)

- Indexing Array
-> Aa we used indexing in the list or tuple, here the way it works, by calling index positon from array, we will get the value

-> Negative indexing
EXAMPLE:-
import numpy as np
a = np.array([1,2,3,4])
print(a[-1])

-> Normal indexing
EXAMPLE:-
import numpy as np
a = np.array([1,2,3,4])
print(a[1])

-> Slicing
EXAMPLE:-
import numpy as np
a = np.array([1,2,3,4])
print(a[:2])

-> Reshape:-
EXAMPLE:-
import numpy as np
a = np.array([[1,2],[4,5],[7,8]])
print(a)
print(a.reshape(2,3))

=> Pandas:-
- Pandas are powerful library, this is buit on the top of numpy
- By used data manipulation will be done
- Pandas have structured data sunch as series and data frame
- To use this we have to import library "import pandas as pd"
EXAMPLE:-
import pandas as pd
d = pd.Series(data = [1000,2000,3000],index = ['earphone','charger','phone'])
print(d)
'''
import pandas as pd
df = {'products' : ['RAM','CPU','pendrive','laptop'],
                  'price' : [2000,3000,1500,100000],
                  'stock' : [10,30,20,9]}
d = pd.DataFrame(df)
print(d)
































