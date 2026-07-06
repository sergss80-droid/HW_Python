from address import Address
from mailing import Mailing

address_from = Address("452000", "Уфа", "Победы", "03", "27")
address_to = Address("123456", "Москва", "Мира", "09", "22")
letter = Mailing(
    to_address=address_to,
    from_address=address_from,
    track="RU123456789RU",
    cost=550
    )
track_info = f"отправление {letter.track} из "
from_info = f"{address_from.formatted()}"
to_info = f" в {address_to.formatted()}. "
cost_info = f"Стоимость {letter.cost} рублей."
print(track_info + from_info + to_info + cost_info)
