from diaries.AbstractDiary import AbstractDiary


class hibikidiary(AbstractDiary):

    def get_date(self):
        return "2020-11-25"

    def get_summary(self):
        return "一限から眠かった"

    def get_author(self):
        return "島中"