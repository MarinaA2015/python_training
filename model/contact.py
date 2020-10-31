from sys import maxsize


class Contact:
    def __init__(self, first_name=None,last_name=None,company=None,home_phone=None, mobile_phone=None,
                 work_phone=None, second_phone=None, id=None, all_phones_from_contact_page=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.second_phone = second_phone
        self.id = id
        self.all_phones_from_contact_page = all_phones_from_contact_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name \
               and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize




