#/////////////////pPRACTICE01//////////////////////

numbers=[1,2,3,4,5,6,7,8,9,10]
squre=[x**2 for x in numbers]
print(squre)

my_tuple=[1,2,3,4,5,6,7,8,9,10]
my_tuple[3]=50
print(my_tuple)


my_tuple=[1,2,3,4,5,6,7,8,9,10]
my_tuple[3]=50
my_tuple[5]=25
print(my_tuple)


numbers=[1,2,3,4,5,6,7,8,9,10]
numbers.remove(10)
print(numbers)



#****************PRACTICE02*****************************


naturalnumbers={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
print(naturalnumbers)
my_tuple={1,2,3,4,5,6,7,8,9,10,}
a,b,c,d,e,f,g,h,i,j=my_tuple
print(a,b,c,d,e,f,g,h,i,j,)
print(a,b,c,d,e)


#--------------PRACTICE03-----------------------------

oddnumbers = [x for x in range(1, 20, 2)]
squaredoddnumbers = [x**2 for x in oddnumbers]

print("Odd Numbers", oddnumbers)
print("Squares of Odd Numbers", squaredoddnumbers)



#++++++++++++++++++PRACTICE04++++++++++++++++++++++++



continents = ("nisha", "tannu", "vimal", "khushi", "gaurav")
print(continents[4]) 
try:
    continents[2] = "preeti"  
except TypeError as e:
    print(f"Error: {e}")  
    print( continents[2])

#===================PRACTICE05===========================

my_tuple=("tanuja",54,7.43)

string_variable, int_variable, float_variable = my_tuple

print("String:", string_variable)
print("Integer:", int_variable)
print("Float:", float_variable)


#@@@@@@@@@@@@@@@@@@PRACTICE06@@@@@@@@@@@@@@@@@@@@@@@@@@@@


my_tuple={2,4,6}
x,y,z=my_tuple
print(y)
new_tuple={8,10,12}
k,l,m=new_tuple
print(k)
print(y,k)

#####################pPRACTICE07######################

oddnumbers = {1, 3, 5, 7, 9}
print(oddnumbers)

evennumbers = {2, 4, 6, 8, 10}
print(evennumbers)
union_set = oddnumbers.union(evennumbers)
intersection_set = oddnumbers.intersection(evennumbers)


print("Union of oddnumbers and evennumbers:", union_set)
print("Intersection of oddnumbers and evennumbers:", intersection_set)


#$$$$$$$$$$$$$$$$$$$PRACTICE08$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

primenumbers={1,2,3,7,13}
print(primenumbers)
primenumbers.add(11)
print(primenumbers)
primenumbers.remove(2)
print(primenumbers)
primenumbers= 7 in primenumbers
print("7 is present in pimenumbers ")
print("Final set of prime numbers:", primenumbers)


#^^^^^^^^^^^^^^^^^^^^^^PRACTICE09^^^^^^^^^^^^^^^^^^^^^^^^^^^^

vowels={"a","e","i","O","u"}
print(vowels)
charvowels = "e" in vowels
print("e in vowels ", charvowels)
charvowels= "w" in vowels
print("w in vowels ", charvowels)


#&&&&&&&&&&&&&&&&&&&&PRACTICE10&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


studentdetail={"name":"tanuja",
               "age":"20",
               "grade":"76"
               }
studentdetail["age"] = 21  


studentdetail['favourate subject']="chemistry"
print(studentdetail)



#********************PRACTICE11***************

city_populations = {
    'New York': 8623000,
    'Los Angeles': 3990456,
    'Chicago': 2705994,
    'Houston': 2320268,
    'Phoenix': 1680992
}


population_population = city_populations.get('New York')
print(f"Population of New York: {population_population}")
removed_city = city_populations.pop('Phoenix')
print(f"Removed city: {removed_city}")
print("Final dictionary after removing Phoenix:")
print(city_populations)


#@@@@@@@@@@@@@@@@@@PRACTICE12@@@@@@@@@@@@@@@@

countries_info = {
    'India': {'capital': 'New Delhi', 'population': 1393409038},
    'Brazil': {'capital': 'Brasília', 'population': 213993437},
    'USA': {'capital': 'Washington D.C.', 'population': 331449281},
    'China': {'capital': 'Beijing', 'population': 1444216107},
    
}

capital_china = countries_info['China']['capital']
print(f"The capital of india is: {capital_china}")
countries_info['USA']['population'] = 332915073  
print("\nFinal dictionary after updates:")
print(countries_info)


