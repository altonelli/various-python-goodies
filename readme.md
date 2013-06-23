# various python utils
created by Noah Coad on 2013-06-23  
I'm a complete newb to python so bear with

## where
* py3 is an alias to python 3 runtime and py2 is an alias to python 2 runtime
* .btm files are "Batch to Memory" files run by the [Take Command](http://noahcoad.com/post/293/ultimate-windows-command-prompt-take-command) Windows command interpreter, and are mostly ancillary support until I figure out how to do more with python

## files
### spell.py
command line app  
calls google spell check from command line

example: py3 spell "john sculzi"  
outputs: john scalzi

equivalent to: `py3 -c "from urltools import Google; import sys; print (Google().spell(sys.argv[1]))"`

uses a normal google search page, meant for casual personal use only, for a supported technique, use [spelling content module](https://developers.google.com/shopping-search/v1/reference-content-module-spelling) api (which requires and api key).  The [SOAP spellcheck](http://www.actionscript.org/forums/showthread.php3?t=187859) api only does one word at a time instead of considering the entire search term.

### urltools.py
library  
various helpful url/html/link routines for stuff link downloading web pages, using google, and interacting with my blog

### HtmlClipboard.py, win32clipboard_helper.py
libraries  
for working with the Windows clipboard, getting/setting HTML fragments or text

### pyclip.btm
runs a python script with the clipboard contents as the input if an input isn't specified, and write the first line of standard output back to the clipboard  
assumes (or edit file): py3 is an alias to python 3 runtime, scripts are in python 3, and scripts are in c:\code\py

syntax: `pyclip <py sciprt w/out extension> [<optional input>]`

example: `pyclip spell`  
does a google spell check against clipboard contents and puts the result back into the clipboard

example: `pyclip spell "john sculzi"`  
does a google spell check against "john sculzi" and puts the result back into the clipboard

useful for launching from a command launcher, like [SlickRun](http://blogs.msdn.com/b/noahc/archive/2006/10/23/slickrun-command-your-pc.aspx)