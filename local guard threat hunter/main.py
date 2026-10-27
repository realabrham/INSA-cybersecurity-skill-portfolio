import sys
import time
from scanner import SystemReconScanner
from analyzer import ThreatAnalyzer
from reporter import SecurityReporter

def print_banner():
    print("=" * 65)
    print("     LocalGuard: Endpoint Threat Hunting & Anomaly Engine     ")
    print("     INSA Summer Camp - Advanced Security Track Project       ")
    print("=" * 65)

def main():
    print_banner()
    print("[*] Initializing LocalGuard security daemon...")
    time.sleep(0.5)
    
    scanner = SystemReconScanner()
    analyzer = ThreatAnalyzer()
    reporter = SecurityReporter()
    
    print("[*] Phase 1: Gathering active network connections and local socket states...")
    raw_network_data = scanner.get_active_connections()
    
    print("[*] Phase 2: Scanning local running processes for anomalies...")
    raw_process_data = scanner.get_running_processes()
    
    print("[*] Phase 3: Running heuristic correlation and threat scoring...")
    threat_findings = analyzer.evaluate_risk(raw_network_data, raw_process_data)
    
    print("[*] Phase 4: Generating security assessment ledger...")
    report_file = reporter.generate_json_report(threat_findings)
    
    print(f"\n[+] Audit completed successfully. Findings saved to: {report_file}")
    print("[*] System status: Secured and logged.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Operation aborted by user. Cleaning up temp sockets...")
        sys.exit(0)
