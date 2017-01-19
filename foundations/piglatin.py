"""
 Implementation of simple pig latin translator
"""

import sys
import logging

__author__ = 'cfung'

'''
For words that begin with consonant sounds, all letters before the initial vowel are placed 
at the end of the word sequence. Then, "ay" (some people just add "a") is added, 
as in the following examples:

"pig" = "igpay"
"banana" = "ananabay"
"trash" = "ashtray"
"happy" = "appyhay"
"duck" = "uckday"
"glove" = "oveglay"
"latin" = "atinlay"
"dopest" = "opestday"

When words begin with consonant clusters (multiple consonants that form one sound), the whole sound is added to the end when speaking or writing

"cheers" = "eerschay"
"shoot" = "ootshay"

For words that begin with vowel sounds, one just adds "way" to the end. Examples are:

"eat" = "eatway"
"omelet" = "omeletway"
"are" = "areway"
'''

def translator():

	user_input = raw_input("Please enter a string...: ")
	
	vowels = ['a', 'e', 'i', 'o', 'u']
	
	position_first_vowel = None

	#result = None
	
	if len(user_input) > 0:

		if user_input[0] in vowels:

			return user_input + "way"


		elif (user_input[0] not in vowels):

			for idx, letter in enumerate(user_input):

				if letter in vowels:  # "pig" = "igpay" "banana" = "ananabay"
					position_first_vowel = idx

					return user_input[position_first_vowel:] + user_input[0:position_first_vowel] + "ay"  


		elif ((user_input[0] not in vowels) and (user_input[0] == user_input[1])):
			
			for idx, letter in enumerate(user_input):

				if letter in vowels:  # "cheers" = "eerschay", "shoot" = "ootshay"
					position_first_vowel = idx

					return user_input[position_first_vowel+1:] + user_input[0:position_first_vowel] + "ay"  

	else:
		print "enter a valid string"
		

if __name__ == '__main__':
    translator()