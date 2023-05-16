# import re
#
# phone = "2004-959-559 # This is Phone Number"
# Result = re.sub('[^0-9]*', '', phone)
# print(Result)
#
#
#
#
#
#
# str_list = ['UMBC', 'UMD', 'UMB', 'TU']
# answer = filter(lambda name: name if (len(name) >= 4) else "", str_list)
# print(type(answer))
# print(list(answer))
# # Output:
# # <class 'filter'>
# # ['UMBC']
#
# string = 'FindMeeeIffYouCan'
#
# # The pattern is one upper case letter followed by three lower case letters
# # pattern = [A-Z][a-z]{3}
#
# # Use a re method to find all instances of pattern as printed below; it should return a list of matches
# match = re.findall('[A-Z][a-z]{3}', string)
#
# print(type(match))
# print(match)
#
# # # output is:
# #
# # <class 'list'>
# # [('F', 'ind'), ('M', 'eee')]
#
#
#
# import re
#
# date = "05$$$18   2021"
#
# result = re.sub('[\W]*[^0-9]', '/', date)
# print(result) # prints 05/18/2021
# #
# #
# #
from functools import reduce

raw_scores = [{'student_name': 'John', 'raw_score': 8}, {'student_name': 'Mary', 'raw_score': 9}]
# print(list(filter(lambda x: x['raw_score', raw_scores)))
final_grades = list(reduce(lambda j, k: j['raw_score'] * 10, raw_scores))

list(final_grades)
# print(list(final_grades))
# # Output:
#
# [80, 90]

# import numpy as np
#
# x = np.reshape([[1, 2, 3], [4, 5, 6], [7, 8, 9]],(3,3)) # create a 2D array 3x3
# print(x)
# # x = array([[1, 2, 3],
# #        [4, 5, 6],
# #        [7, 8, 9]])
#
# answer = x[...]
#
#
#
# # answer
# #
# # array([[9, 8, 7],
# #        [6, 5, 4],
# #        [3, 2, 1]])
