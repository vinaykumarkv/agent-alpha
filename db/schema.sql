CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    equipment_type TEXT,
    detected_issue TEXT,
    confidence_score REAL,
    image_path TEXT,
    telemetry_snapshot TEXT
);

CREATE TABLE IF NOT EXISTS recommendations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER,
    recommended_steps TEXT,
    risk_level TEXT,
    reasoning TEXT,
    source_documents TEXT,
    FOREIGN KEY (event_id) REFERENCES events(id)
);

CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER,
    was_solution_correct BOOLEAN,
    user_comments TEXT,
    actual_fix_applied TEXT,
    time_to_resolve INTEGER,
    feedback_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(id)
);

CREATE TABLE IF NOT EXISTS kpi_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER,
    predicted_mttr INTEGER,
    actual_mttr INTEGER,
    downtime_saved REAL,
    success_rate REAL,
    FOREIGN KEY (event_id) REFERENCES events(id)
);