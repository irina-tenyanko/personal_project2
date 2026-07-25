# творіть функцію "validate_email(email)
#Функція повинна повертати кортеж з двох значень:
#- True або False
#- текст повідомлення


def validate_email(email):

    if "@" not in email:
        return False, "Email ає містити @"
    if "." not in email:
        return False, "Email має містити крапку"
    return True, ""

def validate_phone(phone):
    if not phone:
        return False, "Телефон не має бути порожнім"
    if phone[0] == "+":
        digits = phone[1:]
    else:
        digits = phone
    if not digits.isdigit():
        return False, "Телефон має містити лише цифри та знак + на початку"
    if len(digits) !=12:
        return False, "Тулефон має містити 12 цифр"
    return True, ""