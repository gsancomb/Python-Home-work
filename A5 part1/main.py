import re
# Griffin Sancomb
# cm25251


q1 = "ABCD+++1234+EFGH++****"
result = re.sub('[\W][^/*][+]*', '-',  q1)
#result = re.sub('[^a-zA-Z1-9*][+]*', '-', q1)
print(result) # prints ABCD-1234-EFGH-****

