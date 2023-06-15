
import random
from faker import Faker
from hashlib import sha256


def get_random_transactions(n: int) -> str:
    """"""
    result = ""
    f = Faker()
    for _ in range(n):
        name1 = f.name()
        name2 = f.name()
        amount = random.randint(1, 10000)
        result += f"{name1} pays {amount} coins to {name2}\n"
    return result


def mine(block: str):
    """finds a salt value that validates the previous block"""
    hash = ""
    while not hash.endswith('00000'):
        salt = str(random.random())
        data = block + salt
        hash = sha256(data.encode()).hexdigest()
    print(f"found a new valid hash: {hash}")
    return salt



blockchain = [
    """
    Genesis block - the first block on the blockchain
    """
]

i = 1
while True:
    last_block = blockchain[-1]
    salt = mine(last_block)
    transactions = get_random_transactions(3)
    new_block = f"block #{i}\nsalt: {salt}\n{transactions}"
    print(new_block)
    blockchain.append(new_block)
    i += 1
