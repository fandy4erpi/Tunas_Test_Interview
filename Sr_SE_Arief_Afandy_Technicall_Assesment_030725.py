
# Online Python - IDE, Editor, Compiler, Interpreter
# Arief Afandy

def kemahiran_a(a):
    kemahiran_lawan = a
    return kemahiran_lawan

def kemahiran_b(b):
    list_kemahiran = []
    kemahiran_awal = b
    kemahiran_lawan = kemahiran_a(a)
    if kemahiran_awal >= kemahiran_lawan:
        kemahiran_awal+=1
        return kemahiran_awal
        

def input_lawan(n, m):
    print(n,m)
    list_kemahiran = []
    start_count = 0
    for n in range(n,m):
        kemahiran = kemahiran_b(b+start_count)
        list_kemahiran.append(kemahiran)
        start_count+=1
        
        n+=1

n = int(input('Enter N : '))
m = int(input('Enter M : '))
b = int(input('Enter B : '))
a = int(input('Enter a : '))


input_lawan(n,m)
