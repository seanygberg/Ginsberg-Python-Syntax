
def print_upper_words(words):
    """Print each word in the list in uppercase.

    For example:
      print_upper_words(["Programming", "is", "pretty", "fun"])
        PROGRAMMING
        IS
        PRETTY
        FUN
    """  
    for word in words:
        print(word.upper())

def print_upper_e_words(words):
    """Print each word that starts with E or e in the list in uppercase.

    For example:
      print_upper_e_words(["eagle", "Edward", "Alfred"])
        EAGLE
        EDWARD
    """  
    for word in words:
        if (word.upper().startswith("E")):
            print(word.upper())

def print_upper_given_letters_words(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

        print_upper_given_letters_words(["eagle", "Edward", "Alfred", "zope"], must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

print_upper_words(["Programming", "is", "pretty", "fun"])
print_upper_e_words(["eagle", "Edward", "Alfred"])
print_upper_given_letters_words(["eagle", "Edward", "Alfred", "zope"], must_start_with=["A", "E"])