class room_test(object):
    def __init__(self, room_id, name, capacity):
        self._id = room_id
        self._name = name
        self._capacity = capacity

    @property
    def get_id(self):
        return self._id

    @property
    def get_room_name(self):
        return self._name

    @property
    def get_room_capacity(self):
        return self._capacity

    @property
    def __str__(self):
        return '{}, {}, {}'.format(self._id, self._name, self._capacity)
