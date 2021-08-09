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

print("\n == ANCHOR TAGS == \n")

all_anchor_tags = soup.find_all(name="a")

for index in range(len(all_anchor_tags)):
    print(f"({index + 1})")
    print(all_anchor_tags[index])
    print(all_anchor_tags[index].getText())
    print(all_anchor_tags[index].get("href"))