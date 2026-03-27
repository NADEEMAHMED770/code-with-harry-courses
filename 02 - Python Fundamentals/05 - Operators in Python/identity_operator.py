session_a = [23,67,34,66,22,33,9,99]
# session_b = session_c
session_c = [23,67,34,66,22,33,9]
session_b = session_c
print(session_a is session_b)
print(session_a is not session_c)