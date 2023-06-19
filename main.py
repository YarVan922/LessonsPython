# def strCounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
#
#
# strCounter('abcddgdfghdfgdfg')

# homework
s = input()
log = True
for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        log = False
        break

print(log)
