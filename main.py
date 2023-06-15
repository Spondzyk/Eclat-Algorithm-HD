import pandas as pd
import timeit
from eclat import eclat_algorithm_product_name, eclat_algorithm_subcategory_name, eclat_algorithm_category_name
from statistics import calculate_product_statistics, calculate_subcategory_statistics, calculate_category_statistics


def read_transactions_csv(filename):
    df = pd.read_csv(filename)
    return df


def product_name_main(min_support, min_combination, csv_name, df):
    product_stats = calculate_product_statistics(csv_name)
    print("Statystyki wystąpienia nazw produktów:")
    print(f"Maksymalna ilość wystąpień: {product_stats[0]}")
    print(f"Minimalna ilość wystąpień: {product_stats[1]}")
    print(f"Średnia ilość wystąpień: {product_stats[2]}")
    print(f"Mediana ilości wystąpień: {product_stats[3]}")
    print(f"Moda ilości wystąpień: {product_stats[4]}")
    eclat_algorithm_product_name(df, min_support, min_combination)


def product_subcategory_main(min_support, min_combination, csv_name, df):
    subcategory_stats = calculate_subcategory_statistics(csv_name)
    print("Statystyki wystąpienia podkategorii produktów:")
    print(f"Maksymalna ilość wystąpień: {subcategory_stats[0]}")
    print(f"Minimalna ilość wystąpień: {subcategory_stats[1]}")
    print(f"Średnia ilość wystąpień: {subcategory_stats[2]}")
    print(f"Mediana ilości wystąpień: {subcategory_stats[3]}")
    print(f"Moda ilości wystąpień: {subcategory_stats[4]}")
    eclat_algorithm_subcategory_name(df, min_support, min_combination)


def product_category_main(min_support, min_combination, csv_name, df):
    category_stats = calculate_category_statistics(csv_name)
    print("Statystyki wystąpienia kategorii produktów:")
    print(f"Maksymalna ilość wystąpień: {category_stats[0]}")
    print(f"Minimalna ilość wystąpień: {category_stats[1]}")
    print(f"Średnia ilość wystąpień: {category_stats[2]}")
    print(f"Mediana ilości wystąpień: {category_stats[3]}")
    print(f"Moda ilości wystąpień: {category_stats[4]}")
    eclat_algorithm_category_name(df, min_support, min_combination)


if __name__ == '__main__':
    csv_name = 'transactions.csv'
    df = read_transactions_csv(csv_name)

    min_support = 1 / 100
    min_combination = 2

    execution_time = timeit.timeit(lambda: product_name_main(min_support, min_combination, csv_name, df), number=1)
    print(f"Czas wykonania: {execution_time} sekundy")

    # execution_time = timeit.timeit(lambda: product_subcategory_main(min_support, min_combination, csv_name, df), number=1)
    # print(f"Czas wykonania: {execution_time} sekundy")
    #
    # execution_time = timeit.timeit(lambda: product_category_main(min_support, min_combination, csv_name, df),
    #                                number=1)
    # print(f"Czas wykonania: {execution_time} sekundy")

