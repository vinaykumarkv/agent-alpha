import sqlite3
from datetime import datetime

DB_PATH = "db/audit.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


# ✅ EVENT LOGGING
def log_event(equipment_type, detected_issue, confidence, image_path, telemetry, metrics):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO events (equipment_type, detected_issue, confidence_score, image_path, telemetry_snapshot, metrics_snapshot)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (equipment_type, detected_issue, confidence, image_path, telemetry, metrics))

    event_id = cursor.lastrowid
    conn.commit()
    conn.close()

    return event_id


# ✅ RECOMMENDATION LOGGING
def log_recommendation(event_id, steps, risk, reasoning, sources):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO recommendations (event_id, recommended_steps, risk_level, reasoning, source_documents)
        VALUES (?, ?, ?, ?, ?)
    """, (event_id, steps, risk, reasoning, sources))

    conn.commit()
    conn.close()


# ✅ FEEDBACK CAPTURE
def log_feedback(event_id, correct, comments, fix, time_taken):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO feedback (event_id, was_solution_correct, user_comments, actual_fix_applied, time_to_resolve)
        VALUES (?, ?, ?, ?, ?)
    """, (event_id, correct, comments, fix, time_taken))

    conn.commit()
    conn.close()


# ✅ KPI LOGGING
def log_kpi(event_id, predicted_mttr, actual_mttr, downtime_saved, success):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO kpi_metrics (event_id, predicted_mttr, actual_mttr, downtime_saved, success_rate)
        VALUES (?, ?, ?, ?, ?)
    """, (event_id, predicted_mttr, actual_mttr, downtime_saved, success))

    conn.commit()
    conn.close()


# ✅ FETCH EVENTS (for UI later)
def fetch_all_events():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM events ORDER BY timestamp DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows


def fetch_feedback():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT was_solution_correct FROM feedback")
    rows = cursor.fetchall()

    conn.close()
    return rows
