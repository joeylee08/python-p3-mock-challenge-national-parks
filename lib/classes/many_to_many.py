class NationalPark:
    def __init__(self, name):
        self.name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self and isinstance(trip, Trip)]
    def visitors(self):
        return list(set([trip.visitor for trip in Trip.all if trip.national_park == self and isinstance(trip.visitor, Visitor)]))
    def total_visits(self):
        return len([trip for trip in Trip.all if trip.national_park == self])
    def best_visitor(self):
        visits_per_guest = {}
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor.name not in visits_per_guest:
                    visits_per_guest[trip.visitor.name] = 0
                visits_per_guest[trip.visitor.name] += 1

        the_best_guest = sorted(visits_per_guest, key = lambda item: visits_per_guest[item], reverse = True)
        the_best_guest = the_best_guest[0]
        for trip in Trip.all:
            if trip.national_park == self and trip.visitor.name == the_best_guest:
                return trip.visitor


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Name can only be set once and must be a str > 3 chars.")
    
    @classmethod
    def most_visited(cls):
        total_visits_per_park = {}
        for trip in Trip.all:
            if trip.national_park.name not in total_visits_per_park:
                total_visits_per_park[trip.national_park.name] = 0
            total_visits_per_park[trip.national_park.name] += 1
        total_visits_per_park = sorted(total_visits_per_park, key = lambda item: total_visits_per_park[item], reverse = True)
        most_visited_park = total_visits_per_park[0]
        for trip in Trip.all:
            if trip.national_park.name == most_visited_park:
                return trip.national_park
        return None

class Trip:
    all = []
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, date):
        if isinstance(date, str) and date.split(' ')[0] in Trip.months:
            self._start_date = date
        else:
            raise Exception("Start date must be >= 7 characters and in the proper format.")

    @property
    def end_date(self):
        return self._end_date
    @end_date.setter
    def end_date(self, date):
        if isinstance(date, str) and date.split(' ')[0] in Trip.months:
            self._end_date = date
        else:
            raise Exception("End date must be >= 7 characters and in the proper format.")

    @property
    def visitor(self):
        return self._visitor
    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park
    @national_park.setter
    def national_park(self, park):
        if isinstance(park, NationalPark):
            self._national_park = park
    


class Visitor:
    def __init__(self, name):
        self.name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self and isinstance(trip, Trip)]
    def national_parks(self):
        return list(set([trip.national_park for trip in Trip.all if trip.visitor == self and isinstance(trip.national_park, NationalPark)]))
    def total_visits_at_park(self, park):
        return len([trip for trip in Trip.all if trip.national_park == park and trip.visitor == self])

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Name must be a string between 1 and 15 characters.")