"""
birthday.py
Author: JackMeehan
Credit: lowercase letter help: https://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input('Hello, what is your name? ')
month = input('Hi ' + name + ', what was the name of the month you were born in? ')
year = int(input('And what year were you born in, ' + name + '? '))
day = input('And the day? ')

if str.lower(month)==str.lower(month_name[todaymonth]) and day==str(todaydate):
    print('Happy birthday!')
elif month in ['october', 'October'] and day=='31':
    print('You were born on Halloween!')
elif month in ['December', 'december', 'january', 'January', 'February', 'february'] and year in range(1000,1980):
    print(''+ name + ', you are a winter baby of the stone age.')
elif month in ['December', 'december', 'january', 'January', 'February', 'february'] and year in [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]:
    print(''+ name + ', you are a winter baby of the eighties.')
elif month in ['December', 'december', 'january', 'January', 'February', 'february'] and year in [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]:
    print(''+ name + ', you are a winter baby of the nineties.')
elif month in ['December', 'december', 'january', 'January', 'February', 'february'] and year in range(2000,2018):
    print(''+ name + ', you are a winter baby of the two thousands.')
elif month in ['March', 'march', 'april', 'April', 'may', 'May'] and year in range(1000,1980):
    print(''+ name + ', you are a spring baby of the stone age.')
elif month in ['March', 'march', 'april', 'April', 'may', 'May'] and year in [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]:
    print(''+ name + ', you are a spring baby of the eighties.')
elif month in ['March', 'march', 'april', 'April', 'may', 'May'] and year in [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]:
    print(''+ name + ', you are a spring baby of the nineties.')
elif month in ['March', 'march', 'april', 'April', 'may', 'May'] and year in range(2000,2018):
    print(''+ name + ', you are a spring baby of the two thousands.')
elif month in ['june', 'June', 'July', 'july', 'august', 'August'] and year in range(1000,1980):
    print(''+ name + ', you are a summer baby of the stone age.')
elif month in ['june', 'June', 'July', 'july', 'august', 'August'] and year in [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]:
    print(''+ name + ', you are a summer baby of the eighties.')
elif month in ['june', 'June', 'July', 'july', 'august', 'August'] and year in [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]:
    print(''+ name + ', you are a summer baby of the nineties.')
elif month in ['june', 'June', 'July', 'july', 'august', 'August'] and year in range(2000,2018):
    print(''+ name + ', you are a summer baby of the two thousands.')
elif month in ['September', 'september', 'october', 'October', 'november', 'November', 'December', 'december'] and year in range(1000,1980):
    print(''+ name + ', you are a fall baby of the stone age.')
elif month in ['September', 'september', 'october', 'October', 'november', 'November', 'December', 'december'] and year in [1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989]:
    print(''+ name + ', you are a fall baby of the eighties.')
elif month in ['September', 'september', 'october', 'October', 'november', 'November', 'December', 'december'] and year in [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999]:
    print(''+ name + ', you are a fall baby of the nineties.')
elif month in ['September', 'september', 'october', 'October', 'november', 'November', 'December', 'december'] and year in range(2000,2018):
    print(' '+ name + ', you are a fall baby of the two thousands.')





