import csv


def write_to_csv_list():
    with open('products.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Category", "Name", "Quantity", "Price"])
        writer.writerow([41, "Furnishings", "office Chair", 10, 85])
        writer.writerow([20, "office Supplies", "Pens", 30, 11])
        writer.writerow([33, "words yep", "beds", 1, 111111111])


def write_to_dictionary():
    with open('maintenance-products.csv', 'a') as file:
        headers = ['id', 'category', 'name', 'quantity', 'price']
        writer = csv.DictWriter(file, fieldnames=headers)
        # writer.writeheader()
        item = {'id': 65, 'category': 'maintenance', 'name': 'ladder', 'quantity': 33, 'price': 43}
        writer.writerow(item)


if __name__ == '__main__':
    # write_to_csv_list()
    write_to_dictionary()
