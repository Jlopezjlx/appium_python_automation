class ElementNotFound(Exception):
    def __init__(self, message, error=None):
        super().__init__(f'{message} was not found, please check it')


class NotAbleToCLickOrType(Exception):
    def __init__(self, message, error=None):
        super().__init__(f'{message} was not able to click on or type in, please check it')


class ElementNotDisplayed(Exception):
    def __init__(self, message, error=None):
        super().__init__(f'{message} not displayed')
