import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+917659423105")
phone_number2 = phonenumbers.parse("+919873456321")
phone_number3 = phonenumbers.parse("+918756432555")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"));
print(geocoder.description_for_number(phone_number2,"en"));
print(geocoder.description_for_number(phone_number3,"en"));

