data=[
    {
        "name": "Product 1",
        "price": 29.99,
        "category": "Electronics",
        "color": ["Black", "Silver", "White"]
    },
    {
        "name": "Product 2",
        "price": 19.99,
        "category": "Clothing",
        "color": ["Red", "Blue", "Green"]
    },
    {
        "name": "Product 3",
        "price": 9.99,
        "category": "Toys",
        "color": ["Yellow", "Purple"]
    }
]
def find_name():
  return list(map(lambda data:data.get("name"),data))
names=find_name()

def has_color_b(product):
    isB = False
    for color in product.get("color"):
        if color[0] == "B":
           isB = True
           break
    return isB
print(list(filter(has_color_b,data)))


  