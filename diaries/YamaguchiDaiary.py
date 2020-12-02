from diaries.AbstractDiary import AbstractDiary


class YamaguchiDaiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "Hello"

    def get_author(self):
        return "Yamaguchi"