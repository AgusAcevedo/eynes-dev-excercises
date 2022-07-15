from random import randrange 

def function():
    list_dict = []
    for num in range(10):
        age = randrange(1,100)
        list_dict.append({'id' : num+1, 'edad' : int(age)})
    return list_dict

def orderbyage(list):
    list.sort(key= lambda p: p['edad'])
    print('El id de la persona mas joven es:', list[0]['id'], "con una edad de",list[0]['edad'], "años")
    print('El id de la persona mas vieja es:', list[9]['id'], "con una edad de",list[9]['edad'], "años")

if __name__ == "__main__":
    returned_list = function()
    orderbyage(returned_list)