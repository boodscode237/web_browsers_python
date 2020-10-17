import webbrowser
import sys
import pyperclip


sys.argv

# check if command line args were passes

if len(sys.argv) > 1:
    # [Ekaterinburg Central Park of Culture and Recreation named after V.V. Mayakovsky]
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

# https://www.google.com/maps/place/<ADDRESS>
