class Day(object):

    def __init__(self, day_id, day_name):
        self._id = day_id
        self._day_name = day_name

    @property
    def get_day_id(self):
        return self._id

    @property
    def get_day_name(self):
        return self._day_name

    def save_CSV(self):
        dayDF = pd.DataFrame([self._id, self._day_name])
        dayDF.to_csv(r'output/dayDFTEST.csv', index=False)

    @property
    def __str__(self):
        self.save_CSV()
        return '{}, {}'.format(self._id, self._day_name)
