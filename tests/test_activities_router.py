import unittest
from unittest.mock import patch

from src.backend.routers.activities import get_activities


class GetActivitiesDifficultyFilterTests(unittest.TestCase):
    @patch("src.backend.routers.activities.activities_collection.find")
    def test_filters_by_specific_difficulty(self, mock_find):
        mock_find.return_value = []

        get_activities(difficulty="beginner")

        mock_find.assert_called_once_with({"difficulty": "Beginner"})

    @patch("src.backend.routers.activities.activities_collection.find")
    def test_filters_all_levels_using_missing_difficulty_field(self, mock_find):
        mock_find.return_value = []

        get_activities(difficulty="all")

        mock_find.assert_called_once_with(
            {
                "$or": [
                    {"difficulty": {"$exists": False}},
                    {"difficulty": None},
                ]
            }
        )


if __name__ == "__main__":
    unittest.main()
