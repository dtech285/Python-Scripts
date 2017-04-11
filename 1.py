#! python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))

import webbrowser
ffpath = 'C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'
print(webbrowser._tryorder)
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(ffpath), 1)
print(webbrowser._tryorder)
ff = webbrowser.get('firefox')
ff.open("http://www.bing.com")