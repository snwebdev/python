def primeGenerator(max):
    primeList = [2]
    candidate = 3
    while candidate < max:
        for prime in primeList:
            if candidate % prime == 0:
                candidate += 1
                break
            elif prime == primeList[-1]:
                primeList.append(candidate)
                candidate += 1
                break
    return primeList
