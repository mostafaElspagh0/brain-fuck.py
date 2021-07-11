from dataclasses import dataclass


code = """
+++++ +++++             initialize counter (cell #0) to 10
[                       use loop to set 70/100/30/10
    > +++++ ++              add  7 to cell #1
    > +++++ +++++           add 10 to cell #2
    > +++                   add  3 to cell #3
    > +                     add  1 to cell #4
<<<< -                  decrement counter (cell #0)
]
> ++ .                  print 'H'
> + .                   print 'e'
+++++ ++ .              print 'l'
.                       print 'l'
+++ .                   print 'o'
> ++ .                  print ' '
<< +++++ +++++ +++++ .  print 'W'
> .                     print 'o'
+++ .                   print 'r'
----- - .               print 'l'
----- --- .             print 'd'
> + .                   print '!'
> .                     print '\n'
"""

def is_vaild_char(c):
    v = "><+-.,[]"
    return c in v 

def filter_code ( code ):
    ret = ""
    for c in code : 
        if isvaildChar(c):
            ret+=c
    return ret

code = filter_code(code)
@dataclass
class MemoryNode():
    prev:object
    next:object
    value:int

current_memory_node :MemoryNode = MemoryNode(0 , 0 , 0)

excution_pointer = 0

loop_stack = []

while(excution_pointer < len(code)):
    c = code[excution_pointer]
    if c == '[' :
        loop_stack.append(excution_pointer)
    elif c == ']':
        if current_memory_node.value == 0:
            loop_stack.pop()
        else :
            excution_pointer = loop_stack[-1]
    elif c == '.':
        print(chr(current_memory_node.value),end ="")
    elif c == ',':
        k = input()[0]
        current_memory_node.value = k
    elif c == '>':
        if current_memory_node.next == 0:
            current_memory_node.next = MemoryNode(current_memory_node , 0 , 0)
        current_memory_node = current_memory_node.next
    elif c == '<':
        if current_memory_node.prev == 0:
            current_memory_node.prev = MemoryNode(0 , current_memory_node , 0)
        current_memory_node = current_memory_node.prev
    elif c == '+' :
        current_memory_node.value += 1
    elif c == '-' :
        current_memory_node.value -= 1
     
    excution_pointer+= 1