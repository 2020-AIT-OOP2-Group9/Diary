from diaries.AbstractDiary import AbstractDiary


class Daikidaiary(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "難しかった"

    def get_author(self):
        return "Takeichi Daiki"