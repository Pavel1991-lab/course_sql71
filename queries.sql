CREATE TABLE job (
    id SERIAL PRIMARY KEY,
    employer_name VARCHAR(255),
	employer_information VARCHAR(255),
    employer_address VARCHAR(255),
    employer_salary integer,
    employer_link VARCHAR(255)
);