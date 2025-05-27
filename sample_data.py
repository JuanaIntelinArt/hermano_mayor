from datetime import date, timedelta
from big_brother import BigBrotherSystem

def load_sample_data():
    system = BigBrotherSystem()
    
    b1 = system.add_big_brother("John Smith", 18, "123 Main St", "555-1234")
    b2 = system.add_big_brother("Maria Garcia", 17, "456 Oak Ave", "555-5678")
    
    c1 = system.add_child("Luis Rodriguez", 8, "123 Main St", "Elementary School", "555-1111")
    c2 = system.add_child("Ana Martinez", 7, "123 Main St", "Elementary School", "555-2222")
    c3 = system.add_child("Carlos Lopez", 9, "456 Oak Ave", "Elementary School", "555-3333")
    
    g1 = system.create_group("Downtown Group", b1['id'], [c1['id'], c2['id']])
    g2 = system.create_group("Northside Group", b2['id'], [c3['id']])
    
    today = date.today()
    system.record_attendance(g1['id'], today, {c1['id']: True, c2['id']: True})
    system.record_attendance(g2['id'], today, {c3['id']: False})
    
    system.attendance_records[-1]['incidents'].append({
        'date': datetime.now(),
        'description': "Carlos was absent due to illness"
    })
    
    return system