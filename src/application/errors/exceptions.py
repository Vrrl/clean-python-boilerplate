class ApplicationRuleError(Exception):
    """Exception raised for Application Rules errors.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
