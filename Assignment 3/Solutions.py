"""
Solutions to assignment 3
index number:5240100317 
Class:iteD1
"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
Original _string="programming"
reversed _string=oringinal_string[::-1]
print("reserved_string:)
"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
Full_name=input("Lincoln Osae Mullings:")
name_parts=full_name.strip().split()
initials=".".join([name[0].upper()for name im name parts])+"."
print("initials")
"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
word=input("Enter a word to check of it is a palindromes:")
if word ==word[::-1]:
print(F"'{word}'is not a palindrome.")
else:
print(F"'{word}'is not a palindrome")
"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
sentence=input (" Adel goes to school ")
word=sentence.strip().slipt()
word_count=len(words)
print("number of words in the sentence:")
"""5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
Text="This is a string and it is an example."
modified_text=text.replace("is","was")
print ("modified text:")
