import pytest
from unittest.mock import patch
from main import add_customer, edit_customer

@patch('builtins.input', side_effect=["Test Name", "test@email.com", "12345678"])
def test_add_customer(mocked_input):
  customers = []
  add_customer(customers)
  assert customers[0]["name"] == "Test Name"
  assert customers[0]["email"] == "test@email.com"
  assert customers[0]["mobile"] == "12345678"

@patch('builtins.input', side_effect=["1", "Test Name", "test@email.com", "12345678"])
def test_update_customer(mocked_input):
  customers = [
    {
      "name": "Jon Snow",
      "email":"asd.com",
      "mobile":"171717"
    }
  ]
  edit_customer(customers)
  assert customers[0]["name"] == "Test Name"
  assert customers[0]["email"] == "test@email.com"
  assert customers[0]["mobile"] == "12345678"
  