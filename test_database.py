import sqlite3

conn = sqlite3.connect("bank.db")

def setup():
    conn.execute("""CREATE TABLE customers (
        customer_id INT,
        name VARCHAR,
        balance DECIMAL,
        created_at DATETIME
    )""")
    conn.execute("""CREATE TABLE transactions (
        txn_id INT,
        customer_id INT,
        amount DECIMAL
    )""")

def get_balance(cid):
    return conn.execute("SELECT balance FROM customers WHERE customer_id = ?", (cid,))

def add_txn(cid, amt):
    conn.execute("INSERT INTO transactions VALUES (?, ?, ?)", (1, cid, amt))
    conn.execute("UPDATE customers SET balance = balance + ? WHERE customer_id = ?", (amt, cid))
