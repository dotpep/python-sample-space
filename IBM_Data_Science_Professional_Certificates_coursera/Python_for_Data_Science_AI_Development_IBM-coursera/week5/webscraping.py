from bs4 import BeautifulSoup

html = """<!DOCTYPE html><html><head><title>Document</title></head><body><h3><b id="boldest">Players1</b></h3><p>salary: 150.000$</p><h3>Players2</h3><p>salary: 90.000$</p><h3>Players3</h3><p>salary: 115.000$</p></body></html>"""
soup = BeautifulSoup(html, 'html5lib')

# bs4 Object
tag_object = soup.title

# HTML Tree - using tree representation
tag_object2 = soup.h3

# Into child object
tag_child = tag_object2.b

# Parent attribute - Navigate up the tree
parent_tag = tag_child.parent

# Next-sibling attribute - Find sibling tag object (neighbor tag object)
sibling_1 = tag_object2.next_sibling

# find the sibling of sibling one
sibling_2 = sibling_1.next_sibling

# Navigable string - access the attribute name and value as a key value pair in a dictionary
find_attribute_1 = tag_child.attrs

# Return content - as a Navigable string
return_content_str_1 = tag_child.string

return_content_str_1


# Method find-all
# This is a filter - use filters to filter based on a tags name, its attribute, the text of string, or on some combination of these
html = """<table><tr><td>Pizza Place</td><td>Orders</td><td>Slices.3</td></tr><tr><td>Domain Pizza</td><td>10</td><td>100.3</td></tr><tr><td>Little Caesars</td><td>12</td><td>144</td></tr></table>"""
table = BeautifulSoup(html, 'html5lib')

# looks through a tag's descendants and retrieves all f that match your filters.
# result is a Python iterable just like a list
table_row = table.find_all(name='tr')

# each element is a tag object
first_row = table_row[1]

# extract the first table cell
first_td = first_row.td

first_td


# Variable row - iterate through each table cell
table_rows = ""

for i, row in enumerate(table_rows):
    print("row", i)
    cells = row.find_all("td")

    for j, cell in enumerate(cells):
        print("column", j, "cell", cell)


