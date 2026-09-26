/**
 * Babu Banarasi Das University - School of Computer Applications
 * Department: BCA (DS & AI)
 * Project: Student Management System Using MongoDB
 * Candidate: Sanskriti Puri
 * Faculty Guide: Mr. Harendra Singh
 * 
 * MongoDB Shell (mongosh) Complete Script - 65 Student Records
 */

// 1. CREATE DATABASE
print("=== 1. CREATE DATABASE ===");
use Students;
print("[+] Switched to 'Students' database.");

// 2. CREATE COLLECTION
print("\n=== 2. CREATE COLLECTION ===");
db.students.drop(); // Clean slate for reproducible runs
db.createCollection("students");
print("[+] Created collection 'students'.");

// 3. INSERT SINGLE STUDENT (insertOne - Syllabus Demonstration)
print("\n=== 3. INSERT SINGLE STUDENT (insertOne) ===");
const singleStudent = { roll: 1, name: "Anamika", age: 19, marks: 88, city: "Lucknow" };
const singleRes = db.students.insertOne(singleStudent);
print(`[+] Inserted single student Roll 1 (Anamika). ID: ${singleRes.insertedId}`);

// 4. INSERT MULTIPLE STUDENTS (insertMany - 64 records, Total = 65)
print("\n=== 4. INSERT MULTIPLE STUDENTS (insertMany - 64 records) ===");
const bulkStudents = [
  {roll:2, name:"Uday", age:18, marks:76, city:"Jaunpur"},
  {roll:3, name:"Vaishnavi", age:19, marks:92, city:"Kanpur"},
  {roll:4, name:"Annu", age:18, marks:69, city:"Ayodhya"},
  {roll:5, name:"Vansh", age:19, marks:81, city:"Varanasi"},
  {roll:6, name:"Amrita", age:20, marks:85, city:"Lucknow"},
  {roll:7, name:"Naveen", age:19, marks:73, city:"Prayagraj"},
  {roll:8, name:"Pratik", age:19, marks:90, city:"Lucknow"},
  {roll:9, name:"Sangita", age:20, marks:78, city:"Gorakhpur"},
  {roll:10, name:"Vivek", age:18, marks:65, city:"Kanpur"},
  {roll:11, name:"Tarkeshwar", age:20, marks:71, city:"Jaunpur"},
  {roll:12, name:"Shreya", age:19, marks:95, city:"Lucknow"},
  {roll:13, name:"Akshita", age:18, marks:84, city:"Ayodhya"},
  {roll:14, name:"Shruti", age:19, marks:87, city:"Prayagraj"},
  {roll:15, name:"Kartik", age:20, marks:74, city:"Varanasi"},
  {roll:16, name:"Sejal", age:18, marks:89, city:"Lucknow"},
  {roll:17, name:"Astha", age:19, marks:82, city:"Kanpur"},
  {roll:18, name:"Jai", age:18, marks:58, city:"Gonda"},
  {roll:19, name:"Harshita", age:20, marks:91, city:"Lucknow"},
  {roll:20, name:"Omkar", age:19, marks:63, city:"Bareilly"},
  {roll:21, name:"Ayush", age:18, marks:77, city:"Lucknow"},
  {roll:22, name:"Saumya", age:19, marks:86, city:"Jaunpur"},
  {roll:23, name:"Vidya", age:20, marks:72, city:"Kanpur"},
  {roll:24, name:"Adarsh", age:19, marks:80, city:"Ayodhya"},
  {roll:25, name:"Anmol", age:18, marks:67, city:"Prayagraj"},
  {roll:26, name:"Anushka", age:20, marks:94, city:"Lucknow"},
  {roll:27, name:"Ananya", age:19, marks:88, city:"Varanasi"},
  {roll:28, name:"Bhaskar", age:18, marks:61, city:"Gorakhpur"},
  {roll:29, name:"Rohan", age:19, marks:75, city:"Kanpur"},
  {roll:30, name:"Nishant", age:20, marks:79, city:"Lucknow"},
  {roll:31, name:"Vineet", age:18, marks:68, city:"Jaunpur"},
  {roll:32, name:"Anika", age:19, marks:90, city:"Lucknow"},
  {roll:33, name:"Jai", age:20, marks:55, city:"Ayodhya"},
  {roll:34, name:"Lakshya", age:18, marks:83, city:"Kanpur"},
  {roll:35, name:"Krishna", age:19, marks:96, city:"Prayagraj"},
  {roll:36, name:"Rumana", age:20, marks:70, city:"Lucknow"},
  {roll:37, name:"Priyanshu", age:18, marks:81, city:"Varanasi"},
  {roll:38, name:"Aditya", age:19, marks:66, city:"Gorakhpur"},
  {roll:39, name:"Dhruv", age:20, marks:93, city:"Lucknow"},
  {roll:40, name:"Nivedita", age:19, marks:85, city:"Kanpur"},
  {roll:41, name:"Meenu", age:18, marks:74, city:"Jaunpur"},
  {roll:42, name:"Akanksha", age:20, marks:89, city:"Lucknow"},
  {roll:43, name:"Sarika", age:19, marks:62, city:"Ayodhya"},
  {roll:44, name:"Anchal", age:18, marks:78, city:"Prayagraj"},
  {roll:45, name:"Umra", age:20, marks:84, city:"Lucknow"},
  {roll:46, name:"Nashra", age:19, marks:73, city:"Kanpur"},
  {roll:47, name:"Aman", age:18, marks:59, city:"Gonda"},
  {roll:48, name:"Priya", age:20, marks:87, city:"Lucknow"},
  {roll:49, name:"Rahul", age:19, marks:64, city:"Bareilly"},
  {roll:50, name:"Neha", age:18, marks:91, city:"Varanasi"},
  {roll:51, name:"Alok", age:19, marks:83, city:"Lucknow"},
  {roll:52, name:"Simran", age:18, marks:79, city:"Kanpur"},
  {roll:53, name:"Tushar", age:20, marks:88, city:"Varanasi"},
  {roll:54, name:"Ritu", age:19, marks:75, city:"Prayagraj"},
  {roll:55, name:"Saurabh", age:18, marks:92, city:"Lucknow"},
  {roll:56, name:"Divya", age:20, marks:86, city:"Ayodhya"},
  {roll:57, name:"Abhishek", age:19, marks:71, city:"Gorakhpur"},
  {roll:58, name:"Mansi", age:18, marks:94, city:"Lucknow"},
  {roll:59, name:"Shubham", age:20, marks:68, city:"Jaunpur"},
  {roll:60, name:"Shalini", age:19, marks:89, city:"Kanpur"},
  {roll:61, name:"Mohit", age:18, marks:77, city:"Bareilly"},
  {roll:62, name:"Tanu", age:20, marks:82, city:"Varanasi"},
  {roll:63, name:"Gaurav", age:19, marks:90, city:"Lucknow"},
  {roll:64, name:"Pallavi", age:18, marks:85, city:"Prayagraj"},
  {roll:65, name:"Sanskriti", age:19, marks:97, city:"Lucknow"}
];
const bulkRes = db.students.insertMany(bulkStudents);
print(`[+] Inserted ${Object.keys(bulkRes.insertedIds).length} records. Total documents: ${db.students.countDocuments()}`);

// 5. DISPLAY ALL STUDENTS
print("\n=== 5. DISPLAY ALL STUDENTS (db.students.find()) ===");
const allStudents = db.students.find().limit(5);
printjson(allStudents.toArray());

// 6. EQUAL TO OPERATOR ($eq)
print("\n=== 6. EQUAL TO ($eq: 88) ===");
const eqRes = db.students.find({ marks: { $eq: 88 } });
printjson(eqRes.toArray());

// 7. GREATER THAN OPERATOR ($gt)
print("\n=== 7. GREATER THAN ($gt: 85) ===");
const gtRes = db.students.find({ marks: { $gt: 85 } }).limit(5);
printjson(gtRes.toArray());

// 8. LESS THAN OPERATOR ($lt)
print("\n=== 8. LESS THAN ($lt: 60) ===");
const ltRes = db.students.find({ marks: { $lt: 60 } });
printjson(ltRes.toArray());

// 9. GREATER THAN OR EQUAL TO OPERATOR ($gte)
print("\n=== 9. GREATER THAN OR EQUAL TO ($gte: 90) ===");
const gteRes = db.students.find({ marks: { $gte: 90 } }).limit(5);
printjson(gteRes.toArray());

// 10. LESS THAN OR EQUAL TO OPERATOR ($lte)
print("\n=== 10. LESS THAN OR EQUAL TO ($lte: 70) ===");
const lteRes = db.students.find({ marks: { $lte: 70 } }).limit(5);
printjson(lteRes.toArray());

// 11. UPDATE OPERATION (updateOne)
print("\n=== 11. UPDATE OPERATION (updateOne: roll 5 marks to 95) ===");
const updateRes = db.students.updateOne(
  { roll: 5 },
  { $set: { marks: 95 } }
);
print(`Matched: ${updateRes.matchedCount}, Modified: ${updateRes.modifiedCount}`);
printjson(db.students.findOne({ roll: 5 }));

// 12. UPDATE MANY OPERATION (updateMany - Bonus Practical)
print("\n=== 12. UPDATE MANY OPERATION (updateMany: Add grade 'A+' for marks >= 90) ===");
const updateManyRes = db.students.updateMany(
  { marks: { $gte: 90 } },
  { $set: { grade: "A+" } }
);
print(`Matched: ${updateManyRes.matchedCount}, Modified: ${updateManyRes.modifiedCount}`);

// 13. DELETE ONE OPERATION
print("\n=== 13. DELETE ONE OPERATION (deleteOne: roll 10) ===");
const delOneRes = db.students.deleteOne({ roll: 10 });
print(`Deleted Count: ${delOneRes.deletedCount}`);

// 14. DELETE MANY OPERATION
print("\n=== 14. DELETE MANY OPERATION (deleteMany: marks < 60) ===");
const delManyRes = db.students.deleteMany({ marks: { $lt: 60 } });
print(`Deleted Count: ${delManyRes.deletedCount}`);

// 15. AND OPERATION ($and)
print("\n=== 15. AND OPERATION ($and: marks > 80 AND age = 19) ===");
const andRes = db.students.find({
  $and: [
    { marks: { $gt: 80 } },
    { age: 19 }
  ]
}).limit(5);
printjson(andRes.toArray());

// 16. OR OPERATION ($or)
print("\n=== 16. OR OPERATION ($or: city Lucknow OR Kanpur) ===");
const orRes = db.students.find({
  $or: [
    { city: "Lucknow" },
    { city: "Kanpur" }
  ]
}).limit(5);
printjson(orRes.toArray());

// 17. SORT OPERATION (Ascending & Descending)
print("\n=== 17A. SORT ASCENDING (sort marks: 1) ===");
const sortAsc = db.students.find().sort({ marks: 1 }).limit(5);
printjson(sortAsc.toArray());

print("\n=== 17B. SORT DESCENDING (sort marks: -1) ===");
const sortDesc = db.students.find().sort({ marks: -1 }).limit(5);
printjson(sortDesc.toArray());

// 18. LIMIT OPERATION
print("\n=== 18. LIMIT OPERATION (limit: 5) ===");
const limitRes = db.students.find().limit(5);
printjson(limitRes.toArray());

// 19. SEARCH BY CITY
print("\n=== 19. SEARCH BY CITY (city: 'Lucknow') ===");
const cityRes = db.students.find({ city: "Lucknow" }).limit(5);
printjson(cityRes.toArray());

// 20. COUNT DOCUMENTS
print("\n=== 20. COUNT DOCUMENTS (countDocuments) ===");
const currentCount = db.students.countDocuments();
print(`Total Documents currently in 'students': ${currentCount}`);

// 21. BONUS: AGGREGATION PIPELINE (Average marks per city)
print("\n=== 21. BONUS: AGGREGATION PIPELINE (City-wise Analytics) ===");
const cityStats = db.students.aggregate([
  {
    $group: {
      _id: "$city",
      studentCount: { $sum: 1 },
      avgMarks: { $avg: "$marks" },
      maxMarks: { $max: "$marks" },
      minMarks: { $min: "$marks" }
    }
  },
  { $sort: { avgMarks: -1 } }
]);
printjson(cityStats.toArray());
