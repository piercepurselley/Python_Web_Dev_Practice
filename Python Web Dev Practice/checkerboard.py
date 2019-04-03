new_thang = ''

# for x in new_thang:
#     if x % 2 == 0:

for x in range(0,8):
    if x % 2 == 0:
        new_thang += '*' + ' ' + '*' + ' ' + '*' + ' ' + '*' + '\n'
    if x % 2 !=0:
        new_thang += ' ' + '*' + ' ' + '*' + ' ' + '*' + ' ' + '*' + '\n'
print new_thang



