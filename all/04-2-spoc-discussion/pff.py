#!/usr/bin/env python
# coding: utf-8
# Page Fault Frequence Algo

def test_pff(access_list, T=2):
    memory = []
    last_miss = -1
    miss = 0

    #start resolving
    for i, item in enumerate(access_list):
        print 'access %s:' % item,
        if item in memory:
            print 'hit!',
        else:
            print 'miss. ',
            if i - last_miss <= T or last_miss == -1:
                print 'add to memory.',
            else:
                for page in memory:
                    if page not in access_list[last_miss:i+1]:
                        print 'remove %s.' % page,
                        memory.remove(page)
            memory.append(item)
            miss += 1
            last_miss = i
        memory.sort()
        print 'now in memory:' + str(memory)
    return miss

if __name__ == '__main__':
    access_list = ['a', 'd', 'e', 'c', 'c', 'd', 'b', 'c', 'e', 'c', 'e', 'a', 'd']
    miss = test_pff(access_list)
    print 'Miss times:%d' % miss
