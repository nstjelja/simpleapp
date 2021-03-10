import app
from unittest.mock import patch

@patch('app.read_health')
def test_healthy(test_patch):
    test_patch.return_value = '1'
    (msg,status) = app.healthy()
    assert msg == "yes"
    assert status == 200

@patch('app.read_health')
def test_not_healthy(test_patch):
    test_patch.return_value = '0'
    (msg,status) = app.healthy()
    assert msg == "no"
    assert status == 500
