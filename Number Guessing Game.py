import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    if attempts >= 7:
        print("bakhtiiiiii")
        print(f"adad man {secret_number} boooood")
        break

    try:
        adad_man = int(input("یک عدد وارد کن: "))
    except ValueError:
        print("خطا! شما عدد وارد نکردید، متن وارد کردید.")
  
    attempts += 1

    if adad_man == secret_number:
        print("booooooordi!")
        print(f"تعداد تلاش‌های شما: {attempts}")
        break
    elif adad_man < secret_number:
        print("mannnnn bozorghtaram")
    elif adad_man > secret_number:
        print("mannn kochik tarammm")