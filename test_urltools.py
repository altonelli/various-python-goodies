from linktools import *

l = Linker()
c = CoadBlog()

print(l.get_title(r'http://noahcoad.tumblr.com/post/44331013570/entertaining-videos'))
print(l.get_page('http://coad.net/noah'))
print(l.make_link('http://coad.net/noah', "Noah Coad's Home"))

print(c.lucky('3 steps meteor windows'))
print(c.search_link('south park'))
print(c.email('teched robust'))

print(Google().spell("miscellaneouss"))