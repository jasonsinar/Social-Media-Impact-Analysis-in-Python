from data_loader import load_data
from text_utils import ask_choice
from analysis import search_by_platform, filter_by_impact, impact_summary

PLATFORMS = ["Instagram", "TikTok", "YouTube", "Snapchat", "Twitter", "Reddit", "LinkedIn"]
IMPACTS = ["Beneficial", "Neutral", "Negative"]


def normalize_platform(platform):
    """Konversi nama platform dari menu ke nama yang ada di CSV."""
    if platform.lower() == "twitter":
        return "X (Twitter)"
    return platform


def print_menu():
    print("\n" + "=" * 45)
    print("   Eksplorasi Dampak Media Sosial")
    print("=" * 45)
    print("  [1] Cari Berdasarkan Aplikasi")
    print("  [2] Filter Berdasarkan Dampak")
    print("  [3] Ringkasan Dampak")
    print("  [0] Keluar")
    print("-" * 45)


def get_choice():
    valid = ["0", "1", "2", "3"]
    while True:
        choice = input("  Pilih menu: ").strip()
        if choice in valid:
            return choice
        print(f"  Pilihan tidak valid. Pilih dari: {', '.join(valid)}")


def main():
    print("\nMemuat data...")
    records = load_data()

    if not records:
        print("Tidak ada data. Program berhenti.")
        return

    while True:
        print_menu()
        choice = get_choice()

        if choice == "0":
            print("\n  Terima kasih!\n")
            break

        elif choice == "1":
            print(f"\n  Aplikasi tersedia: {', '.join(PLATFORMS)}")
            platform = ask_choice("  Masukkan nama aplikasi: ", PLATFORMS)
            actual = normalize_platform(platform)
            search_by_platform(records, actual)

        elif choice == "2":
            print(f"\n  Pilihan dampak: {', '.join(IMPACTS)}")
            impact = ask_choice("  Masukkan dampak: ", IMPACTS)
            filter_by_impact(records, impact)

        elif choice == "3":
            impact_summary(records)

        input("\n  Tekan Enter untuk kembali ke menu...")


if __name__ == "__main__":
    main()
