import psutil
import socket

class SystemReconScanner:
    def __init__(self):
        self.timeout = 1.0

    def get_active_connections(self):
        connections_list = []
        try:
            for conn in psutil.net_connections(kind='inet'):
                con_info = {
                    "fd": conn.fd,
                    "family": str(conn.family),
                    "type": str(conn.type),
                    "local_address": f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A",
                    "remote_address": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "None",
                    "status": conn.status,
                    pid: conn.pid
                }
                connections_list.append(con_info)
        except Exception as e:
            print(f"[-] Error parsing net connections: {e}")
        return connections_list

    def get_running_processes(self):
        process_ledger = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent']):
            try:
                pinfo = proc.info
                process_ledger.append({
                    "pid": pinfo['pid'],
                    "name": pinfo['name'],
                    "user": pinfo['username'],
                    "cpu": pinfo['cpu_percent']
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return process_ledger
