print "hello world!"
y = 42
print y

def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + 'from inside the function'
  else:
   print 'No name'

my_list = [1, 'zen', 'hi']
print len(my_list)