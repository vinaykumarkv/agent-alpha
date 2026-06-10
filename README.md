# 🧠 Multimodal Agentic Field Service Copilot

An enterprise-grade AI-powered assistant that intelligently diagnoses equipment faults, provides step-by-step repair guidance, and maintains a complete audit trail—combining vision understanding, retrieval-augmented generation (RAG), multi-agent reasoning, and explainable AI.

---

## 📋 Table of Contents

- [Use Case & Problem Statement](#use-case--problem-statement)
- [Key Features](#key-features)
- [Architecture Overview](#architecture-overview)
- [Installation & Setup](#installation--setup)
- [How to Use](#how-to-use)
- [Integration Guide](#integration-guide)
- [Project Structure](#project-structure)
- [Supported Capabilities](#supported-capabilities)

---

## 🎯 Use Case & Problem Statement

### The Problem
Field technicians often struggle with:
- **Slow fault identification** – Time spent diagnosing equipment issues
- **Manual documentation lookup** – Navigating complex manuals and SOPs
- **Lack of real-time expertise** – No instant access to expert guidance
- **Safety risks** – Incorrect troubleshooting procedures
- **Limited accountability** – No audit trail of diagnostic decisions

### The Solution
**Agent-Alpha** is a multimodal AI copilot that:
- ✅ **Instantly analyzes equipment images** to detect faults and anomalies
- ✅ **Diagnoses root causes** using AI-powered reasoning
- ✅ **Retrieves relevant SOPs/manuals** from your knowledge base automatically
- ✅ **Generates step-by-step repair actions** with risk assessment
- ✅ **Provides explainable recommendations** – technicians understand WHY
- ✅ **Maintains full audit logs** – track all decisions and feedback
- ✅ **Learns from feedback** – continuous improvement loop

### Business Impact
- 🚀 **Reduce MTTR (Mean Time To Repair)** by 40-60%
- 💰 **Lower service costs** through smarter diagnostics
- ⚡ **Improve technician efficiency** – less manual searching
- 🛡️ **Minimize safety risks** – standardized procedures
- 📊 **Gain insights** from audit logs and metrics

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| **Vision-Based Fault Detection** | Uses YOLOv8 to identify equipment types and visible anomalies (overheating, damage, wiring issues, etc.) |
| **Intelligent Diagnostics** | Maps visual evidence to probable root causes with risk assessment (LOW/MEDIUM/HIGH) |
| **RAG-Powered SOP Retrieval** | Retrieves relevant procedures from manuals/SOPs using semantic search |
| **Multi-Agent Reasoning** | Orchestrates 5 specialized AI agents (Vision, Diagnostics, Retrieval, Planning, Supervisor) for robust decisions |
| **Step-by-Step Action Planning** | Generates executable repair steps with safety warnings |
| **Explainable AI** | Provides clear reasoning for every recommendation |
| **Audit & Compliance** | Complete audit trail with timestamps, confidence scores, and decision reasoning |
| **Interactive Feedback Loop** | Technicians can provide feedback to improve future recommendations |
| **Real-Time Dashboard** | Monitor system performance, KPIs, and historical trends |
| **LLM-Agnostic** | Supports OpenAI, Hugging Face, and other LLM providers |

---

## 🏗️ Architecture Overview

### System Flow

```
┌─────────────────────┐
│   User Input        │
│ (Equipment Image)   │
└──────────┬──────────┘
           ↓
┌─────────────────────────────────────────┐
│       Vision Agent                      │
│ - Equipment detection (YOLOv8)          │
│ - Anomaly identification                │
│ - Confidence scoring                    │
└──────────┬──────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│       Diagnostics Agent                 │
│ - Root cause analysis                   │
│ - Risk level assessment                 │
│ - Telemetry correlation                 │
└──────────┬──────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│       Retrieval Agent (RAG)             │
│ - Query formulation                     │
│ - SOP/Manual semantic search            │
│ - Knowledge base lookup                 │
└──────────┬──────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│       Planning Agent                    │
│ - Step-by-step action generation        │
│ - Safety consideration                  │
│ - Sequencing & dependencies             │
└──────────┬──────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│       Supervisor Agent                  │
│ - Validation & cross-checking           │
│ - Explainability generation             │
│ - Final confidence scoring              │
└──────────┬──────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│   Database (SQLite)                     │
│ - Event logging                         │
│ - Recommendation tracking               │
│ - Audit trails                          │
└──────────┬──────────────────────────────┘
           ↓
┌─────────────────────────────────────────┐
│   Output to User                        │
│ - Diagnosis & root cause                │
│ - Repair steps                          │
│ - Risk assessment                       │
│ - Explanation & confidence              │
└─────────────────────────────────────────┘
```

### Technology Stack

- **Vision**: YOLOv8 (object detection), OpenCV (image processing)
- **LLM**: OpenAI GPT-4, Hugging Face models
- **RAG**: FAISS (vector search), Sentence Transformers (embeddings)
- **Orchestration**: Custom Agent Orchestrator with LangChain
- **Database**: SQLite (event logging, audit trails)
- **UI**: Streamlit (interactive dashboard)
- **Server**: FastAPI/Uvicorn (optional REST API)

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- pip or conda
- OpenAI API key (or alternative LLM provider)

### Step 1: Clone & Navigate

```bash
git clone <your-repo>
cd agent-alpha
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```env
# LLM Configuration
OPENAI_API_KEY=your_openai_api_key_here
LLM_PROVIDER=openai  # or huggingface, etc.
LLM_MODEL=gpt-4      # or gpt-3.5-turbo

# Application Configuration
MOCK_MODE=False      # Set to True for testing without real LLM calls
LOG_LEVEL=INFO

# Database (optional)
DATABASE_PATH=data/events.db

# FAISS Vector Store
FAISS_INDEX_PATH=rag/faiss_index/

# Telemetry (optional)
TELEMETRY_ENABLED=True
```

### Step 5: Initialize Database

```bash
python -m db.db_init
```

### Step 6: Prepare Knowledge Base (Optional)

Add manual PDFs or text documents to `data/manuals/`:

```bash
# Documents will be automatically indexed during RAG initialization
```

---

## 💡 How to Use

### Option A: Command-Line Pipeline

```bash
python main.py
```

This runs the complete pipeline on a sample image and logs results to the database.

### Option B: Interactive Streamlit Dashboard

```bash
streamlit run ui/app.py
```

Then open http://localhost:8501 in your browser.

**Available Tabs:**
1. **Home** – Upload equipment images, run analysis, view results
2. **Dashboard** – System performance metrics and historical trends
3. **System Metrics** – Monitor agent performance and token usage
4. **Audit Logs** – View complete audit trail and decision history

### Option C: Python API

```python
from services.pipeline import run_pipeline

# Run the pipeline on an image
result = run_pipeline("data/images/sample.png")

# Access results
print(f"Equipment: {result['vision']['equipment']}")
print(f"Issue: {result['vision']['issue']}")
print(f"Risk Level: {result['diagnostics']['risk_level']}")
print(f"Repair Steps: {result['final_output']['final_steps']}")
print(f"Explanation: {result['final_output']['explanation']}")
```

### Example Output

```json
{
  "event_id": "12345",
  "vision": {
    "equipment": "Industrial Pump",
    "issue": "Overheating with vibration",
    "confidence": 0.92
  },
  "diagnostics": {
    "root_cause": "Bearing wear or coolant blockage",
    "risk_level": "HIGH"
  },
  "knowledge": {
    "query": "pump overheating maintenance procedure",
    "sources": ["SOP-2024-pump-maintenance.pdf"]
  },
  "final_output": {
    "final_steps": [
      "1. Turn off pump and allow cooling for 15 minutes",
      "2. Check coolant reservoir level",
      "3. Inspect bearing housing for debris",
      "4. Replace coolant if discolored",
      "5. Test pump vibration before restart"
    ],
    "explanation": "The visual indicators suggest bearing wear combined with possible coolant degradation. Following preventive maintenance procedures will address both issues.",
    "confidence_level": "HIGH"
  }
}
```

---

## 🔗 Integration Guide

### 1. REST API Integration

Create a FastAPI server to expose the pipeline:

```python
# api_server.py
from fastapi import FastAPI, File, UploadFile
from services.pipeline import run_pipeline
import shutil

app = FastAPI()

@app.post("/analyze")
async def analyze_equipment(file: UploadFile = File(...)):
    # Save uploaded image
    file_path = f"data/images/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Run pipeline
    result = run_pipeline(file_path)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Start the server:
```bash
python api_server.py
```

**Example API Call:**
```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@equipment_photo.jpg"
```

### 2. Enterprise System Integration

```python
# integration_example.py
from services.pipeline import run_pipeline
from db.db_manager import fetch_all_events, fetch_recommendation
import json

class FieldServiceIntegration:
    def __init__(self):
        self.pipeline = run_pipeline
    
    def handle_field_report(self, image_path, technician_id):
        """Integrate with field service management system"""
        result = self.pipeline(image_path)
        
        # Send to your backend
        return {
            "technician_id": technician_id,
            "event_id": result["event_id"],
            "diagnosis": result["diagnostics"],
            "action_plan": result["final_output"]["final_steps"],
            "estimated_repair_time": self.estimate_time(result),
            "required_parts": self.extract_parts(result)
        }
    
    def estimate_time(self, result):
        """Extract repair time from recommendations"""
        return 30  # minutes (example)
    
    def extract_parts(self, result):
        """Extract required parts from final steps"""
        return ["Coolant", "Bearing Kit"]  # example

# Usage
integrator = FieldServiceIntegration()
report = integrator.handle_field_report("data/images/pump.jpg", "TECH-001")
print(json.dumps(report, indent=2))
```

### 3. Knowledge Base Integration

Add your organization's manuals:

```python
# ingest_custom_knowledge.py
from rag.ingest import ingest_documents

# Ingest PDFs from your manual repository
documents = ingest_documents("data/manuals/")

# Now these will be available for RAG queries
# The retrieval agent will find relevant procedures automatically
```

### 4. Database Integration

Access audit logs for compliance/analytics:

```python
from db.db_manager import fetch_all_events, fetch_recommendation

# Get all diagnostic events
events = fetch_all_events()

# Get specific recommendation
event_id = events[0][0]
recommendation = fetch_recommendation(event_id)

print(f"Risk Level: {recommendation[3]}")
print(f"Reasoning: {recommendation[4]}")
```

### 5. CI/CD & Deployment

Add to your deployment pipeline (`docker-compose.yml` example):

```yaml
version: '3.8'

services:
  copilot:
    build: .
    ports:
      - "8501:8501"  # Streamlit
      - "8000:8000"  # FastAPI (optional)
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - LLM_PROVIDER=openai
    volumes:
      - ./data:/app/data
      - ./db:/app/db
    restart: always
```

---

## 📁 Project Structure

```
agent-alpha/
├── main.py                          # Entry point - test pipeline
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── plan.md                          # Detailed build plan
├── .env                             # Configuration (not in git)
├── .env.example                     # Example configuration
│
├── agents/                          # Multi-agent system
│   ├── vision_agent.py              # Equipment detection (YOLOv8)
│   ├── diagnostics_agent.py         # Root cause analysis
│   ├── retrieval_agent.py           # SOP/manual lookup (RAG)
│   ├── planning_agent.py            # Action step generation
│   └── supervisor_agent.py          # Validation & explanation
│
├── services/                        # Core services
│   ├── agent_orchestrator.py        # Orchestrates agent workflow
│   └── pipeline.py                  # Main processing pipeline
│
├── models/                          # AI models
│   ├── vision/
│   │   ├── yolov8_model.py          # YOLOv8 object detection
│   │   └── yolov8n.pt               # Pretrained YOLOv8 weights
│   └── embeddings/
│       └── embedding_model.py       # Sentence Transformers for RAG
│
├── rag/                             # Retrieval-Augmented Generation
│   ├── ingest.py                    # Document ingestion
│   ├── retriever.py                 # Semantic search
│   ├── vector_store.py              # FAISS vector store
│   └── faiss_index/
│       └── index.faiss              # Persisted vector index
│
├── db/                              # Database layer
│   ├── db_init.py                   # Schema initialization
│   ├── db_manager.py                # CRUD operations
│   ├── db_tester.py                 # Database tests
│   ├── schema.sql                   # SQLite schema
│   └── events.db                    # Main database (generated)
│
├── ui/                              # Streamlit dashboard
│   ├── app.py                       # Main Streamlit app
│   └── components/
│       ├── dashboard.py             # Performance metrics
│       ├── audit_viewer.py          # Audit log viewer
│       ├── feedback_form.py         # User feedback collection
│       └── uploader.py              # Image upload handler
│
├── utils/                           # Utility functions
│   ├── llm_client.py                # LLM API wrapper
│   ├── logger.py                    # Logging configuration
│   ├── helpers.py                   # Helper functions
│   ├── metrics.py                   # Performance metrics
│   └── telemetry_simulator.py       # Mock telemetry data
│
├── data/                            # Data storage
│   ├── images/                      # Equipment photos
│   └── manuals/                     # SOP documents (PDFs, TXTs)
│
└── finetuning_yolo/                 # YOLO model fine-tuning
    ├── notebooks/
    │   └── yolo_finetuning.ipynb     # Training notebook
    └── data/
        └── data.yaml                # Dataset config
```

---

## 🎯 Supported Capabilities

### Vision Understanding
- ✅ Equipment type detection (pumps, turbines, motors, etc.)
- ✅ Anomaly detection (overheating, damage, leaks, vibration)
- ✅ Multi-equipment scenes
- ✅ Confidence scoring

### Diagnostic Capabilities
- ✅ Root cause analysis
- ✅ Risk level assessment (LOW/MEDIUM/HIGH)
- ✅ Telemetry correlation
- ✅ Historical pattern matching (from audit logs)

### Knowledge Integration
- ✅ PDF manual ingestion
- ✅ Semantic SOP search
- ✅ Multi-document retrieval
- ✅ Custom knowledge base support

### Planning & Actions
- ✅ Step-by-step repair procedures
- ✅ Safety warning integration
- ✅ Resource requirement identification
- ✅ Estimated repair time

### Audit & Compliance
- ✅ Complete decision audit trail
- ✅ Confidence/risk scoring
- ✅ Feedback tracking
- ✅ Historical trend analysis

---

## 🔧 Configuration Options

Key environment variables in `.env`:

```env
# LLM Settings
OPENAI_API_KEY=                 # Your OpenAI key
LLM_PROVIDER=openai             # openai, huggingface, etc.
LLM_MODEL=gpt-4                 # Model name
TEMPERATURE=0.3                 # Lower = more deterministic
MAX_TOKENS=2000                 # Response length

# Vision Settings
VISION_CONFIDENCE_THRESHOLD=0.6 # Minimum confidence for detections
VISION_MODEL=yolov8n            # yolov8n, yolov8s, yolov8m, etc.

# RAG Settings
EMBEDDING_MODEL=all-MiniLM-L6-v2 # Sentence Transformer model
FAISS_INDEX_PATH=rag/faiss_index/
TOP_K=3                         # Top K documents to retrieve

# Application
MOCK_MODE=False                 # Use mock outputs for testing
LOG_LEVEL=INFO                  # DEBUG, INFO, WARNING, ERROR
DATABASE_PATH=data/events.db    # SQLite database path

# Telemetry
TELEMETRY_ENABLED=True          # Enable telemetry collection
METRICS_ENABLED=True            # Enable metrics tracking
```

---

## 📊 Performance Metrics

Monitor system performance via the dashboard:

- **Total Events Processed**: All historical analyses
- **Average Confidence Score**: Quality of predictions
- **High-Risk Detections**: Critical issues flagged
- **Response Time**: End-to-end pipeline latency
- **Token Usage**: LLM API costs
- **Technician Feedback Accuracy**: System learning effectiveness

---

## 🤝 Contributing

To extend Agent-Alpha:

1. **Add Custom Agents**: Create new agent classes in `agents/`
2. **Fine-tune Vision**: Use `finetuning_yolo/` notebook for your equipment types
3. **Expand Knowledge Base**: Add PDFs to `data/manuals/` and re-run RAG ingestion
4. **Custom Integrations**: Extend `services/pipeline.py` with new workflows

---

## 📝 License

[Add your license here]

---

## 📧 Support

For questions or issues, please contact your development team or create an issue in the repository.
