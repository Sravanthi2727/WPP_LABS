shop = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
top_items = sorted(shop.items(), key=lambda x: x[1], reverse=True)[:3]
for item in top_items:
    print(item[0], item[1])