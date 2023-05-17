given_list = [5,9,6,4,8,2,3,5] #Given list of numbers

'''Calculating Mean'''
mean = sum(given_list)/len(given_list)

'''Calculating Median'''
lst = sorted(given_list)
for i in range(0, int((len(lst)-1.0)/2.0)):
    lst.pop(0)
    lst.pop(int(len(lst)-1))

if (len(lst) == 1.0):
    median = lst[0]
elif (len(lst) == 2.0):
    median = (lst[0]+lst[1])/2.0

'''Calculating Mode'''
count = []
for i in given_list:
    count.append(given_list.count(i))
mx = max(count); ix = count.index(mx)
mode = given_list[ix]

'''Output'''
print(f"The mean of the given list of numbers is = {mean}")
print(f"The median number of the given list of numbers is = {median}")
print(f"The mode number of the given list of numbers is = {mode}")