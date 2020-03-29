# @author Najee Kitchens
# Description: Parse text file to with telephone information that can be searched by country, region, local exchange, SLID, and extension

telephone_book = []

def add_telephone(number):
    count = 0
    country = ""
    region = ""
    localexchange = ""
    slid = ""
    extension = ""

    for char in number:
        store = ""
        if isdigit(char):
            count += 1
            store += char
        elif not isempty(store):
            if store.size < 3 and count < 3:
                country = store
            elif store.size() == 3 and count < 4:
                region = store
            elif store.size() == 3 and count < 7:
                localexchange = store
            elif store.size() == 4 and count < 11:
                slid = store
    if not isempty(store):
        extension = store

    telephone_book.append({"country": country, "region": region, "local exchange": localexchange, "slid": slid, "extension": extension})


def get_telephone_book():
    # Open file
    f = open("data/code_challenge_data_1.txt", "r")
    # Add telephone numbers to an array
    for number in f.read():
        add_telephone(number)

    return telephone_book