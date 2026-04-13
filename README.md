# ☁️ Cloud Storage SaaS Project (HDFS Simulation)

## 📌 Project Description

This project implements a **cloud storage system** using Python and Flask, simulating the core concepts of **Software as a Service (SaaS)** and **Hadoop Distributed File System (HDFS)**.

The system allows users to upload files through a web interface. The uploaded files are divided into smaller chunks (blocks), encrypted for security, and stored across multiple nodes (folders). During download, these chunks are decrypted and merged back to reconstruct the original file.

---

## 🎯 Objectives

* To simulate a cloud storage system over a LAN
* To implement HDFS concepts like file splitting and distributed storage
* To ensure data security using encryption
* To provide a simple SaaS-based user interface

---

## 🚀 Features

* File Upload via Web Interface
* File Splitting into Blocks (HDFS Concept)
* Data Encryption using Fernet
* Distributed Storage across multiple nodes
* File Download and Reconstruction
* Simple and Interactive UI using Flask

---

## 🧠 Technologies Used

* Python
* Flask (Web Framework)
* Cryptography Library (Fernet Encryption)
* HTML (Basic UI)

---

## 🏗️ Project Structure

Cloud-Storage-saas/
│
├── app.py            # Main Flask Application
├── node1/            # Storage Node 1
├── node2/            # Storage Node 2
├── node3/            # Storage Node 3
└── README.md

---

## ⚙️ How It Works

### 🔹 Upload Process

1. User selects a file using the web interface
2. File is divided into smaller chunks (blocks)
3. Each chunk is encrypted
4. Encrypted chunks are distributed across node folders

### 🔹 Download Process

1. System reads chunks from all nodes
2. Decrypts each chunk
3. Merges them in correct order
4. Reconstructs the original file

---

## 🖥️ How to Run the Project

### Step 1: Clone the Repository

git clone https://github.com/vaishnavi902/Cloud-Storage-saas.git
cd Cloud-Storage-saas

### Step 2: Install Dependencies

pip install flask cryptography

### Step 3: Run the Application

python app.py

### Step 4: Open in Browser

http://127.0.0.1:5000

---

## 📊 Concepts Implemented

* **SaaS (Software as a Service)**
  Users interact with the application through a browser without installing it locally.

* **HDFS Simulation**
  Files are split into blocks and stored across multiple nodes.

* **Encryption**
  Ensures secure storage and transfer of data.

* **Client-Server Architecture**
  Frontend (UI) interacts with backend (Flask server).

---

## 📱 Real-Life Use Case

This project is similar to cloud services like storing photos or documents online, where data is uploaded, stored securely, and accessed anytime without relying on local storage.

---

## 🎤 Viva Explanation

This project demonstrates a cloud-based storage system where files are uploaded via a web interface, split into blocks, encrypted, and stored across distributed nodes. During download, the system decrypts and merges the blocks to reconstruct the original file. It simulates SaaS and HDFS concepts using local resources.

---

## ⚠️ Note

This is a **local simulation** of cloud storage. In real-world systems, technologies like distributed storage systems and cloud platforms are used.

---

## 👩‍💻 Author

Vaishnavi Ghadge
