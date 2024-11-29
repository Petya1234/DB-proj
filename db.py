import psycopg2

conn = psycopg2.connect(dbname="postgres", host="localhost", user="postgres", password="12345", port="5432")
cursor = conn.cursor()

class educationsTable():
    def show_educations_table():
        cursor.execute("SELECT * FROM educations")
        lst = cursor.fetchall()
        return sorted(lst)

    def add_to_educations_table(edu_id,eduType):
        cursor.execute("INSERT INTO educations (edu_id,edu) VALUES (%s,%s)", (edu_id,eduType))
        conn.commit()

    def delete_from_education_table(edu_id):
        cursor.execute("DELETE FROM educations WHERE edu_id=%s", (edu_id,))
        conn.commit()

    def update_education_table(edu_id, eduType):
        cursor.execute("UPDATE educations SET edu =%s WHERE edu_id=%s", (eduType, edu_id))
        conn.commit()
        

class unitsTable():
    def show_units_table():
        cursor.execute("SELECT * FROM units")
        lst = cursor.fetchall()
        return sorted(lst)

    def add_to_units_table(unit):
        cursor.execute("INSERT INTO units (unit) VALUES (%s)", (unit,))
        conn.commit()

    def delete_from_education_table(unit_id):
        cursor.execute("DELETE FROM units WHERE id_units=%s", (unit_id,))
        conn.commit()

    def update_education_table(unit_id, unit):
        cursor.execute("UPDATE units SET unit =%s WHERE id_units=%s", (unit, unit_id))
        conn.commit()
        

class positionsTable():
    def show_positions_table():
        cursor.execute("SELECT * FROM positions")
        lst = cursor.fetchall()
        return sorted(lst)

    def add_to_positions_table(post):
        cursor.execute("INSERT INTO positions (post) VALUES (%s)", (post,))
        conn.commit()

    def delete_from_positions_table(post_id):
        cursor.execute("DELETE FROM positions WHERE id_post=%s", (post_id,))
        conn.commit()

    def update_positions_table(post_id, post):
        cursor.execute("UPDATE positions SET post =%s WHERE id_post=%s", (post, post_id))
        conn.commit()