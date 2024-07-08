import os
import csv
import Levenshtein

def extract_product_names(csv_files):
    product_names = []
    for csv_file in csv_files:
        with open(csv_file, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product_names.append(row['Product'])
    return product_names

if __name__ == "__main__":
    result_folder = "result"
    csv_files = [
        os.path.join(result_folder, "gear_result.csv"),
        os.path.join(result_folder, "fpt_result.csv"),
        os.path.join(result_folder, "phucanh_result.csv")
    ]

    product_names = extract_product_names(csv_files)

    # Store product names in variables product_1, product_2, product_3
    product_1, product_2, product_3 = product_names

    # Compare similarity between product names
    similarity_1_2 = Levenshtein.ratio(product_1, product_2)
    similarity_2_3 = Levenshtein.ratio(product_2, product_3)
    similarity_3_1 = Levenshtein.ratio(product_3, product_1)

    # Print similarity scores
    # print(f"{similarity_1_2:.2f}")
    # print(f"{similarity_2_3:.2f}")
    print(f"{similarity_3_1:.2f}")

    print(product_1)
    print(product_2)
    print(product_3)