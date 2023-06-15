import pandas as pd
from scipy.stats import mode


def calculate_product_statistics(filename):
    df = pd.read_csv(filename)
    product_counts = df['Product Name'].value_counts()

    max_count = product_counts.max()
    min_count = product_counts.min()
    mean_count = product_counts.mean()
    median_count = product_counts.median()
    mode_count = mode(product_counts)

    return max_count, min_count, mean_count, median_count, mode_count


def calculate_subcategory_statistics(filename):
    df = pd.read_csv(filename)
    subcategory_counts = df['Subcategory Name'].value_counts()

    max_count = subcategory_counts.max()
    min_count = subcategory_counts.min()
    mean_count = subcategory_counts.mean()
    median_count = subcategory_counts.median()
    mode_count = mode(subcategory_counts)

    return max_count, min_count, mean_count, median_count, mode_count


def calculate_category_statistics(filename):
    df = pd.read_csv(filename)
    category_counts = df['Category Name'].value_counts()

    max_count = category_counts.max()
    min_count = category_counts.min()
    mean_count = category_counts.mean()
    median_count = category_counts.median()
    mode_count = mode(category_counts)

    return max_count, min_count, mean_count, median_count, mode_count
