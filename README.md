🚀 Project Summary

This project is an automated system that fetches real-time gold prices from goldapi.io and sends email notifications to users using Amazon Web Services SNS.

⚙️ What I Built
A Python application to fetch gold price and send notifications
A Docker container to package the application
A Kubernetes CronJob to run the application every 2 minutes
Integration with AWS SNS for email alerts


🧩 How It Works
CronJob runs every 2 minutes
It creates a Job → which runs a Pod
The Pod executes the Python script
Script fetches gold price → sends it to SNS
SNS delivers email to subscribers


🔐 Credential Handling
Gold API key stored securely using Kubernetes Secrets
AWS credentials (Access Key & Secret Key) stored in Kubernetes Secrets and injected as environment variables
No sensitive data is hardcoded or pushed to GitHub
