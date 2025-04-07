class RoomTypeConverter:
    regex = 'standard|half-luxe|luxe'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value


class ServiceTypeConverter:
    regex = 'indoors|special'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value
