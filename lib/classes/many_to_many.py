class Band:
    def __init__(self, name, hometown):
        self.name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def hometown(self):
        return self._hometown

    @property
    def concerts(self):
        return self._concerts if self._concerts else None

    @property
    def venues(self):
        return list(set(concert.venue for concert in self._concerts)) if self._concerts else None

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        self._concerts.append(concert)
        venue.add_concert(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts] if self._concerts else None


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        band._concerts.append(self)
        venue.add_concert(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be an instance of Band class")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be an instance of Venue class")

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")

    def concerts(self):
        return self._concerts if self._concerts else None

    def bands(self):
        return list(set(concert.band for concert in self._concerts)) if self._concerts else None

    def add_concert(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)
        else:
            raise ValueError("Concert must be an instance of Concert class")


if __name__ == "__main__":
    band1 = Band("The Rockers", "New York")
    venue1 = Venue("Madison Square Garden", "New York")
    concert1 = band1.play_in_venue(venue1, "2025-06-15")
    
    print(concert1.introduction())
    print([band.name for band in venue1.bands()])