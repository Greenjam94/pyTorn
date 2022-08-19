### Error codes provided from documentation: https://wiki.torn.com/wiki/API#Error_codes

# 1
class APIKeyMissingError(Exception):
    pass

# 2
class APIKeyIncorrectError(Exception):
    pass

#3
class APIWrongTypeError(Exception):
    pass

#4
class APIWrongFieldsError(Exception):
    pass

#5 - max 100/min
class APITooManyRequests(Exception):
    pass

#6
class APIIncorrectIDError(Exception):
    pass

#7
class APIInvalidIDError(Exception):
    pass

#8
class APIBannedIpError(Exception):
    pass

#9
class APIDisabledError(Exception):
    pass

#10
class APIFeddedKeyError(Exception):
    pass

#11
class APIKeyChangeThrottleError(Exception):
    pass

#12
class APIKeyReadError(Exception):
    pass

#13
class APIKeyOwnerInactiveError(Exception):
    pass

#14
class APIKeyOwnerDailyThrottleError(Exception):
    pass

#16
class APIInvalidPermissionError(Exception):
    pass

errorCodes = {
    1: APIKeyMissingError,
    2: APIKeyIncorrectError,
    3: APIWrongTypeError,
    4: APIWrongFieldsError,
    5: APITooManyRequests,
    6: APIIncorrectIDError,
    7: APIInvalidIDError,
    8: APIBannedIpError,
    9: APIDisabledError,
    10: APIFeddedKeyError,
    11: APIKeyChangeThrottleError,
    12: APIKeyReadError,
    13: APIKeyOwnerInactiveError,
    14: APIKeyOwnerDailyThrottleError,
    16: APIInvalidPermissionError,
}

@staticmethod
def parseErrorCode(number):
    return errorCodes.get(number, Exception)()