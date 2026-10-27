import json
import datetime

class SecurityReporter:
    def __init__(self):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    def generate_json_report(self, findings):
        report_filename = f"security_audit_report_{self.timestamp}.json"
        report_data = {
            "tool_name": "LocalGuard-EDR Core",
            "version": "1.4.2-beta",
            "audit_timestamp": str(datetime.datetime.now()),
            "total_findings": len(findings),
            "findings": findings
        }

        with open(report_filename, "w") as f:
            json.dump(report_data, f, indent=4)
            
        return report_filename
