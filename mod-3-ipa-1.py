'''Module 3: Individual Programming Assignment 1
Thinking Like a Programmer
This assignment covers your intermediate proficiency with Python.
'''


def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return (" ")
    else:
        return (chr((((ord(letter) - 65 + shift) % 26) + 65)))

    def caesar_cipher(message, shift):
        '''Caesar Cipher.
        10 points.

        Apply a shift number to a string of uppercase English letters and spaces.
        Parameters
        ----------
        message: str
            a string of uppercase English letters and spaces.
        shift: int
            the number by which to shift the letters.
        Returns
        -------
        str
            the message, shifted appropriately.
        '''
        # Replace `pass` with your code.
        # Stay within the function. Only use the parameters as input. The function should return your answer.
        def caesar_cipher(message, shift):
        list=[]
        for i in message: 
            list.append(i)
        new=[]
  
        for i in list:
            letter = i
            is_upper = letter.isupper()
            if is_upper:
                num_letter = ord(i)
                total = shift + num_letter
                max = 90
                if i == " ":
                    new.append(" ")
                elif i == "_":
                    new.append("_")
                else:
                    if total > max:
                        remainder = int(total - 90 + 65)
                        new_letter = (chr(remainder-1))
                        new.append(new_letter)
                    else: 
                        new_letter = chr(num_letter+shift)
                        new.append(new_letter)
                    c_cipher =""
                    c_cipher =c_cipher.join(new)
            else:
                num_letter = ord(i)
                total = shift + num_letter
                max = 122
                if i == " ":
                    new.append(" ")
                elif i == "_":
                    new.append("_")
                else:
                    if total > max:
                        remainder = int(total - 122 + 97)
                        new_letter = (chr(remainder-1))
                        new.append(new_letter)
                    else: 
                        new_letter = chr(num_letter+shift)
                        new.append(new_letter)
                    c_cipher =""
                    c_cipher =c_cipher.join(new)
        return c_cipher

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    10 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter.isupper():
        return chr((ord(letter) + (ord(letter_shift) - 65) - 65) % 26 + 65)
    elif letter == " ":
        return " "
    else:
        return "Error"
    

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    message_int = [ord(i) for i in message]
    phrase = ''

    for i in range(len(message_int)):
        if message[i].isalpha():
            value = (message_int[i] + key_as_int[i % key_length]) % 26
            phrase += chr(value + 65)
        else:
            phrase += message[i]
    return phrase


def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.
    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.
    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale
    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".
    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message = str(message)
    shift= int(shift)
    cipher = ""
    
    while len(message)%shift !=0:
        message += "_"
        if  len(message)%shift == 0:
            break
    
    for i, character in enumerate(message):
        index=  (i // shift) + (len(message) // shift) * (i % shift)
        character= message[index]
        cipher += character
    return cipher


def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.
    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.
    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"
    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    decoded = ""

    while (len(decoded) < len(message)):
        decoded += "_"

    for a, b in enumerate(message):
        new = (a // shift) + (len(message) // shift) * (a % shift)
        for c, d in enumerate(decoded):
            decoded = decoded[:new] + b + decoded[new + 1:]
    return decoded
