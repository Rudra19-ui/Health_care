from flask import Flask, request, redirect, url_for, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',  # Replace with your MySQL username
    'password': 'Rudra@192004',  # Replace with your MySQL password
    'database': 'healthcare'
}

# Function to connect to the database
def get_db_connection():
    conn = mysql.connector.connect(**db_config)
    return conn

# Route to handle the form submission
@app.route('/submit_appointment', methods=['POST'])
def submit_appointment():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        dob = request.form['dop']
        disease_type = request.form['disease_type']
        appointment_date = request.form['appointment_date']
        message = request.form['messege']

        # Insert data into the database
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO appointments (name, phone, email, dob, disease_type, appointment_date, message)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, phone, email, dob, disease_type, appointment_date, message))
        conn.commit()
        cursor.close()
        conn.close()

        # Redirect to a success page or home page
        return redirect(url_for('success'))

# Route to display the success page
@app.route('/success')
def success():
    return "Appointment booked successfully!"

# Route to display the form
@app.route('/')
def index():
    return render_template('book_appointment.html')

if __name__ == '__main__':
    app.run(debug=True)

    