# Python CRUD Application for [Business Domain]

A comprehensive Python application for managing lead data with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project caters to the sales and marketing industry, specifically addressing the need to manage lead data efficiently. Lead data plays a crucial role in optimizing sales pipelines, tracking customer interactions, and improving conversion rates, ensuring that businesses can target the right prospects and streamline their sales processes effectively.

**Benefits:**

* Improved data accuracy and consistency in lead tracking
* Streamlined data management processes for the sales and marketing teams
* Increased efficiency in tracking customer interactions and follow-ups
* Facilitated collaboration between sales and marketing teams for unified strategies
* Reduced time spent on manual data entry and management tasks


**Target Users:**

This application is designed for sales representatives and marketing professionals within the organization to facilitate their tracking and management of lead data related to sales opportunities and customer interactions.

## Features

* **Create:**
    * Add new lead entries with essential details like Lead ID, First Name, Last Name, Email, Phone Number, Company Sector, Lead Source, Date Created, Sales Representative, and Transaction.
    * Implement validation rules to ensure data integrity, including:
    * Unique Lead ID and Email checks to prevent duplicates.
    * Format checks for Email and Phone Number to ensure valid input.
    * Validation for Company Sector, Lead Source, and Date Created to ensure proper entries.
* **Read:**
    * Search and retrieve specific lead records by applying filters based on Company Sector and other relevant fields.
    * Display comprehensive information for each lead in a user-friendly format.
    * The code implements a function to show data leads and includes the following features:
        -Menu Display: Presents options to show all data records, search for specific records, or return to the main menu.
        -Show All Data Records: If the data leads list is not empty, it calls a function to display all leads; otherwise, it informs the user that no data is available.
        -Search Data Records: Prompts the user to enter a company sector for searching. It performs a case-insensitive search through the leads and displays matching records.
        -Return to Main Menu: Allows the user to exit the read menu and go back to the main menu.
        -Error Handling: Catches invalid input and provides user-friendly feedback for incorrect choices.
* **Update:**
    * Modify existing lead data to reflect changes in various attributes, such as Lead ID, First Name, Last Name, Email, Phone Number, Company Sector, Lead Source, and Date Created.
    * Provide clear confirmation or error messages based on the success or failure of the update operation.
    - Menu Display: Presents options to update data leads or return to the main menu.
    - Find Lead by Email: Prompts the user for the email of the lead they want to update. If found, it displays the current details of the lead.
    - Re-confirmation: Before making any updates, it confirms with the user to ensure they want to proceed.
    - Select Attribute to Update: Allows the user to choose which attribute of the lead they want to update and validates the input for each field.
    - Confirmation to Save Changes: After making an update, the user is asked to confirm whether they want to save the changes. If they choose not to save, the original values are restored.
    - Error Handling: Handles cases where the lead is not found or where the user inputs invalid data.
* **Delete:**
    * Allow for the removal of unwanted lead records with appropriate authorization checks.
    * Implement soft delete functionality to prevent permanent data loss by moving deleted leads to a separate list.
    * Consider offering data restoration capabilities for deleted leads.
    - Deletion by Email: Users can delete leads based on their email address, with a confirmation prompt to avoid accidental deletions.
    - Soft Deletion: Deleted leads are not permanently removed; instead, they are moved to a separate list for potential restoration.
    - Restoration: Users can restore deleted leads back to the active leads list using their email addresses.
    - Viewing Deleted Leads: Users can view all deleted leads to make informed decisions about restoration.
    - Error Handling: The function includes checks for valid input and feedback if leads cannot be found.
* **Security:**
    * Implement user authentication and authorization mechanisms to control access to different CRUD operations.
    * Use hashed passwords for secure storage and validation.
    * Limit access based on user roles (e.g., admin, user) if applicable.
    - Username and Password Input: Prompts the user for their username and password.
    - Password Hashing: Uses SHA-256 hashing to securely store and verify passwords, preventing plain-text password storage.
    - User Role Return: Returns the user's role upon successful login, allowing for role-based access control in the application.
    - Loop for Retry: If login fails, the function continues to prompt the user until they successfully log in or exit.
* **Reporting:**
    * Generate reports or summaries based on lead data to support business functions.
    * Export data in various formats (e.g., CSV, Excel) for further analysis.
    - Summary Report Generation: The generate_summary_report function counts the number of leads in each company sector and returns a dictionary containing the sector names and their corresponding counts.
    - CSV Export: The export_to_csv function creates a CSV file from the list of data leads using Python's built-in csv module. It writes the headers and each lead's data to the file.
    - Excel Export: The export_to_excel function utilizes the pandas library to create an Excel file from the data leads. It converts the data into a DataFrame and exports it to an Excel file.
    - Menu Navigation: The report_menu function provides a user-friendly interface for generating reports and exporting data. It includes input validation and prompts the user for necessary information.

## Installation

1. **Prerequisites:**
    * Python version: 3.7 or higher
    * Additional dependencies:
    - pandas: For data manipulation and analysis (especially for exporting to Excel).
    - openpyxl: Required for writing Excel files.
    - Any other packages your project depends on.

2. **Installation:**
    ```git clone https://github.com/bayu-prasetya/python_crud_program.git
cd python_crud_program
pip install -r requirements.txt  # If using a requirements.txt file

    ```

3. **Database Setup (if applicable):**
    All data is stored in variables within the code. You can modify these variables directly in the source code to adjust the initial dataset.
Look for the data_lead variable in main.py (or the appropriate file) to update or change the leads as needed.
## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new lead record by providing details such as lead ID, first name, last name, email, phone number, company sector, lead source, and date created.
    * **Read:** Search and retrieve lead information by criteria such as email, company sector, or lead ID.
    * **Update:** Modify lead details, such as updating their contact information or company sector.
    * **Delete:** Remove a lead record from the system, with an option to restore deleted leads if necessary (soft delete functionality).

## Data Model
This project utilizes a [Data Structure] (e.g., relational database, JSON documents) to represent [Data Entity] data. The following fields are typically stored:
   * Lead ID: (Integer) - A unique identifier for each lead, used to distinguish between different leads in the system.
   * First Name: (String) - The first name of the lead, essential for personalization in communication.
   * Last Name: (String) - The last name of the lead, used in conjunction with the first name for full identification.
   * Email: (String) - The lead's email address, used for communication and marketing purposes. Must be validated for correct format.
   * Phone Number: (String) - The lead's phone number, used for direct communication. Must follow a specified format and length.
   * Company Sector: (String) - The industry or sector in which the lead's company operates, useful for categorization and targeted marketing.
   * Lead Source: (String) - The origin of the lead, indicating how the lead was acquired (e.g., referral, online ad).
   * Date Created: (String) - The date when the lead was added to the system, useful for tracking the age of leads and follow-up timing.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to [belamoneta@gmail.com] or submit an issue if you encounter any problems or have suggestions for improvements.

