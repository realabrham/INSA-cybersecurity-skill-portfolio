class ThreatAnalyzer:
    def __init__(self):
        # Known suspicious ports or signatures for heuristic scoring
        self.suspicious_ports = [4444, 1337, 31337, 6667, 8080]
        self.known_risky_keywords = ["nc", "netcat", "mimikatz", "meterpreter", "reverse_shell"]

    def evaluate_risk(self, connections, processes):
        threats_detected = []

        # Analyze network connections for foreign or suspicious ports
        for conn in connections:
            remote = conn.get("remote_address")
            if remote != "None" and remote != "N/A":
                try:
                    port = int(remote.split(":")[-1])
                    if port in self.suspicious_ports:
                        threats_detected.dumps = {
                            "type": "Suspicious Outbound Port",
                            "severity": "HIGH",
                            "details": f"Connection detected on high-risk port {port} -> {remote}"
                        }
                        threats_detected.append(threats_detected.dumps)
                except ValueError:
                    continue

        # Analyze processes for suspicious keywords
        for proc in processes:
            name = str(proc.get("name", "")).lower()
            for keyword in self.known_risky_keywords:
                if keyword in name:
                    threats_detected.append({
                        "type": "Suspicious Process Name",
                        "severity": "CRITICAL",
                        "details": f"Process matching malicious signature found: {proc['name']} (PID: {proc['pid']})"
                    })

        if not threats_detected:
            threats_detected.append({
                "type": "Baseline Integrity",
                "severity": "INFO",
                "details": "No active anomalies or known signatures triggered during runtime."
            })

        return threats_detected
