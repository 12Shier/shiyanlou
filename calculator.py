#!/usr/bin/env python3
import sys
try :
    salary = int(sys.argv[1])
    if salary <= 3500 :
        print(format(0,".2f"))
    elif (salary-3500) < 1500:
        print(format((salary - 3500) * 0.03, ".2f"))
    elif ((salary-3500) >= 1500 and (salary-3500) < 4500):
        print(format((salary - 3500) * 0.1 - 105, ".2f"))
    elif ((salary-3500) >= 4500 and (salary-3500) < 9000):
        print(format((salary - 3500) * 0.2 - 555, ".2f"))
    elif ((salary-3500) >= 9000 and (salary-3500) < 35000):
        print(format((salary - 3500) * 0.25 - 1005, ".2f"))
    elif ((salary-3500) >= 35000 and (salary-3500) < 55000):
        print(format((salary - 3500) * 0.3 - 2755, ".2f"))
    elif ((salary-3500) >= 55000 and (salary-3500) < 80000):
        print(format((salary - 3500) * 0.35 - 5505, ".2f"))
    elif (salary-3500) >= 80000:
        print(format((salary - 3500) * 0.45 - 13505, ".2f"))
except: 
    print("Parameter Error")
