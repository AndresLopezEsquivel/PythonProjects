from bs4 import BeautifulSoup

WEBSITE_PATH_FILE = "./website.html"

with open(WEBSITE_PATH_FILE) as website_file:
    website_content = website_file.read()

# print(website_content)

soup = BeautifulSoup(website_content, "html.parser")

# Showing the soup's content

print(f"Soup's content: {soup.prettify()}")

# Printing website's title

print(f"Website's title tag and content: {soup.title}")

print(f"Website's title content: {soup.title.string}")

# Using  find_all() function

print("\n == ANCHOR TAGS ==")

all_anchor_tags = soup.find_all(name="a")

for index in range(len(all_anchor_tags)):
    print(f"({index + 1})")
    print(all_anchor_tags[index])
    print(all_anchor_tags[index].getText())
    print(all_anchor_tags[index].get("href"))

# Using find() function

heading_with_id = soup.find(name="h1", id="name")

print("\n == GETTING HEADING THROUGH ITS ID ==")

print(heading_with_id)

print(f"Heading's text: {heading_with_id.getText()}")

print("\n == GETTING HEADING THROUGH ITS CLASS ==")

heading_with_class = soup.find(name="h3", class_="heading")

print(heading_with_class)

print(heading_with_class.name)

print(heading_with_class.getText())

print(heading_with_class.get("class"))

# Using select_one() function

print("\n == USING select_one() FUNCTION ==")

first_anchor_tag = soup.select_one(selector="p a")

print(first_anchor_tag)

# Using select() function

print("\n == USING select() FUNCTION ==")

elements_with_heading_class = soup.select(selector=".heading")

print(elements_with_heading_class)