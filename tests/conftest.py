from _pytest.fixtures import fixture

from services.api_service import ApiClient


@fixture
def client():
    return ApiClient()
