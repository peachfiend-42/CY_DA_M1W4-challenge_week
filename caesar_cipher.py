def caesar_cipher(plain_txt, shift_step): # define func: take plain text and value to shift cipher
    encypted_txt = "" #establish variable to hold the encrypted text
    for char in plain_txt: # as it says: for each character in the text we're encryping, do...
        if char.isalpha(): # check to see if the character being encrypted is a letter
            abc_fixer = ord(char) + shift_step # definte variable to apply the cipher shift
            if abc_fixer > ord('z'): # if the shift goes beyond z...
                abc_fixer -= 26 # ... then basically push it around to A and onward to get the right cipher letter

        else: # in case character is not a letter
            abc_fixer = char # feels weird based on variable name, but if it's not a letter, leave it be.

        latest_char = chr(abc_fixer)
        encypted_txt += latest_char
    print(encypted_txt)
    return encypted_txt


caesar_cipher("abc", 3) #Output:  "def"  
caesar_cipher("xyz", 2) #Output:  "zab"  
caesar_cipher("Hello, World!", 5) #Output:  "Mjqqt, Btwqi!"