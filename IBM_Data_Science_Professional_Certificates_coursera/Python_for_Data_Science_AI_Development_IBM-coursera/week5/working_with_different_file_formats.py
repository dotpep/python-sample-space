# Data Engineering
"""
Is one of the most critical and foundational skills in any data scientist’s toolkit.

Data Engineering Process
There are several steps in Data Engineering process.

Extract - Data extraction is getting data from multiple sources. Ex. Data extraction from a website using Web scraping or gathering information from the data that are stored in different formats(JSON, CSV, XLSX etc.).

Transform - Tarnsforming the data means removing the data that we don't need for further analysis and converting the data in the format that all the data from the multiple sources is in the same format.

Load - Loading the data inside a data warehouse. Data warehouse essentially contains large volumes of data that are accessed to gather insights.
"""
# Working with different file formats (csv, xml, json, xlsx)
"""
In the real-world, people rarely get neat tabular data. Thus, it is mandatory for any data scientist (or data engineer) to be aware of different file formats, common challenges in handling them and the best, most efficient ways to handle this data in real life. We have reviewed some of this content in other modules.

File Format
A file format is a standard way in which information is encoded for storage in a file. First, the file format specifies whether the file is a binary or ASCII file. Second, it shows how the information is organized. For example, the comma-separated values (CSV) file format stores tabular data in plain text.

To identify a file format, you can usually look at the file extension to get an idea. For example, a file saved with name “Data” in “CSV” format will appear as “Data.csv”. By noticing the “.csv” extension, we can clearly identify that it is a “CSV” file and the data is stored in a tabular format.

There are various formats for a dataset, .csv, .json, .xlsx etc. The dataset can be stored in different places, on your local machine or sometimes online.

In this section, you will learn how to load a dataset into our Jupyter Notebook.

Now, we will look at some file formats and how to read them in Python:

Comma-separated values (CSV) file format
The Comma-separated values file format falls under a spreadsheet file format.

In a spreadsheet file format, data is stored in cells. Each cell is organized in rows and columns. A column in the spreadsheet file can have different types. For example, a column can be of string type, a date type, or an integer type.

Each line in CSV file represents an observation, or commonly called a record. Each record may contain one or more fields which are separated by a comma.
"""
# Reading data from CSV in Python
"""
The Pandas Library is a useful tool that enables us to read various datasets into a Pandas data frame

Let us look at how to read a CSV file in Pandas Library.

We use pandas.read_csv() function to read the csv file. In the parentheses, we put the file path along with a quotation mark as an argument, so that pandas will read the file into a data frame from that address. The file path can be either a URL or your local file address.
"""



# import piplite
# await piplite.install(['seaborn', 'lxml', 'openpyxl'])
# import pandas as pd
# from pyodide.http import pyfetch
#
#
# filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"
#
# async def download(url, filename):
#     response = await pyfetch(url)
#     if response.status == 200:
#         with open(filename, "wb") as f:
#             f.write(await response.bytes())
#
# await download(filename, "addresses.csv")
#
# df = pd.read_csv("addresses.csv", header=None)
# df
#
# df.columns = ["First Name", "Last Name", "Location", "City", "State", "Area Code"]
# df
#
# df["First Name"]
#
# df = df[["First Name", "Last Name", "Location", "City", "State", "Area Code"]]
#
# # to select the first row
# df.loc[0]
#
# # to select the 0th, 1st and 2nd row of "First Name" column only
# df.loc[[0, 1, 2], "First Name"]
#
# # to select the 0th,1st and 2nd row of "First Name" column only
# df.iloc[[0,1,2], 0]
#



# Transform Function in Pandas
"""
Python’s Transform function returns a self-produced dataframe with transformed values after applying the function specified in its parameter.

Let's see how Transform function works.
"""
import pandas as pd
import numpy as np

# creating a dataframe
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

df = df.transform(func=lambda x: x + 10)

result = df.transform(func=['sqrt'])
result




# JSON file Format
"""
JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write.

JSON is built on two structures:

A collection of name/value pairs. In various languages, this is realized as an object, record, struct, dictionary, hash table, keyed list, or associative array.

An ordered list of values. In most languages, this is realized as an array, vector, list, or sequence.

JSON is a language-independent data format. It was derived from JavaScript, but many modern programming languages include code to generate and parse JSON-format data. It is a very common data format with a diverse range of applications.

The text in JSON is done through quoted string which contains the values in key-value mappings within { }. It is similar to the dictionary in Python.

Python supports JSON through a built-in package called json. To use this feature, we import the json package in Python script.
import json
"""

# Writing JSON to a File
"""
This is usually called serialization. It is the process of converting an object into a special format which is suitable for transmitting over the network or storing in file or database.

To handle the data flow in a file, the JSON library in Python uses the dump() or dumps() function to convert the Python objects into their respective JSON object. This makes it easy to write data to files.
"""
import json
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}
"""
serialization using dump() function
json.dump() method can be used for writing to JSON file.

Syntax: json.dump(dict, file_pointer)

Parameters:

dictionary – name of the dictionary which should be converted to JSON object.
file pointer – pointer of the file opened in write or append mode.
"""
with open('person.json', 'w') as f: # writing json object
    json.dump(person, f)

"""
serialization using dumps() function
json.dumps() that helps in converting a dictionary to a JSON object.

It takes two parameters:

dictionary – name of the dictionary which should be converted to JSON object.
indent – defines the number of units for indentation
"""
# serializing json
json_object = json.dumps(person, json_object = indent = 4)

# writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

