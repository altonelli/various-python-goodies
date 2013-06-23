# created by Noah Coad 2013-06-23
# perform a google spell check and return results
# command line tool, specify input as first parameter
# example: python spell.py "john sculzi"

from urltools import Google
import sys

print (Google().spell(sys.argv[1]))
