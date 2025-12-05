from peewee import *
import streamlit as st
from data_to_insert import CUSTOMERS_STARTING_DATA, STYLISTS_STARTING_DATA, APPOINTMENTS_STARTING_DATA
import time
import pandas as pd

# If you can't get supabase to work, switch this to False to just use SQLite
USE_SUPABASE = True

if USE_SUPABASE:
    db = PostgresqlDatabase(
        st.secrets.get("SUPABASE_DB_NAME"),
        user=st.secrets.get("SUPABASE_DB_USER", "postgres"),
        password=st.secrets.get("SUPABASE_DB_PASSWORD"),
        host=st.secrets.get("SUPABASE_DB_HOST"),
        port=int(st.secrets.get("SUPABASE_DB_PORT", "5432")),
        sslmode="require",
    )
else:
    db = SqliteDatabase("hair_salon.db")

class BaseModel(Model):
    class Meta:
        database = db

class Customer(BaseModel):
    c_id = AutoField(primary_key=True)
    c_first_name = CharField()
    c_last_name = CharField()
    c_phone_number = CharField()
    c_gender = CharField()
        
    def get_customer_message(self):
        num_appointments = len(self.appointments)
        if num_appointments > 0:
            return f"Welcome back {self.c_first_name} {self.c_last_name}! You've had {len(self.appointments)} appointments with us!"
        else:
            return f"Welcome {self.c_first_name} {self.c_last_name}! We hope you enjoy your first appointment!"
    
    def get_most_recent_appointment(self):
        try:
            return self.appointments.order_by(Appointment.a_date_time.desc()).first()
        except:
            return None

class Stylist(BaseModel):
    s_id = AutoField(primary_key=True)
    s_first_name = CharField()
    s_last_name = CharField()
    s_hire_date = DateField()
    s_gender = CharField()

    # This defines what displays when you print a Stylist object
    # This is set so that it prints out the first and last name when we use a list of objects in a selectbox widget.
    def __str__(self):
        return f"{self.s_first_name} {self.s_last_name}"

class Appointment(BaseModel):
    a_id = AutoField(primary_key=True)
    a_haircut_type = CharField()
    a_date_time = DateTimeField()
    a_payment = FloatField()
    a_satisfied = BooleanField()
    c_id = ForeignKeyField(Customer, backref='appointments', on_delete='CASCADE')
    s_id = ForeignKeyField(Stylist, backref='appointments', on_delete='CASCADE')

    def get_appointment_info(self):
        if self.a_satisfied:
            satisfaction_str = 'satisfied'
        else:
            satisfaction_str = 'not satisified'
        return f"Appointment {self.a_id} on {self.a_date_time}: {self.c_id.c_first_name} {self.c_id.c_last_name} got a {self.a_haircut_type} from {self.s_id.s_first_name} {self.s_id.s_last_name}. {self.c_id.c_first_name} was {satisfaction_str}."


def start_from_scratch(db_to_restart = db):
    """
    Drops specified tables ('appointment', 'stylist', 'customer') in the SQLite database if they exist, then recreates them.
    """
    db_to_restart.connect()
    tables_to_drop = ['appointment', 'stylist', 'customer']
    with db_to_restart.atomic():
        for table in tables_to_drop:
            db.execute_sql(f"DROP TABLE IF EXISTS {table};")
    db_to_restart.create_tables([Customer, Stylist, Appointment]) # creates the tables for the classes written if they don't exist.
    Customer.insert_many(CUSTOMERS_STARTING_DATA).execute()
    Stylist.insert_many(STYLISTS_STARTING_DATA).execute()
    Appointment.insert_many(APPOINTMENTS_STARTING_DATA).execute()
    db_to_restart.close()
    print("Recreated database structure from scratch")

def clean_phone_number(string):
    string = str(string)
    cleaned_string = ''
    for character in string:
        if character.isdecimal():
            cleaned_string += character
    
    if len(cleaned_string) == 10:
        return cleaned_string
    else:
        return None
    
def get_customer_if_exists(phone_number):
    try:
        return Customer.get(Customer.c_phone_number == phone_number)
    except Customer.DoesNotExist:
        return None
    
def get_all_stylists():
    return list(Stylist.select().order_by(Stylist.s_first_name))

def get_index_of_most_recent_stylist(appt_object):
    for index, stylist in enumerate(get_all_stylists()):
        if appt_object.s_id.s_id == stylist.s_id:
            return index
    # if it can't find one, just return None as the default:
    return None

def pretend_to_get_a_haircut():
    latest_iteration = st.empty()
    bar = st.progress(0)
    list_of_steps = ["Sitting down", "Making small talk", "Getting that haircut!", "Washing your hair", "Do you need any product today?", "Thanks for coming in!"]
    current_progress = 0.0
    for message in list_of_steps:
        # Update the progress bar with each iteration.
        latest_iteration.text(message)
        current_progress += 1/len(list_of_steps)
        bar.progress(round(current_progress, 1))
        time.sleep(0.5)

def get_manager_tools_df(database_conn = db):
    sql_query = '''
        SELECT
        s.s_first_name,
        s.s_last_name,
        ROUND(
            (SUM(CASE WHEN a.a_satisfied = TRUE THEN 1 ELSE 0 END) * 1.0) / COUNT(*),
            2
        ) AS satisfaction_rate,
        SUM(CASE WHEN a.a_satisfied = TRUE THEN 1 ELSE 0 END) AS num_satisfied,
        SUM(CASE WHEN a.a_satisfied = FALSE THEN 1 ELSE 0 END) AS num_dissatisfied,
        COUNT(*) AS total_num_appts
        FROM stylist s
        JOIN appointment a ON s.s_id = a.s_id
        GROUP BY s.s_id, s.s_first_name, s.s_last_name
        ORDER BY satisfaction_rate DESC;
    '''
    return pd.read_sql(sql_query, database_conn)



hairstyles_dict = {
    "Undercut": 22.0,
    "Mullet": 18.0,
    "Fade":	20.0,
    "Buzz Cut":	15.0,
    "Pixie Cut": 30.0,
    "Bob": 28.0,
    "Pompadour": 40.0,
    "Layered Cut": 25.0,
    "Crew Cut": 16.0,
    "Shag": 35.0
}



if __name__ == '__main__':
    start_from_scratch(db)