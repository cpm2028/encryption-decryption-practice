#This program will help be the basis for my final project, replacing certain letters with numbers.
#Source that helped me figure this out: https://www.w3schools.com/python/ref_dictionary_get.asp , https://www.w3schools.com/python/ref_string_join.asp
#user decides if they need it encrypted or decrypted
user_decision=input("Would you like to encrypt or decrypt: ")

#if the user chooses encrypt
if user_decision=="encrypt":
    #prompt for phrase
    user_phrase = input("What is the word or phrase you would like to encrypt: ")
    #dictionary to assign vowels with other characters or numbers
    replacement_vowel = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 'u': '-'}
    #dictionary to assign other words with characters or numbers
    replacement_words = {
        's': '$', 'l': '|', 'y': 'yzy', 't': '-|-',
        'k': '|/_', 'w': '-_-'
    }
    #combine the dictionarys into one variable
    replacement = {**replacement_vowel, **replacement_words}
    #combine them into one string based off input
    encryption = ''.join(replacement.get(char, char) for char in user_phrase.lower())
    #output encrypted text
    print(encryption)
elif user_decision=="decrypt":
    #ask user for inputs
    user_phrase = input("What is the word or phrase you would like to decrypt: ")
    # dictionary to assign vowels with other characters or numbers
    deplacement_words = {
        '$': 's', '|': 'l', 'yzy': 'y', '-|-': 't',
        '|/_': 'k', '-_-': 'w'
    }
    # dictionary to assign other words with characters or numbers
    deplacement_vowels = {
        '@': 'a', '3': 'e', '1': 'i', '0': 'o', '-': 'u'
    }
    #combine the dictionaries into one variable
    deplacement = {**deplacement_vowels, **deplacement_words}
    #combine variable into a string based off input
    decrypt = ''.join(deplacement.get(char, char) for char in user_phrase.lower())
    #output decryption
    print(decrypt)
else:
    #if the user does not enter encrypt or decrypt, it outputs invalid
    print("Invalid, you can only encrypt or decrypt")