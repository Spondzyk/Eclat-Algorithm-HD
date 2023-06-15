import os

import pandas as pd
import plotly.express as px
from pyECLAT import ECLAT


def transform_data_to_algorithm(df, name_of_column):
    transactions = {}
    for _, row in df.iterrows():
        transaction_id = row['Transaction ID']
        product_name = row[name_of_column]

        if transaction_id not in transactions:
            transactions[transaction_id] = []

        transactions[transaction_id].append(product_name)
    return transactions


def eclat_algorithm_product_name(df, min_support, min_combination, max_combination):
    folder_name = "name"
    df_bin_file = os.path.join(folder_name, 'df_bin_product_name.csv')
    items_per_transaction_file = os.path.join(folder_name, 'items_per_transaction_product_name.csv')
    result_file = os.path.join(folder_name, 'result_product_name.csv')

    eclat = ECLAT(data=pd.DataFrame(list(transform_data_to_algorithm(df, 'Product Name').values())))
    eclat.df_bin.to_csv(df_bin_file, index=False)  # Save eclat.df_bin to CSV file

    items_total = eclat.df_bin.astype(int).sum(axis=0)
    items_per_transaction = eclat.df_bin.astype(int).sum(axis=1)
    items_per_transaction.to_csv(items_per_transaction_file, index=False)  # Save items_per_transaction to CSV file

    df_items = pd.DataFrame({'items': items_total.index, 'transactions': items_total.values})
    df_table = df_items.sort_values("transactions", ascending=False)

    fig = px.bar(df_table.head(20), x='items', y='transactions', hover_data=['items'])
    fig.show()

    rule_indices, rule_supports = eclat.fit(min_support=min_support,
                                            min_combination=min_combination,
                                            max_combination=max_combination,
                                            separator=' & ',
                                            verbose=True)

    result = pd.DataFrame(rule_supports.items(), columns=['Item Name', 'Support'])
    result = result.sort_values(by=['Support'], ascending=False)
    result.to_csv(result_file, index=False)
    print(result.head(10))


def eclat_algorithm_subcategory_name(df, min_support, min_combination, max_combination):
    folder_name = "subcategory"
    df_bin_file = os.path.join(folder_name, 'df_bin_subcategory_name.csv')
    items_per_transaction_file = os.path.join(folder_name, 'items_per_transaction_subcategory_name.csv')
    result_file = os.path.join(folder_name, 'result_subcategory_name.csv')

    eclat = ECLAT(data=pd.DataFrame(list(transform_data_to_algorithm(df, 'Subcategory Name').values())))
    eclat.df_bin.to_csv(df_bin_file, index=False)  # Save eclat.df_bin to CSV file

    items_total = eclat.df_bin.astype(int).sum(axis=0)
    items_per_transaction = eclat.df_bin.astype(int).sum(axis=1)
    items_per_transaction.to_csv(items_per_transaction_file, index=False)  # Save items_per_transaction to CSV file

    df_items = pd.DataFrame({'items': items_total.index, 'transactions': items_total.values})
    df_table = df_items.sort_values("transactions", ascending=False)

    fig = px.bar(df_table.head(20), x='items', y='transactions', hover_data=['items'])
    fig.show()

    rule_indices, rule_supports = eclat.fit(min_support=min_support,
                                            min_combination=min_combination,
                                            max_combination=max_combination,
                                            separator=' & ',
                                            verbose=True)

    result = pd.DataFrame(rule_supports.items(), columns=['Subcategory Name', 'Support'])
    result = result.sort_values(by=['Support'], ascending=False)
    result.to_csv(result_file, index=False)
    print(result.head(10))


def eclat_algorithm_category_name(df, min_support, min_combination, max_combination):
    folder_name = "category"
    df_bin_file = os.path.join(folder_name, 'df_bin_category_name.csv')
    items_per_transaction_file = os.path.join(folder_name, 'items_per_transaction_category_name.csv')
    result_file = os.path.join(folder_name, 'result_category_name.csv')

    eclat = ECLAT(data=pd.DataFrame(list(transform_data_to_algorithm(df, 'Category Name').values())))
    eclat.df_bin.to_csv(df_bin_file, index=False)  # Save eclat.df_bin to CSV file

    items_total = eclat.df_bin.astype(int).sum(axis=0)
    items_per_transaction = eclat.df_bin.astype(int).sum(axis=1)
    items_per_transaction.to_csv(items_per_transaction_file, index=False)  # Save items_per_transaction to CSV file

    df_items = pd.DataFrame({'items': items_total.index, 'transactions': items_total.values})
    df_table = df_items.sort_values("transactions", ascending=False)

    fig = px.bar(df_table.head(20), x='items', y='transactions', hover_data=['items'])
    fig.show()

    rule_indices, rule_supports = eclat.fit(min_support=min_support,
                                            min_combination=min_combination,
                                            max_combination=max_combination,
                                            separator=' & ',
                                            verbose=True)

    result = pd.DataFrame(rule_supports.items(), columns=['Category Name', 'Support'])
    result = result.sort_values(by=['Support'], ascending=False)
    result.to_csv(result_file, index=False)
    print(result.head(10))
