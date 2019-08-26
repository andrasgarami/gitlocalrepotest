import sys

if len(sys.argv) == 1:
    print("Hello World!")

else:
    del(sys.argv[0])
    str1 = ' '.join(sys.argv)
    print("Hello " + str1 + "!")

#https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string