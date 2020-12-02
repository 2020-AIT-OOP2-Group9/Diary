from diaries.AbstractDiary import AbstractDiary


class NishioDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "資料を調べた"

    def get_author(self):
        return "Nishio"