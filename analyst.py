"""
I've been presented with a List of items(a list of stocks profit) which is
[5,7,9,13,11,6,6,3,3]

The code below is to assign each value in the list to two variables (i,j)

where i will equal the values on the list
    for each value of i, j will equal the next value,to the end of the list
    for each unique pair values of i and j.
    the program is to sum them up and check if the sum equal a target(12)

    if the sum equals the target (12), the program is to print the pair
    
    after the program has run thru all the values in the list
    it shold print out all the pairs and how many distinct pair.
 
"""

"""
Pseudocode
1 > i'll state the list 
2 > i'll state the target
3 > i'll loop over the list for the list (for the length times of the list) assigning each value 
    to a variable i
    for every value of i, i'll loop over the list(for the length times if the list starting from
    the next value after that value of i) assigning the next value to avariable j
4 > for each loop set, i'll sum the values of i and j and check if they equal the target(12)
    if they do, i'll save the pair in another list,
5 > i'll check for any re-occuring pair in the new list
    if any pop one
6 > i'll print the final list of pair without any repeating pair
7 > i'll print the number of items on the list(which represents the number of unique pairs that
    equals the target)
"""

# definition function
#this function accepts two values, the list and the target
def sum_of_profit(stocks , target):
    #declaration of new list
    list_of_pairs = []
    # The first loop that will asssign values to i beginning from 0 to the end of the list length
    for i in range(0, len(stocks)):
    # The second loop that assigns vallues to j begining from the value after i to the list length
        for j in range (i + 1, len(stocks)):
            # checking if sum equals the target and if yes store the pair in a list
            if stocks[i] + stocks[j] == target:
                target_pairs = (stocks[i],stocks[j])
                list_of_pairs.append(target_pairs)
    list_sets = list(set(list_of_pairs))
    print(list_sets)
    print("The number of unique pairs that equals the Target is", len(list_sets))




stocks = [5,7,9,13,11,6,6,3,3]
target = 12
sum_of_profit(stocks, target)
#print(sum_of_profit(stocks, target))