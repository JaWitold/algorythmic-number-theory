import random
from sympy import isprime


def generate_random_prime(bits):
    while True:
        p_10 = random.getrandbits(bits)
        if p_10.bit_length() >= bits and isprime(p_10):
            return p_10

def main():
    # (a) generate a random prime number p10 having at least 100 bits in length
    p_10 = generate_random_prime(100)
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    # (b) generate random exponents αi ≥ 15, i = 1, 2, . . . , 9, such that the number
    prime = 1
    while not isprime(prime):
        alphas = [random.randint(15, 20) for _ in range(9)]
        prime = p_10
        for a, b in zip(alphas, bases):
            prime *= pow(b, a)
        prime += 1
    print(f"Prime: {prime}")

    alphas.append(1)
    bases.append(p_10)
    
    # (c) generate ten random numbers gj ∈ {2, 3, . . . , p − 2}, j = 1, 2, . . . , 10,
    g = [random.randint(2, prime-2) for i in range(10)]    
    K = prime - 1
    Q = [int((K // pow(pp, a)) % prime) for a, pp in zip(alphas, bases)]
    gg = [[pow(G, q, prime) for q in Q] for G in g]

    # (d) for each j = 1, 2, . . . , 10 calculate ord_gj in F*p
    for i, G in enumerate(gg):
        betas = [0 for _ in g]
        order = 1
        for j, _ in enumerate(G):
            while gg[i][j] != 1:
                gg[i][j] = pow(gg[i][j], bases[j], prime)
                betas[j] += 1
        
        # calculate the order
        for pp, b in zip(bases, betas):
            order = (order * pow(pp, b, prime)) % prime
        print(f"order {order}")

        # (e) make sure that the results ordgj are correct by implementing tests.
        assert pow(g[i], order, prime) == 1, "Test failed for i = {i}"


if __name__ == "__main__":
    main()
    print("Finnished without asserts")
