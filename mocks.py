class Mocks():
    DHT11 = {
        'temperature' : 27.5,
        'humidity' : 45
    }

    POSTS = [
        {'id': 1, 'temperature': 27.5, 'humidity': 45},
        {'id': 2, 'temperature': 30, 'humidity': 30},
        {'id': 3, 'temperature': 35, 'humidity': 25},
        {'id': 4, 'temperature': 25, 'humidity': 80},
        {'id': 5, 'temperature': 27.5, 'humidity': 45}
    ]
    

    @classmethod
    def DHT11_temp(cls):
        pass

    @classmethod
    def DHT11_hum(cls):
        pass

    @classmethod
    def all(cls):
        return cls.POSTS
