from diaries.DiaryKoizumi import DiaryKoizumi
from diaries.NishioDiaryNew import NishioDiaryNew
from diaries.DiarySample import DiarySample
from diaries.YamaguchiDaiary import YamaguchiDaiary
from diaries.daikidiary import daikidaiary

diaries = [DiarySample(), daikidaiary() ,NishioDiaryNew(),DiaryKoizumi(),YamaguchiDaiary()]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()