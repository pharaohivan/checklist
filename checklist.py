

checklist = list()

def create(item):
    checklist.append('Blue')

# READ
def read(index):
    item = checklist[index]
    return item
# UPDATE
def update(index, item):
    checklist[index] = item

    # DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    # Add code here that marks an item as completed
    checklist[index] = ("√" + item)

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    #print(read(1))

test()
