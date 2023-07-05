# functions to print only even no.s inside a given list
given_list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def evenno(list):
    return [num for num in list if num%2 == 0]
    
