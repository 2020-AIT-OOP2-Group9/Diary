from diaries.AbstractDiary import AbstractDiary


class DiaryTakeichi(AbstractDiary):

    def get_date(self):
        return "2020-11-30"

    def get_summary(self):
        return "難しかった"

    def get_author(self):
        return "Takeichi"