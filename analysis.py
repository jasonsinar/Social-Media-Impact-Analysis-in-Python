from text_utils import clean


def average(values):
    values = [v for v in values if v is not None]
    if not values:
        return 0.0
    return round(sum(values) / len(values), 2)


def urutkan_durasi(records):
    data = list(records)
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j].daily_hours < data[j+1].daily_hours:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def search_by_platform(records, platform):
    results = urutkan_durasi([r for r in records if clean(r.platform) == clean(platform)])

    if not results:
        print(f"\n  Tidak ada data untuk platform '{platform}'.")
        return

    print(f"\n  Aplikasi: {platform}  ({len(results)} pengguna)")
    print("-" * 65)
    print(f"  {'Usia':<6} {'Durasi/hari':<13} {'Jam Tidur':<11} {'Kualitas Tidur':<16} {'Malam Hari':<12} {'Dampak'}")
    print("-" * 65)

    for r in results:
        malam = "Ya" if r.late_night else "Tidak"
        print(f"  {r.age:<6} {r.daily_hours:<13} {r.sleep_hours:<11} {r.sleep_quality:<16} {malam:<12} {r.impact}")

    print("-" * 65)
    print(f"  Rata-rata durasi penggunaan : {average([r.daily_hours for r in results])} jam/hari")
    print(f"  Rata-rata jam tidur         : {average([r.sleep_hours for r in results])} jam")
    print(f"  Rata-rata kualitas tidur    : {average([r.sleep_quality for r in results])}")


def filter_by_impact(records, impact):
    results = [r for r in records if clean(r.impact) == clean(impact)]

    if not results:
        print(f"\n  Tidak ada data untuk dampak '{impact}'.")
        return

    print(f"\n  Dampak: {impact}  ({len(results)} pengguna)")
    print("-" * 65)
    print(f"  {'Durasi/hari':<13} {'Jam Tidur':<11} {'Kualitas Tidur':<16} {'Malam Hari':<12} {'Aplikasi'}")
    print("-" * 65)

    for r in results:
        malam = "Ya" if r.late_night else "Tidak"
        print(f"  {r.daily_hours:<13} {r.sleep_hours:<11} {r.sleep_quality:<16} {malam:<12} {r.platform}")

    print("-" * 65)
    print(f"  Rata-rata durasi penggunaan : {average([r.daily_hours for r in results])} jam/hari")
    print(f"  Rata-rata jam tidur         : {average([r.sleep_hours for r in results])} jam")
    print(f"  Rata-rata kualitas tidur    : {average([r.sleep_quality for r in results])}")
    malam_count = sum(1 for r in results if r.late_night)
    malam_pct = round(malam_count / len(results) * 100, 1)
    print(f"  Pengguna malam hari         : {malam_count} ({malam_pct}%)")

    platform_count = {}
    for r in results:
        platform_count[r.platform] = platform_count.get(r.platform, 0) + 1
    top_platform = max(platform_count, key=lambda p: platform_count[p])
    print(f"  Aplikasi terbanyak          : {top_platform} ({platform_count[top_platform]} pengguna)")


def impact_summary(records):
    total = len(records)
    if total == 0:
        print("  Tidak ada data.")
        return

    categories = ["Beneficial", "Neutral", "Negative"]

    print(f"\n  Ringkasan Dampak Media Sosial  (total: {total} data)")
    print("-" * 65)
    print(f"  {'Dampak':<12} {'Jumlah':<9} {'Persen':<9} {'Rata Durasi':<13} {'Rata Tidur'}")
    print("-" * 65)

    for cat in categories:
        group = [r for r in records if clean(r.impact) == clean(cat)]
        count = len(group)
        pct = round(count / total * 100, 1)
        avg_usage = average([r.daily_hours for r in group])
        avg_sleep = average([r.sleep_hours for r in group])
        print(f"  {cat:<12} {count:<9} {str(pct)+'%':<9} {avg_usage:<13} {avg_sleep}")

    print("-" * 65)

    malam_negatif = [r for r in records if r.late_night and clean(r.impact) == "negative"]
    print(f"  Pakai malam hari + dampak negatif : {len(malam_negatif)} pengguna")

    tidak_malam_positif = [r for r in records if not r.late_night and clean(r.impact) == "beneficial"]
    print(f"  Tidak malam hari + dampak positif : {len(tidak_malam_positif)} pengguna")
