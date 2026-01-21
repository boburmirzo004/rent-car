"""
All tables queries
"""

users = """
        CREATE TABLE IF NOT EXISTS users
        (
            id         BIGSERIAL PRIMARY KEY,
            username   VARCHAR(255) NOT NULL,
            phone      VARCHAR(15) NOT NULL,
            password   VARCHAR(128) NOT NULL,
            is_active  BOOLEAN   DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) \
        """

cars = """
         CREATE TABLE IF NOT EXISTS cars
         (
            id         BIGSERIAL PRIMARY KEY,
            title      VARCHAR(255) NOT NULL,
            color      VARCHAR(255) NOT NULL,
            price      BIGINT NOT NULL,
            is_active  BOOLEAN DEFAULT FALSE,
            deactivate BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
         ) \
         """

orders = """
           CREATE TABLE IF NOT EXISTS orders
           (
               id          BIGSERIAL PRIMARY KEY,
               user_id     BIGINT REFERENCES users (id) ON DELETE SET NULL,
               car_id      BIGINT REFERENCES cars (id) ON DELETE SET NULL,
               is_active   BOOLEAN DEFAULT FALSE,
               rent_at     DATE NOT NULL DEFAULT CURRENT_DATE,
               return_at   DATE
           ) \
           """
