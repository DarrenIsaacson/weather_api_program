from pprint import pprint
import setup
import ui
import api_request
import tools


def main():

    key = setup.setup_api()

    city, state, country = ui.get_search_information()

    data = api_request.send_api_request(city, state, country, key)

    list = tools.seperate_needed_data(data)

    ui.display(list)

if __name__ == '__main__':
    main()
