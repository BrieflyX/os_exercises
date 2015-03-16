#!/usr/bin/python
#coding: utf-8

class PmmManager():
    '''
    Worst-Fit algo
    '''
    def __init__(self, init_block):
        self.freed = [init_block]  # (size, start_address)
        self.used = []
    
    def near_block(self, block1, block2):
        if block1[1] < block2[1]:
            if block1[1] + block1[0] == block2[1]:
                return True
            else:
                return False
        else:
            if block2[1] + block2[0] == block1[1]:
                return True
            else:
                return False

    def merge_block(self, block1, block2):
        if block1[1] < block2[1]:
            return (block1[1], block1[0] + block2[0])
        else:
            return (block2[1], block1[0] + block2[0])

    def malloc(self, size):
        if len(self.freed) == 0 or self.freed[0][0] < size:
            return None                               # Not enough space
        else:
            block = self.freed[0]                     # Try the first block
            pointer = (size, block[1])                # Space to return
            self.freed.pop(0)
            self.used.append((block[1], size))
            self.freed.append((block[0] - size, block[1] + size))
            self.freed.sort(reverse=True)                   # Sort by size (big to small)
            return pointer 

    def free(self, block):
        if block not in self.used:
            return False                              # Cannot find the block
        else:
            self.used.remove(block)
            while True:
                merged = False
                for item in self.freed:
                    if near_block(item, block):
                        block = merge_block(item, block)
                        self.freed.remove(item)
                        merged = True
                if merged is False:
                    break
            self.freed.append(block)
            self.freed.sort(reverse=True)
            return True

def test_pmm():
    pmm = PmmManager((64, 0x00))
    space1 = pmm.malloc(16)
    print '[+] Malloc:' + str(space1)
    space2 = pmm.malloc(32)
    print '[+] Malloc:' + str(space2)
    space3 = pmm.malloc(32)
    print '[+] Malloc:' + str(space3)
    pmm.free(space2)
    print '[-] Free:' + str(space2)

if __name__ == "__main__":
    test_pmm(); 
