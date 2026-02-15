import unittest
from unittest.mock import patch, MagicMock
import socket
import sys

from client import(
    print_response,
    text_validation,
    date_time_validation,
    validation_checks,
    create_dt_request,
    resolve_hostname
)