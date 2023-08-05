"""def str_counter(s):
    for sym in set(s):
        counter=0
        for sub_sym in s:
            if sym==sub_sym: counter+=1
        print(sym, counter)

str_counter("qwertttyq")"""

"""
def str_counter(s):
    syms_counter={}
    for sym in s:
        syms_counter[sym]=syms_counter.get(sym, 0)+1
    
    for sym, count in syms_counter.items():
        print(sym, count)

str_counter("qwertttyq")

"""
# Практика, задача 4

def palindromic():
    Input=input(">>> ")                                  # 1) Ввод строки в любом виде
    Input=Input.replace(" ", "").lower()                 # 2) Поставить строку в нижний регистр; убрать пробелы
    Double=len(Input)//2                                 # 3) Разделить строку на 2 строки пополам
    if Input[:Double]==Input[Double:][::-1]: print(True) # 4) Если первая часть строки (слева) равна перевёрнутой второй части строки (справа), то вывести True 
    else: print(False)                                   # 5) В противном случае False

palindromic()