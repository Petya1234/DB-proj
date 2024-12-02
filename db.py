import psycopg2

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
    def show_employees_table():
        cursor.execute("SELECT  id_employee, surname, phone_number, edu FROM employees JOIN educations ON employees.edu_id = educations.edu_id")
        lst = cursor.fetchall()
        return sorted(lst)

    def add_to_employees_table(surname, phone_num, edu_id):
        try:
            cursor.execute("INSERT INTO employees (surname, phone_number, edu_id) VALUES (%s,%s,%s)", (surname,phone_num, edu_id))
        except Exception as e:
            print(type(e))
        conn.commit()
        

    def delete_from_employees_table(employee_id):
        cursor.execute("DELETE FROM employees WHERE id_employee=%s", (employee_id,))
        conn.commit()

    def update_employees_table(employee_id,surname, phone_number, edu_id):
        if surname:
            cursor.execute("UPDATE employees SET surname=%s WHERE id_employee=%s", (surname,employee_id))
        if phone_number:
            cursor.execute("UPDATE employees SET phone_number=%s WHERE id_employee=%s", (phone_number,employee_id))
        if edu_id:
            cursor.execute("UPDATE employees SET edu_id=%s WHERE id_employee=%s", (edu_id,employee_id))
        conn.commit()
        
class stringsTable():
    def show_string_a_table():
        cursor.execute("SELECT * FROM string_a")
        lst = cursor.fetchall()
        return sorted(lst)

    def add_to_string_a_table(empl_id, assign_date, post_id, unit_id, salary):
        cursor.execute("INSERT INTO string_a (id_employee, assign_date, id_post, id_units, salary) VALUES (%s,%s,%s, %s, %s)", (empl_id, assign_date, post_id, unit_id, salary))
        conn.commit()

    def delete_from_string_a_table(string_id):
        cursor.execute("DELETE FROM string_a WHERE id_string=%s", (string_id,))
        conn.commit()

    def update_string_a_table(string_id,empl_id, assign_date, post_id, unit_id, salary):
        if empl_id:
            cursor.execute("UPDATE string_a SET id_employee=%s WHERE id_string=%s", (empl_id,string_id))
        if assign_date:
            cursor.execute("UPDATE string_a SET assign_date=%s WHERE id_string=%s", (assign_date,string_id))
        if post_id:
            cursor.execute("UPDATE string_a SET id_post=%s WHERE id_string=%s", (post_id,string_id))
        if unit_id:
            cursor.execute("UPDATE string_a SET id_units=%s WHERE id_string=%s", (unit_id,string_id))
        if salary:
            cursor.execute("UPDATE employees SET salary=%s WHERE id_string=%s", (salary,string_id))
        conn.commit()