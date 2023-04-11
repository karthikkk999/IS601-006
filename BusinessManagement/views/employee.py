from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import re

employee = Blueprint('employee', __name__, url_prefix='/employee')

# UCID: sk3374 || Date: 4/8/2023
def is_valid_email(email):
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, email)


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    # UCID: sk3374 || Date: 4/8/2023
    query = """
        SELECT e.id, e.first_name, e.last_name, e.email, c.id as company_id, IF(c.name is null, 'N/A', c.name) as company_name
        FROM IS601_MP3_Employees e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id WHERE 1=1
    """

    args = [] # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    allowed_list = [(v, v) for v in allowed_columns]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    # UCID: sk3374 || Date: 4/8/2023 
    fn = request.args.get("fn")
    ln = request.args.get("ln")
    email = request.args.get("email")
    company = request.args.get("company")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", default=10)

    # TODO search-3 append like filter for first_name if provided
    # UCID: sk3374 || Date: 4/8/2023
    if fn:
        query += " AND first_name LIKE %s"
        args.append(f"%{fn}%")

    # TODO search-4 append like filter for last_name if provided
    # UCID: sk3374 || Date: 4/8/2023
    if ln:
        query += " AND last_name LIKE %s"
        args.append(f"%{ln}%")

    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND email LIKE %s"
        args.append(f"%{email}%")

    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += f" AND company_id = {company}"

    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"

    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds    
    if limit and (int(limit) <= 0 or int(limit) > 100):
        flash("Enter the limit between 1 and 100", 'warning')
    else:
        limit = int(limit) if limit else 10
        query += " LIMIT %s"
        args.append(limit)
        
    print("query", query)
    print("args", args)
    
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        # UCID: sk3374 || Date: 4/8/2023
          flash("An error occurred while searching for employees.", "danger")

    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    # # UCID: sk3374 || Date: 4/8/2023
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_list)
 
@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        has_error = False # use this to control whether or not an insert occurs
    
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # UCID: sk3374 || Date: 4/8/2023 
        
        first_name = str(request.form.get("first_name"))
        last_name = str(request.form.get("last_name"))
        company = request.form.get("company")
        email = str(request.form.get("email"))

        # TODO add-2 first_name is required (flash proper error message)
        # UCID: sk3374 || Date: 4/8/2023
        if not first_name:
            flash("first name is required.", "danger")
            has_error = True

        # TODO add-3 last_name is required (flash proper error message)
        # UCID: sk3374 || Date: 4/8/2023
        if not last_name:
            flash("last name is required.", "danger")
            has_error = True

        # TODO add-4 company (may be None)
        # company variable is already retrieved
        # UCID: sk3374 || Date: 4/8/2023
        if not company:
            company = None

        # TODO add-5 email is required (flash proper error message)
        # UCID: sk3374 || Date: 4/8/2023
        if not email:
            flash("email is required.", "danger")
            has_error = True
        # TODO add-5a verify email is in the correct format
        # UCID: sk3374 || Date: 4/8/2023
        elif not is_valid_email(email):
            flash("invalid email format.", "danger")
            has_error = True

            
        if not has_error:
            try:
                # UCID: sk3374 || Date: 4/8/2023
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees
                (first_name, last_name, company_id, email) VALUES (%s, %s, %s, %s);
                """, first_name, last_name, company, email)  # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                flash(f"An error occurred while adding the employee.{str(e)}", "danger")
    return render_template("add_employee.html")

@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    #UCID: sk3374@njit.edu || Date: 4/8/2023
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("Employee ID is required.", "danger")
        return redirect(url_for("employee.search"))
    else:
        if request.method == "POST":
            
            has_error = False # use this to control whether or not an insert occurs
            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            #UCID: sk3374@njit.edu || Date: 4/8/2023
            first_name = str(request.form.get("first_name"))
            last_name = str(request.form.get("last_name"))
            company = request.form.get("company")
            email = str(request.form.get("email"))
            
            # TODO edit-2 first_name is required (flash proper error message)
            #UCID: sk3374@njit.edu || Date: 4/8/2023
            if not first_name:
                flash("First name is required.", "danger")
                has_error = True
                return redirect("add")

            # TODO edit-3 last_name is required (flash proper error message)
            #UCID: sk3374@njit.edu || Date: 4/8/2023
            if not last_name:
                flash("Last name is required.", "danger")
                has_error = True
                return redirect("add")

            # TODO edit-4 company (may be None)
            # company variable is already retrieved
            #UCID: sk3374@njit.edu || Date: 4/8/2023
            if not company:
                company = None

            # TODO edit-5 email is required (flash proper error message)
            #UCID: sk3374@njit.edu || Date: 4/8/2023
            if not email:
                flash("Email is required.", "danger")
                has_error = True
            # TODO edit-5a verify email is in the correct format
            #UCID: sk3374@njit.edu || Date: 4/8/2023
            elif not is_valid_email(email):
                flash("Invalid email format.", "danger")
                has_error = True
                
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    #UCID: sk3374@njit.edu || Date: 4/8/2023
                    result =  DB.update("""
                    UPDATE IS601_MP3_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s WHERE id = %s
                    """,first_name,last_name,company, email, id)
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    #UCID: sk3374@njit.edu || Date: 4/8/2023
                    flash("An error occurred while updating the employee.", "danger")
        row = {}
        try:
            # TODO edit-8 fetch the updated data 
            
            result = DB.selectOne("""
            SELECT e.id as id, e.first_name, e.last_name, e.email, c.id as company_id, c.name as company_name
            FROM IS601_MP3_Employees e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id
            WHERE e.id = %s
            """, (id,))
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(f"An error occurred while fetching employee data. {str(e)}", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", employee=row)

@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    # TODO delete-1 delete employee by id

    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    
    id = request.args.get("id")

    if not id:
        flash("Employee ID id required", "danger")
        return redirect(url_for("employee.search")) 
    try:
        result = DB.delete("DELETE FROM IS601_MP3_Employees WHERE id = %s", id)
        if result.status:
            flash("Deleted Employee", "success")
    except Exception as e:
        flash(f"There was an error deleting the employee. {str(e)}", "danger")

    query_params = request.args.copy()
    query_params.pop("id", None)
    return redirect(url_for("employee.search", **query_params))
    