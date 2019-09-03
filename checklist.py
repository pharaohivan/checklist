

checklist = list()

def create(item):
    checklist.append('Blue')

print(checklist)
checklist.append('Orange')
print(checklist)

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

def test():

test()
