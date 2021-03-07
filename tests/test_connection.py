import pytest

from src.database import ConnectionSql
from src import openJson

config = openJson("config/config.json")

@pytest.mark.connection
def test_connection():

    tables = [('actors',), ('casting_with',), ('comments_rate',), ('directing_by',), ('directors',), ('genres',), ('movies',), ('type_movies',), ('users',)]

    db = ConnectionSql(**config)

    res = db.showDatabase()
    print(res)

    assert res == tables