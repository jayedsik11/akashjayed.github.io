# write-html-2-windows.py

import webbrowser

f = open('hi.html','w')

message = 'ju'

f.write(message)
f.close()

webbrowser.open_new_tab('hi.html')