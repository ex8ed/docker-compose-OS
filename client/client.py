# -*- coding: UTF-8 -*-

import urllib.request

# Taked a port from server part
cl = urllib.request.urlopen("http://localhost:9999/")

_encoded = cl.read()
_decoded = _encoded.decode("UTF-8")

# Printing data from index.html on the screen
print(_decoded)
cl.close()
