import csv
from Levenshtein import ratio

def find_most_similar_product(product, products):
    most_similar_product = None
    max_similarity = 0

    for other_product in products:
        similarity = ratio(product, other_product)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_product = other_product
    
    return most_similar_product, max_similarity

def compare_products(gearvn_products, phucanh_products,fpt_products):
    comparison_results = []

    for phucanh_product in phucanh_products:
        fpt_product, fpt_similarity = find_most_similar_product(phucanh_product, fpt_products)
        gearvn_product, gearvn_similarity = find_most_similar_product(phucanh_product, gearvn_products)
        # phucanh_product, phucanh_similarity = find_most_similar_product(fpt_product, phucanh_products)
        comparison_results.append([phucanh_product, gearvn_product, fpt_product, gearvn_similarity, fpt_similarity])
    
    return comparison_results

def write_comparison_results(comparison_results, output_filename):
    with open(output_filename, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(['Phucanh product', 'Gearvn product', 'Fpt product', 'Gearvn similarity', 'Fpt similarity'])
        writer.writerows(comparison_results)

def read_products(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        return [row[0] for row in reader]

# Define filenames
fpt_filename = './../validated_result/Fpt_validated.csv'
gearvn_filename = './../validated_result/Gearvn_validated.csv'
phucanh_filename = './../validated_result/Phucanh_validated.csv'
output_filename = './../compare_result/Fpt_compare.csv'

# Read products from CSV files
fpt_products = read_products(fpt_filename)
gearvn_products = read_products(gearvn_filename)
phucanh_products = read_products(phucanh_filename)

# Compare products
comparison_results = compare_products( gearvn_products, phucanh_products, fpt_products)

# Write comparison results to CSV
write_comparison_results(comparison_results, output_filename)

print("Comparison completed and results saved to Fpt_compare.csv")
