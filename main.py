from pprint import pprint

def dict_collector(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        menu = {}
        for line in f:
            dish_name = line[:-1]
            counter = f.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                ingridient = f.readline().strip().split(' | ')
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            f.readline()

    return(menu)

dict_collector('reciepts_initial.txt')

def get_shop_list_by_dishes(dishes, persons=int):
    '''
    {
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 4},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
    '''
    menu = dict_collector('reciepts_initial.txt')
    print('Наше меню выглядит вот так:')
    pprint(menu)
    print()
    shopping_list = {}
    pprint(menu.keys())
    try:
        for dish in dishes:
            for item in (menu[dish]):
                print(item['ingredient_name'])
                print(item['measure'])
                print(item['quantity'])
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    print(f' Такое {items_list} уже есть в списке. Добавил еще')
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    print(extra_item)
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    shopping_list[item['ingredient_name']]['quantity'] *= persons
                    shopping_list.update(items_list)

        print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")


get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10)