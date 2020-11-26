from diaries.DiarySample import DiarySample
from diaries.YamaguchiDaiary import YamaguchiDaiary

diaries = [DiarySample(), YamaguchiDaiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()