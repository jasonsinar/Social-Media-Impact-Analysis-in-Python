CSV_FILENAME = "Social_media_impact_on_life.csv"
MAX_ROWS = 2000


class Record:
    def __init__(self, age, platform, daily_hours, sleep_hours, sleep_quality, late_night, impact):
        self.age = age
        self.platform = platform
        self.daily_hours = daily_hours
        self.sleep_hours = sleep_hours
        self.sleep_quality = sleep_quality
        self.late_night = late_night
        self.impact = impact

    def sleep_deficit(self):
        return round(8.0 - self.sleep_hours, 1)

    def usage_category(self):
        if self.daily_hours < 3:
            return "Low"
        elif self.daily_hours <= 6:
            return "Medium"
        else:
            return "High"

    def __str__(self):
        late = "Yes" if self.late_night else "No"
        return (f"Platform: {self.platform:<12} Usage: {self.daily_hours:<5} "
                f"Sleep: {self.sleep_hours:<5} Quality: {self.sleep_quality:<3} "
                f"Late: {late:<4} Impact: {self.impact}")
