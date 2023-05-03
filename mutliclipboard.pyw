#!C:\Users\mehul\AppData\Local\Programs\Python\Python310\python.exe
#mcb.pyw - saves and load a piece of text to the clipboard

#Usage -   mcb.pyw save <keyword> - save the clipboard to that keyword
#          mcb.pyw <keyword> - loads the text associated with that keyword to the clipboard
#          mcb.pyw list - Loads all the keywords currently in used into the clipboard


import shelve,pyperclip,sys

mcbShelf = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()