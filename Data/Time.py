class Time(object):

    def __init__(self, timeID, timeSlot, Details):
        self._timeID = timeID
        self._timeSlot = timeSlot
        self._Details = Details

    @property
    def get_timeID(self):
        return self._timeID

    @property
    def get_timeSlot(self):
        return self._timeSlot

    @property
    def get_timeSlot_Details(self):
        return self._Details

    @property
    def __str__(self):
        return '{}, {}, {} '.format(self._timeID, self._timeSlot, self._Details)
