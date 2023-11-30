import pytest
from django.contrib.auth.models import User


# @pytest.fixture
# def create_user():
#     user = User.objects.create(
#         username="ayush2111", email="ayush2111@gmail.com", password="admin")
#     return user



def check_user():
    assert "ayush" == "ayush"


# @pytest.mark.django_db
# def test_create_user():
#     user = User.objects.create_user(username="ayush2111", email="ayush2@gmail.com", password="admin")
#     user.save()
#     print(user)
#     assert user is not None


# @pytest.fixture
# def data():
#     print("hello world")
#     return 2


# @pytest.mark.slow
# def test_example():
#     assert 1 == 1


# def test_example1(data):
#     assert data == 1
