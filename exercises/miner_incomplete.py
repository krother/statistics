
import random
from faker import Faker
from hashlib import sha256


def get_random_transactions(n: int) -> str:
    result = ""
    f = Faker()
    for _ in range(n):
        name1 = f.name()
        name2 = f.name()
        amount = random.randint(1, 10000)
        result += f"{name1} pays {amount} coins to {name2}\n"
    return result


# hashing is at the core of crypto mining
hash = sha256(data.encode()).hexdigest()
print(hash)
