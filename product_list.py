def work_on_product_list(product_list):

    new_product_list = dict()
    new_product_list['products'] = product_list['products']
    new_product_list['total_price'] = 0
    price = 'price'
    cost = 'net_cost'

    for index in range(len(new_product_list['products'])):
        new_product_list['products'][index][price] = new_product_list['products'][index].pop(cost)
        new_product_list['products'][index][price] *= (product_list['margin'] + 1) * (product_list['tax'] + 1)
        new_product_list['total_price'] += new_product_list['products'][index][price]

    print(new_product_list)
