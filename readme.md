
# Local Network File Transfer Service

A simple and lightweight file transfer solution for devices on the same local network, **without relying on social media apps**.

---

### Installation & Usage

1. **Clone the GitHub Repo**
   ```bash
   git clone https://github.com/Mount-Isaac/network-files-upload.git
   ```

2. **Pull the Docker Image**
   ```bash
   docker pull theisaac/files-webapp:latest
   ```

3. **Run the Docker Container**
   ```bash
   docker run -p 1515:1515 theisaac/files-webapp
   ```

4. **Rebuild the Image (Optional)**  
   If you want to change the default password or modify the app:
   ```bash
   docker build -t theisaac/files-webapp .
   ```

---

### Firewall Setup

Ensure the server allows inbound traffic on port **1515**:

- **Linux**:
  ```bash
  sudo ufw allow 1515/tcp
  ```

- **Windows**:  
  Open Windows Firewall and allow inbound traffic on **port 1515**.

---

### Access the Web App

Once the service is running, you can access the web app through any device on the same network by visiting:

- [http://localhost:1515](http://localhost:1515)  
- [http://127.0.0.1:1515](http://127.0.0.1:1515)  
- [http://0.0.0.0:1515](http://0.0.0.0:1515)

---

Enjoy transferring files between devices with ease!
```

