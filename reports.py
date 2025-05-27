from datetime import date

def generate_text_report(system, group_id, start_date, end_date):
    report = system.generate_report(group_id, start_date, end_date)
    
    text = f"""
    GROUP {group_id} REPORT
    Period: {report['period']}
    ----------------------------------
    Total days: {report['total_days']}
    Days with records: {report['days_with_records']}
    
    ATTENDANCE:
    """
    
    for child_id, days_attended in report['children_attendance'].items():
        child = next(c for c in system.children if c['id'] == child_id)
        text += f"\n- {child['name']}: {days_attended} of {report['days_with_records']} days"
    
    if report['incidents']:
        text += "\n\nINCIDENTS:"
        for incident in report['incidents']:
            text += f"\n- {incident['description']} ({incident['date'].strftime('%Y-%m-%d')})"
    
    return text