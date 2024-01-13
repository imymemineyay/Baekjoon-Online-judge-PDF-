a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

lst = [a,b,c,d,e]
sorted_lst = []

while len(lst) > 0 : 
    the_smallest = min(lst)
    lst.remove(the_smallest)
    sorted_lst.append(the_smallest)

avg = sum(sorted_lst) // len(sorted_lst)
print(avg)

median_num = sorted_lst[2]
print(median_num)
