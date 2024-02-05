import re

"""
- домашній номер телефону (тільки цифри та довжина номера)
"""
home_phone = ['123456', '1234', '1234567', '+12345']

for number in home_phone:
    if re.match(r'^\d{6}$', number):
        print(f'Phone number {number} is correct.')
    else:
        print(f'Phone number {number} is not correct.')
"""
- Мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
"""
mobile_numbers = ["+380683830544", "380683830544", "+3806838305444", "+38068383054", '++380683830544']
for number in mobile_numbers:
    if re.match(r"^\+?\d{12}$", number):
        print(f'Mobile number: {number} is correct.')
    else:
        print(f'Mobile number: {number} is not correct.')
"""
- email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
"""
emails = ['test@gmail.com', 'test_1@gmail.com', 'test_2@gmail', 'test_gmail', 'test_4@']
for email in emails:
    if re.match("^[0-9a-zA-Z]+[./+_-]{0,1}[0-9a-zA-Z]+[@][a-zA-Z0-9]+[.][a-zA-Z]{2,}$", email):
        print(f'Email: {email} is correct.')
    else:
        print(f'Email: {email} is not correct.')
"""
- ПІБ клієнта (3 слова, мінімальна довжина 2 символи, максимальна довжина 20)
"""
users = ['Vasya Vasya Vasya', 'vasya vasya vasya', 'vasya1 vasya vasya', 'vasya_vasya vasya', 'vasya vasya vasya vasya']
for user in users:
    if re.match(
            r"^[A-ZA-ЯЁЇІЄҐ][a-za-яёїієґ]{1,19}\s[A-ZA-ЯЁЇІЄҐ][a-za-яёїієґ]{1,19}\s[A-ZA-ЯЁЇІЄҐ][a-za-яёїієґ]{1,19}$",
            user):
        print(f'User: {user} is correct.')
    else:
        print(f'User: {user} is not correct.')
"""
- Пароль (мінімально: одна велика літера, одна маленька літера, одна цифра, один символ, довжина пароля – від 8 до 16 символів)
"""
passwords = ['Admin123!', 'admin123!', 'Admin123', 'Admin!', 'admin']

for password in passwords:
    if re.match(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!*@#$%^&+=]).*$", password):
        print(f"{password} is correct.")
    else:
        print(f"{password} is not correct.")
