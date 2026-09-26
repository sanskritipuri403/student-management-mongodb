"""
Automated Python test runner for Student Management System Using MongoDB
Connects to MongoDB localhost:27017, loads 65 students, executes all queries,
and captures verified outputs.
"""

import json
import os
from pymongo import MongoClient, ASCENDING, DESCENDING

def run():
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
    db = client["Students"]
    
    # Clean drop
    db.students.drop()
    print("[+] Dropped old 'students' collection in 'Students' database.")
    
    data_file = os.path.join(os.path.dirname(__file__), "..", "data", "students_dataset_65.json")
    with open(data_file, "r", encoding="utf-8") as f:
        students = json.load(f)
        
    print(f"[+] Loaded {len(students)} student records.")
    
    # Step 3: Insert single
    doc1 = students[0]
    res1 = db.students.insert_one(doc1)
    print(f"[+] insertOne: Roll 1 inserted with ObjectId: {res1.inserted_id}")
    
    # Step 4: Insert bulk
    bulk_docs = students[1:]
    res_bulk = db.students.insert_many(bulk_docs)
    print(f"[+] insertMany: Inserted {len(res_bulk.inserted_ids)} records.")
    
    total = db.students.count_documents({})
    print(f"[+] Total Student Count: {total} (Meets >= 60 requirement: {'YES' if total >= 60 else 'NO'})")
    
    # Run test queries
    q_eq = list(db.students.find({"marks": 88}))
    print(f"[+] $eq (88 marks): Found {len(q_eq)} students -> {[s['name'] for s in q_eq]}")
    
    q_gt = list(db.students.find({"marks": {"$gt": 85}}))
    print(f"[+] $gt (marks > 85): Found {len(q_gt)} students")
    
    q_lt = list(db.students.find({"marks": {"$lt": 60}}))
    print(f"[+] $lt (marks < 60): Found {len(q_lt)} students -> {[s['name'] for s in q_lt]}")
    
    # Update
    u1 = db.students.update_one({"roll": 5}, {"$set": {"marks": 95}})
    print(f"[+] updateOne roll 5: Matched={u1.matched_count}, Modified={u1.modified_count}")
    
    # Delete one
    d1 = db.students.delete_one({"roll": 10})
    print(f"[+] deleteOne roll 10: Deleted={d1.deleted_count}")
    
    # Delete many
    dm = db.students.delete_many({"marks": {"$lt": 60}})
    print(f"[+] deleteMany marks < 60: Deleted={dm.deleted_count}")
    
    remaining = db.students.count_documents({})
    print(f"[+] Remaining students in collection: {remaining}")
    
    # Aggregation
    agg = list(db.students.aggregate([
        {"$group": {
            "_id": "$city",
            "count": {"$sum": 1},
            "avg_marks": {"$avg": "$marks"}
        }},
        {"$sort": {"avg_marks": -1}}
    ]))
    print("[+] City-wise Performance Aggregation:")
    for row in agg:
        print(f"    - {row['_id']:<12}: {row['count']} students, Avg Marks: {row['avg_marks']:.2f}")

if __name__ == "__main__":
    run()
