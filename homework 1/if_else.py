value = int(input("Enter your score :"))


if value >= 80:
    print("Grade : A")


elif value > 74 and value < 80:
    print("Grade : B+")


elif value > 70 and value < 75:
    print("Grade : B")


elif value >= 70 and value < 75:
    print("Grade : B")


elif value < 70 and value >= 65:
    print("Grade : C+")


elif value < 65 and value >= 60:
    print("Grade : C")


elif value < 60 and value >= 55:
    print("Grade : D+")

elif value < 55 and value >= 50:
    print("Grade : D")


else:
    print("Grade : F")
