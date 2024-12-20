import psycopg2
from datetime import datetime
conn = psycopg2.connect(dbname="postgres", host="localhost", user="postgres", password="12345", port="5432")
cursor = conn.cursor()

class educationsTable():
    def show_educations_table():
        cursor.execute("SELECT * FROM educations")
        lst = cursor.fetchall()
        return sorted(lst)

    def add_to_educations_table(edu_id,eduType):
        try:
            cursor.execute("INSERT INTO educations (edu_id,edu) VALUES (%s,%s)", (edu_id,eduType))
            conn.commit()
        except (psycopg2.errors.UniqueViolation):
            conn.commit()
            return "repeat"
        
    def delete_from_education_table(edu_id):
        if edu_id not in [i[0] for i in educationsTable.show_educations_table()]:
            conn.commit()
            return "Not in table"
        try:
            cursor.execute("DELETE FROM educations WHERE edu_id=%s", (edu_id,))
            conn.commit()
        except (psycopg2.errors.ForeignKeyViolation):
            conn.commit()
            return "FK error"
        
    def update_education_table(edu_id, eduType):
        if edu_id not in [i[0] for i in educationsTable.show_educations_table()]:
            conn.commit()
            return "Not in table"
        cursor.execute("UPDATE educations SET edu =%s WHERE edu_id=%s", (eduType, edu_id))
        conn.commit()
        

class unitsTable():
    def show_units_table_by_name(unit):
        cursor.execute("SELECT id_units FROM units WHERE unit = %s", (unit,))
        unitId = cursor.fetchall()[0]
        cursor.execute("SELECT DISTINCT id_employee FROM string_a WHERE id_units = %s", (unitId,))
        employeesId = cursor.fetchall()
        employeesNames = []
        for item in employeesId:
            cursor.execute("SELECT surname FROM employees WHERE id_employee = %s",(item[0],))
            name = cursor.fetchall()[0]
            employeesNames.append(name)
        return employeesNames
        
    def show_units_table():
        cursor.execute("SELECT * FROM units")
        lst = cursor.fetchall()
        return sorted(lst)

    def add_to_units_table(unit):
        try:
            cursor.execute("INSERT INTO units (unit) VALUES (%s)", (unit,))
            conn.commit()
        except (psycopg2.errors.UniqueViolation):
            conn.commit()
            return "repeat"
       

    def delete_from_units_table(unit_id):
        if unit_id not in [i[0] for i in unitsTable.show_units_table()]:
            conn.commit()
            return "Not in table"
        try:
            cursor.execute("DELETE FROM units WHERE id_units=%s", (unit_id,))
            conn.commit()
        except (psycopg2.errors.ForeignKeyViolation):
            conn.commit()
            return "FK error"

    def update_units_table(unit_id, unit):
        if unit_id not in [i[0] for i in unitsTable.show_units_table()]:
            conn.commit()
            return "Not in table"
        cursor.execute("UPDATE units SET unit =%s WHERE id_units=%s", (unit, unit_id))
        conn.commit()
        

class positionsTable():
    def show_positions_table_by_name(post):
        cursor.execute("SELECT id_post FROM positions WHERE post = %s", (post,))
        postId = cursor.fetchall()[0]
        cursor.execute("SELECT DISTINCT id_employee FROM string_a WHERE id_post = %s", (postId,))
        employeesId = cursor.fetchall()
        employeesNames = []
        for item in employeesId:
            cursor.execute("SELECT surname FROM employees WHERE id_employee = %s",(item[0],))
            name = cursor.fetchall()[0]
            employeesNames.append(name)
        return employeesNames
    
    def show_positions_table():
        cursor.execute("SELECT * FROM positions")
        lst = cursor.fetchall()
        return sorted(lst)

    def add_to_positions_table(post):
        try:
            cursor.execute("INSERT INTO positions (post) VALUES (%s)", (post,))
            conn.commit()
        except (psycopg2.errors.UniqueViolation):
            conn.commit()
            return "repeat"
            
    def delete_from_positions_table(post_id):
        if post_id not in [i[0] for i in positionsTable.show_positions_table()]:
            conn.commit()
            return "Not in table"
        try:
            cursor.execute("DELETE FROM positions WHERE id_post=%s", (post_id,))
            conn.commit()
        except (psycopg2.errors.ForeignKeyViolation):
            conn.commit()
            return "FK error"

    def update_positions_table(post_id, post):
        if post_id not in [i[0] for i in positionsTable.show_positions_table()]:
            conn.commit()
            return "Not in table"
        cursor.execute("UPDATE positions SET post =%s WHERE id_post=%s", (post, post_id))
        conn.commit()

class employeesTable():
    def show_employees_table_by_edu(edu_id = None):
        cursor.execute("SELECT surname FROM employees WHERE edu_id =%s", (edu_id,))
        lst = cursor.fetchall()
        return sorted(lst)
    def show_employees_table():
        cursor.execute("SELECT  id_employee, surname, phone_number, edu FROM employees JOIN educations ON employees.edu_id = educations.edu_id")
        lst = cursor.fetchall()
        return sorted(lst)

    def add_to_employees_table(surname, phone_num, edu_id):
        try:
            cursor.execute("INSERT INTO employees (surname, phone_number, edu_id) VALUES (%s,%s,%s)", (surname,phone_num, edu_id))
            conn.commit()
        except (psycopg2.errors.UniqueViolation):
            conn.commit()
            return "repeat"
        

    def delete_from_employees_table(employee_id):
        if employee_id not in [i[0] for i in employeesTable.show_employees_table()]:
            conn.commit()
            return "Not in table"
        cursor.execute("DELETE FROM employees WHERE id_employee=%s", (employee_id,))
        conn.commit()

    def update_employees_table(employee_id,surname, phone_number, edu_id):
        if employee_id not in [i[0] for i in employeesTable.show_employees_table()]:
            conn.commit()
            return "Not in table"
        if surname:
            cursor.execute("UPDATE employees SET surname=%s WHERE id_employee=%s", (surname,employee_id))
        if phone_number:
            cursor.execute("UPDATE employees SET phone_number=%s WHERE id_employee=%s", (phone_number,employee_id))
        if edu_id:
            cursor.execute("UPDATE employees SET edu_id=%s WHERE id_employee=%s", (edu_id,employee_id))
        conn.commit()
        
class stringsTable():
    def show_string_a_table_with_ids():
        cursor.execute("SELECT id_string, surname, assign_date, post, unit, salary FROM string_a JOIN employees ON string_a.id_employee = employees.id_employee JOIN positions ON string_a.id_post = positions.id_post \
                        JOIN units ON string_a.id_units = units.id_units")
        lst = cursor.fetchall()
        return sorted(lst)
    
    def show_string_a_table():
        cursor.execute("SELECT surname, assign_date, post, unit, salary FROM string_a JOIN employees ON string_a.id_employee = employees.id_employee JOIN positions ON string_a.id_post = positions.id_post \
                        JOIN units ON string_a.id_units = units.id_units")
        lst = cursor.fetchall()
        return sorted(lst)

    def add_to_string_a_table(empl_id, assign_date, post_id, unit_id, salary):
        try:
            datetime.strptime(assign_date, "%Y-%m-%d")
        except:
            return "Invalid date"
        if datetime.strptime(assign_date, "%Y-%m-%d").date() > datetime.now().date():
            return "Invalid date"
        if salary == "":
            return "Invalid salary"
        try:
            cursor.execute("INSERT INTO string_a (id_employee, assign_date, id_post, id_units, salary) VALUES (%s,%s,%s, %s,%s)", (empl_id, assign_date, post_id, unit_id, salary))
            conn.commit()
        except (psycopg2.errors.InvalidDatetimeFormat):
            conn.commit()
            return "Invalid date"

    def delete_from_string_a_table(string_id):
        if string_id not in [i[0] for i in stringsTable.show_string_a_table_with_ids()]:
            conn.commit()
            return "Not in table"
        cursor.execute("DELETE FROM string_a WHERE id_string=%s", (string_id,))
        conn.commit()

    def update_string_a_table(string_id, assign_date, salary):
        try:
            datetime.strptime(assign_date, "%Y-%m-%d")
        except:
            return "Invalid date"
        if datetime.strptime(assign_date, "%Y-%m-%d").date() > datetime.now().date():
            return "Invalid date"
        if salary == "":
            conn.commit()
            return "Invalid salary"
        if string_id not in [x[0] for x in stringsTable.show_string_a_table_with_ids()]:
            conn.commit()
            return "Not in table"
        if assign_date:
            try:
                cursor.execute("UPDATE string_a SET assign_date=%s WHERE id_string=%s", (assign_date,string_id))
                conn.commit()
            except (psycopg2.errors.InvalidDatetimeFormat):
                conn.commit()
                return "Invalid date"
        if salary:
            cursor.execute("UPDATE string_a SET salary=%s WHERE id_string=%s", (salary,string_id))
        conn.commit()