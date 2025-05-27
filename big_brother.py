from datetime import date, datetime

class BigBrotherSystem:
    def __init__(self):
        self.big_brothers = []
        self.children = []
        self.groups = []
        self.attendance_records = []
        self.next_brother_id = 1
        self.next_child_id = 1
        self.next_group_id = 1

    def add_big_brother(self, name, age, address, contact):
        brother = {
            'id': self.next_brother_id,
            'name': name,
            'age': age,
            'address': address,
            'contact': contact,
            'registration_date': date.today()
        }
        self.next_brother_id += 1
        self.big_brothers.append(brother)
        return brother

    def add_child(self, name, age, address, school, emergency_contact):
        child = {
            'id': self.next_child_id,
            'name': name,
            'age': age,
            'address': address,
            'school': school,
            'emergency_contact': emergency_contact,
            'registration_date': date.today()
        }
        self.next_child_id += 1
        self.children.append(child)
        return child

    def create_group(self, name, brother_id, children_ids):
        group = {
            'id': self.next_group_id,
            'name': name,
            'brother_id': brother_id,
            'children_ids': children_ids,
            'route': None,
            'schedule': None,
            'creation_date': date.today()
        }
        self.next_group_id += 1
        self.groups.append(group)
        return group

    def record_attendance(self, group_id, date, attendance):
        record = {
            'group_id': group_id,
            'date': date,
            'attendance': attendance,
            'incidents': []
        }
        self.attendance_records.append(record)
        return record

    def generate_report(self, group_id, start_date, end_date):
        report = {
            'group_id': group_id,
            'period': f"{start_date} to {end_date}",
            'total_days': (end_date - start_date).days + 1,
            'days_with_records': 0,
            'children_attendance': {},
            'incidents': []
        }

        for record in self.attendance_records:
            if record['group_id'] == group_id and start_date <= record['date'] <= end_date:
                report['days_with_records'] += 1
                for child_id, attended in record['attendance'].items():
                    if child_id not in report['children_attendance']:
                        report['children_attendance'][child_id] = 0
                    if attended:
                        report['children_attendance'][child_id] += 1
                report['incidents'].extend(record['incidents'])

        return report