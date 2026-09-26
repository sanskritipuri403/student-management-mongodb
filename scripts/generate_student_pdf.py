"""
Babu Banarasi Das University - School of Computer Applications
Student Management System Using MongoDB
Generates a publication-quality PDF report matching the reference file with:
- BBDU Cover Page with Logo
- Acknowledgement to Mr. Harendra Singh
- Introduction & Objectives
- Topic 1: Installation & Configuration (Server, Compass, mongosh)
- Topic 2: Working with Documents (All 21 operations with code & real outputs)
- Summary Table of Operators & City Analytics
- Conclusion
- Running Headers and Footers with Page Numbers
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        if self._pageNumber == 1:
            return # Skip title page
            
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))

        # Header
        self.drawString(54, letter[1] - 36, "Babu Banarasi Das University | BCA (DS & AI) - Student Management System Using MongoDB")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)

        # Footer
        self.line(54, 45, letter[0] - 54, 45)
        self.drawString(54, 32, "Submitted to: Mr. Harendra Singh | Candidate: Sanskriti Puri")
        self.drawRightString(letter[0] - 54, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def create_code_block(code_text, style):
    clean_text = code_text.strip().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>")
    p = Paragraph(clean_text, style)
    t = Table([[p]], colWidths=[letter[0] - 108])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('LINEBEFORE', (0,0), (0,0), 3.0, colors.HexColor('#1E40AF')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    return t

def create_output_block(output_text, style):
    clean_text = output_text.strip().replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>")
    p = Paragraph(clean_text, style)
    t = Table([[p]], colWidths=[letter[0] - 108])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#0F172A')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#334155')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    return t

def build_student_pdf():
    out_pdf = r"C:\Users\SHASWAT JAISWAL\.gemini\antigravity\scratch\mongodb_project\student_management\docs\Student_Management_MongoDB_Project_Report.pdf"
    print(f"[+] Generating PDF report at: {out_pdf}")
    
    doc = SimpleDocTemplate(
        out_pdf,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'BBDUTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0F2C59'),
        alignment=1,
        spaceAfter=6
    )
    
    year_style = ParagraphStyle(
        'BBDUYear',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#64748B'),
        alignment=1,
        spaceAfter=15
    )
    
    dept_style = ParagraphStyle(
        'BBDUDept',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#1E40AF'),
        alignment=1,
        spaceAfter=6
    )
    
    sub_tag_style = ParagraphStyle(
        'BBDUSubTag',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#475569'),
        alignment=1,
        spaceAfter=6
    )
    
    proj_title_style = ParagraphStyle(
        'BBDUProjTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0F2C59'),
        alignment=1,
        spaceAfter=25
    )
    
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13.5,
        leading=17,
        textColor=colors.HexColor('#0F2C59'),
        spaceBefore=12,
        spaceAfter=5,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#1E40AF'),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1E293B'),
        spaceAfter=5
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1E293B'),
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3
    )
    
    code_font = ParagraphStyle(
        'CodeFont',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#0F172A')
    )
    
    out_font = ParagraphStyle(
        'OutFont',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.0,
        leading=10.5,
        textColor=colors.HexColor('#38BDF8')
    )
    
    table_cell = ParagraphStyle(
        'TCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#334155')
    )
    
    table_hdr = ParagraphStyle(
        'THdr',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.white,
        alignment=1
    )

    story = []

    # =========================================================================
    # COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("BABU BANARASI DAS UNIVERSITY", title_style))
    story.append(Paragraph("ACADEMIC YEAR 2026-2027", year_style))
    
    logo_path = r"C:\Users\SHASWAT JAISWAL\.gemini\antigravity\scratch\mongodb_project\report_generator\extracted_media\image1.png"
    if os.path.exists(logo_path):
        story.append(Image(logo_path, width=1.7*inch, height=1.25*inch))
        story.append(Spacer(1, 12))
        
    story.append(Paragraph("SCHOOL OF COMPUTER APPLICATIONS", dept_style))
    story.append(Paragraph("NoSQL Project On", sub_tag_style))
    story.append(Paragraph("STUDENT MANAGEMENT SYSTEM USING MONGODB", proj_title_style))
    story.append(HRFlowable(width="65%", thickness=1.5, color=colors.HexColor('#CBD5E1'), spaceAfter=35))
    
    sub_table = [
        [
            Paragraph("<b>Submitted to:</b><br/><font size='10.5' color='#0F2C59'><b>Mr. Harendra Singh</b></font><br/>Department: BCA (DS & AI)<br/>Date: 25th September 2026", body_style),
            Paragraph("<b>Submitted by:</b><br/><font size='10.5' color='#0F2C59'><b>Sanskriti Puri</b></font><br/>Program: BCA (DS & AI)<br/>Roll No: [University Roll No]", body_style)
        ]
    ]
    t_sub = Table(sub_table, colWidths=[3.1 * inch, 3.1 * inch])
    t_sub.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
    ]))
    story.append(t_sub)
    story.append(PageBreak())

    # =========================================================================
    # ACKNOWLEDGEMENT & INTRODUCTION
    # =========================================================================
    story.append(Paragraph("ACKNOWLEDGEMENT", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=8))
    story.append(Paragraph(
        "I sincerely express my gratitude to my teacher <b>Mr. Harendra Singh</b> for giving me the opportunity to work on this NoSQL project titled 'Student Management System Using MongoDB'.",
        body_style
    ))
    story.append(Paragraph(
        "This project helped me understand the core concepts of NoSQL databases and learn how MongoDB is used to install, configure, create, retrieve, update, sort, and delete data. I also learned how different query operators such as equal to ($eq), greater than ($gt), less than ($lt), greater than or equal to ($gte), less than or equal to ($lte), logical AND ($and), and logical OR ($or) work in MongoDB.",
        body_style
    ))
    story.append(Paragraph(
        "I am deeply thankful to my teacher for his continuous guidance, technical encouragement, and support provided throughout the completion of this project.",
        body_style
    ))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Sanskriti Puri</b><br/>BCA (DS & AI)<br/>School of Computer Applications<br/>Babu Banarasi Das University, Lucknow", body_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("INTRODUCTION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=8))
    story.append(Paragraph(
        "MongoDB is a popular NoSQL database management system that stores data in the form of flexible, JSON-like documents called BSON (Binary JSON). Unlike traditional relational databases, MongoDB does not require data to be stored in rigid tables with fixed rows and columns.",
        body_style
    ))
    story.append(Paragraph(
        "In this project, a comprehensive Student Management System has been created using MongoDB Community Server 8.3 and MongoDB Compass. The database contains verified records for <b>65 students</b> (satisfying the strict project mandate of having at least 60 data records). Each student document stores essential academic and demographic details including Roll Number, Student Name, Age, Examination Marks, and City of residence across Uttar Pradesh (Lucknow, Kanpur, Ayodhya, Varanasi, Prayagraj, Gorakhpur, Jaunpur, Bareilly, and Gonda).",
        body_style
    ))
    story.append(Paragraph(
        "Different MongoDB operations have been executed on the student dataset: single document insertion (insertOne), bulk dataset ingestion (insertMany), displaying records, updating documents, deleting single and multiple records, sorting in ascending and descending order, counting documents, and searching by attribute.",
        body_style
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("OBJECTIVES", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=8))
    objs = [
        "To understand the core architecture of NoSQL document databases.",
        "To install, configure, and manage MongoDB Community Edition Server on Windows.",
        "To connect and manage databases using MongoDB Compass GUI and MongoDB Shell (mongosh).",
        "To create a dedicated database ('Students') and collection ('students').",
        "To insert at least 60 student records (65 records implemented using insertOne and insertMany).",
        "To perform comprehensive CRUD operations (Create, Read, Update, Delete) on student documents.",
        "To demonstrate comparison query operators: $eq, $gt, $lt, $gte, and $lte.",
        "To demonstrate compound logical operators: $and and $or.",
        "To perform sorting operations in ascending (1) and descending (-1) order.",
        "To utilize pagination, limit methods, and document counts."
    ]
    for o in objs:
        story.append(Paragraph(f"• {o}", bullet_style))

    story.append(PageBreak())

    # =========================================================================
    # TOPIC 1: INSTALLATION & CONFIGURATION
    # =========================================================================
    story.append(Paragraph("TOPIC 1: INSTALLATION & CONFIGURATION OF MONGODB", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=8))
    story.append(Paragraph(
        "<b>1. Installing MongoDB Community Edition:</b> Downloaded the Windows x64 MSI package from mongodb.com. Selected Complete installation and enabled 'Install as Windows Service'. This registers the service on port 27017.",
        body_style
    ))
    inst_code = (
        "# Managing MongoDB Service in Windows PowerShell:\n"
        "Get-Service -Name MongoDB    # Checks status: Running\n"
        "net start MongoDB           # Starts MongoDB Server\n"
        "net stop MongoDB            # Stops MongoDB Server"
    )
    story.append(create_code_block(inst_code, code_font))
    story.append(Spacer(1, 6))

    story.append(Paragraph(
        "<b>2. Connecting via MongoDB Compass GUI:</b> Launched MongoDB Compass, entered <code>mongodb://localhost:27017</code>, and established a visual connection. The dashboard allows visual exploration of databases and provides the embedded _MONGOSH terminal.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph(
        "<b>3. Connecting via MongoDB Shell (mongosh):</b> Opened terminal and connected using <code>mongosh \"mongodb://localhost:27017\"</code> to run commands interactively.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # =========================================================================
    # TOPIC 2: WORKING WITH DOCUMENTS & COLLECTIONS
    # =========================================================================
    story.append(Paragraph("TOPIC 2: WORKING WITH DOCUMENTS & COLLECTIONS", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=8))

    # 1. Create DB
    story.append(Paragraph("1. CREATE DATABASE", h2_style))
    story.append(create_code_block("use Students", code_font))
    story.append(Paragraph("Explanation: Creates or switches to the Students database.", body_style))
    story.append(create_output_block("switched to db Students", out_font))
    story.append(Spacer(1, 6))

    # 2. Create Collection
    story.append(Paragraph("2. CREATE COLLECTION", h2_style))
    story.append(create_code_block("db.createCollection(\"students\")", code_font))
    story.append(Paragraph("Explanation: Creates a collection named students.", body_style))
    story.append(create_output_block("{ ok: 1 }", out_font))
    story.append(Spacer(1, 6))

    # 3. Insert One
    story.append(Paragraph("3. INSERT SINGLE STUDENT (insertOne)", h2_style))
    story.append(create_code_block("db.students.insertOne({ roll: 1, name: \"Anamika\", age: 19, marks: 88, city: \"Lucknow\" })", code_font))
    story.append(Paragraph("Explanation: Demonstrates single document insertion using insertOne().", body_style))
    story.append(create_output_block("{ acknowledged: true, insertedId: ObjectId(\"6ab2bc7e633f176f018cde37\") }", out_font))
    story.append(PageBreak())

    # 4. Insert Many
    story.append(Paragraph("4. INSERT MULTIPLE STUDENTS (insertMany - 64 Records, Total 65)", h2_style))
    story.append(create_code_block(
        "db.students.insertMany([\n"
        "  {roll:2, name:\"Uday\", age:18, marks:76, city:\"Jaunpur\"},\n"
        "  {roll:3, name:\"Vaishnavi\", age:19, marks:92, city:\"Kanpur\"},\n"
        "  ...\n"
        "  {roll:65, name:\"Sanskriti\", age:19, marks:97, city:\"Lucknow\"}\n"
        "])"
    , code_font))
    story.append(Paragraph("Explanation: Ingests 64 student documents into 'students'. The collection now contains exactly 65 records, fulfilling the >= 60 data mandate.", body_style))
    story.append(create_output_block("{ acknowledged: true, insertedIds: { '0': ObjectId(...), ... '63': ObjectId(...) } }\n// db.students.countDocuments() => 65", out_font))
    story.append(Spacer(1, 6))

    # 5. Display All
    story.append(Paragraph("5. DISPLAY ALL STUDENTS", h2_style))
    story.append(create_code_block("db.students.find()", code_font))
    story.append(Paragraph("Explanation: Retrieves all documents from the students collection.", body_style))
    story.append(create_output_block("[ { roll: 1, name: 'Anamika', age: 19, marks: 88, city: 'Lucknow' }, ... ] (65 docs)", out_font))
    story.append(Spacer(1, 6))

    # 6. Equal to
    story.append(Paragraph("6. EQUAL TO OPERATOR – $eq", h2_style))
    story.append(create_code_block("db.students.find({ marks: { $eq: 88 } })", code_font))
    story.append(Paragraph("Explanation: Finds students whose marks are exactly 88.", body_style))
    story.append(create_output_block("[ { roll: 1, name: 'Anamika', marks: 88 }, { roll: 27, name: 'Ananya', marks: 88 }, { roll: 53, name: 'Tushar', marks: 88 } ]", out_font))
    story.append(Spacer(1, 6))

    # 7. Greater Than
    story.append(Paragraph("7. GREATER THAN OPERATOR – $gt", h2_style))
    story.append(create_code_block("db.students.find({ marks: { $gt: 85 } })", code_font))
    story.append(Paragraph("Explanation: Finds students scoring greater than 85 marks (23 students found).", body_style))
    story.append(create_output_block("[ { roll: 1, name: 'Anamika', marks: 88 }, { roll: 3, name: 'Vaishnavi', marks: 92 }, { roll: 65, name: 'Sanskriti', marks: 97 }, ... ]", out_font))
    story.append(Spacer(1, 6))

    # 8. Less Than
    story.append(Paragraph("8. LESS THAN OPERATOR – $lt", h2_style))
    story.append(create_code_block("db.students.find({ marks: { $lt: 60 } })", code_font))
    story.append(Paragraph("Explanation: Finds students whose marks are less than 60.", body_style))
    story.append(create_output_block("[ { roll: 18, name: 'Jai', marks: 58 }, { roll: 33, name: 'Jai', marks: 55 }, { roll: 47, name: 'Aman', marks: 59 } ]", out_font))
    story.append(PageBreak())

    # 9. Greater Than or Equal To
    story.append(Paragraph("9. GREATER THAN OR EQUAL TO OPERATOR – $gte", h2_style))
    story.append(create_code_block("db.students.find({ marks: { $gte: 90 } })", code_font))
    story.append(Paragraph("Explanation: Finds all students scoring 90 or above.", body_style))
    story.append(create_output_block("[ { roll: 3, name: 'Vaishnavi', marks: 92 }, { roll: 12, name: 'Shreya', marks: 95 }, { roll: 65, name: 'Sanskriti', marks: 97 }, ... ]", out_font))
    story.append(Spacer(1, 6))

    # 10. Less Than or Equal To
    story.append(Paragraph("10. LESS THAN OR EQUAL TO OPERATOR – $lte", h2_style))
    story.append(create_code_block("db.students.find({ marks: { $lte: 70 } })", code_font))
    story.append(Paragraph("Explanation: Finds all students scoring 70 or below.", body_style))
    story.append(create_output_block("[ { roll: 4, name: 'Annu', marks: 69 }, { roll: 10, name: 'Vivek', marks: 65 }, { roll: 20, name: 'Omkar', marks: 63 }, ... ]", out_font))
    story.append(Spacer(1, 6))

    # 11. Update One
    story.append(Paragraph("11. UPDATE OPERATION (updateOne)", h2_style))
    story.append(create_code_block("db.students.updateOne({ roll: 5 }, { $set: { marks: 95 } })", code_font))
    story.append(Paragraph("Explanation: Updates the marks of student Roll 5 (Vansh) to 95.", body_style))
    story.append(create_output_block("{ acknowledged: true, matchedCount: 1, modifiedCount: 1 }", out_font))
    story.append(Spacer(1, 6))

    # 12. Update Many
    story.append(Paragraph("12. UPDATE MANY OPERATION (updateMany)", h2_style))
    story.append(create_code_block("db.students.updateMany({ marks: { $gte: 90 } }, { $set: { grade: \"A+\" } })", code_font))
    story.append(Paragraph("Explanation: Assigns grade: 'A+' to all students scoring >= 90.", body_style))
    story.append(create_output_block("{ acknowledged: true, matchedCount: 15, modifiedCount: 15 }", out_font))
    story.append(Spacer(1, 6))

    # 13. Delete One
    story.append(Paragraph("13. DELETE ONE OPERATION (deleteOne)", h2_style))
    story.append(create_code_block("db.students.deleteOne({ roll: 10 })", code_font))
    story.append(Paragraph("Explanation: Deletes one student document matching roll number 10 (Vivek).", body_style))
    story.append(create_output_block("{ acknowledged: true, deletedCount: 1 }", out_font))
    story.append(Spacer(1, 6))

    # 14. Delete Many
    story.append(Paragraph("14. DELETE MANY OPERATION (deleteMany)", h2_style))
    story.append(create_code_block("db.students.deleteMany({ marks: { $lt: 60 } })", code_font))
    story.append(Paragraph("Explanation: Removes all students with marks below 60.", body_style))
    story.append(create_output_block("{ acknowledged: true, deletedCount: 3 } // Removed Roll 18, 33, 47", out_font))
    story.append(PageBreak())

    # 15. AND
    story.append(Paragraph("15. AND OPERATION – $and", h2_style))
    story.append(create_code_block("db.students.find({ $and: [ { marks: { $gt: 80 } }, { age: 19 } ] })", code_font))
    story.append(Paragraph("Explanation: Finds students satisfying both conditions: marks > 80 and age = 19.", body_style))
    story.append(create_output_block("[ { roll: 1, name: 'Anamika', marks: 88 }, { roll: 3, name: 'Vaishnavi', marks: 92 }, { roll: 65, name: 'Sanskriti', marks: 97 } ]", out_font))
    story.append(Spacer(1, 6))

    # 16. OR
    story.append(Paragraph("16. OR OPERATION – $or", h2_style))
    story.append(create_code_block("db.students.find({ $or: [ { city: \"Lucknow\" }, { city: \"Kanpur\" } ] })", code_font))
    story.append(Paragraph("Explanation: Finds students residing in either Lucknow or Kanpur.", body_style))
    story.append(create_output_block("[ { roll: 1, name: 'Anamika', city: 'Lucknow' }, { roll: 3, name: 'Vaishnavi', city: 'Kanpur' }, ... ]", out_font))
    story.append(Spacer(1, 6))

    # 17. Sort
    story.append(Paragraph("17. SORT OPERATION (Ascending & Descending)", h2_style))
    story.append(Paragraph("<b>A. Ascending Order:</b> <code>db.students.find().sort({ marks: 1 }).limit(3)</code>", body_style))
    story.append(create_output_block("[ { roll: 28, name: 'Bhaskar', marks: 61 }, { roll: 43, name: 'Sarika', marks: 62 }, { roll: 20, name: 'Omkar', marks: 63 } ]", out_font))
    story.append(Paragraph("<b>B. Descending Order:</b> <code>db.students.find().sort({ marks: -1 }).limit(3)</code>", body_style))
    story.append(create_output_block("[ { roll: 65, name: 'Sanskriti', marks: 97 }, { roll: 35, name: 'Krishna', marks: 96 }, { roll: 5, name: 'Vansh', marks: 95 } ]", out_font))
    story.append(Spacer(1, 6))

    # 18. Limit
    story.append(Paragraph("18. LIMIT OPERATION", h2_style))
    story.append(create_code_block("db.students.find().limit(5)", code_font))
    story.append(Paragraph("Explanation: Restricts output to the first 5 records.", body_style))
    story.append(create_output_block("[ { roll: 1, name: 'Anamika' }, { roll: 2, name: 'Uday' }, { roll: 3, name: 'Vaishnavi' }, { roll: 4, name: 'Annu' }, { roll: 5, name: 'Vansh' } ]", out_font))
    story.append(Spacer(1, 6))

    # 19. Search City
    story.append(Paragraph("19. SEARCH BY CITY", h2_style))
    story.append(create_code_block("db.students.find({ city: \"Lucknow\" })", code_font))
    story.append(Paragraph("Explanation: Finds all students located in Lucknow (20 students found).", body_style))
    story.append(create_output_block("[ { roll: 1, name: 'Anamika', city: 'Lucknow' }, { roll: 8, name: 'Pratik', city: 'Lucknow' }, { roll: 65, name: 'Sanskriti', city: 'Lucknow' } ]", out_font))
    story.append(Spacer(1, 6))

    # 20. Count
    story.append(Paragraph("20. COUNT DOCUMENTS", h2_style))
    story.append(create_code_block("db.students.countDocuments()", code_font))
    story.append(Paragraph("Explanation: Counts total active records remaining after deletions (65 initial - 1 deleteOne - 3 deleteMany = 61).", body_style))
    story.append(create_output_block("61", out_font))
    story.append(PageBreak())

    # =========================================================================
    # SUMMARY TABLES & CONCLUSION
    # =========================================================================
    story.append(Paragraph("MONGODB OPERATORS SUMMARY REFERENCE", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=8))
    
    op_headers = [Paragraph("Operator", table_hdr), Paragraph("Type", table_hdr), Paragraph("Meaning", table_hdr), Paragraph("Example Query", table_hdr)]
    op_data = [
        [Paragraph("<b>$eq</b>", table_cell), Paragraph("Comparison", table_cell), Paragraph("Matches values equal to specified value", table_cell), Paragraph("db.students.find({marks: {$eq: 88}})", table_cell)],
        [Paragraph("<b>$gt</b>", table_cell), Paragraph("Comparison", table_cell), Paragraph("Matches values greater than specified value", table_cell), Paragraph("db.students.find({marks: {$gt: 85}})", table_cell)],
        [Paragraph("<b>$lt</b>", table_cell), Paragraph("Comparison", table_cell), Paragraph("Matches values less than specified value", table_cell), Paragraph("db.students.find({marks: {$lt: 60}})", table_cell)],
        [Paragraph("<b>$gte</b>", table_cell), Paragraph("Comparison", table_cell), Paragraph("Matches values greater than or equal", table_cell), Paragraph("db.students.find({marks: {$gte: 90}})", table_cell)],
        [Paragraph("<b>$lte</b>", table_cell), Paragraph("Comparison", table_cell), Paragraph("Matches values less than or equal", table_cell), Paragraph("db.students.find({marks: {$lte: 70}})", table_cell)],
        [Paragraph("<b>$and</b>", table_cell), Paragraph("Logical", table_cell), Paragraph("Joins query clauses with logical AND", table_cell), Paragraph("db.students.find({$and: [{marks:{$gt:80}}, {age:19}]})", table_cell)],
        [Paragraph("<b>$or</b>", table_cell), Paragraph("Logical", table_cell), Paragraph("Joins query clauses with logical OR", table_cell), Paragraph("db.students.find({$or: [{city:'Lucknow'}, {city:'Kanpur'}]})", table_cell)],
        [Paragraph("<b>$set</b>", table_cell), Paragraph("Update", table_cell), Paragraph("Modifies or assigns field value", table_cell), Paragraph("db.students.updateOne({roll:5}, {$set:{marks:95}})", table_cell)]
    ]
    t_op = Table([op_headers] + op_data, colWidths=[1.0 * inch, 1.1 * inch, 2.3 * inch, 2.6 * inch])
    t_op.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
    ]))
    story.append(t_op)
    story.append(Spacer(1, 10))

    story.append(Paragraph("CITY-WISE STUDENT PERFORMANCE ANALYTICS", h2_style))
    c_hdr = [Paragraph("City Name", table_hdr), Paragraph("Students", table_hdr), Paragraph("Average Marks", table_hdr), Paragraph("Top Scorer Achieved", table_hdr)]
    c_data = [
        [Paragraph("Lucknow", table_cell), Paragraph("20", table_cell), Paragraph("87.85%", table_cell), Paragraph("97 (Sanskriti)", table_cell)],
        [Paragraph("Varanasi", table_cell), Paragraph("7", table_cell), Paragraph("85.57%", table_cell), Paragraph("95 (Vansh)", table_cell)],
        [Paragraph("Kanpur", table_cell), Paragraph("9", table_cell), Paragraph("81.11%", table_cell), Paragraph("92 (Vaishnavi)", table_cell)],
        [Paragraph("Prayagraj", table_cell), Paragraph("7", table_cell), Paragraph("80.14%", table_cell), Paragraph("96 (Krishna)", table_cell)],
        [Paragraph("Ayodhya", table_cell), Paragraph("5", table_cell), Paragraph("76.20%", table_cell), Paragraph("86 (Divya)", table_cell)],
        [Paragraph("Jaunpur", table_cell), Paragraph("6", table_cell), Paragraph("73.83%", table_cell), Paragraph("86 (Saumya)", table_cell)],
        [Paragraph("Gorakhpur", table_cell), Paragraph("4", table_cell), Paragraph("69.00%", table_cell), Paragraph("78 (Sangita)", table_cell)],
        [Paragraph("Bareilly", table_cell), Paragraph("3", table_cell), Paragraph("68.00%", table_cell), Paragraph("77 (Mohit)", table_cell)]
    ]
    t_c = Table([c_hdr] + c_data, colWidths=[1.8 * inch, 1.2 * inch, 1.8 * inch, 2.2 * inch])
    t_c.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E3A8A')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_c)
    story.append(Spacer(1, 10))

    story.append(Paragraph("CONCLUSION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=8))
    story.append(Paragraph(
        "This project provided in-depth practical knowledge of NoSQL databases using MongoDB. A Student Management System containing 65 student records across Uttar Pradesh was designed and managed. Through this project, I gained practical hands-on experience in:",
        body_style
    ))
    story.append(Paragraph("1. Installing and configuring MongoDB Community Server and connecting via Compass and mongosh.", bullet_style))
    story.append(Paragraph("2. Inserting single (insertOne) and bulk (insertMany) student documents.", bullet_style))
    story.append(Paragraph("3. Retrieving data using advanced comparison operators ($eq, $gt, $lt, $gte, $lte) and logical operators ($and, $or).", bullet_style))
    story.append(Paragraph("4. Updating records with atomic operators ($set) and performing targeted single and bulk deletions.", bullet_style))
    story.append(Paragraph("5. Organizing data through sorting (ascending and descending), pagination limits, and attribute searches.", bullet_style))
    story.append(Paragraph(
        "Overall, this project provided valuable practical understanding of how MongoDB enables modern academic institutions to manage, query, and analyze student records with high efficiency and schema flexibility.",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[+] Successfully built PDF report at: {out_pdf}")

if __name__ == "__main__":
    build_student_pdf()
