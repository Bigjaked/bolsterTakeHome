from candidate_api.models import Experience, User
from candidate_api.utils.csv_utils import (
    load_tsv_file,
    load_users_data,
    load_experience_data,
)

from candidate_api.utils.generate_data_structure import (
    generate_object_map_array,
    generate_user_map,
)


class TestLoadFile:
    def test_load_file_does_not_exist(self):
        assert load_tsv_file("does_not_exist.txt", dict) is None

    def test_load_file_test_file(self):
        assert load_tsv_file("tests/test_files/test_file.tsv", dict) == [
            dict(id="1", name="jake"),
            dict(id="2", name="bob"),
            dict(id="3", name="frank"),
        ]

    def test_load_file_test_user(self):
        assert load_users_data("tests/test_files/test_user.tsv") == [
            User(id="user", name="some user", bio="some bio", picture="some picture"),
            User(
                id="user2", name="some user2", bio="some bio2", picture="some picture2"
            ),
        ]

    def test_load_file_test_experience(self):
        assert load_experience_data("tests/test_files/test_experiences.tsv") == [
            Experience(
                id="1",
                company="company1",
                title="title1",
                dates="1000|2000",
                description="some description1",
            ),
            Experience(
                id="2",
                company="company2",
                title="title2",
                dates="3000|4000",
                description="some description2",
            ),
        ]


class TestGenerateDataStructures:
    def test_generate_user_map_is_empty(self):
        assert generate_user_map([]) is None

    def test_generate_user_map(self):
        assert generate_user_map(
            [
                User(id="1", name="user1"),
                User(id="2", name="user2"),
            ]
        ) == {
            "1": User(id="1", name="user1"),
            "2": User(id="2", name="user2"),
        }

    def test_generate_object_map_array_is_empty(self):
        assert generate_object_map_array([]) is None

    def test_generate_object_map_array(self):
        assert generate_object_map_array(
            [
                Experience(id="1", company="company1"),
                Experience(id="1", company="company2"),
                Experience(id="1", company="company3"),
                Experience(id="2", company="company4"),
                Experience(id="2", company="company5"),
                Experience(id="2", company="company6"),
            ]
        ) == {
            "1": [
                Experience(id="1", company="company1"),
                Experience(id="1", company="company2"),
                Experience(id="1", company="company3"),
            ],
            "2": [
                Experience(id="2", company="company4"),
                Experience(id="2", company="company5"),
                Experience(id="2", company="company6"),
            ],
        }
