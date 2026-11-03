def clean(text):
    return text.strip().lower()


def ask_choice(prompt, choices):
    lower_map = {c.lower(): c for c in choices}
    while True:
        raw = input(prompt).strip().lower()
        if raw in lower_map:
            return lower_map[raw]
        print(f"  Tidak valid. Pilih dari: {', '.join(choices)}")
