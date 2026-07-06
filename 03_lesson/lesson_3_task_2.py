from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S9+", "+79274567896"),
    Smartphone("Samsung", "A51", "+79375426345"),
    Smartphone("iPhone", "17_Pro", "+79894715295"),
    Smartphone("Infinix", "Hot_30", "+79991597586"),
    Smartphone("Samsung", "A54", "+79873215749"),
]
for smartphone in catalog:
    print(
        f"{smartphone.mark} - {smartphone.model}."
        f"{smartphone.subscriber_number}"
        )
