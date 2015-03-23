#!/usr/bin/env python
# coding: utf-8

pde_mask = 0xffc00000
pde_shift = 22
pte_mask = 0x003ff000
pte_shift = 12
page_mask = 0xfffff000
page_shift = 8

def read_testdata(filename='test.txt'):
    f = open(filename, 'r')
    test_case = []
    for line in f.readlines():
        addr = line.split(',')
        va = int(addr[0].strip().split(' ')[1][2:], 16)
        pa = int(addr[1].strip().split(' ')[1][2:], 16)
        test_case.append((va, pa))
    f.close()
    return test_case

def translate(data):
    outtitle = ['va', 'pa', 'pde_idx', 'pde_ctx', 'pte_idx', 'pte_ctx']
    for item in data:
        va = item[0]
        pa = item[1]
        pde_idx = (va & pde_mask) >> pde_shift
        pde_ctx = ((pde_idx - 0x300 + 1) << 12) | 0x003
        pte_idx = (va & pte_mask) >> pte_shift
        pte_ctx = (pa & page_mask) | 0x003 
        outdata = [va, pa, pde_idx, pde_ctx, pte_idx, pte_ctx]
        for k, v in zip(outtitle, outdata):
            print k + ': 0x%08x, ' % v,
        print

if __name__ == '__main__':
    translate(read_testdata())
