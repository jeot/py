import random

for wordLen in range(3,5):
	for x in range(7): # i like 7
		word = "";
		for ci in range(wordLen):
			word += chr(random.randint(97,122))
		print(word) # the "jeot" was selected!