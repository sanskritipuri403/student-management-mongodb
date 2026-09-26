# 🎓 Student Management System Using MongoDB

<p align="center">
  <img src="assets/bbdu_logo.png" alt="BBDU Logo" width="160" />
</p>

<p align="center">
  <b>Babu Banarasi Das University, Lucknow</b><br>
  <b>School of Computer Applications — BCA (DS & AI)</b><br>
  <i>Academic Year 2026–2027</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Database-MongoDB%20v8.3-green.svg?logo=mongodb" alt="MongoDB" />
  <img src="https://img.shields.io/badge/Tool-MongoDB%20Compass-brightgreen.svg?logo=mongodb" alt="Compass" />
  <img src="https://img.shields.io/badge/CLI-MongoDB%20Shell%20(mongosh)-blue.svg?logo=mongodb" alt="mongosh" />
  <img src="https://img.shields.io/badge/Status-Completed%20%26%20Verified-success.svg" alt="Status" />
  <img src="https://img.shields.io/badge/Data%20Records-65%20Students-orange.svg" alt="Records" />
</p>

---

## 📌 Project Overview

This repository contains the complete **Student Management System** developed strictly using **MongoDB Community Server 8.3**, **MongoDB Compass**, and **MongoDB Shell (`mongosh`)**.

* **Author / Candidate**: **Sanskriti Puri**
* **Department**: BCA (Data Science & Artificial Intelligence)
* **Faculty Guide**: **Mr. Harendra Singh**

The project satisfies all syllabus requirements:
1. **Topic 1: Installation and Configuration of MongoDB** (Server deployment as Windows Service, MongoDB Compass GUI setup, and `mongosh` terminal commands).
2. **Topic 2: Working with MongoDB Documents and Collections** (Single document insert via `insertOne`, bulk load of 64 documents via `insertMany` achieving **65 verified records**, and complete CRUD queries).
3. **Comprehensive Query Coverage**: Includes comparison operators (`$eq`, `$gt`, `$lt`, `$gte`, `$lte`), logical operators (`$and`, `$or`), atomic updates (`updateOne`, `updateMany`), deletions (`deleteOne`, `deleteMany`), sorting, limiting, search by city, document counts, and city-wise performance aggregations.
4. **Detailed Project Reports**: Available in both **Word (.docx)** and publication-grade **PDF** format with the university emblem.

---

## 📁 Repository Structure

```
student_management/
├── assets/
│   └── bbdu_logo.png                    # Babu Banarasi Das University emblem logo
├── data/
│   └── students_dataset_65.json         # Master dataset of 65 student records
├── scripts/
│   └── student_queries.js               # Complete runnable MongoDB Shell (mongosh) script (21 operations)
├── docs/
│   ├── Student_Management_MongoDB_Project_Report.docx  # Formatted Word Document
│   └── Student_Management_MongoDB_Project_Report.pdf   # 7-Page Publication PDF Report
├── .gitignore                           # Git ignore rules
└── README.md                            # Complete documentation & quickstart guide
```

---

## 📊 Dataset Summary (65 Student Records)

The collection `students` inside database `Students` stores records with attributes: `roll`, `name`, `age`, `marks`, and `city`.

| City of Residence | Number of Students | Average Marks (%) | Highest Score Achieved |
| :--- | :---: | :---: | :---: |
| **Lucknow** | 20 | 87.85% | 97 (Sanskriti) |
| **Varanasi** | 7 | 85.57% | 95 (Vansh) |
| **Kanpur** | 9 | 81.11% | 92 (Vaishnavi) |
| **Prayagraj** | 7 | 80.14% | 96 (Krishna) |
| **Ayodhya** | 5 | 76.20% | 86 (Divya) |
| **Jaunpur** | 6 | 73.83% | 86 (Saumya) |
| **Gorakhpur** | 4 | 69.00% | 78 (Sangita) |
| **Bareilly** | 3 | 68.00% | 77 (Mohit) |
| **Gonda** | 2 | 58.50% | 59 (Aman) |
| **TOTAL** | **65** | **81.42%** | **97 (Top Scorer)** |

---

## 🛠️ Implemented Operations & Query Reference

| Step # | Operation | MongoDB Command Syntax | Description |
| :---: | :--- | :--- | :--- |
| **1** | **Create Database** | `use Students` | Switches to or initializes `Students` database |
| **2** | **Create Collection** | `db.createCollection("students")` | Creates `students` collection |
| **3** | **Insert Single Student** | `db.students.insertOne({ roll: 1, name: "Anamika", age: 19, marks: 88, city: "Lucknow" })` | Single record ingestion (`insertOne`) |
| **4** | **Insert Multiple Students** | `db.students.insertMany([... 64 students ...])` | Bulk ingestion reaching 65 total records |
| **5** | **Display All Students** | `db.students.find()` | Retrieves all active student documents |
| **6** | **Equal To (`$eq`)** | `db.students.find({ marks: { $eq: 88 } })` | Matches students with marks equal to 88 |
| **7** | **Greater Than (`$gt`)** | `db.students.find({ marks: { $gt: 85 } })` | Matches students with marks above 85 (23 students) |
| **8** | **Less Than (`$lt`)** | `db.students.find({ marks: { $lt: 60 } })` | Matches students with marks below 60 |
| **9** | **Greater Than Equal (`$gte`)** | `db.students.find({ marks: { $gte: 90 } })` | Matches students with marks 90 or higher |
| **10** | **Less Than Equal (`$lte`)** | `db.students.find({ marks: { $lte: 70 } })` | Matches students with marks 70 or lower |
| **11** | **Update One** | `db.students.updateOne({ roll: 5 }, { $set: { marks: 95 } })` | Modifies Roll 5 (Vansh) marks to 95 |
| **12** | **Update Many** | `db.students.updateMany({ marks: { $gte: 90 } }, { $set: { grade: "A+" } })` | Assigns grade 'A+' to all high scorers |
| **13** | **Delete One** | `db.students.deleteOne({ roll: 10 })` | Removes single record (Roll 10: Vivek) |
| **14** | **Delete Many** | `db.students.deleteMany({ marks: { $lt: 60 } })` | Removes 3 records having marks < 60 |
| **15** | **Logical AND (`$and`)** | `db.students.find({ $and: [{ marks: { $gt: 80 } }, { age: 19 }] })` | Both criteria must be satisfied |
| **16** | **Logical OR (`$or`)** | `db.students.find({ $or: [{ city: "Lucknow" }, { city: "Kanpur" }] })` | Either city matches |
| **17** | **Sort (Asc / Desc)** | `sort({ marks: 1 })` / `sort({ marks: -1 })` | Sorts by marks from lowest or highest |
| **18** | **Limit** | `db.students.find().limit(5)` | Restricts output to first 5 documents |
| **19** | **Search by City** | `db.students.find({ city: "Lucknow" })` | Filters students residing in Lucknow |
| **20** | **Count Documents** | `db.students.countDocuments()` | Counts active documents (61 active post-deletion) |
| **21** | **City-Wise Aggregation** | `db.students.aggregate([{ $group: { _id: "$city", avg: { $avg: "$marks" } } }])` | Aggregation pipeline for regional analytics |

---

## 🚀 How to Run the Project in MongoDB

### Prerequisites
* [MongoDB Community Server v8.0+](https://www.mongodb.com/try/download/community) installed and running on port `27017`.
* [MongoDB Compass](https://www.mongodb.com/try/download/compass) or [MongoDB Shell (`mongosh`)](https://www.mongodb.com/try/download/shell).

### Option 1: Using MongoDB Shell (mongosh)
You can execute the entire query script directly from your terminal:
```bash
mongosh "mongodb://localhost:27017" scripts/student_queries.js
```

### Option 2: Using MongoDB Compass GUI
1. Open **MongoDB Compass**.
2. Connect to `mongodb://localhost:27017`.
3. Open the **_MONGOSH** terminal bar at the bottom.
4. Copy and paste queries from `scripts/student_queries.js` or load the script using:
   ```javascript
   load("scripts/student_queries.js")
   ```

---

## 📑 Project Reports

Formal documentation generated for university assessment:
* 📄 **[PDF Project Report](docs/Student_Management_MongoDB_Project_Report.pdf)** — 7-page publication-quality PDF featuring running headers, page numbers, and query outputs.
* 📝 **[Word Document Report](docs/Student_Management_MongoDB_Project_Report.docx)** — Fully styled DOCX file with official university branding.

---

## 👩‍💻 Author
**Sanskriti Puri**  
Bachelor of Computer Applications (Data Science & AI)  
School of Computer Applications, Babu Banarasi Das University, Lucknow  
Faculty Guide: **Mr. Harendra Singh**
