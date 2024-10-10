import sqlite3, random
def ensure_database():
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='customer';''')


    if cursor.fetchone() is None:
        cursor.execute('''
                CREATE TABLE customer(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                contact_number TEXT NOT NULL,
                contact_email TEXT NOT NULL,
                has_order BOOLEAN DEFAULT FALSE,
                order_id TEXT NOT NULL,
                location TEXT NOT NULL,
                contact_method TEXT NOT NULL,
                loyalty_status TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                modified_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                    ''')
        cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_status TEXT NOT NULL,
        current_location TEXT NOT NULL,
        shipping_address TEXT NOT NULL,
        customer_id INTEGER,
        order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        total_amount DECIMAL(10, 2),
        FOREIGN KEY (customer_id) REFERENCES customer(id)
    );''')
        
        
def create_new_random():
        conn = sqlite3.connect('comrade.db')
        cursor = conn.cursor()
        names = [
            "Liam", "Emma", "Lucas", "Sophie", "Nicolas",
            "Vladimir", "Elena", "Mikhail", "Anastasia", "Mateusz",
            "Isabella", "Javier", "Francesca", "Dimitri", "Zara",
            "Petr", "Katarina", "Igor", "Svetlana", "Jarek",
            "Kwame", "Amina", "Ngozi", "Kofi", "Fatima",
            "Omar", "Layla", "Khalid", "Amira", "Yusuf",
            "Hiroshi", "Sakura", "Chen", "Ravi", "Ayesha",
            "Zainab", "Mohammed", "Chinedu", "Sunil", "Mei"
        ]

        surnames = [
            "Ivanov", "Nowak", "Kovacs", "Petrov", "Stoica",
            "Müller", "Dupont", "Martínez", "Rossi", "Smith",
            "Okafor", "Diop", "Banda", "Abebe", "Nguyen",
            "Al-Masri", "Hassan", "Rahman", "Farouk", "Nasser",
            "Tanaka", "Wang", "Kim", "Singh", "Li",
            "Mbatha", "Osei", "Khan", "Jiang", "Patel"
        ]
        locations = [
            "London, United Kingdom", "Paris, France", "Berlin, Germany", "Rome, Italy", "Madrid, Spain",
            "Moscow, Russia", "Warsaw, Poland", "Prague, Czech Republic", "Budapest, Hungary", "Bucharest, Romania",
            "Lagos, Nigeria", "Cairo, Egypt", "Johannesburg, South Africa", "Nairobi, Kenya", "Accra, Ghana",
            "Riyadh, Saudi Arabia", "Dubai, UAE", "Amman, Jordan", "Beirut, Lebanon", "Algiers, Algeria",
            "Tokyo, Japan", "Beijing, China", "Mumbai, India", "Seoul, South Korea", "Bangkok, Thailand",
            "Casablanca, Morocco", "Dakar, Senegal", "Tehran, Iran", "Hanoi, Vietnam", "Manila, Philippines"
        ]


        # Generate a random name and surname pair
        name = random.choice(names)
        surname = random.choice(surnames)
        location = random.choice(locations)
        # Insert the random pair into the customers table
        cursor.execute("INSERT INTO customers (name, surname, contact_number, contact_email, location, contact_method, loyalty_status) VALUES (?, ?, '', '', '', '', '')", (name, surname))

        contact_number = f"+{random.randint(1000000000, 9999999999)}"
        contact_email = f"{name}{surname}{random.randint(0,100)}@example.com"
        location = f"{location}"
        contact_method = random.choice(["phone", "email"])
        loyalty_status = random.choice(["bronze", "silver", "gold"])

        cursor.execute("""
            UPDATE customers
            SET contact_number = ?,
                contact_email = ?,
                location = ?,
                contact_method = ?,
                loyalty_status = ?
            WHERE id = LAST_INSERT_ROWID()
        """, (contact_number, contact_email, location, contact_method, loyalty_status))

        # Commit the changes to the database
        conn.commit()

        # Close the connection to the database
        conn.close()
