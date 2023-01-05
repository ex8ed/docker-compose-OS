# -*- coding: UTF-8 -*-

import http.server
import sockerserver

# simple server on python base-libs
_handler = http.server.SimpleHTTPRequestHandler

# Here is a server on a port :9999 ; its omportant to edit it in .yml file
with socketserver.TCPServer(("", 9999), _handler) as httpd:
	httpd.serve_forever()
