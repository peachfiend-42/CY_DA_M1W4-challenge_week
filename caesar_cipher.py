# what a pain in the ass.

def caesar_cipher(plain_txt, shift_step): # define func: take plain text and value to shift cipher

    encypted_txt = "" #establish variable to hold the encrypted text

    for char in plain_txt: # as it says: for each character in the text we're encryping...
        if char.isalpha(): # ...check to see if the character being encrypted is a letter.

            if char.isupper(): # because referencing both uppercase and lowercase letters in strings.
                abc_fixer = ord(char) + shift_step # change the letter to an ascii code (int), apply cipher shift, store in abc_fixer.
                if abc_fixer > ord('Z'): # if the shift goes beyond Z...
                    abc_fixer -= 26 # ...then basically push it around to A and onward to get the right cipher letter.

            elif char.islower(): # because referencing both uppercase and lowercase letters in strings.
                abc_fixer = ord(char) + shift_step # change the letter to an ascii code (int), apply cipher shift, store in abc_fixer.
                if abc_fixer > ord('z'): # if the shift goes beyond 'z'...
                    abc_fixer -= 26 # ...then basically push it around to 'a' and onward to get the right cipher letter.

        else: # in case character is not a letter
            abc_fixer = ord(char) # feels weird based on variable name, but if it's not a letter, leave it be.

        latest_char = chr(abc_fixer) # turns ascii(unicode?) value of abc_fixer back to a letter
        encypted_txt += latest_char # tack the latest encrypted letter/character onto the encrypted text we're building
    print(encypted_txt) # does what it says
    return encypted_txt # because functions must "return"?

caesar_cipher("abc", 3) #Output:  "def"  
caesar_cipher("xyz", 2) #Output:  "zab"  
caesar_cipher("Hello, World!", 5) #Output:  "Mjqqt, Btwqi!"