from random import randrange

def function():
    matrix = []
    for x in range(5):
        matrix.append([0]*5)

    for y in range(5):
        for z in range(5):
            matrix[y][z] = int(randrange(1,3))
    for x in matrix:
        print(x)
    return matrix

def findpattern(matrix,y):
    secuence_count= 0
    position = 0
    for x in matrix:
        if ckeckList(x[0:4]):
            secuence_count +=1
            if y:  
                print("Secuencia encontrada en las coordenadas:(",position,", 0 ) a (",position,", 3 )")
            elif not y:
                print("Secuencia encontrada en las coordenadas:( 1 ,",position,") a ( 4,", position,")")

        if ckeckList(x[1:5]):
            secuence_count +=1
            if y:  
                print("Secuencia encontrada en las coordenadas:(",position,", 1 ) a (",position,", 4 )")
            elif not y:
                print("Secuencia encontrada en las coordenadas:( 0 ,", position,") a ( 3,", position,")")
        position += 1

    return secuence_count

def ckeckList(lst):
    ele = lst[0]
    chk = True

    for item in lst:
        if ele != item:
            chk = False
            break
              
    if (chk == True): return True
    else: return False  

def rotate(matrix):
      temp_matrix = []
      column = len(matrix)-1
      for column in range(len(matrix)):
         temp = []
         for row in range(len(matrix)-1,-1,-1):
            temp.append(matrix[row][column])
         temp_matrix.append(temp)
      for i in range(len(matrix)):
         for j in range(len(matrix)):
            matrix[i][j] = temp_matrix[i][j]
      return matrix


if __name__ == "__main__":
    total_patterns = 0

    matrix = function()
    patterns_1 = findpattern(matrix,True)

    rotated_matrix = rotate(matrix)
    patterns_2 = findpattern(rotated_matrix,False)

    total_patterns = patterns_1 + patterns_2
    print(total_patterns)