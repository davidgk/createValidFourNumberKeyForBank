

class WrongKeyException(Exception):

    def __init__(self, msg):
        super(WrongKeyException, self).__init__(msg)