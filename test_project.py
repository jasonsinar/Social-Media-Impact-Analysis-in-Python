import unittest
from unittest.mock import patch
from models import Record
from text_utils import clean
from data_loader import parse_row
from analysis import average
from main import normalize_platform, print_menu, get_choice


def make_record(**overrides):
    defaults = dict(
        age=20, platform="Instagram", daily_hours=4.0,
        sleep_hours=7.0, sleep_quality=3, late_night=False, impact="Neutral"
    )
    defaults.update(overrides)
    return Record(**defaults)


def base_row(**overrides):
    row = {
        "Student_ID": "STU_001", "Age": "20", "Gender": "Female",
        "Academic_Level": "Undergraduate", "Primary_Platform": "Instagram",
        "Daily_Usage_Hours": "4.0", "Weekend_Extra_Hours": "1.5",
        "Device_Type": "Smartphone", "Sleep_Duration_Hours": "7.0",
        "Sleep_Quality_Score": "3", "Late_Night_Usage": "True",
        "Social_Comparison_Frequency": "Sometimes", "Perceived_Stress_Score": "15.0",
        "Mental_Health_Index": "80", "Academic_Performance_GPA": "3.20",
        "Overall_Impact": "Neutral",
    }
    row.update(overrides)
    return row


class TestModels(unittest.TestCase):
    def test_usage_category(self):
        self.assertEqual(make_record(daily_hours=2.0).usage_category(), "Low")
        self.assertEqual(make_record(daily_hours=5.0).usage_category(), "Medium")
        self.assertEqual(make_record(daily_hours=8.0).usage_category(), "High")


class TestTextUtils(unittest.TestCase):
    def test_clean(self):
        self.assertEqual(clean("  Instagram  "), "instagram")


class TestDataLoader(unittest.TestCase):
    def test_parse_row(self):
        rec = parse_row(base_row())
        self.assertEqual(rec.platform, "Instagram")
        self.assertAlmostEqual(rec.daily_hours, 4.0)
        self.assertTrue(rec.late_night)


class TestAnalysis(unittest.TestCase):
    def test_average(self):
        self.assertAlmostEqual(average([2.0, 4.0, 6.0]), 4.0)


class TestMain(unittest.TestCase):
    def test_normalize_platform_twitter(self):
        self.assertEqual(normalize_platform("Twitter"), "X (Twitter)")

    def test_normalize_platform_other(self):
        self.assertEqual(normalize_platform("Instagram"), "Instagram")

    def test_get_choice_valid(self):
        with patch("builtins.input", return_value="1"):
            self.assertEqual(get_choice(), "1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
