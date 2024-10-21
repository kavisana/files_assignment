from load_json import load_json
from save_books_by_category import save_books_by_category


# Load the JSON data
data = load_json()

if data:
    category_name = input("Enter the book category: ")
    save_books_by_category(data, category_name, f'{category_name}_books.txt')
    print(f"Books in {category_name} category saved to {category_name}_books.txt")
