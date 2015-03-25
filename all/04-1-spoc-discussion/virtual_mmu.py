#!/usr/bin/env python
# coding: utf-8

__author__ = 'Pei Zhongyu'

pdbr = 0xd80
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
disk = []      # Disk data

mem_lines = range(5, 133)
disk_lines = range(137, 265)

def print_page(pageaddr, title='page', target=memory):
    print '  ' + title + ' %02x:' % pageaddr,
    for i in target[pageaddr]:
        print '%02x' % i,
    print

def read_byte(memaddr, target=memory):
    return target[(memaddr & page_mask) >> 5][memaddr & offset_mask]

def dump_memory(filename='../04-1-spoc-memdiskdata.md', lines=mem_lines, target=memory):
    data = open(filename, 'r').readlines()
    for i in lines:
        l = data[i][8:].strip().split(' ')
        target.append([int(x, 16) for x in l])

def mmu(va):
    print
    print 'Virtual Address 0x%04x' % va
    
    # first find pde
    pde_index = (va & pde_mask) >> pde_shift
    pde_entry = read_byte(pdbr + pde_index)
    valid = (pde_entry & valid_mask) >> valid_shift
    pfn = pde_entry & pfn_mask
    print '  --> pde index:0x%02x pde contents:(valid %d, pfn 0x%02x)' % (pde_index, valid, pfn)

    if valid == 0 or pde_index > 7:
        print '    --> Fault (page directory entry not valid)'
        return
    print_page(pfn) 
    
    # then find pte
    pte_index = (va & pte_mask) >> pte_shift
    pte_entry = memory[pfn][pte_index] 
    valid = (pte_entry & valid_mask) >> valid_shift
    pfn = pte_entry & pfn_mask
    print '    --> pte index:0x%02x pte contents:(valid %d, pfn 0x%02x)' % (pte_index, valid, pfn)

    # switch to disk
    if valid == 0:
        disk_addr = (pfn << 5) + (va & offset_mask)
        print_page(pfn, 'disk', disk)
        print '      --> To Disk Sector Address 0x%03x --> Value: 0x%02x' % (disk_addr, read_byte(disk_addr, disk))
    else:
        # at last get the physical value
        ph_addr = (pfn << 5) + (va & offset_mask)
        print_page(pfn)
        print '      --> To Physical Address 0x%03x --> Value: 0x%02x' % (ph_addr, read_byte(ph_addr))

if __name__ == '__main__':
    dump_memory(lines=mem_lines, target=memory)
    dump_memory(lines=disk_lines, target=disk)
    test_vas = [0x0330, 0x1e6f]
    vas = [0x6653, 0x1c13, 0x6890, 0x0af6, 0x1e6f]
    for va in vas:
        mmu(va)
