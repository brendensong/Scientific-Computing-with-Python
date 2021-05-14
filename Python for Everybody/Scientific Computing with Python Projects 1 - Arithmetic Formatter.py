#!/usr/bin/env python
# coding: utf-8

# # Project 1. Arithmetic FormatterPassed
# 
# Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side.

# ### Assignment
# 
# Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
# ```
#   235
# +  52
# -----
# ```
# 
# Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to `True`, the answers should be displayed.
# 
# ### For example
# 
# Function Call:
# ```py
# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
# ```
# 
# Output:
# ```
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----
# ```
# 
# Function Call:
# ```py
# arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
# ```
# 
# Output:
# ```
#   32         1      9999      523
# +  8    - 3801    + 9999    -  49
# ----    ------    ------    -----
#   40     -3800     19998      474
# ```
# 
# ### Rules
# 
# The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will **return** a **string** that describes an error that is meaningful to the user.  
# 
# 
# * Situations that will return an error:
#   * If there are **too many problems** supplied to the function. The limit is **five**, anything more will return:
#     `Error: Too many problems.`
#   * The appropriate operators the function will accept are **addition** and **subtraction**. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be:
#     `Error: Operator must be '+' or '-'.`
#   * Each number (operand) should only contain digits. Otherwise, the function will return:
#     `Error: Numbers must only contain digits.`
#   * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
#     `Error: Numbers cannot be more than four digits.`
# *  If the user supplied the correct format of problems, the conversion you return will follow these rules:
#     * There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
#     * Numbers should be right-aligned.
#     * There should be four spaces between each problem.
#     * There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
# 
# ### Development
# 
# Write your code in `arithmetic_arranger.py`. For development, you can use `main.py` to test your `arithmetic_arranger()` function. Click the "run" button and `main.py` will run.
# 
# ### Testing 
# 
# The unit tests for this project are in `test_module.py`. We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.
# 
# ### Submitting
# 
# Copy your project's URL and submit it to freeCodeCamp.
# 
# - My submission: https://replit.com/@SeongjooBrenden/boilerplate-arithmetic-formatter-1#arithmetic_arranger.py

# In[38]:


# arithmetic_arranger.py

def arithmetic_arranger(problems, secondArgument=False):

    # check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    newList = []
    answerList = []
    fLine = []
    sLine = []
    dashLine = []
    ansLine = []

    for item in problems:

        newList = item.split()
        sign = newList[1]
        num1 = newList[0]
        num2 = newList[2]

        # check if the operator is not '+' or '-'
        if sign != '+' and sign != '-':
            return "Error: Operator must be '+' or '-'."

        # check if numbers contain non-digits
        elif num1.isnumeric() == False or num2.isnumeric() == False:
            return "Error: Numbers must only contain digits."

        # check if numbers are more than 4 digits
        elif len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        else:
            if sign == '+':
                answer = int(num1) + int(num2)
            else:
                answer = int(num1) - int(num2)

            answerList.append([num1, sign, num2, str(answer)])

    for answer in answerList:
        numLen1 = len(answer[0])
        numLen2 = len(answer[2])

        maxLength = max(numLen1, numLen2) + 2

        line1 = str(answer[0].rjust(maxLength))
        line2 = str(answer[1] + answer[2].rjust(maxLength - 1))
        fLine.append(line1)
        sLine.append(line2)

        dash = maxLength * '-'
        line3 = str(dash.rjust(maxLength))
        dashLine.append(line3)

        line4 = str(answer[3].rjust(maxLength))
        ansLine.append(line4)

    finalLine1 = '    '.join(map(str, fLine))
    finalLine2 = '    '.join(map(str, sLine))
    finalLine3 = '    '.join(map(str, dashLine))
    finalLine4 = '    '.join(map(str, ansLine))

    if secondArgument == True:
        arranged_problems = finalLine1 + '\n' + finalLine2 + '\n' + finalLine3 + '\n' + finalLine4
    else:
        arranged_problems = finalLine1 + '\n' + finalLine2 + '\n' + finalLine3

    return arranged_problems


# In[ ]:


# test_module.py

import unittest
from arithmetic_arranger import arithmetic_arranger


# the test case
class UnitTests(unittest.TestCase):
    def test_arrangement(self):
        actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]')

        actual = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
        expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]')

    def test_too_many_problems(self):
        actual = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
        expected = "Error: Too many problems."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."')

    def test_incorrect_operator(self):
        actual = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Operator must be '+' or '-'."
        self.assertEqual(actual, expected, '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."''')
        
    def test_too_many_digits(self):
        actual = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers cannot be more than four digits."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that has a number over 4 digits long to return "Error: Numbers cannot be more than four digits."')

    def test_only_digits(self):
        actual = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
        expected = "Error: Numbers must only contain digits."
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."')

    def test_solutions(self):
        actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True)
        expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172"
        self.assertEqual(actual, expected, 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with arithmetic problems and a second argument of `True`.')


if __name__ == "__main__":
    unittest.main()


# In[ ]:


# main.py

# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger
from unittest import main


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main(module='test_module', exit=False)


# In[ ]:


# Result

> python main.py
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
......
----------------------------------------------------------------------
Ran 6 tests in 0.052s

OK
>

