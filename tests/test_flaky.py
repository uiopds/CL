import pytest


@pytest.mark.quarantine
def test_unstable_external_service():
    """Тест, находящийся в карантине (имитирует сбой внешнего сервиса)."""
    assert False, "Temporary network timeout"