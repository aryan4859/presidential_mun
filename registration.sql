-- Ensure you're using the presidential_mun database
USE presidential_mun;

-- Create the registrations table
CREATE TABLE registrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    current_address VARCHAR(255) NOT NULL,
    dob DATE,
    phone1 VARCHAR(20) NOT NULL,
    phone2 VARCHAR(20),
    whatsapp VARCHAR(20),
    food_pref VARCHAR(255),
    prev_college VARCHAR(255),
    stream VARCHAR(255),
    prev_mun VARCHAR(255),
    primary_committee VARCHAR(255) NOT NULL,
    secondary_committee VARCHAR(255) NOT NULL,
    contrib_view TEXT NOT NULL,
    future_goals TEXT NOT NULL,
    medical TEXT NOT NULL,
    payment_receipt VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Optionally, you can add indexes for faster querying (e.g., for email)
CREATE INDEX idx_email ON registrations (email);
