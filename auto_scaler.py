import subprocess
import time
import requests

PROMETHEUS = 'http://localhost:9090'
QUERY = '100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)'

def get_cpu_usage():
    response = requests.get(f'{PROMETHEUS}/api/v1/query', params={'query': QUERY})
    result = response.json()['data']['result']
    if result:
        return float(result[0]['value'][1])
    return 0.0

def create_gcp_instance():
    print("Creating GCP VM...")
    cmd = [
        "/home/vboxuser/Downloads/autoscaler_project/google-cloud-sdk/bin/gcloud",
        "compute", "instances", "create", "autoscaled-vm",
        "--zone=us-central1-a",
        "--machine-type=e2-micro",
        "--image-family=debian-11",
        "--image-project=debian-cloud",
        "--metadata=startup-script-url=https://raw.githubusercontent.com/Ashutosh0212/auto-scalar/main/startup.sh"
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    print("Starting Auto-Scaler Monitor...")
    while True:
        cpu_usage = get_cpu_usage()
        print(f"CPU Usage: {cpu_usage}%")
        if cpu_usage > 75:
            create_gcp_instance()
            break
        time.sleep(60)
