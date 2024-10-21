import csv

def save_adoptions_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['adoption_id', 'adoption_date', 'quantity', 'book_title', 'book_category'])

        for item in data:
            for adoption in item['adoptions']:
                writer.writerow([adoption['id'], adoption['date'], adoption['quantity'], adoption['book']['title'], adoption['book']['category']])
