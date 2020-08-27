n = [[1, 2, 3],[4, 5, 6],[7, 8, 9]] #data awal

def counterClockwise(data):
    list1 = []                  #variabel utk menampung tiap data pada index 2
    list2 = []                  #variabel utk menampung tiap data pada index 1
    list3 = []                  #variabel utk menampung tiap data pada index 0
    list_akhir = []             #variabel untuk menampung semua list yg dibuat (list1 - 3)
    for i in data:
        x = i[2]                #menampung index terakhir pada tiap list kedalam x
        list1.append(x)         #menambah x ke dalam list1
        x = i[1]                #menampung index kedua pada tiap list kedalam x
        list2.append(x)         #menambah x ke dalam list2
        x = i[0]                #menampung index pertama pada tiap list kedalam x
        list3.append(x)         #menambah x ke dalam
    list_akhir.append(list1)    #menambah list1 ke dalam list_akhir
    list_akhir.append(list2)    #menambah list2 ke dalam list_akhir
    list_akhir.append(list3)    #menambah list3 ke dalam list_akhir
    return list_akhir

print(n)
print(counterClockwise(n))