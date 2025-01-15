
#This file filled with functions for basic CRUD 
import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

def create_connection():
    """This function is to create and return a database connection"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="XXX", #your password here
            database="LeadManagementDB"
        )
        if connection.is_connected():  #if connection work, then execute 
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
    
def check_user_credential(username, password):
    """This function is to check user credential"""
    query = "Select * from valid_user where  username = %s and password = %s"
    params = (username, password)
    result = fetch_query(query, params)
    return len(result) > 0 if result else False


def fetch_query(query, params=None):
    """
    Execute a SELECT query and return the result.
    """
    connection = create_connection()
    if not connection:
        print("Failed to establish a connection.")
        return []  # Return an empty list if the connection fails

    result = None
    cursor = connection.cursor(dictionary=True) 
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
        if not result:  # If no records are found, return an empty list
            return []
    except Error as e:
        print(f"Error: {e}")
        return []  # Return an empty list if an error occurs
    finally:
        cursor.close()
        connection.close()

    return result


def print_lead(lead):
    """Format and print a single lead in a readable table format."""
    headers = ["Field", "Value"]
    table = [[key.replace('_', ' ').capitalize(), value] for key, value in lead.items()]
    print(tabulate(table, headers=headers, tablefmt="grid"))


def execute_query(query, params=None): #think as query as order and params specific request to customize your order
    """This funnction will execute query that modified the data INSERT, UPDATE, DELETE"""
    connection = create_connection()
    if connection:
        cursor= connection.cursor() #cursor works as a bookmark: it helps mark position in the database
        try: 
            cursor.execute(query, params)
            connection.commit() #finalize the chages 
            if cursor.rowcount == 0 :  #to check if there is any matching record in the database
                print("No matching record found ")
                return False
            else:
                return True
        except Error as e:
            print(f"Error : {e}")
        finally:
            cursor.close()
            connection.close()

def show_all_data_records():
    """Fetch and display all leads in a tabular format."""
    query = "SELECT * FROM data_lead"
    leads = fetch_query(query)
    if leads:  # Check if leads is not empty
        print("======= ALL DATA LEADS =======")
        headers = ["Lead ID", "First Name", "Last Name", "Email", "Phone Number", "Company Sector", "Lead Source", "Date Created", "Sales Rep", "Transaction", "Status"]
        table = [[
            lead['lead_id'], lead['first_name'], lead['last_name'], lead['email'], lead['phone_number'],
            lead['company_sector'], lead['lead_source'], lead['date_created'], lead['sales_rep'],
            lead['transaction'], lead['status']
        ] for lead in leads]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    else:
        print("No data leads found.")
        return []
    
def get_deleted_leads():
    """This function is to fetch and return all deleted leads """
    query = "SELECT * from deleted_leads"
    return  fetch_query(query)

def show_deleted_leads():
    """This function is to fetch and display all deleted leads."""
    deleted_leads = get_deleted_leads()  # Fetch deleted leads from the data source
    if deleted_leads:  # Check if there are any deleted leads
        print("========= DELETED LEADS ============")
        for lead in deleted_leads:
            print(f"ID: {lead['lead_id']}, Name: {lead['first_name']}, Last Name: {lead['last_name']}, "
                  f"Email: {lead['email']}, Phone Number: {lead['phone_number']}, "
                  f"Company Sector: {lead['company_sector']}, Lead Source: {lead['lead_source']}, "
                  f"Date Created: {lead['date_created']}, Sales Representative: {lead['sales_rep']}, "
                  f"Transaction: {lead['transaction']}, Status: {lead['status']}")
    else:  # This else corresponds to the if statement, not the for loop
        print("No deleted leads found.")  # Print message if no deleted leads are present


def permanently_delete_lead_by_email(email):
    """This function is to permanently delete a lead by email in deleted_lead table"""
    query = "Delete from deleted_leads where email = %s"
    params = (email)
    return execute_query(query, params)

def restore_lead_by_email(email):
    """Restores a lead from the deleted_leads table to the main data_lead table."""
    
    # Check if the lead exists in the deleted_leads table directly in the main function
    select_query = "SELECT * FROM deleted_leads WHERE email = %s"
    select_params = (email,)
    lead = execute_query(select_query, select_params)

    if not lead:
        return False  # Lead not found in deleted_leads

    # Move the lead back to the main data_lead table
    restore_query = "INSERT INTO data_lead (first_name, last_name, email, phone_number, company_sector, lead_source, date_created, sales_rep, transaction, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    params = (
        email['first_name'], email['last_name'], email['email'], email['phone_number'],
        email['company_sector'], email['lead_source'], email['date_created'],
        email['sales_rep'], email['transaction'], email['status']
    )
    insert_result = execute_query(restore_query, params)
    if not insert_result:
        return False  # Return False if the insertion fails

    # Remove the lead from the deleted_leads table after restoring
    delete_query = "DELETE FROM deleted_leads WHERE email = %s"
    delete_params = (email,)
    execute_query(delete_query, delete_params)
    
    return True  # Return True if everything is successful


def show_all_leads():
    """Fetch and display all leads in a tabular format."""
    query = "SELECT * FROM data_lead"
    leads = fetch_query(query)
    if leads:  # Check if leads is not empty
        print("======= ALL DATA LEADS =======")
        headers = ["Lead ID", "First Name", "Last Name", "Email", "Phone Number", "Company Sector", "Lead Source", "Date Created", "Sales Rep", "Transaction", "Status"]
        table = [[
            lead['lead_id'], lead['first_name'], lead['last_name'], lead['email'], lead['phone_number'],
            lead['company_sector'], lead['lead_source'], lead['date_created'], lead['sales_rep'],
            lead['transaction'], lead['status']
        ] for lead in leads]
        print(tabulate(table, headers=headers, tablefmt="grid"))
        return leads
    else:
        print("No data leads found.")
        return []


def create_new_lead(new_lead):
    """Insert a new lead into the database."""
    query = """
    INSERT INTO data_lead (first_name, last_name, email, phone_number, company_sector, lead_source, date_created, sales_rep, transaction, status)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        new_lead['first_name'], new_lead['last_name'], new_lead['email'], new_lead['phone_number'],
        new_lead['company_sector'], new_lead['lead_source'], new_lead['date_created'],
        new_lead['sales_rep'], new_lead['transaction'], new_lead['status']
    )
    return execute_query(query, params)

def confirm_action(prompt):
    response = input(prompt).strip().lower()
    return response == "yes"


def delete_lead_by_email(email):
    """This function is to delete lead by email"""
    query = "Delete from data_lead where email = %s"
    params = (email,)
    return execute_query(query, params)

def update_leads(new_value, field, lead_id):
    """Update a specific field in the data_lead table based on lead_id."""
    query = f"UPDATE data_lead SET {field} = %s WHERE lead_id = %s"
    params = (new_value, lead_id)
    return execute_query(query, params)
    
def get_company_sectors():
    """Fetch and return all available company sectors."""
    query = "SELECT sector_name FROM leadmanagementdb.company_sector"
    sectors = fetch_query(query)
    return [sector['sector_name'] for sector in sectors] if sectors else []

def get_lead_sources():
    """Fetch and return all available lead sources."""
    query = "SELECT source_name FROM leadmanagementdb.lead_source"
    sources = fetch_query(query)
    return [source['source_name'] for source in sources] if sources else []

def get_sales_representatives():
    """Fetch and return all available sales representatives."""
    query = "SELECT name FROM leadmanagementdb.sales_reps"
    reps = fetch_query(query)
    return [rep['name'] for rep in reps] if reps else []

def get_status_options():
    """Fetch and return all available status options."""
    query = "SELECT status_name FROM leadmanagementdb.status_options"
    statuses = fetch_query(query)
    return [status['status_name'] for status in statuses] if statuses else []

def generate_summary_report(data_leads):
    """Generates a summary report of data leads by sector."""
    report = {}  # This is to hold sector 
    
    # Check if data_leads is valid
    if data_leads is None or not data_leads:
        print("No data leads available.")
        return report  # Return empty report if no data leads are present

    for lead in data_leads:
        # Ensure lead has the expected structure (list or dictionary)
        if isinstance(lead, dict) and 'company_sector' in lead:  # Assuming leads are dictionaries
            sector = lead['company_sector']  # Extract the sector
            
            # Increment the count for this sector in the report
            if sector in report:
                report[sector] += 1
            else:
                report[sector] = 1  # Initialize the count for new sector
        else:
            print("Lead is not a valid structure or missing 'company_sector':", lead)

    return report
