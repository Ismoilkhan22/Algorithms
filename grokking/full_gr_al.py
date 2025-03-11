"""
-bo‘lim: Introduction to Algorithms (Advanced)
Nazariya (Chuqur)
Algoritmning mohiyati:
Algoritm – bu nafaqat qadamlar ketma-ketligi, balki resurslarni (vaqt, xotira) optimallashtirish san’ati. Web3’da bu gaz xarajatlari va blokcheyn cheklovlari bilan bog‘liq.
Big O Notation (kengaytirilgan):
O(1): Doimiy vaqt – masalan, hash jadvalidan element olish.
O(log n): Logarifmik vaqt – binary search kabi, katta ma’lumotlarni qidirishda foydali.
O(n): Chiziqli vaqt – oddiy qidirish yoki ro‘yxatni aylanib chiqish.
O(n log n): Sortlashning eng yaxshi o‘rtacha holati (quicksort).
O(n²): Kvadratik vaqt – ichma-ich tsikllar, masalan, bubble sort.
O(2^n): Eksponensial vaqt – murakkab rekursiv muammolar (masalan, Fibonacci).
Amortizatsiya tahlili: Ba’zi algoritmlarda o‘rtacha vaqtni hisoblash (hash table resizing kabi).
Web3’da nima uchun muhim?:
Smart-kontraktlarda har bir operatsiya gaz stoimostiga ega. O(n²) algoritm ishlatish kontraktingni qimmat qiladi, lekin O(log n) yoki O(1) tejamkor qiladi.

"""


# 1 O(n) linear search (simply)

def liner_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# 2. O(logn) - Binary Search (optimallashtirilgan)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# 3.
