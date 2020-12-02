from diaries.DiaryKoizumi import DiaryKoizumi
from diaries.NishioDiaryNew import NishioDiaryNew
from diaries.DiarySample import DiarySample 
from diaries.DiaryTakeichi import DiaryTakeichi


from diaries.YamaguchiDaiary import YamaguchiDaiary
from diaries.hibikidiary import hibikidiary

diaries = [DiarySample(),NishioDiaryNew(),DiaryKoizumi(),YamaguchiDaiary(),hibikidiary(),DiaryTakeichi()]



for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()