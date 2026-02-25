data = []

def create(item):
    data.append(item)

def read():
    return data

def update(index, new_item):
    data[index] = new_item

def delete(index):
    data.pop(index)

create("temp 35")
create("humidity 40")
print("After create:", read())

update(0, "temp 36")
print("After update:", read())

delete(1)
print("After delete:", read())