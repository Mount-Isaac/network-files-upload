# Local Network File Transfer Service

This service provides a seamless way to transfer files between devices without relying on social media apps or being distracted by them. It enables direct file transfers within your local network, keeping you focused and away from social media interruptions.

## Features
- **Simple Setup**: Easily transfer files between devices on the same network.
- **Flask-based Web App**: Lightweight and resource-friendly.
- **Cross-platform**: Runs on all major operating systems (Windows, Linux, macOS).
- **Customizable**: Default password is ‘isaac’, but it can be changed by cloning the GitHub repository and rebuilding the image locally.

## Installation & Usage

### 1. **Connect Devices to the Same Network**
   Ensure that all devices are on the same local network.

### 2. **Run the Service on the Server**
   Run the service on the computer you want to use as the server. This computer will handle the file transfers.

### 3. **Access the Web App**
   Open the web app from a browser on any device connected to the same network.

### 4. **Change Default Password (Optional)**
   The default password is ‘isaac’. To change it, clone the GitHub repository and rebuild the image locally.

## Firewall Setup

### Windows:
   - Open the Windows Firewall and whitelist **port 1515** for inbound traffic. This allows all computers on the network to access the web app.

### Linux:
   - Use the following command to enable access to the service:
     ```bash
     sudo ufw allow 1515/tcp
     ```


