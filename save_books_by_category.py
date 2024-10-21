def save_books_by_category(data, category_name, output_file):
    with open(output_file, 'w') as file:
        for item in data:
            for adoption in item['adoptions']:
                if adoption['book']['category'].lower() == category_name.lower():
                    file.write(f"Book Title: {adoption['book']['title']}\n")
