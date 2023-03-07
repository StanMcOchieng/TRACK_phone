import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+254712645980")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"));
