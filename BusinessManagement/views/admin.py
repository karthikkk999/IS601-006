import io
from flask import Blueprint, render_template, request, redirect, flash
import csv
from werkzeug.utils import secure_filename
from sql.db import DB
import traceback
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route("/import", methods=["GET","POST"])
def importCSV():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file', "warning")
            return redirect(request.url)
        # TODO importcsv-1 check that it's a .csv file, return a proper flash message if it's not
        # UCID: sk3374
        # Time Added: 4/8/23 7:02 PM
        # added an another condition to the below if which checks for the file extension ".csv"
        if file and secure_filename(file.filename) and file.filename.endswith('.csv'):
            companies = []
            employees = []
            # DON'T EDIT
            company_query = """
            INSERT INTO IS601_MP3_Companies (name, address, city, country, state, zip, website)
                        VALUES (%(name)s, %(address)s, %(city)s, %(country)s, %(state)s, %(zip)s, %(website)s)
                        ON DUPLICATE KEY UPDATE 
                        address=values(address),
                        city=values(city),
                        country=values(country),
                        state=values(state),
                        zip=values(zip),
                        website=values(website)
            """
            # DON'T EDIT
            employee_query = """
             INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, (SELECT id FROM IS601_MP3_Companies WHERE name = %(company_name)s LIMIT 1))
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, 
                        last_name = %(last_name)s, email = %(email)s, 
                        company_id = (SELECT id FROM IS601_MP3_Companies WHERE name=%(company_name)s LIMIT 1)
            """
            # Note: this reads the file as a stream instead of requiring us to save it
            # TODO importcsv-2 read the csv file stream as a dict
            stream = io.TextIOWrapper(file.stream._file, "UTF8", newline=None)

            csv_reader = csv.DictReader(stream)

            for row in csv_reader:
                pass # todo remove
                # print(row) #example
                # TODO importcsv-3 extract company data and append to company list 
                # as a dict only with company data if all is present
                if all(field in row for field in ['name', 'address', 'city', 'country', 'state', 'zip', 'website']):
                    company = {key: row[key] for key in ['name', 'address', 'city', 'country', 'state', 'zip', 'website']}
                    companies.append(company)

                # TODO importcsv-4 extract employee data and append to employee list 
                # as a dict only with employee data if all is present
                if all(field in row for field in ['first_name', 'last_name', 'email', 'company_name']):
                    employee = {key: row[key] for key in ['first_name', 'last_name', 'email', 'company_name']}
                    employees.append(employee)
               
               
            if len(companies) > 0:
                print(f"Inserting or updating {len(companies)} companies")
                try:
                    result = DB.insertMany(company_query, companies)
                    # TODO importcsv-5 display flash message about number of companies inserted
                    flash(f"{len(companies)} companies inserted or updated", "success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                # TODO importcsv-6 display flash message (info) that no companies were loaded
                flash("No companies were loaded", "info")
                #pass

            if len(employees) > 0:
                print(f"Inserting or updating {len(employees)} employees")
                try:
                    result = DB.insertMany(employee_query, employees)
                    # TODO importcsv-7 display flash message about number of employees loaded
                    flash(f"{len(employees)} employees inserted or updated", "success")
                except Exception as e:
                    traceback.print_exc()
                    flash("There was an error loading in the csv data", "danger")
            else:
                 # TODO importcsv-8 display flash message (info) that no employees were loaded
                flash("No employees were loaded", "info")
                #pass
            try:
                result = DB.selectOne("SHOW SESSION STATUS LIKE 'questions'")
                print(f"Result {result}")
            except Exception as e:
                    traceback.print_exc()
                    flash("There was an error counting session queries", "danger")
    return render_template("upload.html")
