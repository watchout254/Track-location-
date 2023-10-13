import phonenumbers
from phonenumbers import geocoder

phone_no1 = phonenumbers.parse('+254123456789')
phone_no2 = phonenumbers.parse('+49123456789')
phone_no3 = phonenumbers.parse('+91123456789')

print("Track the phone numbers\nPhone number locations are: ")
print(geocoder.description_for_number(phone_no1, "en"))
print(geocoder.description_for_number(phone_no2, "en"))
print(geocoder.description_for_number(phone_no3, "en"))
