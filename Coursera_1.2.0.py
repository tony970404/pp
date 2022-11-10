# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =================================================================PatternCount
# # ACTAT, ACAACTATGCATACTATCGGGAACTATCCT
# 
# Pattern = input("Please enter a pattern: ")
# Text = input("then, enter a part of the sequence: ")
# =============================================================================
# print(Text.count(Pattern))
# =============================================================================
# count = 0
# for i in range(len(Text)-len(Pattern)+1):
#         if Text[i:i+len(Pattern)] == Pattern:
#             count = count+1
# print(count)
# =============================================================================
# def PatternCount1(Pattern, Text):
#     return Text.count(Pattern)
# print(PatternCount1(Pattern, Text))
# =============================================================================
# def PatternCount2():
#     print(Text.count(Pattern))
# PatternCount2()
# =============================================================================
# def PatternCount3(Text, Pattern):
#     count = 0
#     for i in range(len(Text)-len(Pattern)+1):
#         if Text[i:i+len(Pattern)] == Pattern:
#             count = count+1
#     return count
# print(PatternCount3(Text, Pattern))
# =============================================================================

# =====================================================================pigLatin
# def pigLatin():
#     pyg = 'ay'
#     print("Welcome to Pig Latin Translator")
#     original = input("Please enter a word: ")
#     if len(original)>0:
#         if original.isalpha():
#             word = original.lower()
#             first = word[0]
#             new_word = word + first + pyg
#             new_word = new_word[1:len(new_word)]
#             print(new_word)
#         else:
#             print("Wrong Format!")
#     else:
#         print("HEY!")
# pigLatin()
# =============================================================================

# ====================================================================clinic_ex
# def clinic():
#     print("You've just entered the clinic!")
#     print("Do you take the door on the left or the right?")
#     answer = input("Type left or right and hit 'Enter'.").lower()
#     if answer == "left" or answer == "l":
#         print("This is the Verbal Abuse Room, you heap of parrot droppings!")
#     elif answer == "right" or answer == "r":
#         print("Of course this is the Argument Room, I've told you that already!")
#     else:
#         print("You didn't pick left or right! Try again.")
#         clinic()
# clinic()
# =============================================================================
