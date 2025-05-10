import math
import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(bits=8):
    while True:
        p = random.getrandbits(bits)
        if p % 4 == 3 and is_prime(p):
            return p

class BlumBlumShub:
    def __init__(self, bits=8):
        self.p = generate_prime(bits)
        self.q = generate_prime(bits)
        self.n = self.p * self.q

        while True:
            seed = random.randint(2, self.n - 1)
            if math.gcd(seed, self.n) == 1:
                self.state = seed
                break

    def next_bit(self):
        self.state = pow(self.state, 2, self.n)
        return self.state & 1

    def next_bits(self, k):
        bits = 0
        for _ in range(k):
            bits = (bits << 1) | self.next_bit()
        return bits

    def randbelow(self, upper):
        while True:
            val = self.next_bits(16)  # 16 бит
            if val < (1 << 16) - ((1 << 16) % upper):
                return val % upper

# Перемешиваем список [0..5] с помощью BBS
def bbs_shuffle_v6():
    bbs = BlumBlumShub()
    items = list(range(6))
    for i in range(len(items) - 1, 0, -1):
        j = bbs.randbelow(i + 1)
        items[i], items[j] = items[j], items[i]
    return items

