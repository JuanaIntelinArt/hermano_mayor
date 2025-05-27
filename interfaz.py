from big_brother import BigBrotherSystem
from sample_data import load_sample_data

def show_menu():
    print("\nBig Brother System")
    print("1. View big brothers")
    print("2. View registered children")
    print("3. View groups")
    print("4. Generate group report")
    print("5. Exit")

def run_system():
    system = load_sample_data()
    
    while True:
        show_menu()
        option = input("Select an option: ")
        
        if option == "1":
            print("\nBig Brothers:")
            for b in system.big_brothers:
                print(f"ID: {b['id']}, Name: {b['name']}, Contact: {b['contact']}")
        
        elif option == "2":
            print("\nRegistered Children:")
            for c in system.children:
                print(f"ID: {c['id']}, Name: {c['name']}, School: {c['school']}")
        
        elif option == "3":
            print("\nGroups:")
            for g in system.groups:
                print(f"ID: {g['id']}, Name: {g['name']}, Brother: {g['brother_id']}, Children: {g['children_ids']}")
        
        elif option == "4":
            group_id = int(input("Group ID: "))
            days = int(input("Days to report (from today): "))
            report = system.generate_report(group_id, date.today() - timedelta(days=days), date.today())
            
            print("\nGroup Report:")
            for key, value in report.items():
                print(f"{key}: {value}")
        
        elif option == "5":
            print("Exiting system...")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run_system()