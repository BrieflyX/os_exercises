# coding: utf-8
# working-set page-replacement algo

def test_working_set(access_list, window_size = 4):
    memory = []
    miss = 0

    #start resovling
    for i in range(0, len(access_list)):
        if access_list[i] in memory:
            res = 'hit'
        else:
            res = 'miss'
            miss += 1

        memory = []
        memory.append(access_list[i])
        for j in range(1, window_size):
            if (i - j >= 0) and not(access_list[i - j] in memory):
                memory.append(access_list[i - j])
        memory.sort()

        print i + 1, ': visit', access_list[i], res, str(memory)
    return miss
        
if __name__ == '__main__':
    access_list = ['c','c','d','b','c','e','c','e','a','d','f','h','a','c','d','z','y','a','x']
    miss = test_working_set(access_list)
    print 'miss times:%d' %miss
