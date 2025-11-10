text = input("Введите строку для проверки палиндрома")

text = text.lower()
text = text.replace(" ", "")

reverse_text = text[::-1]
if text == reverse_text:
    print("палиндром")
else:
    print("не палиндром")