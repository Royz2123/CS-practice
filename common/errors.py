class RecognizedSiteException(Exception):
    def __init__(self, err_msg: str):
        super(Exception, self).__init__(err_msg)


class JavaProgramException(Exception):
    def __init__(self, err_msg: str, err_info: str):
        super(Exception, self).__init__(err_msg)
        self.err_info = err_info
