#have a HELP command
#have a SHOW command
#clean code up in general


#make a list to hold onto our items
shopping_list = []

# print out instructions on how to use app
def show_help():
	print("What should we put in the list to pick up at the store?")
	print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for instructions
Enter 'SHOW' to see what is in the shopping list
""")

def show_list():
	print("here's your list:")
	for item in shopping_list:
		print(item)

#add new items to list
def add_to_list(new_item):
	shopping_list.append(new_item)	
	print("Added {}. list now has {} items.".format(new_item, len(shopping_list)))

show_help()

while True:
	#ask for new items
	new_item = input("> ")

	#be able to quit app
	if new_item == 'DONE':
		break
	elif new_item == 'HELP':
		show_help()
		continue
	elif new_item == 'SHOW':
		show_list()
		continue
	
	add_to_list(new_item)
	


#print oout the list
