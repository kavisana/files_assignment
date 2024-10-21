import csv

def save_universities_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['university_id', 'university_name', 'city', 'state'])

        for item in data:
            university = item['university']
            writer.writerow([university['id'], university['name'], university['city'], university['state']])
