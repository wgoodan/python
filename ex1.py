word = raw_input("Please input a word in English")
if (word == ""):
	print "Check to make sure you entered a valid word"
	elif (word[0] != "a" and word[0]!= "e" and word[0]!= "i" and word[0]!= "o" and word[0]!= "u")#探测辅音开头
	
		word = word[len(word)] 

	else# 元音开头










'''
Ask the user to input a word in English

Check to make sure the user entered a valid word

Convert the word from English to Pig Latin

Display the translation result

Notice that some of the steps can themselves be broken down into individual steps. For example, we'll want to think through the algorithm for step #3 before we start coding.
'''