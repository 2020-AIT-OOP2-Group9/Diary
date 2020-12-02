from diaries.AbstractDiary import AbstractDiary

class DiaryKoizumi(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "こんにちは"

    def get_author(self):
        return "koizumi"