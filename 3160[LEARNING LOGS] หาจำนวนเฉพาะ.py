"""[LEARNING LOGS] หาจำนวนเฉพาะ"""
def main():
    """ksjiufhwe"""
    start, end = map(int, input().split())
    prime = []

    prime_num = 0

    for i in range(start, end+1):

        if not i % 2 or not i % 3 or not i % 5 or not i % 7:
            if i == 2:
                prime.append(i)
                prime_num += 1
            if i == 3:
                prime.append(i)
                prime_num += 1
            if i == 5:
                prime.append(i)
                prime_num += 1
            if i == 7:
                prime.append(i)
                prime_num += 1
            else:
                prime_num += 0
        elif i == 1:
            pass
        else:
            prime.append(i)
            prime_num += 1

    if len(prime) > 0:
        print(*prime)
    print(f"Total primes: {prime_num}")
main()
