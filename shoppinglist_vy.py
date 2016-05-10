my_shoppinglist = []

def menu():
	print "0 - Main Menu"
	print "1 - Show current shopping list"
	print "2 - Add an item to shopping list"
	print "3 - Remove an item from shopping list"
	print "4 - Replace an old item with new item on shopping list"
	print "5 - Exit"
	menu_option = int(raw_input("Please choose one option from the menu:"))
	return menu_option

def add_item(item):
	item = item.lower()
	if item in my_shoppinglist:
		print "%s already exists." % (item)
	else:
		my_shoppinglist.append(item)
		print "Here's your updated list:", sorted_shoppinglist()

def sorted_shoppinglist():
	my_shoppinglist.sort()
	return my_shoppinglist

def remove_item(item):
	item = item.lower()
	if item in my_shoppinglist:
		my_shoppinglist.remove(item)
		print "%s has been removed. Here's your updated list:" % (item), sorted_shoppinglist()
	else:
		print "%s not found." % (item)

def replace_item(old_item, new_item):
	old_item = old_item.lower()
	new_item = new_item.lower()
	if old_item in my_shoppinglist:
		item_index = my_shoppinglist.index(old_item)
		print "%s has replaced %s in the list." % (new_item, old_item)
	else:
		print "%s is not in the list." % (old_item)

def main():
	menu_option = menu
	while (True):
		menu()
		if menu_option == "0":
			menu ()
		elif menu_option == "1":
			sorted_shoppinglist()
		elif menu_option == "2":
			add_item()
		elif menu_option == "3":
			remove_item()
		elif menu_option == "4":
			replace_item()
		elif menu_option == "5":
			break

if __name__ == '__main__':
	main()

#TEST FUNCTIONS
#1 - add 4 items to your shopping list
add_item("sugar")
add_item("cream")
add_item("eggs")
add_item("flour")

#2 - add an item that is already in the list
add_item("cream")

#3 - remove an item from your list
remove_item("cream")

#4 - remove an item not on your list
remove_item("milk")

#5 - replace an item on your list with a new item
replace_item("eggs", "butter")

print my_shoppinglist