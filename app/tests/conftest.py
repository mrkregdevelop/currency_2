import pytest


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture()
def api_client():
    from rest_framework.test import APIClient
    client = APIClient()
    yield client


@pytest.fixture(scope='function')
def api_client_authorized(django_user_model):
    from rest_framework.test import APIClient
    client = APIClient()

    user = django_user_model.objects.create(
        email='admin@example.com',
    )
    user.set_password('qwertyasd')

    client.login(email='admin@example.com', password='qwertyasd')
    yield client
