from pprint import pprint


cook_book = {}

with open('cook_book.txt', 'rt+', encoding='utf-8') as file:
    for line in file:
        dish = line.strip()
        ingredient_list = []
        quantity_count = file.readline()
        for _ in range(int(quantity_count)):
            emp = file.readline()
            ingredient_name, quantity, measure = emp.strip().split(' | ')
            ingredient_list.append({'ingredient_name': ingredient_name,
                           'quantity': quantity,
                           'measure': measure})
            dep = {dish: ingredient_list}

        blank_line = file.readline()
        cook_book[dish] = ' , '.join(repr(e) for e in ingredient_list)
        cook_book.update()
    # pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for key, value in dish.items():
        if key in dishes:
            for ingredients in value:
                for value in ingredients.values():
                    pass
                quant_ingr = ingredients["quantity_ingredient"] * person_count
                list_products = {}
                list_products["measure"] = value
                list_products["quantity_ingredient"] = quant_ingr
                shop_list[ingredients["name"]] = list_products
    return print(shop_list)
