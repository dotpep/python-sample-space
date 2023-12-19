from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


# Beautiful Soup Object
html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, 'html.parser')

# method prettify - to display the HTML in the nested structure
soup.prettify()


# Tags
tag_object = soup.title
print("tag object: ",tag_object)
print("tag object type: ",type(tag_object))

tag_object=soup.h3
print(tag_object)


# Children, Parents, and Siblings
tag_child = tag_object.b
print("tag object children: ", tag_child)

parent_tag = tag_child.parent
print("tag object children parents: ", parent_tag)

sibling_1 = tag_object.next_sibling
print("tag object sibling or neighbor: ", sibling_1)

sibling_2 = sibling_1.next_sibling
print("tag object siblings of siblings: ", sibling_2)


# HTML Attributes
# access a tag's attributes by treating the tag like a dictionary
print("tag attributes of tag object child variable: ", tag_child['id'])
print("tag dictionary attributes of tag_child: ", tag_child.attrs)


# Navigable String
tag_string = tag_child.string
print("tag string of tag_child: ", tag_string)
print("tag string type: ", type(tag_string))

unicode_string = str(tag_string)
print("tag string unicode convert: ", unicode_string)


# Filter
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")



print(r"\\", "\n\n")

# find all
"""
The find_all() method looks through a tag’s descendants and retrieves all descendants that match your filters.

The Method signature for find_all(name, attrs, recursive, string, limit, **kwargs)
"""
# Name
table_rows = table_bs.find_all('tr')
first_row = table_rows[0]
print(type(first_row))
print(first_row.td)

# iterate each element of list
for i, row in enumerate(table_rows):
    print("row", i, "is", row)

# extract table cells object cells using td and find_all method
for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all('td')
    for j, cell in enumerate(cells):
        print("column", j, "cell", cell)


list_input = table_bs.find_all(name=["tr", "td"])
print("\n", list_input)



print(r"\\", "\n\n")

# Attributes
print("find all attributes id='flight': ", table_bs.find_all(id="flight"))

list_input = table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print("find all href: ", list_input)
print("find all href boolean True: ",table_bs.find_all(href=True))

table_bs.find_all("a")
table_bs.find_all(href=False)
soup.find_all(id="boldest")

# string
table_bs.find_all(string="Florida")



print(r"\\", "\n\n")

# Find
"""
The find_all() method scans the entire document looking for results, it’s if you are looking for one element you can use the find() method to find the first element in the document. Consider the following two table:
"""

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_tables_bs = BeautifulSoup(two_tables, "html.parser")

two_tables_bs.find("table")
print(two_tables_bs.find("table",class_='pizza'))


