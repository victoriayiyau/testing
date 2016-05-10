print "Should you eat that bacon?"
print "Do you want to feel like angels are frolicking on your taste buds?"
choice1 = raw_input("""Choose from the following:
0 - Yes!
1 - No
2 - Yes, but I'm afraid bacon will kill me
""")

if choice1 == "0":
	print "Eat it!"
elif choice1 == "1":
	print "Your've clearly never tasted bacon. Eat it."
else:
	choice2 = raw_input("""Are you a coward?
	0 - I am not!
	1 - Yes, I am a coward.
	""")
	if choice2 == "0":
		print "Then eat it."
	else:
		print "Bacon will turn you into a true warrior."
