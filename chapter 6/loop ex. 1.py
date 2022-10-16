#
# max_num = None
# min_num = None
# while True:
#     number = input('enter a number greater than 1:\n')
#     if number == 'done':
#         break
#     try:
#         if  max_num is None or int(number) > max_num:
#             max_num = int(number)
#
#         if  min_num is None or int(number) < min_num:
#             min_num = int(number)
#     except:
#         print('Invalid input')
#
#
# print(f'Maximum is {max_num}\nMinimum is {min_num}')
#

user = input('enter file name\n')
if user == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd")
    exit()

try:

    file_entered = open(user, encoding='utf-8')
except:
    print('file cannot be opened: ', user)
    exit()

counter = 0


for sentence in file_entered:
    if sentence.startswith('Subject:'):

        counter +=1
#
print('There were %d subject lines in ' % counter, user)


