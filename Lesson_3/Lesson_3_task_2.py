from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 14 Pro", "+79123456789"),
    Smartphone("Samsung", "Galaxy S23", "+79223334455"),
    Smartphone("Xiaomi", "13 Pro", "+79335556677"),
    Smartphone("Google", "Pixel 7", "+79447778899"),
    Smartphone("OnePlus", "11", "+79550001122")
]
print("Каталог смартфонов:")
for phone in catalog:
    print(phone)
