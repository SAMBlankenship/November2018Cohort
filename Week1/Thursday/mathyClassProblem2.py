def determinant(list1, list2, list3):
 

    for indexList1 in list1 :
        
        list3SummedValue = 0
        print("list 1 index: {}".format(indexList1))
        for indexList2 in list2: 
            list3SummedValue += indexList1 * indexList2
            print("accumulatedValue {}".format(list3SummedValue))
        
        list3.append(list3SummedValue)

    print(list3)

l1 = [1,5,3,6,7]

l2 = [3,6,9,10,2]

l3 = []

l4 = []
l5 = []

stop = 'no'
l4Values = 'no'
l5Values = 'no'
while stop != 'yes':
    print("enter in integer for  first vector value, type done when finished ")
    while l4Values != 'yes':
        # l4.append(int(input("enter in integer for vector value ")))
        # l4Values = input('done with l4: yes or no')
        answer = input(">>")
        if answer == 'done':
            l4Values = 'yes'
        else:
            l4.append(int(answer))
    print("enter in integer for  second vector value, type done when finished ")
    while l5Values != 'yes':
        # l5.append(int(input("enter in integer for vector value ")))
        # l5Values = input('done with l5: yes or no')

        answer = input(">>")
        if answer == 'done':
            l5Values = 'yes'
        else:
            l5.append(int(answer))
        stop = 'yes'
    


print(l4)
print(l5)
determinant(l4, l5, l3)