# lab0 SPOC思考题

## 个人思考题

---

能否读懂ucore中的AT&T格式的X86-32汇编语言？请列出你不理解的汇编语言。
- 大部分能够读懂，部分指令不太明白，譬如cli、cld等。

>  http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm

虽然学过计算机原理和x86汇编（根据THU-CS的课程设置），但对ucore中涉及的哪些硬件设计或功能细节不够了解？
- 计算机原理课程主要内容是对CPU的架构及实现的介绍，对其他外设功能的实现讲解不太深入。希望能够更好地了解硬件驱动机制。

>   


哪些困难（请分优先级）会阻碍你自主完成lab实验？
- 从高到低：阅读别人的代码；理解设计的思想；对Linux C和Linux系统相关工具的不熟悉。

>   

如何把一个在gdb中或执行过程中出现的物理/线性地址与你写的代码源码位置对应起来？
- 一般来说是线性关系，代码源码靠后的部分物理地址较大，没有确切的对应关系因为源码语句编译成汇编指令之后需要的汇编指令条数不同。

>   

了解函数调用栈对lab实验有何帮助？
- 可以更好地对源码进行调试，理解程序的运行机制和可能出现的问题。

>   

你希望从lab中学到什么知识？
- Linux C的编程技巧，ucore的设计理念与思想，各种编程工具和代码审计工具的使用。

>   

---

## 小组讨论题

---

搭建好实验环境，请描述碰到的困难和解决的过程。
- 没有遇到太大困难。

> 

熟悉基本的git命令行操作命令，从github上
的 http://www.github.com/chyyuu/ucore_lab 下载
ucore lab实验
- 对基本的git命令已经有所了解而且下载了ucore lab的实验代码到本地。

> 

尝试用qemu+gdb（or ECLIPSE-CDT）调试lab1
- 已经调试。

> 

对于如下的代码段，请说明”：“后面的数字是什么含义
```
/* Gate descriptors for interrupts and traps */
struct gatedesc {
    unsigned gd_off_15_0 : 16;        // low 16 bits of offset in segment
    unsigned gd_ss : 16;            // segment selector
    unsigned gd_args : 5;            // # args, 0 for interrupt/trap gates
    unsigned gd_rsv1 : 3;            // reserved(should be zero I guess)
    unsigned gd_type : 4;            // type(STS_{TG,IG32,TG32})
    unsigned gd_s : 1;                // must be 0 (system)
    unsigned gd_dpl : 2;            // descriptor(meaning new) privilege level
    unsigned gd_p : 1;                // Present
    unsigned gd_off_31_16 : 16;        // high bits of offset in segment
};
```

- 对应变量位域的大小，表示变量所占的位数。

> 

对于如下的代码段，
```
#define SETGATE(gate, istrap, sel, off, dpl) {            \
    (gate).gd_off_15_0 = (uint32_t)(off) & 0xffff;        \
    (gate).gd_ss = (sel);                                \
    (gate).gd_args = 0;                                    \
    (gate).gd_rsv1 = 0;                                    \
    (gate).gd_type = (istrap) ? STS_TG32 : STS_IG32;    \
    (gate).gd_s = 0;                                    \
    (gate).gd_dpl = (dpl);                                \
    (gate).gd_p = 1;                                    \
    (gate).gd_off_31_16 = (uint32_t)(off) >> 16;        \
}
```

如果在其他代码段中有如下语句，
```
unsigned intr;
intr=8;
SETGATE(intr, 0,1,2,3);
```
请问执行上述指令后， intr的值是多少？

- [x]  

> 

请分析 [list.h](https://github.com/chyyuu/ucore_lab/blob/master/labcodes/lab2/libs/list.h)内容中大致的含义，并能include这个文件，利用其结构和功能编写一个数据结构链表操作的小C程序

- 声明了结构体：list的entry，即链表的条目。定义了链表的创建、添加、删除、清空等操作。
- #include "list.h"
- int main(){
- list_entry* en = (list_entry)malloc(sizeof(list_entry));
- list_init(en);
- return 0;}

> 

---

## 开放思考题

---

是否愿意挑战大实验（大实验内容来源于你的想法或老师列好的题目，需要与老师协商确定，需完成基本lab，但可不参加闭卷考试），如果有，可直接给老师email或课后面谈。
- 否 

>  

---
