import datetime  
from datetime import date 
import calendar 
  
def findDay(date): 
    day, month, year = (int(i) for i in date.split(' '))     
    born = datetime.date(year, month, day) 
    return born.strftime("%A") 
date=str(input('Enter the date(format:dd mm yyyy):'))
print(findDay(date)) 