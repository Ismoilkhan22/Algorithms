

# the code for quicksort
"""
Qanday ishlaydi?
Quicksort algoritmi quyidagi asosiy qadamlarga ega:

Pivot tanlash: Massivdan bir element tanlanadi, bu "pivot" deb ataladi. 
    Pivot sifatida odatda massivning birinchi, oxirgi yoki o‘rtadagi elementi tanlanishi mumkin. 
    Kitobda odatda birinchi element pivot sifatida misol qilib ko‘rsatiladi.
    
Bo‘linish (Partitioning): Massiv pivotga nisbatan ikkiga bo‘linadi:
    Pivotdan kichik bo‘lgan elementlar bir guruhga.
    Pivotdan katta bo‘lgan elementlar boshqa guruhga.
    Pivot o‘z joyida qoladi.
    
Rekursiya: Keyin bu ikki kichik guruh (sub-massivlar) uchun ham xuddi shu jarayon takrorlanadi — ya’ni har bir guruh uchun yangi pivot tanlanadi va bo‘linish davom etadi.
    Bu jarayon massivda 1 yoki 0 ta element qolguncha davom etadi (bular bazaviy holat hisoblanadi).
    
Birlashtirish: Har bir kichik massiv saralangach, ular avtomatik ravishda to‘g‘ri tartibda joylashadi, chunki pivot har doim o‘zining to‘g‘ri pozitsiyasida bo‘ladi.
Misol
Massiv: [33, 15, 10]

Pivot sifatida 33 tanlanadi.
Bo‘linish:
    33 dan kichik: [15, 10]
    33 dan katta: [] (bo‘sh)
Pivot: [33]
    [15, 10] uchun quicksort qo‘llaniladi:
Pivot: 15
15 dan kichik: [10]
15 dan katta: []
Natija: [10, 15]
Oxirgi natija: [10, 15, 33]


"""
array = []
def quicksort(array):
    if len(array) < 2:  # Bazaviy holat: 0 yoki 1 elementli massiv allaqachon saralangan
        return array    
    else:
        pivot = array[0]  # Pivot sifatida birinchi element tanlanadi
        less = [i for i in array[1:] if i <= pivot]  # Pivotdan kichik yoki teng elementlar
        greater = [i for i in array[1:] if i > pivot]  # Pivotdan katta elementlar
        return quicksort(less) + [pivot] + quicksort(greater) # Rekursiv chaqiruv

print(quicksort([10, 5, 2,3]))



































