from diaries.DiaryKoizumi import DiaryKoizumi

diaries = [DiarySample(), DiaryKoizumi()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()