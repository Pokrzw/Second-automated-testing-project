import unittest
from unittest.mock import Mock, patch
import pytest
from modules.main import get_data

@pytest.mark.parametrize("_status, _return", [(200, 'Dziala'),(400, -1)])
def test_get_data( _status, _return):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = _status
        mock_get.return_value.json.return_value = _return
        assert get_data()==_return

if __name__ == '__main__':
    unittest.main()