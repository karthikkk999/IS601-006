from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')
import pycountry

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # UCID: sk3374@njit.edu || Date: 4/8/2023
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *
    
    query = " SELECT c.id, c.name, c.address, c.city, c.country, c.state, c.zip, c.website, (SELECT COUNT(e.id) FROM IS601_MP3_Employees e WHERE e.company_id = c.id) as employees FROM IS601_MP3_Companies c WHERE 1=1"
    args = [] # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    allowed_list = [(v, v) for v in allowed_columns]
    # TODO search-2 get name, country, state, column, order, limit request args
    # UCID: sk3374@njit.edu || Date: 4/8/2023
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit")

    # UCID: sk3374@njit.edu || Date: 4/8/2023
    # TODO search-3 append a LIKE filter for name if provided
    # TODO search-4 append an equality filter for country if provided
    # TODO search-5 append an equality filter for state if provided
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    if name:
        query += " AND name LIKE %s"
        args.append(f"%{name}%")

    if country:
        query += " AND country LIKE %s"
        args.append(f"%{country}%")

    if state:
        query += " AND state LIKE %s"
        args.append(f"%{state}%")

    if column and order and column in allowed_columns and order.lower() in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"

    if limit and (int(limit) <= 0 or int(limit) > 100):
        flash("Enter the limit between 1 and 100", 'warning')
    else:
        limit = int(limit) if limit else 10
        query += " LIMIT %s"
        args.append(limit)
    
    print("query",query)
    print("args", args)

    try:
        result = DB.selectAll(query, *args)
        #print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        # UCID: sk3374@njit.edu || Date: 4/8/2023
        flash(f"There was an error processing your search. {str(e)}", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    allowed_columns = [(col, col.capitalize()) for col in allowed_columns]
    
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_list)

@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # UCID: sk3374@njit.edu || Date: 4/8/2023
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zipcode = request.form.get("zip")
        website = request.form.get("website")

        has_error = False # use this to control whether or not an insert occurs
        
        # UCID: sk3374@njit.edu || Date: 4/8/2023
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        # TODO add-8 zipcode is required (flash proper error message)
        
        if not name:
            flash("Name is required", "danger")
            has_error = True

        if not address:
            flash("Address is required", "danger")
            has_error = True

        if not city:
            flash("City is required", "danger")
            has_error = True

        if not state:
            flash("State is required", "danger")
            has_error = True        
            state_code = country + "-" + state            
            state_name = pycountry.subdivisions.get(code=state_code).name
            if state_name.lower() not in [s.name.lower() for s in pycountry.subdivisions.get(country_code=country.upper())]:
                flash("Enter valid state", 'danger')
                return redirect("edit")

        
        if not country:
            flash("Country is required", "danger")
            has_error = True        
            country_name = pycountry.countries.get(alpha_2=country)
            if country_name is None:
                flash("Enter valid country", 'danger')
                return redirect("edit")
            
            
        if not zipcode:
            flash("Zipcode is required", "danger")
            has_error = True


        if not has_error:
            try:
                # UCID: sk3374@njit.edu || Date: 4/8/2023
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies
                (name, address, city, country, state, zip, website) VALUES(%s, %s, %s, %s, %s, %s, %s)
                """, name, address, city, country, state, zipcode, website) # <-- TODO add-8 add query and add arguments
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash(f"There was an error adding the company. str{e}", "danger")
        
    return render_template("add_company.html")

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    # UCID: sk3374@njit.edu || Date: 4/8/2023
    id = id = request.args.get("id")

    if not id: # TODO update this for TODO edit-1
        flash("Company ID is required", "danger")
        return redirect(url_for("company.search"))
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            # UCID: sk3374@njit.edu || Date: 4/8/2023
            name = request.form.get("name")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            zipcode = request.form.get("zip")
            website = request.form.get("website") or ''

            has_error = False # use this to control whether or not an insert occurs
            # TODO edit-2 name is required (flash proper error message)
            # TODO edit-3 address is required (flash proper error message)
            # TODO edit-4 city is required (flash proper error message)
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            # TODO edit-8 zipcode is required (flash proper error message)
            # UCID: sk3374@njit.edu || Date: 4/8/2023
            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings

            if not name:
                flash("Name is required", "danger")
                has_error = True

            if not address:
                flash("Address is required", "danger")
                has_error = True

            if not city:
                flash("City is required", "danger")
                has_error = True

            if not state:
                flash("State is required", "danger")
                has_error = True
                state_code = country + "-" + state
                state_name = pycountry.subdivisions.get(code=state_code).name                
                if state_name.lower() not in [s.name.lower() for s in pycountry.subdivisions.get(country_code=country.upper())]:
                    flash("Enter valid state", 'danger')
                    return redirect("edit")

            if not country:
                flash("Country is required", "danger")
                has_error = True
                country_name = pycountry.countries.get(alpha_2=country)
                if country_name is None:
                    flash("Enter valid country", 'danger')
                    return redirect("edit")

            if not zipcode:
                flash("Zipcode is required", "danger")
                has_error = True
            
            if not has_error:
                try:
                    # UCID: sk3374@njit.edu || Date: 4/8/2023
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website

                    result = DB.update("""
                    UPDATE IS601_MP3_Companies 
                    SET name = %s, address = %s, city = %s, country = %s, state = %s, zip = %s, website = %s
                    WHERE id = %s""", name, address, city, country, state, zipcode, website, id)
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    # UCID: sk3374@njit.edu || Date: 4/8/2023
                    flash(f"There was an error updating the company. {str(e)}", "danger")
    row = {}
    try:
        # TODO edit-11 fetch the updated data
        # UCID: sk3374@njit.edu || Date: 4/8/2023
        result = DB.selectOne("SELECT name, address, city, country, state, zip, website FROM IS601_MP3_Companies WHERE id = %s", (id,))
        if result.status:
            row = result.row
            
    except Exception as e:
        # TODO edit-12 make this user-friendly
        # UCID: sk3374@njit.edu || Date: 4/8/2023
        flash(f"There was an error fetching the company data. {str(e)}", "danger")
    # TODO edit-13 pass the company data to the render template
    # UCID: sk3374@njit.edu || Date: 4/8/2023
    return render_template("edit_company.html", company=row)

@company.route("/delete", methods=["GET"])
    # UCID:sk3374@njit.edu || Date: 4/9/2023
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
def delete():

    id = request.args.get("id")

    if not id:
        flash("company ID id required", "danger")
        return redirect(url_for("company.search")) 
    try:
        DB.update("UPDATE IS601_MP3_Employees SET company_id = NULL WHERE company_id = %s", id)
        result = DB.delete("DELETE FROM IS601_MP3_Companies WHERE id = %s", id)

        if result.status:
            flash("Deleted company and unassigned associated employees", "success")
    except Exception as e:
        flash(f"There was an error deleting the company. {str(e)}", "danger")

    query_params = request.args.copy()
    query_params.pop("id", None)
    return redirect(url_for("company.search", **query_params))
    