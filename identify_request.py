from urllib.parse import urlparse, parse_qsl


class IdentifyRequest:
    def __init__(self, uri: str):
        self.uri = uri
        self._parse_uri()

    def _parse_uri(self):
        """Parses the given uri with urllib library functions.
        """
        parsed_uri = urlparse(self.uri)

        self.scheme = parsed_uri.scheme
        self.path = parsed_uri.netloc
        self.parameters = dict(parse_qsl(parsed_uri.query))

    @property
    def scheme(self):
        return self._scheme

    @scheme.setter
    def scheme(self, value: str):
        if value != 'visma-identity':
            raise ValueError('Incorrect scheme.')
        self._scheme = value

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value: str):
        if value not in ['login', 'confirm', 'sign']:
            raise ValueError('Incorrect path.')
        self._path = value

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, value: dict):
        # Confirming source is valid here because it's in every path.
        if 'source' not in value.keys():
            raise KeyError('No source.')
        if not isinstance(value['source'], str):
            raise TypeError('Source type should be a string.')

        if self.path == 'login':
            self._validate_login_parameters(value)

        elif self.path == 'confirm':
            self._validate_confirm_parameters(value)
            # Changing the payment number to int (was str before).
            value['paymentnumber'] = int(value['paymentnumber'])

        elif self.path == 'sign':
            self._validate_sign_parameters(value)

        self._parameters = value

    def _validate_login_parameters(self, parameters: dict):
        ''' Validates the parameters when the path is login.
        '''
        if len(parameters) > 1 or len(parameters) <= 0:
            raise ValueError('Incorrect amount of parameters for login.')

    def _validate_confirm_parameters(self, parameters: dict):
        ''' Validates the parameters when the path is confirm.
        '''
        if len(parameters) > 2 or len(parameters) <= 1:
            raise ValueError('Incorrect amount of parameters for confirm.')
        if 'paymentnumber' not in parameters.keys():
            raise KeyError('No payment number.')
        if not parameters['paymentnumber'].isdigit():
            raise TypeError('Payment number should be an integer.')

    def _validate_sign_parameters(self, parameters: dict):
        ''' Validates the parameters when the path is sign.
        '''
        if len(parameters) > 2 or len(parameters) <= 1:
            raise ValueError('Incorrect amount of parameters for sign.')
        if 'documentid' not in parameters.keys():
            raise KeyError('No document id.')

    def __str__(self):
        return f'Path: {self.path}\nParameters: {self.parameters}'

    def __repr__(self):
        return self.path, self.parameters
