import math
print(math.sqrt(25))
print(math.pow(2,3))
print(math.factorial(5))
print(math.ceil(4.2))
print(math.floor(4.9))


# random module
import random
print(random.randint(1,10))
print(random.random())
print(random.choice(["a","b","c"]))
mylist=[1,2,3,4,5,6,7,8,9]
print(random.shuffle(mylist))
print(mylist)
print(random.uniform(10,20))

# datetime module

import datetime
print(datetime.datetime.now())
print(datetime.date(25,1,1))
print(datetime.time(10,30,15))
print(datetime.timedelta(days=5))
dte=datetime.date.today()
print(dte.strftime("%d/%m/%y"))

# statistics Module
import statistics
print(statistics.mean([10,20,30]))
print(statistics.median([1,3,5]))
print(statistics.mode([1,2,2,2,2,3,5]))
print(statistics.stdev([1,3,5]))
print(statistics.variance([1,3,5]))

