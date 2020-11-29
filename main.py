from diaries.DiarySample import DiarySample
from diaries.Daikidiary import Daikidaiary

diaries = [DiarySample(),Daikidaiary() ,]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()