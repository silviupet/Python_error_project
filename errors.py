class Myerror(TypeError):
    """
    exception raised when a specific error code is needed
    """



    def __init__(self, message, code):
        # super().__init__(message)
        super().__init__(f"error code {code}: {message}")
        self.code = code


err = Myerror("an error code is needed " , 500)
print(err) #error code 500: an error code is needed
print(err.__doc__) #exception raised when a specific error code is needed    