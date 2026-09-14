from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15 Pro", "+79123456789"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79234567890"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79345678901"),
    Smartphone("Google", "Pixel 8 Pro", "+79456789012"),
    Smartphone("Huawei", "P60 Pro", "+79567890123"),
]

for smartphone in catalog:
    print(
        f"{smartphone.brand} - {smartphone.model}. "
        f"{smartphone.phone_number}"
    )
