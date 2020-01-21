#!/usr/bin/env python3
import cgi
import cgitb
import os
#import BeautifulSoup
cgitb.enable()


print("Content-Type: text/plain\n")
print()
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")


#q1
print(os.environ)
#print(cgi.print_environ_usage())
