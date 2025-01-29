def binary_search(arr, item):
    low = 0
    high = len(arr) - 1  # massiv uzunligi
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]  # taxmin qilaman va osha elemntni guess ga yuklayman
        if guess == item:  # agar taxmin qilgan element va topish kerak bulgan element teng bulsa mid ni qaytaradi
            return mid
        elif guess > item:  # agar  men olgan guess item dan kotta bolsa yuqori qismini tashlayman va ortadagi mid dan 1 ni ayrib high ga yukleman
            high = mid - 1
        else:  # agar guess item dan kichik bolsa pastki qisimni olib tashlayman va low ga mid + 1 ni yuklayman.
            low = mid + 1
    return None


"""
① past va yuqori roʻyxatning qaysi qismida qidirayotganingizni kuzatib boring.

② Siz uni bitta elementga qisqartirmagansiz. . .

③ . . . o'rta elementni tekshiring.

④ Element topildi.

⑤ Taxmin juda baland edi.

⑥ Taxmin juda past edi.

⑦ Element mavjud emas.

⑧ Keling, sinab ko'ramiz!

⑨ Esingizda bo'lsin, ro'yxatlar 0 dan boshlanadi. Ikkinchi slotda indeks 1 mavjud.

⑩ None Pythonda null degani. Bu element topilmaganligini bildiradi.

"""
