def clean_sale(val):
    valid_values = []
    for number in val:
        if number is not None and number > 0:
            valid_values.append(number)
    return valid_values


list_n = [1000,None,0,-1,1000,1000,4000,5000]
clean = clean_sale(list_n)
print(clean)


def remove_duplicates(val2):
    return set(val2)

unique_sales = remove_duplicates(clean)
print(unique_sales)

def analyze_sales(val3):
    return  {'average': sum(val3) / len(val3),'max_sale': max(val3),'min_sale': min(val3)}

relator = analyze_sales(unique_sales)
for key, value in relator.items():
  print(f'{key} : {value}')