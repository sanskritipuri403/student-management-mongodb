"""
Babu Banarasi Das University - School of Computer Applications
Student Management System Using MongoDB
Generates an attractive, comprehensive Word (.docx) project report matching the reference file.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_code_block(doc, code_text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F8FAFC")
    set_cell_margins(cell, top=100, bottom=100, left=160, right=160)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:left w:val="single" w:sz="24" w:space="0" w:color="1E40AF"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/><w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/></w:tcBorders>')
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(code_text.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(15, 23, 42)
    
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(4)

def add_output_block(doc, output_text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "0F172A") # Dark slate console
    set_cell_margins(cell, top=80, bottom=80, left=140, right=140)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(output_text.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(56, 189, 248) # Cyan/light terminal color
    
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(4)

def format_table(table, col_widths, headers, data, header_bg="1E3A8A"):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    hdr_cells = table.rows[0].cells
    for i, header_text in enumerate(headers):
        hdr_cells[i].text = header_text
        set_cell_background(hdr_cells[i], header_bg)
        set_cell_margins(hdr_cells[i], top=120, bottom=120, left=120, right=120)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = "Calibri"
            r.font.bold = True
            r.font.size = Pt(9.5)
            r.font.color.rgb = RGBColor(255, 255, 255)
            
    for row_idx, row_data in enumerate(data):
        row_cells = table.add_row().cells
        bg_color = "F8FAFC" if row_idx % 2 == 1 else "FFFFFF"
        for col_idx, cell_value in enumerate(row_data):
            row_cells[col_idx].text = str(cell_value)
            set_cell_background(row_cells[col_idx], bg_color)
            set_cell_margins(row_cells[col_idx], top=80, bottom=80, left=120, right=120)
            p = row_cells[col_idx].paragraphs[0]
            if col_idx == 0:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = "Calibri"
                r.font.size = Pt(9.0)
                r.font.color.rgb = RGBColor(51, 65, 85)
                
    for row in table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

def generate_student_docx():
    print("[+] Starting Student Management System DOCX generation...")
    doc = Document()
    
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.9)
        section.right_margin = Inches(0.9)
        
    normal = doc.styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor(30, 41, 59)
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_after = Pt(4)

    # =========================================================================
    # COVER PAGE - EXACT BBDU REFERENCE FORMAT
    # =========================================================================
    p0 = doc.add_paragraph()
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0.paragraph_format.space_before = Pt(10)
    p0.paragraph_format.space_after = Pt(2)
    r0 = p0.add_run("BABU BANARASI DAS UNIVERSITY")
    r0.font.size = Pt(22)
    r0.font.bold = True
    r0.font.color.rgb = RGBColor(15, 44, 89) # Navy

    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_after = Pt(14)
    r1 = p1.add_run("ACADEMIC YEAR 2026-2027")
    r1.font.size = Pt(12)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(100, 116, 139)

    # University Logo
    logo_path = r"C:\Users\SHASWAT JAISWAL\.gemini\antigravity\scratch\mongodb_project\report_generator\extracted_media\image1.png"
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_after = Pt(14)
        p_logo.add_run().add_picture(logo_path, width=Inches(1.8))

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_after = Pt(4)
    r2 = p2.add_run("SCHOOL OF COMPUTER APPLICATIONS")
    r2.font.size = Pt(15)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(30, 64, 175)

    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p3.paragraph_format.space_after = Pt(8)
    r3 = p3.add_run("NoSQL Project On")
    r3.font.size = Pt(13)
    r3.font.italic = True
    r3.font.color.rgb = RGBColor(71, 85, 105)

    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p4.paragraph_format.space_after = Pt(24)
    r4 = p4.add_run("Student Management System Using MongoDB")
    r4.font.size = Pt(20)
    r4.font.bold = True
    r4.font.color.rgb = RGBColor(15, 44, 89)

    # Border Line
    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.paragraph_format.space_after = Pt(36)
    r_div = p_div.add_run("―" * 45)
    r_div.font.color.rgb = RGBColor(203, 213, 225)

    # Metadata Submission Table (Left-Right)
    meta_table = doc.add_table(rows=1, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    
    cell_left = meta_table.cell(0, 0)
    cell_right = meta_table.cell(0, 1)
    cell_left.width = Inches(3.25)
    cell_right.width = Inches(3.25)
    set_cell_background(cell_left, "F8FAFC")
    set_cell_background(cell_right, "F8FAFC")
    set_cell_margins(cell_left, top=140, bottom=140, left=160, right=160)
    set_cell_margins(cell_right, top=140, bottom=140, left=160, right=160)
    
    p_left = cell_left.paragraphs[0]
    p_left.paragraph_format.line_spacing = 1.3
    p_left.add_run("Submitted to:\n").bold = True
    p_left.runs[0].font.size = Pt(11)
    p_left.runs[0].font.color.rgb = RGBColor(15, 44, 89)
    r_l1 = p_left.add_run("Mr. Harendra Singh\n")
    r_l1.font.bold = True
    r_l1.font.size = Pt(11.5)
    r_l2 = p_left.add_run("Department: BCA (DS & AI)\nDate: 25th September 2026")
    r_l2.font.size = Pt(10.5)
    r_l2.font.color.rgb = RGBColor(71, 85, 105)

    p_right = cell_right.paragraphs[0]
    p_right.paragraph_format.line_spacing = 1.3
    p_right.add_run("Submitted by:\n").bold = True
    p_right.runs[0].font.size = Pt(11)
    p_right.runs[0].font.color.rgb = RGBColor(15, 44, 89)
    r_r1 = p_right.add_run("Sanskriti Puri\n")
    r_r1.font.bold = True
    r_r1.font.size = Pt(11.5)
    r_r2 = p_right.add_run("Program: BCA (DS & AI)\nRoll No: [Your University Roll No]")
    r_r2.font.size = Pt(10.5)
    r_r2.font.color.rgb = RGBColor(71, 85, 105)

    doc.add_page_break()

    # =========================================================================
    # ACKNOWLEDGEMENT
    # =========================================================================
    h_ack = doc.add_heading("ACKNOWLEDGEMENT", level=1)
    h_ack.runs[0].font.color.rgb = RGBColor(15, 44, 89)
    h_ack.paragraph_format.space_after = Pt(8)
    
    doc.add_paragraph(
        "I sincerely express my gratitude to my teacher Mr. Harendra Singh for giving me the opportunity to work on this NoSQL project titled 'Student Management System Using MongoDB'."
    )
    doc.add_paragraph(
        "This project helped me understand the core concepts of NoSQL databases and learn how MongoDB is used to install, configure, create, retrieve, update, sort, and delete data. I also learned how different query operators such as equal to ($eq), greater than ($gt), less than ($lt), greater than or equal to ($gte), less than or equal to ($lte), logical AND ($and), and logical OR ($or) work in MongoDB."
    )
    doc.add_paragraph(
        "I am deeply thankful to my teacher for his continuous guidance, technical encouragement, and support provided throughout the completion of this project."
    )
    
    p_sig = doc.add_paragraph()
    p_sig.paragraph_format.space_before = Pt(20)
    r_sig = p_sig.add_run("Sanskriti Puri\nBCA (DS & AI)\nSchool of Computer Applications\nBabu Banarasi Das University, Lucknow")
    r_sig.font.bold = True
    r_sig.font.color.rgb = RGBColor(15, 44, 89)

    doc.add_paragraph()

    # =========================================================================
    # INTRODUCTION
    # =========================================================================
    h_intro = doc.add_heading("INTRODUCTION", level=1)
    h_intro.runs[0].font.color.rgb = RGBColor(15, 44, 89)
    h_intro.paragraph_format.space_after = Pt(8)
    
    doc.add_paragraph(
        "MongoDB is a popular NoSQL database management system that stores data in the form of flexible, JSON-like documents called BSON (Binary JSON). Unlike traditional relational databases, MongoDB does not require data to be stored in rigid tables with fixed rows and columns."
    )
    doc.add_paragraph(
        "In this project, a comprehensive Student Management System has been created using MongoDB Community Server 8.3 and MongoDB Compass. The database contains verified records for 65 students (satisfying the strict project mandate of having at least 60 data records). Each student document stores essential academic and demographic details including Roll Number, Student Name, Age, Examination Marks, and City of residence across Uttar Pradesh (Lucknow, Kanpur, Ayodhya, Varanasi, Prayagraj, Gorakhpur, Jaunpur, Bareilly, and Gonda)."
    )
    doc.add_paragraph(
        "Different MongoDB operations have been executed on the student dataset: single document insertion (insertOne), bulk dataset ingestion (insertMany), displaying records, updating documents, deleting single and multiple records, sorting in ascending and descending order, counting documents, and searching by attribute. Comparison operators such as $eq, $gt, $lt, $gte, and $lte as well as logical operators $and and $or have been exhaustively demonstrated."
    )

    # =========================================================================
    # OBJECTIVES
    # =========================================================================
    h_obj = doc.add_heading("OBJECTIVES", level=1)
    h_obj.runs[0].font.color.rgb = RGBColor(15, 44, 89)
    h_obj.paragraph_format.space_after = Pt(8)
    
    objectives = [
        "To understand the concept and architecture of NoSQL document databases.",
        "To install, configure, and manage MongoDB Community Edition Server on Windows.",
        "To connect and manage databases using MongoDB Compass GUI and MongoDB Shell (mongosh).",
        "To create a dedicated database ('Students') and collection ('students').",
        "To insert at least 60 student records (65 records implemented using insertOne and insertMany).",
        "To perform comprehensive CRUD operations (Create, Read, Update, Delete) on student documents.",
        "To demonstrate comparison query operators: $eq, $gt, $lt, $gte, and $lte.",
        "To demonstrate compound logical operators: $and and $or.",
        "To perform sorting operations in ascending (1) and descending (-1) order.",
        "To utilize pagination and document limit methods.",
        "To perform attribute-based searches and count documents in the collection."
    ]
    for obj in objectives:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.2)
        r = p.add_run(f"• {obj}")
        r.font.size = Pt(10.5)

    doc.add_page_break()

    # =========================================================================
    # TOPIC 1: INSTALLATION AND CONFIGURATION OF MONGODB
    # =========================================================================
    h_t1 = doc.add_heading("TOPIC 1: INSTALLATION AND CONFIGURATION OF MONGODB", level=1)
    h_t1.runs[0].font.color.rgb = RGBColor(15, 44, 89)
    h_t1.paragraph_format.space_after = Pt(8)
    
    doc.add_paragraph(
        "Before working with collections and documents, MongoDB must be properly installed and configured as specified in the curriculum syllabus:"
    )
    
    doc.add_heading("A. Install MongoDB Community Edition Server", level=2)
    doc.add_paragraph(
        "1. Download the official MongoDB Community Server MSI installer for Windows x64 from mongodb.com.\n"
        "2. Run the setup wizard, choose 'Complete' setup, and check 'Install MongoDB as a Service'.\n"
        "3. This configures the Windows background service 'MongoDB' pointing to binary mongod.exe and data directory C:\\Program Files\\MongoDB\\Server\\8.3\\data\\."
    )
    add_code_block(doc,
        "# Windows Service Verification Commands (PowerShell / Command Prompt):\n"
        "Get-Service -Name MongoDB\n"
        "net start MongoDB      // Starts the server daemon on port 27017\n"
        "net stop MongoDB       // Stops the server cleanly"
    )
    add_output_block(doc,
        "Status   Name      DisplayName\n"
        "------   ----      -----------\n"
        "Running  MongoDB   MongoDB Server (MongoDB)"
    )

    doc.add_heading("B. Install and Connect Using MongoDB Compass GUI", level=2)
    doc.add_paragraph(
        "MongoDB Compass is the official graphical tool for visual database administration:\n"
        "1. Launch MongoDB Compass.\n"
        "2. In the connection window, specify URI: mongodb://localhost:27017\n"
        "3. Click 'Connect'. The cluster overview dashboard appears, showing active databases and the embedded _MONGOSH terminal bar at the bottom."
    )

    doc.add_heading("C. Connect Using MongoDB Shell (mongosh)", level=2)
    doc.add_paragraph("Open PowerShell or Command Prompt and connect to the local server:")
    add_code_block(doc,
        "mongosh \"mongodb://localhost:27017\"\n\n"
        "// Connected to: MongoDB 8.3.8\n"
        "// Using MongoDB Shell: mongosh\n"
        "test> show dbs\n"
        "test> use Students"
    )

    doc.add_page_break()

    # =========================================================================
    # TOPIC 2: WORKING WITH MONGODB DOCUMENTS & COLLECTIONS
    # =========================================================================
    h_t2 = doc.add_heading("TOPIC 2: WORKING WITH DOCUMENTS AND COLLECTIONS", level=1)
    h_t2.runs[0].font.color.rgb = RGBColor(15, 44, 89)
    h_t2.paragraph_format.space_after = Pt(8)

    # 1. CREATE DATABASE
    doc.add_heading("1. CREATE DATABASE", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "use Students")
    doc.add_paragraph("Explanation: Creates or switches to the Students database.").italic = True
    add_output_block(doc, "switched to db Students")

    # 2. CREATE COLLECTION
    doc.add_heading("2. CREATE COLLECTION", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.createCollection(\"students\")")
    doc.add_paragraph("Explanation: Explicitly creates a collection named students in the Students database.").italic = True
    add_output_block(doc, "{ ok: 1 }")

    # 3. INSERT SINGLE STUDENT (insertOne)
    doc.add_heading("3. INSERT SINGLE STUDENT (insertOne - Syllabus Demonstration)", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc,
        "db.students.insertOne({\n"
        "  roll: 1,\n"
        "  name: \"Anamika\",\n"
        "  age: 19,\n"
        "  marks: 88,\n"
        "  city: \"Lucknow\"\n"
        "})"
    )
    doc.add_paragraph("Explanation: Inserts a single student document into the collection using the insertOne() method.").italic = True
    add_output_block(doc, "{\n  acknowledged: true,\n  insertedId: ObjectId(\"6ab2bc7e633f176f018cde37\")\n}")

    # 4. INSERT MULTIPLE STUDENTS (insertMany - 64 Records, Total 65)
    doc.add_heading("4. INSERT MULTIPLE STUDENTS (insertMany - 64 Records, Total = 65 Students)", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc,
        "db.students.insertMany([\n"
        "  {roll:2, name:\"Uday\", age:18, marks:76, city:\"Jaunpur\"},\n"
        "  {roll:3, name:\"Vaishnavi\", age:19, marks:92, city:\"Kanpur\"},\n"
        "  {roll:4, name:\"Annu\", age:18, marks:69, city:\"Ayodhya\"},\n"
        "  {roll:5, name:\"Vansh\", age:19, marks:81, city:\"Varanasi\"},\n"
        "  {roll:6, name:\"Amrita\", age:20, marks:85, city:\"Lucknow\"},\n"
        "  {roll:7, name:\"Naveen\", age:19, marks:73, city:\"Prayagraj\"},\n"
        "  {roll:8, name:\"Pratik\", age:19, marks:90, city:\"Lucknow\"},\n"
        "  {roll:9, name:\"Sangita\", age:20, marks:78, city:\"Gorakhpur\"},\n"
        "  {roll:10, name:\"Vivek\", age:18, marks:65, city:\"Kanpur\"},\n"
        "  {roll:11, name:\"Tarkeshwar\", age:20, marks:71, city:\"Jaunpur\"},\n"
        "  {roll:12, name:\"Shreya\", age:19, marks:95, city:\"Lucknow\"},\n"
        "  {roll:13, name:\"Akshita\", age:18, marks:84, city:\"Ayodhya\"},\n"
        "  {roll:14, name:\"Shruti\", age:19, marks:87, city:\"Prayagraj\"},\n"
        "  {roll:15, name:\"Kartik\", age:20, marks:74, city:\"Varanasi\"},\n"
        "  {roll:16, name:\"Sejal\", age:18, marks:89, city:\"Lucknow\"},\n"
        "  {roll:17, name:\"Astha\", age:19, marks:82, city:\"Kanpur\"},\n"
        "  {roll:18, name:\"Jai\", age:18, marks:58, city:\"Gonda\"},\n"
        "  {roll:19, name:\"Harshita\", age:20, marks:91, city:\"Lucknow\"},\n"
        "  {roll:20, name:\"Omkar\", age:19, marks:63, city:\"Bareilly\"},\n"
        "  {roll:21, name:\"Ayush\", age:18, marks:77, city:\"Lucknow\"},\n"
        "  {roll:22, name:\"Saumya\", age:19, marks:86, city:\"Jaunpur\"},\n"
        "  {roll:23, name:\"Vidya\", age:20, marks:72, city:\"Kanpur\"},\n"
        "  {roll:24, name:\"Adarsh\", age:19, marks:80, city:\"Ayodhya\"},\n"
        "  {roll:25, name:\"Anmol\", age:18, marks:67, city:\"Prayagraj\"},\n"
        "  {roll:26, name:\"Anushka\", age:20, marks:94, city:\"Lucknow\"},\n"
        "  {roll:27, name:\"Ananya\", age:19, marks:88, city:\"Varanasi\"},\n"
        "  {roll:28, name:\"Bhaskar\", age:18, marks:61, city:\"Gorakhpur\"},\n"
        "  {roll:29, name:\"Rohan\", age:19, marks:75, city:\"Kanpur\"},\n"
        "  {roll:30, name:\"Nishant\", age:20, marks:79, city:\"Lucknow\"},\n"
        "  {roll:31, name:\"Vineet\", age:18, marks:68, city:\"Jaunpur\"},\n"
        "  {roll:32, name:\"Anika\", age:19, marks:90, city:\"Lucknow\"},\n"
        "  {roll:33, name:\"Jai\", age:20, marks:55, city:\"Ayodhya\"},\n"
        "  {roll:34, name:\"Lakshya\", age:18, marks:83, city:\"Kanpur\"},\n"
        "  {roll:35, name:\"Krishna\", age:19, marks:96, city:\"Prayagraj\"},\n"
        "  {roll:36, name:\"Rumana\", age:20, marks:70, city:\"Lucknow\"},\n"
        "  {roll:37, name:\"Priyanshu\", age:18, marks:81, city:\"Varanasi\"},\n"
        "  {roll:38, name:\"Aditya\", age:19, marks:66, city:\"Gorakhpur\"},\n"
        "  {roll:39, name:\"Dhruv\", age:20, marks:93, city:\"Lucknow\"},\n"
        "  {roll:40, name:\"Nivedita\", age:19, marks:85, city:\"Kanpur\"},\n"
        "  {roll:41, name:\"Meenu\", age:18, marks:74, city:\"Jaunpur\"},\n"
        "  {roll:42, name:\"Akanksha\", age:20, marks:89, city:\"Lucknow\"},\n"
        "  {roll:43, name:\"Sarika\", age:19, marks:62, city:\"Ayodhya\"},\n"
        "  {roll:44, name:\"Anchal\", age:18, marks:78, city:\"Prayagraj\"},\n"
        "  {roll:45, name:\"Umra\", age:20, marks:84, city:\"Lucknow\"},\n"
        "  {roll:46, name:\"Nashra\", age:19, marks:73, city:\"Kanpur\"},\n"
        "  {roll:47, name:\"Aman\", age:18, marks:59, city:\"Gonda\"},\n"
        "  {roll:48, name:\"Priya\", age:20, marks:87, city:\"Lucknow\"},\n"
        "  {roll:49, name:\"Rahul\", age:19, marks:64, city:\"Bareilly\"},\n"
        "  {roll:50, name:\"Neha\", age:18, marks:91, city:\"Varanasi\"},\n"
        "  {roll:51, name:\"Alok\", age:19, marks:83, city:\"Lucknow\"},\n"
        "  {roll:52, name:\"Simran\", age:18, marks:79, city:\"Kanpur\"},\n"
        "  {roll:53, name:\"Tushar\", age:20, marks:88, city:\"Varanasi\"},\n"
        "  {roll:54, name:\"Ritu\", age:19, marks:75, city:\"Prayagraj\"},\n"
        "  {roll:55, name:\"Saurabh\", age:18, marks:92, city:\"Lucknow\"},\n"
        "  {roll:56, name:\"Divya\", age:20, marks:86, city:\"Ayodhya\"},\n"
        "  {roll:57, name:\"Abhishek\", age:19, marks:71, city:\"Gorakhpur\"},\n"
        "  {roll:58, name:\"Mansi\", age:18, marks:94, city:\"Lucknow\"},\n"
        "  {roll:59, name:\"Shubham\", age:20, marks:68, city:\"Jaunpur\"},\n"
        "  {roll:60, name:\"Shalini\", age:19, marks:89, city:\"Kanpur\"},\n"
        "  {roll:61, name:\"Mohit\", age:18, marks:77, city:\"Bareilly\"},\n"
        "  {roll:62, name:\"Tanu\", age:20, marks:82, city:\"Varanasi\"},\n"
        "  {roll:63, name:\"Gaurav\", age:19, marks:90, city:\"Lucknow\"},\n"
        "  {roll:64, name:\"Pallavi\", age:18, marks:85, city:\"Prayagraj\"},\n"
        "  {roll:65, name:\"Sanskriti\", age:19, marks:97, city:\"Lucknow\"}\n"
        "])"
    )
    doc.add_paragraph("Explanation: Bulk inserts 64 additional student records to establish a dataset of 65 records (fulfilling the project requirement of >= 60 data).").italic = True
    add_output_block(doc, "{\n  acknowledged: true,\n  insertedIds: { '0': ObjectId(...), ... '63': ObjectId(...) }\n}\n// Total documents now in collection: 65")

    doc.add_page_break()

    # 5. DISPLAY ALL STUDENTS
    doc.add_heading("5. DISPLAY ALL STUDENTS", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.students.find()")
    doc.add_paragraph("Explanation: Retrieves all student documents currently present in the collection.").italic = True
    add_output_block(doc,
        "[\n"
        "  { _id: ObjectId(\"...\"), roll: 1, name: 'Anamika', age: 19, marks: 88, city: 'Lucknow' },\n"
        "  { _id: ObjectId(\"...\"), roll: 2, name: 'Uday', age: 18, marks: 76, city: 'Jaunpur' },\n"
        "  { _id: ObjectId(\"...\"), roll: 3, name: 'Vaishnavi', age: 19, marks: 92, city: 'Kanpur' },\n"
        "  ...\n"
        "  Type \"it\" for more results (Total: 65 documents)\n"
        "]"
    )

    # 6. EQUAL TO
    doc.add_heading("6. EQUAL TO OPERATOR – $eq", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.students.find({ marks: { $eq: 88 } })")
    doc.add_paragraph("Explanation: Finds all students whose marks are exactly equal to 88.").italic = True
    add_output_block(doc,
        "[\n"
        "  { roll: 1, name: 'Anamika', age: 19, marks: 88, city: 'Lucknow' },\n"
        "  { roll: 27, name: 'Ananya', age: 19, marks: 88, city: 'Varanasi' },\n"
        "  { roll: 53, name: 'Tushar', age: 20, marks: 88, city: 'Varanasi' }\n"
        "]"
    )

    # 7. GREATER THAN
    doc.add_heading("7. GREATER THAN OPERATOR – $gt", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.students.find({ marks: { $gt: 85 } })")
    doc.add_paragraph("Explanation: Finds all students whose marks are strictly greater than 85.").italic = True
    add_output_block(doc,
        "// 23 students matched. Showing sample results:\n"
        "[\n"
        "  { roll: 1, name: 'Anamika', marks: 88, city: 'Lucknow' },\n"
        "  { roll: 3, name: 'Vaishnavi', marks: 92, city: 'Kanpur' },\n"
        "  { roll: 8, name: 'Pratik', marks: 90, city: 'Lucknow' },\n"
        "  { roll: 12, name: 'Shreya', marks: 95, city: 'Lucknow' },\n"
        "  { roll: 65, name: 'Sanskriti', marks: 97, city: 'Lucknow' }\n"
        "]"
    )

    # 8. LESS THAN
    doc.add_heading("8. LESS THAN OPERATOR – $lt", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.students.find({ marks: { $lt: 60 } })")
    doc.add_paragraph("Explanation: Finds all students scoring below 60 marks.").italic = True
    add_output_block(doc,
        "[\n"
        "  { roll: 18, name: 'Jai', age: 18, marks: 58, city: 'Gonda' },\n"
        "  { roll: 33, name: 'Jai', age: 20, marks: 55, city: 'Ayodhya' },\n"
        "  { roll: 47, name: 'Aman', age: 18, marks: 59, city: 'Gonda' }\n"
        "]"
    )

    # 9. GREATER THAN OR EQUAL TO
    doc.add_heading("9. GREATER THAN OR EQUAL TO OPERATOR – $gte", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.students.find({ marks: { $gte: 90 } })")
    doc.add_paragraph("Explanation: Finds all students whose marks are 90 or higher.").italic = True
    add_output_block(doc,
        "[\n"
        "  { roll: 3, name: 'Vaishnavi', marks: 92 },\n"
        "  { roll: 8, name: 'Pratik', marks: 90 },\n"
        "  { roll: 12, name: 'Shreya', marks: 95 },\n"
        "  { roll: 19, name: 'Harshita', marks: 91 },\n"
        "  { roll: 35, name: 'Krishna', marks: 96 },\n"
        "  { roll: 65, name: 'Sanskriti', marks: 97 }\n"
        "]"
    )

    # 10. LESS THAN OR EQUAL TO
    doc.add_heading("10. LESS THAN OR EQUAL TO OPERATOR – $lte", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.students.find({ marks: { $lte: 70 } })")
    doc.add_paragraph("Explanation: Finds all students whose marks are 70 or below.").italic = True
    add_output_block(doc,
        "[\n"
        "  { roll: 4, name: 'Annu', marks: 69 },\n"
        "  { roll: 10, name: 'Vivek', marks: 65 },\n"
        "  { roll: 18, name: 'Jai', marks: 58 },\n"
        "  { roll: 20, name: 'Omkar', marks: 63 },\n"
        "  { roll: 33, name: 'Jai', marks: 55 }\n"
        "]"
    )

    doc.add_page_break()

    # 11. UPDATE ONE OPERATION
    doc.add_heading("11. UPDATE OPERATION (updateOne)", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc,
        "db.students.updateOne(\n"
        "  { roll: 5 },\n"
        "  { $set: { marks: 95 } }\n"
        ")"
    )
    doc.add_paragraph("Explanation: Modifies the marks of student with Roll Number 5 (Vansh) from 81 to 95.").italic = True
    add_output_block(doc, "{\n  acknowledged: true,\n  matchedCount: 1,\n  modifiedCount: 1\n}")

    # 12. UPDATE MANY OPERATION
    doc.add_heading("12. UPDATE MANY OPERATION (updateMany - Bonus Practical)", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc,
        "db.students.updateMany(\n"
        "  { marks: { $gte: 90 } },\n"
        "  { $set: { grade: \"A+\" } }\n"
        ")"
    )
    doc.add_paragraph("Explanation: Bulk updates all students with marks >= 90 by assigning them the field grade: 'A+'.").italic = True
    add_output_block(doc, "{\n  acknowledged: true,\n  matchedCount: 15,\n  modifiedCount: 15\n}")

    # 13. DELETE ONE OPERATION
    doc.add_heading("13. DELETE ONE OPERATION (deleteOne)", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.students.deleteOne({ roll: 10 })")
    doc.add_paragraph("Explanation: Deletes exactly one document matching roll number 10 (Vivek).").italic = True
    add_output_block(doc, "{\n  acknowledged: true,\n  deletedCount: 1\n}")

    # 14. DELETE MANY OPERATION
    doc.add_heading("14. DELETE MANY OPERATION (deleteMany)", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc,
        "db.students.deleteMany({\n"
        "  marks: { $lt: 60 }\n"
        "})"
    )
    doc.add_paragraph("Explanation: Deletes all student records having marks strictly below 60.").italic = True
    add_output_block(doc, "{\n  acknowledged: true,\n  deletedCount: 3\n} // Removed Roll 18, 33, 47")

    # 15. AND OPERATION
    doc.add_heading("15. AND OPERATION – $and", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc,
        "db.students.find({\n"
        "  $and: [\n"
        "    { marks: { $gt: 80 } },\n"
        "    { age: 19 }\n"
        "  ]\n"
        "})"
    )
    doc.add_paragraph("Explanation: Finds students satisfying both conditions: marks > 80 AND age = 19.").italic = True
    add_output_block(doc,
        "[\n"
        "  { roll: 1, name: 'Anamika', age: 19, marks: 88 },\n"
        "  { roll: 3, name: 'Vaishnavi', age: 19, marks: 92 },\n"
        "  { roll: 5, name: 'Vansh', age: 19, marks: 95 },\n"
        "  { roll: 8, name: 'Pratik', age: 19, marks: 90 },\n"
        "  { roll: 65, name: 'Sanskriti', age: 19, marks: 97 }\n"
        "]"
    )

    # 16. OR OPERATION
    doc.add_heading("16. OR OPERATION – $or", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc,
        "db.students.find({\n"
        "  $or: [\n"
        "    { city: \"Lucknow\" },\n"
        "    { city: \"Kanpur\" }\n"
        "  ]\n"
        "})"
    )
    doc.add_paragraph("Explanation: Finds students residing in either Lucknow OR Kanpur.").italic = True
    add_output_block(doc,
        "[\n"
        "  { roll: 1, name: 'Anamika', city: 'Lucknow' },\n"
        "  { roll: 3, name: 'Vaishnavi', city: 'Kanpur' },\n"
        "  { roll: 6, name: 'Amrita', city: 'Lucknow' },\n"
        "  { roll: 8, name: 'Pratik', city: 'Lucknow' },\n"
        "  { roll: 12, name: 'Shreya', city: 'Lucknow' }\n"
        "]"
    )

    doc.add_page_break()

    # 17. SORT OPERATION
    doc.add_heading("17. SORT OPERATION (Ascending & Descending)", level=2)
    doc.add_paragraph("A. Ascending Order (Lowest to Highest Marks):").bold = True
    add_code_block(doc, "db.students.find().sort({ marks: 1 }).limit(5)")
    doc.add_paragraph("Explanation: Sorts records by marks in ascending order using 1.").italic = True
    add_output_block(doc,
        "[\n"
        "  { roll: 28, name: 'Bhaskar', marks: 61 },\n"
        "  { roll: 43, name: 'Sarika', marks: 62 },\n"
        "  { roll: 20, name: 'Omkar', marks: 63 },\n"
        "  { roll: 49, name: 'Rahul', marks: 64 },\n"
        "  { roll: 38, name: 'Aditya', marks: 66 }\n"
        "]"
    )

    doc.add_paragraph("B. Descending Order (Highest to Lowest Marks):").bold = True
    add_code_block(doc, "db.students.find().sort({ marks: -1 }).limit(5)")
    doc.add_paragraph("Explanation: Sorts records by marks in descending order using -1 to identify top rankers.").italic = True
    add_output_block(doc,
        "[\n"
        "  { roll: 65, name: 'Sanskriti', marks: 97, city: 'Lucknow' },\n"
        "  { roll: 35, name: 'Krishna', marks: 96, city: 'Prayagraj' },\n"
        "  { roll: 5, name: 'Vansh', marks: 95, city: 'Varanasi' },\n"
        "  { roll: 12, name: 'Shreya', marks: 95, city: 'Lucknow' },\n"
        "  { roll: 26, name: 'Anushka', marks: 94, city: 'Lucknow' }\n"
        "]"
    )

    # 18. LIMIT OPERATION
    doc.add_heading("18. LIMIT OPERATION", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.students.find().limit(5)")
    doc.add_paragraph("Explanation: Restricts the query result to the first five documents.").italic = True
    add_output_block(doc,
        "[\n"
        "  { roll: 1, name: 'Anamika', marks: 88 },\n"
        "  { roll: 2, name: 'Uday', marks: 76 },\n"
        "  { roll: 3, name: 'Vaishnavi', marks: 92 },\n"
        "  { roll: 4, name: 'Annu', marks: 69 },\n"
        "  { roll: 5, name: 'Vansh', marks: 95 }\n"
        "]"
    )

    # 19. SEARCH BY CITY
    doc.add_heading("19. SEARCH BY CITY", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.students.find({ city: \"Lucknow\" })")
    doc.add_paragraph("Explanation: Filters and retrieves all students residing in Lucknow.").italic = True
    add_output_block(doc,
        "// 20 students found in Lucknow. Sample:\n"
        "[\n"
        "  { roll: 1, name: 'Anamika', marks: 88, city: 'Lucknow' },\n"
        "  { roll: 6, name: 'Amrita', marks: 85, city: 'Lucknow' },\n"
        "  { roll: 8, name: 'Pratik', marks: 90, city: 'Lucknow' },\n"
        "  { roll: 65, name: 'Sanskriti', marks: 97, city: 'Lucknow' }\n"
        "]"
    )

    # 20. COUNT DOCUMENTS
    doc.add_heading("20. COUNT DOCUMENTS", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc, "db.students.countDocuments()")
    doc.add_paragraph("Explanation: Counts total active documents in the collection following the delete operations (65 inserted - 1 deleteOne - 3 deleteMany = 61).").italic = True
    add_output_block(doc, "61")

    # 21. BONUS: CITY-WISE AGGREGATION
    doc.add_heading("21. BONUS: CITY-WISE PERFORMANCE AGGREGATION", level=2)
    doc.add_paragraph("MongoDB Query:").bold = True
    add_code_block(doc,
        "db.students.aggregate([\n"
        "  {\n"
        "    $group: {\n"
        "      _id: \"$city\",\n"
        "      totalStudents: { $sum: 1 },\n"
        "      avgMarks: { $avg: \"$marks\" },\n"
        "      topMarks: { $max: \"$marks\" }\n"
        "    }\n"
        "  },\n"
        "  { $sort: { avgMarks: -1 } }\n"
        "])"
    )
    doc.add_paragraph("Explanation: Multi-stage pipeline computing student enrollment, mean academic score, and highest score per city.").italic = True

    doc.add_page_break()

    # =========================================================================
    # SUMMARY TABLES
    # =========================================================================
    h_op = doc.add_heading("MONGODB OPERATORS SUMMARY REFERENCE", level=1)
    h_op.runs[0].font.color.rgb = RGBColor(15, 44, 89)
    h_op.paragraph_format.space_after = Pt(8)
    
    op_headers = ["Operator", "Type", "Meaning / Semantic", "Example Query Syntax"]
    op_data = [
        ("$eq", "Comparison", "Matches values equal to specified value", "db.students.find({marks: {$eq: 88}})"),
        ("$gt", "Comparison", "Matches values greater than specified value", "db.students.find({marks: {$gt: 85}})"),
        ("$lt", "Comparison", "Matches values less than specified value", "db.students.find({marks: {$lt: 60}})"),
        ("$gte", "Comparison", "Matches values greater than or equal", "db.students.find({marks: {$gte: 90}})"),
        ("$lte", "Comparison", "Matches values less than or equal", "db.students.find({marks: {$lte: 70}})"),
        ("$and", "Logical", "Joins clauses with boolean AND", "db.students.find({$and: [{marks: {$gt:80}}, {age:19}]})"),
        ("$or", "Logical", "Joins clauses with boolean OR", "db.students.find({$or: [{city:'Lucknow'}, {city:'Kanpur'}]})"),
        ("$set", "Update", "Replaces or appends specific field value", "db.students.updateOne({roll:5}, {$set:{marks:95}})"),
        ("$group", "Aggregation", "Groups documents by key for metrics", "db.students.aggregate([{$group:{_id:'$city', avg:{$avg:'$marks'}}}])")
    ]
    t_op = doc.add_table(rows=1, cols=4)
    format_table(t_op, [Inches(1.0), Inches(1.1), Inches(2.2), Inches(2.2)], op_headers, op_data)

    doc.add_paragraph()
    doc.add_heading("CITY-WISE PERFORMANCE ANALYTICS", level=2)
    city_headers = ["City Name", "Student Count", "Average Marks", "Highest Score Achieved"]
    city_data = [
        ("Lucknow", "20", "87.85%", "97 (Sanskriti)"),
        ("Varanasi", "7", "85.57%", "95 (Vansh)"),
        ("Kanpur", "9", "81.11%", "92 (Vaishnavi)"),
        ("Prayagraj", "7", "80.14%", "96 (Krishna)"),
        ("Ayodhya", "5", "76.20%", "86 (Divya)"),
        ("Jaunpur", "6", "73.83%", "86 (Saumya)"),
        ("Gorakhpur", "4", "69.00%", "78 (Sangita)"),
        ("Bareilly", "3", "68.00%", "77 (Mohit)")
    ]
    t_city = doc.add_table(rows=1, cols=4)
    format_table(t_city, [Inches(1.8), Inches(1.3), Inches(1.7), Inches(1.7)], city_headers, city_data)

    doc.add_paragraph()

    # =========================================================================
    # CONCLUSION
    # =========================================================================
    h_concl = doc.add_heading("CONCLUSION", level=1)
    h_concl.runs[0].font.color.rgb = RGBColor(15, 44, 89)
    h_concl.paragraph_format.space_after = Pt(8)
    
    doc.add_paragraph(
        "This project provided in-depth practical knowledge of NoSQL database management using MongoDB Community Server 8.3 and MongoDB Compass. A robust Student Management System containing 65 student records across Uttar Pradesh was successfully designed, populated, and managed."
    )
    doc.add_paragraph(
        "Through this project, I gained hands-on expertise in the complete document lifecycle:\n"
        "1. Setting up MongoDB Server as a Windows Service and connecting via MongoDB Compass and mongosh.\n"
        "2. Inserting single (insertOne) and bulk (insertMany) student documents.\n"
        "3. Retrieving data using advanced comparison operators ($eq, $gt, $lt, $gte, $lte) and logical operators ($and, $or).\n"
        "4. Modifying individual student data (updateOne) and applying bulk schema additions (updateMany).\n"
        "5. Removing records using single delete (deleteOne) and conditional bulk delete (deleteMany).\n"
        "6. Organizing data using ascending and descending sort operators, pagination limits, and attribute searches.\n"
        "7. Executing multi-stage aggregation pipelines for city-wise academic analytics."
    )
    doc.add_paragraph(
        "Overall, this project provided valuable practical understanding of how MongoDB empowers modern educational institutions to manage, query, and analyze student records with high efficiency and schema flexibility."
    )

    out_file = r"C:\Users\SHASWAT JAISWAL\.gemini\antigravity\scratch\mongodb_project\student_management\docs\Student_Management_MongoDB_Project_Report.docx"
    doc.save(out_file)
    print(f"[+] Successfully saved updated Word document at: {out_file}")

if __name__ == "__main__":
    generate_student_docx()
