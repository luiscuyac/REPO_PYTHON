"""
Valida una cadena de 81 dígitos como tablero de Sudoku comprobando únicamente
filas (horizontales) y columnas (verticales).

Nota: Esta validación no comprueba repeticiones dentro de las subcuadrículas
de 3x3; solo verifica ausencia de duplicados en cada fila y cada columna.
"""

entrance = list(input("Ingresa el sudoku: "))
my_list = [[] for i in range(9)]
flag = True

count = 0
for number in entrance:
    if number not in my_list[count]:
        my_list[count].append(number)
        if len(my_list[count]) == 9:
            count += 1
    else:
        flag = False
        break

my_colum = [[] for i in range(9)]
if flag:
    for n in range(9):
        for i in my_list:
            if i[n] not in my_colum[n]:
                my_colum[n].append(i[n])
            else:
                flag = False
                break

print(flag)

# Comprobadores

# 295743861431865927876192543387459216612387495549216738763524189928671354154938672
# True

# 195743862431865927876192543387459216612387495549216738763524189928671354254938671
# True

# 295743861431865927876192543387459216612387495549216738763524189928671354154938622
# False
