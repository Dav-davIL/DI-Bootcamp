#Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = {1,2,3,4,5}

#Add two new numbers to the set
my_fav_numbers.add(6)
my_fav_numbers.add(7)

#Remove the last number.
my_fav_numbers.discard(7)

#friend’s favorites numbers.
friend_fav_numbers  = {6,7,8,9}

our_fav_numbers = set.union(my_fav_numbers, friend_fav_numbers)