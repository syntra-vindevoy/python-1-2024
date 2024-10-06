def kerstboom (char, size):
    if len(char) == 1 and size > 2:
        for i in range (size+1, 1, -1):
            print (" " * i + char*(size+2 -i) + char * (size+1-i))
        print (" " * (size+1) + "|")
    else:
        if len (char) < 1:
            print ("Enter a character")
        if len (char) > 1:
            print ("Only one character allowed for drawing tree")
        if size < 3:
            print ("Minimum size is 3")

kerstboom ("", 5)