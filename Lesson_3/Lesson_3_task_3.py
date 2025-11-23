from address import Address
from mailing import Mailing
from_addr = Address("101000", "Москва", "Тверская", "10", "5")
to_addr = Address("191025", "Санкт-Петербург", "Невский проспект", "25", "12")
mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=250,
    track="RU1234567890"
)
mailing.print_info()