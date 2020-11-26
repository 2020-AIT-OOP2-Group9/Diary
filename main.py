from diaries.DiarySample import DiarySample
from diaries.daikidiary import daikidaiary

diaries = [DiarySample(), daikidaiary() ,]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()