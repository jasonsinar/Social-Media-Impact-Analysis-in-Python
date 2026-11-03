import unittest
from models import Record
from text_utils import clean, ask_choice
from data_loader import parse_row
from analysis import average, urutkan_durasi


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
    # Test 1 — models.py: usage_category mengkategorikan durasi dengan benar
    def test_usage_category(self):
        self.assertEqual(make_record(daily_hours=2.0).usage_category(), "Low")
        self.assertEqual(make_record(daily_hours=5.0).usage_category(), "Medium")
        self.assertEqual(make_record(daily_hours=8.0).usage_category(), "High")


class TestTextUtils(unittest.TestCase):
    # Test 2 — text_utils.py: clean menghapus spasi dan mengubah ke huruf kecil
    def test_clean(self):
        self.assertEqual(clean("  Instagram  "), "instagram")


class TestDataLoader(unittest.TestCase):
    # Test 3 — data_loader.py: parse_row menghasilkan Record dengan nilai yang benar
    def test_parse_row(self):
        rec = parse_row(base_row())
        self.assertEqual(rec.platform, "Instagram")
        self.assertAlmostEqual(rec.daily_hours, 4.0)
        self.assertTrue(rec.late_night)


class TestAverage(unittest.TestCase):
    # Test 4 — analysis.py: average menghitung rata-rata dengan benar
    def test_average(self):
        self.assertAlmostEqual(average([2.0, 4.0, 6.0]), 4.0)


class TestUrutkanDurasi(unittest.TestCase):
    # Test 5 — analysis.py: urutkan_durasi mengurutkan dari tertinggi ke terendah
    def test_urutkan_durasi(self):
        records = [make_record(daily_hours=2.0), make_record(daily_hours=6.0), make_record(daily_hours=4.0)]
        result = urutkan_durasi(records)
        self.assertEqual(result[0].daily_hours, 6.0)
        self.assertEqual(result[2].daily_hours, 2.0)


class TestTambahan(unittest.TestCase):
    # Test 6 — sleep_deficit menghitung kurang tidur dengan benar
    def test_sleep_deficit(self):
        self.assertAlmostEqual(make_record(sleep_hours=6.0).sleep_deficit(), 2.0)

    # Test 7 — average mengembalikan 0.0 jika list kosong
    def test_average_list_kosong(self):
        self.assertEqual(average([]), 0.0)

    # Test 8 — parse_row: Late_Night_Usage "False" menghasilkan False
    def test_late_night_false(self):
        self.assertFalse(parse_row(base_row(Late_Night_Usage="False")).late_night)

    # Test 9 — urutkan_durasi tidak error dengan list kosong
    def test_urutkan_kosong(self):
        self.assertEqual(urutkan_durasi([]), [])

    # Test 10 — clean tidak mengubah string yang sudah bersih
    def test_clean_sudah_bersih(self):
        self.assertEqual(clean("tiktok"), "tiktok")


if __name__ == "__main__":
    unittest.main(verbosity=2)
