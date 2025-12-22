# find total number of phone number in text
import re
text = "Contact us at 1234567890 or 9876543210 for more information"
phone_number=re.findall(r"\d{10}",text)
print(f"phone number is:{phone_number}")
print(f"total fhone number found : {len(phone_number)}")