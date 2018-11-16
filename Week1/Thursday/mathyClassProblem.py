
def determinant(list1, list2, list3):
     

    for indexList1 in list1 :
        
        list3SummedValue = 0
        print("list 1 index: {}".format(indexList1))
        for indexList2 in list2: 
            list3SummedValue += indexList1 * indexList2
            print("accumulatedValue {}".format(list3SummedValue))
        
        list3.append(list3SummedValue)

    print(list3)

v1R = ""

v1 = []
print('vector1 values: to end type done')
while (v1R != 'done'):
    if(v1R != 'done'):
        v1.append(int(input(">>")))

print(v1)



# l1 = [1,5,3,6,7]

# l2 = [3,6,9,10,2]

# l3 = []
#determinant(l1, l2, l3)