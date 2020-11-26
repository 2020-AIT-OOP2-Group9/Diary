
from diaries.NishioDiaryNew import NishioDiaryNew
from diaries.DiarySample import DiarySample

diaries = [DiarySample(), NishioDiaryNew()]

from diaries.daikidiary import daikidaiary

diaries = [DiarySample(), daikidaiary() ,]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()