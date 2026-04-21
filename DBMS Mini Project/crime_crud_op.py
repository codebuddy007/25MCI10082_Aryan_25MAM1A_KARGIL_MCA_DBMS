# crime_crud_op.py
import tkinter as tk
from tkinter import ttk, messagebox
from db import get_db_connection
import datetime

# -------------------- Database operations --------------------

def authenticate_officer(email, password):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT officer_id, name FROM users WHERE email=%s AND password=%s", (email, password))
        row = cur.fetchone()
        return row
    finally:
        cur.close()
        conn.close()

# --- Crimes ---
def get_all_crimes():
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT c.id, c.type, c.description, c.date_reported, c.location, c.status, c.officer_id, u.name AS officer_name
            FROM crimes c
            LEFT JOIN users u ON c.officer_id = u.officer_id
            ORDER BY c.date_reported DESC
        """)
        rows = cur.fetchall()
        return rows
    finally:
        cur.close()
        conn.close()

def search_crimes(keyword):
    kw = f"%{keyword}%"
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT c.id, c.type, c.description, c.date_reported, c.location, c.status, c.officer_id, u.name AS officer_name
            FROM crimes c
            LEFT JOIN users u ON c.officer_id = u.officer_id
            WHERE c.type LIKE %s OR c.location LIKE %s
            ORDER BY c.date_reported DESC
        """, (kw, kw))
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def add_crime(type_, description, date_str, location, officer_id, status='reported'):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except Exception:
            date_obj = None
        cur.execute(
            "INSERT INTO crimes (type, description, date_reported, location, officer_id, status) VALUES (%s, %s, %s, %s, %s, %s)",
            (type_, description, date_obj, location, officer_id, status)
        )
        conn.commit()
        return cur.lastrowid
    except Exception as e:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

def update_crime(crime_id, type_, description, date_str, location, status):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        try:
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except Exception:
            date_obj = None
        cur.execute(
            "UPDATE crimes SET type=%s, description=%s, date_reported=%s, location=%s, status=%s WHERE id=%s",
            (type_, description, date_obj, location, status, crime_id)
        )
        conn.commit()
        return cur.rowcount > 0
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

def delete_crime(crime_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM crimes WHERE id=%s", (crime_id,))
        conn.commit()
        return cur.rowcount > 0
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

def get_crime_by_id(crime_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM crimes WHERE id=%s", (crime_id,))
        return cur.fetchone()
    finally:
        cur.close()
        conn.close()

# --- Witnesses ---
def get_witnesses_for_crime(crime_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("""
            SELECT w.id, w.crime_id, w.witness_name, w.statement, w.user_id
            FROM witnesses w
            LEFT JOIN users u ON w.user_id = u.officer_id -- Assuming witness user_id links to user's officer_id
            WHERE w.crime_id = %s
        """, (crime_id,))
        result = cur.fetchall()
        return result
    finally:
        cur.close()
        conn.close()

def add_witness(crime_id, user_id, witness_name, statement):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO witnesses (crime_id, user_id, witness_name, statement) VALUES (%s, %s, %s, %s)", (crime_id, user_id, witness_name, statement))
        conn.commit()
        return cur.lastrowid
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

def delete_witness(witness_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM witnesses WHERE id=%s", (witness_id,))
        conn.commit()
        return cur.rowcount > 0
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

# --- Suspects ---
def get_suspects_for_crime(crime_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, crime_id, name, description FROM suspects WHERE crime_id=%s", (crime_id,))
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def add_suspect(crime_id, name, description):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO suspects (crime_id, name, description) VALUES (%s, %s, %s)", (crime_id, name, description))
        conn.commit()
        return cur.lastrowid
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

def delete_suspect(suspect_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM suspects WHERE id=%s", (suspect_id,))
        conn.commit()
        return cur.rowcount > 0
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

# --- Evidence ---
def get_evidence_for_crime(crime_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT evidence_id, crime_id, description, location_found, date_found FROM crimeevidence WHERE crime_id=%s", (crime_id,))
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

def add_evidence(crime_id, description, location_found, date_str=None):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        date_obj = None
        if date_str:
            try:
                date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            except Exception:
                pass
        cur.execute("INSERT INTO crimeevidence (crime_id, description, location_found, date_found) VALUES (%s, %s, %s, %s)",
                    (crime_id, description, location_found, date_obj))
        conn.commit()
        return cur.lastrowid
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

def delete_evidence(evidence_id):
    conn = get_db_connection()
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM crimeevidence WHERE evidence_id=%s", (evidence_id,))
        conn.commit()
        return cur.rowcount > 0
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()