from collections import Counter


def shoe_shop_profit(sizes: str, number_of_customers: int) -> None:

    sizes_list = [int(x) for x in sizes.split(' ')]  # [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
    collection_stats = Counter(sizes_list)  # {5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1}
    profit = 0

    for i in range(1, number_of_customers + 1):
        customer_input = input(f'Customer {i} (size offer): ').split(' ')
        needed_size = int(customer_input[0])
        offered_price = int(customer_input[1])

        if collection_stats[needed_size]:
            profit += offered_price
            collection_stats[needed_size] -= 1

    print(profit)


if __name__ == '__main__':
    a = int(input('Number of shoes: '))  # integer (нам  не требуется сохранять этот ввод для решения задачи)
    b = input('Sizes of shoes: ')  # space separated integers (with len = a)  - 2 3 4 5 6 8 7 6 5 18
    c = int(input('Number of customers: '))  # integer
    shoe_shop_profit(b, c)

    # shoe_shop_profit(10, '2 3 4 5 6 8 7 6 5 18', 6)

    # Input:
    # 10
    # 2 3 4 5 6 8 7 6 5 18
    # 6
    # 6 55
    # 6 45
    # 6 55
    # 4 40
    # 18 60
    # 10 50

    # Output -> 200
