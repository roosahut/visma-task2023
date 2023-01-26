from identify_request import IdentifyRequest


def main():
    """ The main loop so the user can test the identifying class
      with the terminal.
    """
    while True:
        print()
        print('Give an URI to test the Identifying Class')
        uri = input('URI: ')
        try:
            identify = IdentifyRequest(uri)
            print()
            print('Identifying the request was successful.')
            print('Identified request:')
            print(identify)
        except Exception as e:
            print()
            print('Not a valid URI.')
            print(f'Error message: {e}')


main()
