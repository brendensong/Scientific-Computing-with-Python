#!/usr/bin/env python
# coding: utf-8

# ### Assignment
# 
# Write a function named `add_time` that takes in two required parameters and one optional parameter:
# * a start time in the 12-hour clock format (ending in AM or PM) 
# * a duration time that indicates the number of hours and minutes
# * (optional) a starting day of the week, case insensitive
# 
# The function should add the duration time to the start time and return the result.
# 
# If the result will be the next day, it should show `(next day)` after the time. If the result will be more than one day later, it should show `(n days later)` after the time, where "n" is the number of days later.
# 
# If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.
# 
# Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.
# ```py
# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM
# 
# add_time("11:30 AM", "2:32", "Monday")
# # Returns: 2:02 PM, Monday
# 
# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM
# 
# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)
# 
# add_time("11:43 PM", "24:20", "tueSday")
# # Returns: 12:03 AM, Thursday (2 days later)
# 
# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)
# ```
# 
# Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
# 
# ### Development
# 
# Write your code in `time_calculator.py`. For development, you can use `main.py` to test your `time_calculator()` function. Click the "run" button and `main.py` will run.
# 
# ### Testing 
# 
# The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.
# 
# ### Submitting
# 
# Copy your project's URL and submit it to freeCodeCamp.
# 
# - My submission : https://replit.com/@SeongjooBrenden/boilerplate-time-calculator#time_calculator.py

# In[ ]:


# time_calculator.py

def add_time(start, duration, day=None):

    tList1 = start.split(':')
    tList2 = tList1[1].split()

    duList = duration.split(':')
    defDay = None
    rDate = 0

    if day != None:
        defDay = (day.lower()).capitalize()

    sHour = int(tList1[0])
    sMin = int(tList2[0])
    sFormat = tList2[1]

    dHour = int(duList[0])
    dMin = int(duList[1])

    rMin = sMin + dMin

    if rMin >= 60:
        rMin = format((rMin - 60), "02")
        rHour = sHour + dHour + 1
    else:
        rMin = format(rMin, '02')
        rHour = sHour + dHour

    if sFormat == 'AM':
        if rHour < 12:
            rDate = 0
            rFormat = sFormat
        elif rHour >= 12 and rHour < 24:
            rHour = rHour - 12
            if rHour == 0:
                rHour = 12
            rFormat = 'PM'
            rDate = 0
        elif rHour >= 24:
            rHour = rHour - 24 * int(rHour / 24)
            if rHour >= 12:
                if rHour == 12:
                    rDate = 0
                    rFormat = 'PM'
                else:
                    rHour = rHour - 12
                    rFormat = 'PM'
                    rDate = int(dHour / 24)
            else:
                rFormat = sFormat
                rDate = int(dHour / 24)
    elif sFormat == 'PM':
        if rHour < 12:
            rDate = 0
            rFormat = sFormat
        elif rHour >= 12 and rHour < 24:
            if rHour == 0:
                rHour == 12
            rHour = rHour - 12
            rFormat = 'AM'
            rDate = 1
        elif rHour >= 24:
            rHour = rHour - 24 * int(rHour / 24)
            if rHour >= 12:
                if rHour == 12:
                    rDate = int(dHour / 24) + 1
                else:
                    rHour = rHour - 12
                rFormat = 'AM'
                rDate = int(dHour / 24) + 1
            else:
                rFormat = sFormat
                rDate = int(dHour / 24) + 1

    days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday'
    ]

    defDayIndex = 0
    i = 0
    for item in days:
        if item == defDay:
            defDayIndex = i
        i = i + 1

    nDayIndex = defDayIndex + rDate

    if nDayIndex < 7:
        nDay = days[nDayIndex]
    else:
        nDayIndex = nDayIndex - int(nDayIndex / 7) * 7
        nDay = days[nDayIndex]

    if day == None:
        if rDate > 1:
            new_time = str(rHour) + ':' + str(
                rMin) + ' ' + rFormat + ' (' + str(rDate) + ' days later)'
        elif rDate == 1:
            new_time = str(rHour) + ':' + str(
                rMin) + ' ' + rFormat + ' (next day)'
        elif rDate == 0:
            new_time = str(rHour) + ':' + str(rMin) + ' ' + rFormat
    elif day != None:
        if rDate > 1:
            new_time = str(rHour) + ':' + str(
                rMin) + ' ' + rFormat + ', ' + nDay + ' (' + str(
                    rDate) + ' days later)'
        elif rDate == 1:
            new_time = str(rHour) + ':' + str(
                rMin) + ' ' + rFormat + ', ' + nDay + ' (next day)'
        elif rDate == 0:
            new_time = str(rHour) + ':' + str(
                rMin) + ' ' + rFormat + ', ' + nDay

    return new_time


# In[ ]:


# test_module.py

import unittest
from time_calculator import add_time


class UnitTests(unittest.TestCase):

    def test_same_period(self):
        actual = add_time("3:30 PM", "2:12")
        expected = "5:42 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12" to return "5:42 PM"')

    def test_different_period(self):
        actual = add_time("11:55 AM", "3:12")
        expected = "3:07 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:55 AM", "3:12" to return "3:07 PM"')

    def test_next_day(self):
        actual = add_time("9:15 PM", "5:30")
        expected = "2:45 AM (next day)"
        self.assertEqual(actual, expected, 'Expected time to end with "(next day)" when it is the next day.')

    def test_period_change_at_twelve(self):
        actual = add_time("11:40 AM", "0:25")
        expected = "12:05 PM"
        self.assertEqual(actual, expected, 'Expected period to change from AM to PM at 12:00')

    def test_twenty_four(self):
        actual = add_time("2:59 AM", "24:00")
        expected = "2:59 AM (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00" to return "2:59 AM"')

    def test_two_days_later(self):
        actual = add_time("11:59 PM", "24:05")
        expected = "12:04 AM (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05" to return "12:04 AM (2 days later)"')

    def test_high_duration(self):
        actual = add_time("8:16 PM", "466:02")
        expected = "6:18 AM (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02" to return "6:18 AM (20 days later)"')

    def test_no_change(self):
        actual = add_time("5:01 AM", "0:00")
        expected = "5:01 AM"
        self.assertEqual(actual, expected, 'Expected adding 0:00 to return initial time.')

    def test_same_period_with_day(self):
        actual = add_time("3:30 PM", "2:12", "Monday")
        expected = "5:42 PM, Monday"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12", "Monday" to return "5:42 PM, Monday"')

    def test_twenty_four_with_day(self):
        actual = add_time("2:59 AM", "24:00", "saturDay")
        expected = "2:59 AM, Sunday (next day)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "2:59 AM", "24:00", "saturDay" to return "2:59 AM, Sunday (next day)"')

    def test_two_days_later_with_day(self):
        actual = add_time("11:59 PM", "24:05", "Wednesday")
        expected = "12:04 AM, Friday (2 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05", "Wednesday" to return "12:04 AM, Friday (2 days later)"')

    def test_high_duration_with_day(self):
        actual = add_time("8:16 PM", "466:02", "tuesday")
        expected = "6:18 AM, Monday (20 days later)"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "8:16 PM", "466:02", "tuesday" to return "6:18 AM, Monday (20 days later)"')

if __name__ == "__main__":
    unittest.main()


# In[ ]:


# main.py

# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))


# Run unit tests automatically
main(module='test_module', exit=False)


# In[ ]:


# result

> python main.py
1:08 AM (next day)
............
----------------------------------------------------------------------
Ran 12 tests in 0.019s

OK
>

