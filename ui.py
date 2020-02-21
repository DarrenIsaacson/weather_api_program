def get_search_information():
    city = input("What city do you live in? Enter Here:")
    state = input("What state do you live in? Enter Here:")
    country = input("What country do you live in? Enter Here:")


    return city, state, country

def display(list):

    for s in list:
        print(s)
