class Flight:
    def __init__(self, flight_id, departure, destination, date, time, ready: bool) -> None:
        self.flight_id = flight_id
        self.departure = departure
        self.destination = destination
        self.date = date
        self.time = time
        self.ready = ready