#Aaron Miller
#Feb 17 2017 
#python 3.6.0

#this program will make the first half of a string lower case and the second half upper caase
#by using the made sillycase method

def sillycase(fun_stuff):
	half_uppercase = fun_stuff[len(fun_stuff)//2:].upper()
	half_lowercase = fun_stuff[:len(fun_stuff)//2].lower()
	return half_lowercase+half_uppercase

print(sillycase("LoveYourLife"))
print(sillycase("GetYourPassion"))
print(sillycase("BeUrBest"))
#abstract: note: pointers are not created when using splice 
thing = "some things"
other_thing = thing
other_thing="if this equals thing then when you dont you splice your create something very close to a pointer"#it does not
print(thing)
