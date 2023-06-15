import pyodbc
import pandas as pd


def get_transaction_product_data():
    # Konfiguracja połączenia z bazą danych
    server = 'HURTOWNIE'
    database = 'AdventureWorks2019'

    # Nawiązanie połączenia z bazą danych
    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;')

    # Utworzenie kursora
    cursor = conn.cursor()

    # Przygotowanie zapytania SQL
    query = """
            SELECT s.SalesOrderID, p.Name, pc.Name AS Category, psc.Name AS Subcategory
            FROM Sales.SalesOrderDetail s
            INNER JOIN Production.Product p ON s.ProductID = p.ProductID
            INNER JOIN Production.ProductSubcategory psc ON p.ProductSubcategoryID = psc.ProductSubcategoryID
            INNER JOIN Production.ProductCategory pc ON psc.ProductCategoryID = pc.ProductCategoryID
            """

    # Wykonanie zapytania SQL
    cursor.execute(query)

    # Pobranie wyników zapytania
    results = cursor.fetchall()

    # Tworzenie słownika transakcji
    transactions = {}

    # Przetwarzanie wyników i tworzenie słownika transakcji
    for row in results:
        transaction_id = row.SalesOrderID
        product_name = row.Name
        category_name = row.Category
        subcategory_name = row.Subcategory

        if transaction_id not in transactions:
            transactions[transaction_id] = []

        transactions[transaction_id].append([product_name, subcategory_name, category_name])

    # Zamykanie kursora i połączenia z bazą danych
    cursor.close()
    conn.close()

    return transactions


def convert_transactions_to_dataframe(transactions):
    data = []

    for transaction_id, transaction_data in transactions.items():
        for item_data in transaction_data:
            product_name = item_data[0]
            subcategory_name = item_data[1]
            category_name = item_data[2]
            data.append([transaction_id, product_name, subcategory_name, category_name])

    df = pd.DataFrame(data, columns=['Transaction ID', 'Product Name', 'Subcategory Name', 'Category Name'])
    return df


def export_dataframe_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"DataFrame został wyeksportowany do pliku {filename}.")


if __name__ == '__main__':
    transactions = get_transaction_product_data()
    df = convert_transactions_to_dataframe(transactions)
    export_dataframe_to_csv(df, 'transactions.csv')
