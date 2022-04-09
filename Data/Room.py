class room_test(object):
    def __init__(self, room_id, name):
        self._id = room_id
        self._name = name

    def get_id(self):
        return self._id

    def get_room_name(self):
        return self._name

    def __str__(self):
        return '{}, {}'.format(self._id, self._name)
