while True:
    print("\n1. Qo'shish")
    print("2. Ayirish")
    print("3. Ko'paytirish")
    print("4. Bo'lish")
    print("5. Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "5":
        break

    a = float(input("1-son: "))
    b = float(input("2-son: "))

    if tanlov == "1":
        print(a + b)
    elif tanlov == "2":
        print(a - b)
    elif tanlov == "3":
        print(a * b)
    elif tanlov == "4":
        if b != 0:
            print(a / b)
        else:
            print("0 ga bo'lish mumkin emas")