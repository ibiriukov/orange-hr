# utils/test_data_generators.py
import random
import string

def generate_employee_name(first_name="Ej2$1"):
    random_last = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    return first_name, random_last, random_id
