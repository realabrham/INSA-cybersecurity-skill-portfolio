# LocalGuard: Endpoint Threat Hunting & Anomaly Correlation Engine

## 📖 Background & Motivation
Developed as part of the INSA Cybersecurity Summer Camp skill-based track. **LocalGuard** is a lightweight, modular endpoint security telemetry and anomaly detection engine written in Python. It is designed to bridge the gap between passive network reconnaissance and active process behavior monitoring by performing heuristic correlation on active sockets, routing tables, and running system daemons.

Unlike simple port scanners, LocalGuard correlates open listening/established sockets with active OS process tables, flagging anomalous outbound connections and unverified background execution signatures.

## 🛠️ Architecture & Modules
The engine is structured into a clean Model-Analysis-Reporting pipeline:
1. **`main.py`**: CLI orchestrator, managing the audit lifecycle and logging threads.
2. **`scanner.py`**: Low-level telemetry collector utilizing cross-platform OS interfaces to query active sockets (`psutil`-backed) and process metadata.
3. **`analyzer.py`**: Heuristic anomaly scoring engine that checks endpoints against known adversary port distributions and signature keywords.
4. **`reporter.py`**: Structured JSON security ledger generator for downstream SIEM ingestion.

## ⚙️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/LocalGuard-ThreatHunter.git
   cd LocalGuard-ThreatHunter
   ```

2. Clone the repository:
   ```bash
   pip install psutil
   ```

3. Execute the audit engine:
   ```bash
   python main.py
   ```

## 🔍 Sample Output Ledger
```json
{
    "tool_name": "LocalGuard-EDR Core",
    "version": "1.4.2-beta",
    "total_findings": 1,
    "findings": [
        {
            "type": "Baseline Integrity",
            "severity": "INFO",
            "details": "No active anomalies or known signatures triggered during runtime."
        }
    ]
}
```
