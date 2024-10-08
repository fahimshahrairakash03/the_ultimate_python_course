s = {8, 7, 12, "Harry", [1,2]}
 #list can not be included in set

 #Can you change the values inside a list which is contained in set S? s = {8, 7, 12, "Harry", [1,2]}

 #--->
#No, you cannot change the values inside a list that is contained in a set directly, because lists cannot be added to a set in the first place. This is due to the fact that lists are mutable (their contents can be changed), and Python sets only allow immutable elements (elements that cannot be changed, like integers, strings, and tuples).