from http import HTTPStatus

from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from src.use_cases.exceptions.use_case_exceptions_reasons_enum import (
    UseCaseExceptionsReasonsEnum,
)


class UnexpectedUseCaseException(UseCaseBaseException):
    _reason = UseCaseExceptionsReasonsEnum.UNEXPECTED_EXCEPTION_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR


class MalformedRequestInputException(UseCaseBaseException):
    _reason = UseCaseExceptionsReasonsEnum.MALFORMED_REQUEST_INPUT_ERROR
    _http_status_code = HTTPStatus.BAD_REQUEST


class UnableToRegisterCurrencyExchange(UseCaseBaseException):
    _reason = UseCaseExceptionsReasonsEnum.UNABLE_TO_REGISTER_CURRENCY_EXCHANGE_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR


class UnableToRetrieveCurrencyExchange(UseCaseBaseException):
    _reason = UseCaseExceptionsReasonsEnum.UNABLE_TO_RETRIEVE_CURRENCY_EXCHANGE_ERROR
    _http_status_code = HTTPStatus.INTERNAL_SERVER_ERROR
