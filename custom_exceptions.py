#!/usr/bin/python3

class Error(Exception):
    pass

class ExtraParametersError(Error):
    pass

class TooFewParametersError(Error):
    pass

class NoNumericParameterError(Error):
    pass
