from diaries.DiarySample import DiarySample
from diaries.NishioDiaryNew import NishioDiaryNew


diaries = [DiarySample(), NishioDiaryNew()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()