"""
Write a function that checks whether a given string is a palindrome — 
a word or phrase that reads the same backward as forward (ignoring capitalization, 
spaces, and punctuation).

Define a function called is_palindrome that accepts a single string.
Return True if the string is a palindrome, and False otherwise.
Normalize the string by:
    Converting it to lowercase
    Removing spaces (and optionally punctuation)
Reverse the normalized string and compare it to the original normalized version.
    Converting it to lowercase
    Removing spaces (and optionally punctuation)
"""
def is_palindrome(some_words):
    scrubbed_words = some_words.lower()
    scrubbed_words = scrubbed_words.replace(" ", "")
    return scrubbed_words[::-1] == scrubbed_words

print(is_palindrome("racecar")) # Output: True
print(is_palindrome("hello")) # Output: False
print(is_palindrome("A man a plan a canal Panama")) # Output: True
