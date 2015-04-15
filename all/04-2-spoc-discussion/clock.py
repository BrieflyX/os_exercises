#!/usr/bin/env python
# coding: utf-8

def test_clock(memory_size=3, access_list=[]):

    memory = []
    access = {}
    head = 0
    miss = 0

    for item in access_list:
        print 'access %s:' % str(item),
        if item in memory:
            access[item] = 1
            print 'hit!',
        else:
            # miss
            print 'miss.',
            miss += 1
            if len(memory) < memory_size:
                memory.append(item)
                access[item] = 1
                head = (head + 1) % memory_size
            else:
                while access[memory[head]] == 1:
                    access[memory[head]] = 0
                    head = (head + 1) % memory_size
                print 'swap out %s' % memory[head],
                memory[head] = item
                access[item] = 1
                head = (head + 1) % memory_size
        total_list = [(x, access[x]) for x in memory]
        print 'Memory:%s' % str(total_list),
        print 'head = %d' % head

    return miss

if __name__ == '__main__':
    access_str = 'abcdabeabcde'
    miss = test_clock(3, list(access_str))
    print 'miss = %d' % miss