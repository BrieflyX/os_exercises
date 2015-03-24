#!/usr/bin/python
# coding: utf-8

pdbr = 0x220
valid_mask = 0x80
valid_shift = 7
pde_mask = 0x7c00
pde_shift = 10
pte_mask = 0x03e0
pte_shift = 5
pfn_mask = 0x007f

offset_mask = 0x001f
page_mask = 0x0fe0

memory = []    # Memory data

def read_byte(memaddr):
    return memory[(memaddr & page_mask) >> 5][memaddr & offset_mask]

def dump_memory():
    filename = '03-2-spoc-testdata.md'
    lines = range(5, 133)
    data = open(filename, 'r').readlines()
    for i in lines:
        l = data[i][8:].strip().split(' ')
        memory.append([int(x, 16) for x in l])

def mmu(va):
    print 'Virtual Address 0x%04x' % va
    
    # first find pde
    pde_index = (va & pde_mask) >> pde_shift
    pde_entry = read_byte(pdbr + pde_index)
    valid = (pde_entry & valid_mask) >> valid_shift
    pfn = pde_entry & pfn_mask
    print '  --> pde index:0x%02x pde contents:(valid %d, pfn 0x%02x)' % (pde_index, valid, pfn)

    if valid == 0:
        print '    --> Fault (page directory entry not valid)'
        return

    # then find pte
    pte_index = (va & pte_mask) >> pte_shift
    pte_entry = memory[pfn][pte_index] 
    valid = (pte_entry & valid_mask) >> valid_shift
    pfn = pte_entry & pfn_mask
    print '    --> pte index:0x%02x pte contents:(valid %d, pfn 0x%02x)' % (pte_index, valid, pfn)

    if valid == 0:
        print '      --> Fault (page table entry not valid)'
        return

    # at last get the physical value

    ph_addr = (pfn << 5) + (va & offset_mask)
    print '      --> Translates to Physical Address 0x%03x --> Value: 0x%02x' % (ph_addr, read_byte(ph_addr))


if __name__ == '__main__':
    dump_memory()
    vas = [0x6c74, 0x6b22, 0x03df, 0x69dc, 0x317a, 0x4546, 0x2c03, 0x7fd7, 0x390e, 0x748b]
    for va in vas:
        mmu(va)
