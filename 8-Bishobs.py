import time
import os

os.system('cls')
print("\n"*2)

n = int(input("Enter the size of the board : "))
print("\n"*2)

bord = [[' .' for _ in range(n)] for _ in range(n)]


def safe(row, col):
    # چک کردن سطر
    for j in range(col):
        if bord[row][j] == ' ∎':
            return False

    # چک کردن قطر اصلی (↖)
    for i in range(1, col + 1):
        r = row - i 
        c = col - i
        if r >= 0 and c >= 0:
            if bord[r][c] == ' ∎':
                return False

    # چک کردن قطر فرعی (↗)
    for i in range(1, col + 1):
        r = row + i
        c = col - i
        if r < n and c >= 0:
            if bord[r][c] == ' ∎':
                return False

    return True


def show():
    os.system('cls')
    print("\n"*4)
    for r in bord:
        for j in r:
            print(j, end='      ')
        print("\n"*2)
    time.sleep(0.8)


def solve(col):
    if col == n:
        return True

    for row in range(n):  # حالا برای هر ستون، بررسی می‌کنیم که کدوم سطر مناسب است
        # نمایش تلاش برای بررسی این خونه
        bord[row][col] = ' ?' ; show() ; bord[row][col] = ' .'# نشون می‌ده الان داریم بررسی می‌کنیم
        
          # پاکش می‌کنیم چون هنوز تصمیم نگرفتیم

        if safe(row, col):
            bord[row][col] = ' ∎'
            show()
            if solve(col + 1):  # حرکت به ستون بعدی
                return True
            bord[row][col] = ' .'  # پاک کردن ∎ برای بک ترک
            show()
    return False


solve(0)  # شروع از ستون 0
print("\n"*2)
