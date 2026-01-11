# AWS CloudWatch Monitoring Agent 

A lightweight Python agent that captures local system metrics (CPU & RAM) and transmits them to **AWS CloudWatch** for real-time monitoring and alerting.

## Features
- **Real-time Monitoring:** Captures CPU and Memory usage using `psutil`.
- **Cloud Integration:** Pushes custom metrics to AWS CloudWatch using `boto3`.
- **Alerting:** Configured with AWS SNS to trigger email alarms when CPU usage exceeds thresholds.
- **Security:** Implements IAM roles with least-privilege permissions (no root access).

## Technologies
- **Python 3**
- **AWS SDK (Boto3)**
- **AWS Services:** CloudWatch, IAM, SNS.

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/FelipePoliszuk/aws-monitor-agent.git
   cd aws-monitor-agent
   ```

2. **Set up Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure AWS Credentials**
   ```bash
   aws configure
   ```

4. **Run the Agent**
   ```bash
   python monitor.py
   ```
