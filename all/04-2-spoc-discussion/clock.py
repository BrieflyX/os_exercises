#!/usr/bin/env python
# coding: utf-8

class Page():
    
    def __init__(self, index):
        self.ref = 0     # reference
        self.mod = 0     # modify
        self.idx = index


def test_clock(memory_size=8, access_list=[]):

    in_page = []
    memory = {}
    head = 0
    pattern = [(0,0), (0,1), (1,0), (1,1)]
    # modify pattern
    change_pattern = {(0,0) : (0,0), (0,1) : (0,0), (1,0) : (0,0), (1,1) : (1,0)}
    miss = 0

    for i in range(memory_size):
        in_page.append(Page(i))
        memory[i] = i
    
    #Start resolve
    for access in access_list:
        print 'access :' + str(access)
        if access[0] in memory.keys():
            # page in memory
            if access[1] == 'r':
                in_page[memory[access[0]]].ref = 1
            else:
                in_page[memory[access[0]]].mod = 1
        else:
            # page not in memory
            print 'page fault: head=%d' % head
            miss += 1
            while True:
                p = (in_page[head].ref, in_page[head].mod)
                if p == (0,0):
                    break
                else:
                    # give it a second chance
                    p = (in_page[head].ref, in_page[head].mod)
                    p = change_pattern[p]
                    in_page[head].ref = p[0]
                    in_page[head].mod = p[1]
                head = (head + 1) % memory_size

            # swap the victim
            idx = in_page[head].idx
            memory.pop(idx)
            print 'victim is %d' % idx
            memory[access[0]] = head
            if access[1] == 'r':
                in_page[head].ref = 1
                in_page[head].mod = 0
            else:
                in_page[head].ref = 0
                in_page[head].mod = 1
    return miss

if __name__ == '__main__':
    memory_size = 8
    access_list = [(0,'r'), (1,'r'), (3, 'w'), (10, 'w'), (2, 'r'), (5, 'w'), (9, 'r'), (0, 'w'), (11, 'r')]
    miss = test_clock(memory_size, access_list)
    print 'miss=%d' % miss
