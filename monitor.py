import boto3
import psutil
import time
import socket

# --- CONFIGURATION ---
NAMESPACE = 'MonitorAWS'
INTERVAL_SECONDS = 10

# Initialize CloudWatch client
cw_client = boto3.client('cloudwatch')

def get_system_metrics():
    """
    Captures the current CPU and RAM usage of the system.
    
    Returns:
        tuple: (cpu_usage_percent, ram_usage_percent)
    """
    # interval=1 blocks for 1 second to calculate CPU usage accurately
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    return cpu, ram

def send_metrics_to_aws(cpu, ram):
    """
    Sends the captured metrics to AWS CloudWatch.
    
    Args:
        cpu (float): CPU usage percentage.
        ram (float): RAM usage percentage.
    """
    hostname = socket.gethostname()
    
    try:
        response = cw_client.put_metric_data(
            Namespace=NAMESPACE,
            MetricData=[
                {
                    'MetricName': 'CPU_Usage',
                    'Dimensions': [
                        {'Name': 'ServerName', 'Value': hostname}
                    ],
                    'Value': cpu,
                    'Unit': 'Percent'
                },
                {
                    'MetricName': 'RAM_Usage',
                    'Dimensions': [
                        {'Name': 'ServerName', 'Value': hostname}
                    ],
                    'Value': ram,
                    'Unit': 'Percent'
                }
            ]
        )
        print(f"[OK] Sent -> CPU: {cpu}% | RAM: {ram}%")
    except Exception as error:
        print(f"[ERROR] Failed to send metrics to AWS: {error}")

# --- MAIN LOOP ---
if __name__ == "__main__":
    print(f"Starting Monitoring Agent on: {socket.gethostname()}")
    print("Press CTRL+C to stop.")

    try:
        while True:
            cpu_val, ram_val = get_system_metrics()
            send_metrics_to_aws(cpu_val, ram_val)
            time.sleep(INTERVAL_SECONDS)
            
    except KeyboardInterrupt:
        print("\nAgent stopped by user.")