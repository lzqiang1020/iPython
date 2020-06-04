def cal(goodsPriceA, goodsPriceB, actualAmount):
    allAmount = goodsPriceA + goodsPriceB
    discountRate = actualAmount / allAmount
    print(discountRate)
    return (round(goodsPriceA*discountRate, 2), round(goodsPriceB*discountRate, 2))

def main():
    a, b = cal(10, 20, 25)
    print(a, b)

if __name__ == '__main__':
    main()


