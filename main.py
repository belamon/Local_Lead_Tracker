
# /************************************/
import re
from conn import show_deleted_leads, permanently_delete_lead_by_email, restore_lead_by_email, show_all_leads, delete_lead_by_email, update_leads, create_new_lead, check_user_credential,show_all_data_records, print_lead,get_company_sectors, get_lead_sources, get_sales_representatives, get_status_options, confirm_action, generate_summary_report
from utils import is_valid_email, is_valid_phone_number, validate_date


# /===== Feature Program =====/
# Create your feature program here


#Main Menu Function 
def main_menu_choice():
    """Function to display the main menu and get user input"""
    while True: #This will keep asking usert for input until a valid menu option is seleted
        print("\n\t================LEAD MANAGEMENT SYSTEM================")
        print("1. Show Leads")
        print("2. Create Leads")
        print("3. Update Leads")
        print("4. Delete Leads")
        print("5. Manage Leads ")
        print("6. Report Menu")
        print("7. Exit")

        
        try:
            menu = int(input("Input program menu from (1-7): ")) #menu is the variable to hold menu value 
            if 1 <= menu <= 7:  # check if input is valid between this range
                return menu #return the selected menu option 
            else:
                print("*************** Invalid choice. Please select a number between 1 and 7. ***************")
        except ValueError:
            print("*********** Invalid input. Please enter a valid number between 1 and 7. ************")

#Read Menu Functon 
def show_data_leads():
    """Function to display data leads when the user chooses number 1 on the main menu."""
    while True:
        print("\n===== Data Leads =====")
        print("1. Show All Data Records")
        print("2. Search Data Records")
        print("3. Back to Main Menu")

        user_input = input("Enter your choice: ")
        if user_input == "1":
            all_leads = show_all_data_records()
            if all_leads:  # Check if all_leads is not None or empty
                for lead in all_leads:
                    print(lead)

        elif user_input == "2":
            all_leads = show_all_leads()
            search_input = input("Enter email of the lead: ")
            data_found = False
            for lead in all_leads:
                if lead['email'] == search_input:
                    print_lead(lead)
                    data_found = True
                    break
            if not data_found:
                print("No data found.")
        
        elif user_input == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid input. Please enter a number between 1-3.")


#Create menu option 
def create_data_lead():
    """Function to display the result when the user choosing number 2 on main menu """
    while True:
        # Displaying the main menu for creatin a new lead or going back 
        print("\t\t=========CREATE NEW LEAD===============")
        print("1. Create New Lead")
        print("2. Back to Menu")

        user_input = input("Enter chouce:")

        if user_input == "1":
            all_leads = show_all_leads()

            

                        # Validate email format
            while True:
                lead_email = input("Enter lead email you want to input:")
                if not lead_email:  # Check for empty input
                    print("Email cannot be empty. Please enter a valid email.")
                    continue

                if not is_valid_email(lead_email):
                    print("Invalid email format. Please enter a valid email.")
                    continue  # Prompt the user to enter a valid email again

                if any(lead['email'] == lead_email for lead in all_leads):
                    print("Email already exists.")
                    continue
                else:
                    break

            
            #input name 
            first_name = input("Please enter lead first name")
            last_name = input("Please enter lead last name")
            # Validate phone number format
            while True:
                phone_number = input("Enter phone number of lead:")
                if not is_valid_phone_number(phone_number):
                    print("Invalid phone number format. Please enter a valid phone number (10-15 digits).")
                    continue
                else:
                    break

                # Validate company sector format
            available_sectors = get_company_sectors()
            if not available_sectors:
                print("No company sectors found in the database.")
                break

            print("Available Company Sectors:", ", ".join(available_sectors))

            # Loop until a valid company sector is provided
            while True:
                company_sector = input("Enter company sector of the lead: ")
                if company_sector.lower() not in [sector.lower() for sector in available_sectors]:
                    print("Invalid company sector. Please choose from the available options.")
                    print(", ".join(available_sectors))
                else:
                    break  # Exit the loop if the company sector is valid


            # Fetch and validate lead source
            available_sources = get_lead_sources()
            if not available_sources:
                print("No lead sources found in the database.")
                break

            print("Available Lead Sources:", ", ".join(available_sources))

            # Loop until a valid lead source is provided (case-insensitive)
            while True:
                lead_source = input("Enter lead source of the lead: ")
                if lead_source.lower() not in [source.lower() for source in available_sources]:
                    print("Invalid lead source. Please choose from the available options.")
                    print("Available Lead Sources:", ", ".join(available_sources))
                else:
                    break  # Exit the loop if the lead source is valid

            # Date validation within the main lead creation function
            while True:
                date_created = input("Enter date created of lead data (YYYY-MM-DD): ")
                if not validate_date(date_created):
                    print("Invalid date format. Please enter a valid date (YYYY-MM-DD).")
                else:
                    break  # Valid date, exit the loop

            # Fetch and validate sales representative
            available_reps = get_sales_representatives()
            if not available_reps:
                print("No sales representatives found in the database.")
                break

            print("Available Sales Representatives:", ", ".join(available_reps))

            # Loop until a valid sales representative is provided (case-insensitive)
            while True:
                sales_rep = input("Enter Sales representative of the lead: ")
                if sales_rep.lower() not in [rep.lower() for rep in available_reps]:
                    print("Invalid sales representative. Please choose from the available options.")
                    print("Available Sales Representatives:", ", ".join(available_reps))
                else:
                    break  # Exit the loop if the sales representative is valid

            #input transaction 
            while True:
                transaction = input("Enter transaction of the lead:")
                if transaction.isdigit():
                    transaction = int(transaction)
                    break
                else:
                    print("Invalid transaction. Please enter a valid integer.")

            #Input status 
            # Fetch and validate status
            available_statuses = get_status_options()
            if not available_statuses:
                print("No status options found in the database.")
                break

            print("Available Statuses:", ", ".join(available_statuses))
            while True:
                status = input("Enter status of the lead: ")

                if status.lower() not in [status.lower() for status in available_statuses]:
                    print("Invalid status. Please choose from the available options.")
                    print("Available Sales Representatives:", ", ".join(available_statuses))
                else:
                    break


            #store to new variable 
            new_lead = {
                'email': lead_email,
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number,
                'company_sector': company_sector,
                'lead_source': lead_source,
                'date_created': date_created,
                'sales_rep': sales_rep,
                'transaction': transaction,
                'status': status

            }

             # Display collected data for confirmation
            print("\nReview the collected data:")
            for key, value in new_lead.items():
                print(f"{key.replace('_', ' ').capitalize()}: {value}")

            # Use the confirm_action function
            if confirm_action("\nDo you want to save this lead? (yes/no): "):
                create_new_lead(new_lead)
                print("Lead has been successfully created.")
            else:
                print("Lead creation has been cancelled.")

        elif user_input == "2":
            print("You are now back to the main menu")
            break
        else:
            print("Invalid choice. Please choose a valid option")

                
        


#Update Data Leads Function 
def update_data_lead():
    """Function to display the result when the user inputs number 3 on the main menu."""
    
    while True:  # Outer loop for updating data leads
        print("\t\t============UPDATE DATA LEADS====================")
        # Show options to the user 
        print("\nOptions:")
        print("1. Update Data Leads")
        print("2. Back to Menu")

        user_input = input("Enter Choice:")

        if user_input == "1":  # Update data leads 
            all_leads = show_all_leads()

            email = input("Enter lead email you want to update:")

            # Check if the email exists in all leads 
            if any(lead['email'] == email for lead in all_leads):
                lead_id = next(lead['lead_id'] for lead in all_leads if lead['email'] == email)

                print("\t\t============SELECT FIELD TO UPDATE====================")
                print("1. First Name")
                print("2. Last Name")
                print("3. Email")
                print("4. Phone Number")
                print("5. Company Sector")
                print("6. Lead Source")
                print("7. Date Created")
                print("8. Sales Representative")
                print("9. Transaction")
                print("10. Status")

                choice = input("Choose a field that you want to update:")
                
                field_map = {
                    "1": "first_name",
                    "2": "last_name",
                    "3": "email",
                    "4": "phone_number",
                    "5": "company_sector",
                    "6": "lead_source",
                    "7": "date_created",
                    "8": "sales_rep",
                    "9": "transaction",
                    "10": "status"
                }

                if choice in field_map:
                    while True:
                        new_value = input(f"Enter the new value for {field_map[choice]}:")

                        if choice == "3":  # Validate email format
                            if not is_valid_email(new_value):
                                print("Invalid email format. Please enter the correct format.")
                                continue
                            else:
                                print(f"{field_map[choice]} successfully updated to {new_value}.")
                                break

                        elif choice == "4":  # Validate phone number format
                            if not is_valid_phone_number(new_value):
                                print("Invalid phone number format. Please enter the correct phone number format.")
                                continue
                            else:
                                print(f"{field_map[choice]} successfully updated to {new_value}.")
                                break

                        elif choice == "9":  # Transaction must be an integer
                            if not new_value.isdigit():
                                print("Invalid transaction value. Please enter an integer.")
                                continue
                            else:
                                new_value = int(new_value)  # Convert to integer for update
                                print(f"{field_map[choice]} successfully updated to {new_value}.")
                                break

                        elif choice == "10":  # Validate status
                            available_statuses = get_status_options()
                            if not available_statuses:
                                print("No status options found in the database.")
                                break
                            if new_value.lower() not in [status.lower() for status in available_statuses]:
                                print("Invalid status. Please choose from the available options.")
                                print("Available Statuses:", ", ".join(available_statuses))
                                continue
                            else:
                                print(f"{field_map[choice]} successfully updated to {new_value}.")
                                break

                        else:
                            print(f"{field_map[choice]} successfully updated to {new_value}.")
                            break
                #Ask confirmation 
                    if confirm_action("\nDo you wat to save this lead? (yes/no):"):
                        update_leads(new_value, field_map[choice], lead_id)
                        print("Update saved successfully.")
                    else:
                        print("Update canceled.")
                else:
                    print("Invalid choice. Please enter a number between 1-10.")
            else: 
                print("Email not found")
        elif user_input == "2":
            return
        else:
            print("Invalid choice. Please enter 1 or 2.")

#Delete data function

def delete_data():
    """Function to delete leads based on user input."""
    
    while True:
        print("====DELETE DATA LEAD=====")

        # Show options to the user
        print("\nOptions:")
        print("1. Delete lead by email")
        print("2. Back to Main Menu")

        user_input = input("Enter Choice: ")

        if user_input == "1":  # Delete lead by email
            show_all_leads()
            email = input("Enter the email of the lead you want to delete: ")

            #use confirmation action function
            if confirm_action("\nDo you want to delete  this lead? (yes/no):"):
                delete_lead_by_email(email)
                print(f"Lead with this email {email}has been successfully deleted")
            else:
                print("Lead deletation has been cancelled")
        elif user_input == "2":  # Back to Main Menu
            return  # Exit back to the main menu
        else:
            print("Invalid choice. Please enter 1 or 2.")

#Option to Manage Deleted Leads 

def handleDeletedLeads():
    """Function to give users options to either restore or permanently delete leads."""
    
    while True:
        print("======= MANAGE DELETED LEADS =======")

        # Show options to the users 
        print("\nOptions:")
        print("1. Delete Lead Permanently")
        print("2. Restore Lead")
        print("3. Back to Main Menu ")

        user_input = input("Enter Choice: ")

        if user_input == "1":  # Delete Lead by email 
            deleted_leads = show_deleted_leads()  # Fetch and display deleted leads
            if deleted_leads:  # Only ask for email if there are deleted leads
                email = input("\nEnter email of the lead to delete permanently: ")
                result = permanently_delete_lead_by_email(email)
                if not result:
                    print("Operation could not be completed as no matching lead was found.")
                else:
                    print("Lead successfully deleted.")
            else:
                print("No deleted leads available to delete.")

        elif user_input == "2":  # Restore deleted lead by email 
            deleted_leads = show_deleted_leads()  # Fetch and display deleted leads
            if deleted_leads:  # Only ask for email if there are deleted leads
                email = input("\nEnter email of the lead to restore: ")
                restore_result = restore_lead_by_email(email)
                if not restore_result:
                    print("Operation could not be completed as no matching lead was found.")
                else:
                    print("Lead successfully restored.")
            else:
                print("No deleted leads available to restore.")

        elif user_input == "3":  # User will return to the main menu
            print("Returning to the main menu...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

            
#report data function 
def report_menu():
    while True:
        print("\n==== Reporting Menu ====")
        print("1. Generate Summary Report")
        print("2. Back to Main Menu")
    
        choice = input("Enter your choice: ")

        if choice == "1":
            data_leads = show_all_leads()
            # Check if data_leads is None
            if data_leads is None:
                print("Error retrieving data leads. Please try again later.")
                continue  # Optionally loop back to the menu
            
            report = generate_summary_report(data_leads)

            if report:  # Check if the report is not None or empty
                print("\n============ Summary Report ===========")
                for sector, count in report.items():
                    print(f"{sector}: {count}")
                input("\nPress Enter to continue...")
            else:
                print("No report data available.")
        
        elif choice == "2":
            print("Returning to the main menu...")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")



def login():
        
    while True:

        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if check_user_credential(username, password):
            print("Login successful!")
            return True
        else:
            print("Invalid username or password. Please try again.")




# /===== Main Program =====/
# Create your main program here
# Main program loop
while True:
    if login():  # Only proceed if the login is successful
        while True:
            menu_choice = main_menu_choice()
            if menu_choice == 1:
                show_data_leads()
            elif menu_choice == 2:
                create_data_lead()  
            elif menu_choice == 3:
                update_data_lead()  
            elif menu_choice == 4:
                delete_data()  
            elif menu_choice == 5:
                handleDeletedLeads()
            elif menu_choice == 6:
                report_menu()
            elif menu_choice == 7:
                print("Exiting program, Goodbye!")
                exit()  # Break the outer loop and exit the program
            else:
                print("Invalid choice. Please select a valid option.")    
    else:
        # Failed login, retry
        print("Login failed. Please try again.")
        