
try: raw_input
except: raw_input = input

total = sum(map(int, raw_input().split()))
print('total sum is : {}' .format(total))
