import csv
import psycopg2

# Параметры подключения к базе данных
connection_params = {
    "database": "ibm6_ds_rdb_w2v2",
    "user": "root",
    "password": "123456789",
    "host": "198.51.100.106"
}

# Сопоставление CSV-файлов с таблицами базы данных
csv_files = {
    r"D:\Programming\Python\Data Science - IBM Professional Certificates in coursera\Databases and SQL for Data Science with Python\week2\v2\Departments.csv": "DEPARTMENTS",
    r"D:\Programming\Python\Data Science - IBM Professional Certificates in coursera\Databases and SQL for Data Science with Python\week2\v2\Employees.csv": "EMPLOYEES",
    r"D:\Programming\Python\Data Science - IBM Professional Certificates in coursera\Databases and SQL for Data Science with Python\week2\v2\Jobs.csv": "JOBS",
    r"D:\Programming\Python\Data Science - IBM Professional Certificates in coursera\Databases and SQL for Data Science with Python\week2\v2\Locations.csv": "LOCATIONS",
    r"D:\Programming\Python\Data Science - IBM Professional Certificates in coursera\Databases and SQL for Data Science with Python\week2\v2\JobsHistory.csv": "JOB_HISTORY"
}

# Подключение к базе данных
conn = psycopg2.connect(**connection_params)
cursor = conn.cursor()

# Загрузка данных из CSV-файлов в таблицы
for csv_file, table_name in csv_files.items():
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропустить заголовок
        for row in reader:
            placeholders = ', '.join(['%s'] * len(row))
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(query, row)

# Закрытие соединения с базой данных
conn.commit()
conn.close()

print("Данные успешно загружены в таблицы.")
