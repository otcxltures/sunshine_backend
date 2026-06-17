#!/usr/bin/env python3
"""Seed the database with sample courses and school info."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy.orm import Session
from app.core.database import engine, SessionLocal, Base
from app.models.course import Course
from app.models.school_info import SchoolInfo
from app.models.user import User
from app.core.security import get_password_hash


def seed_database():
    db = SessionLocal()
    try:
        Base.metadata.create_all(bind=engine)
        
        existing = db.query(Course).first()
        if existing:
            print("Database already seeded. Skipping...")
            return
        
        courses = [
            Course(
                title="Bachelor of Medicine & Surgery (MBChB)",
                name="Medicine",
                description="A comprehensive 6-year medical degree program covering anatomy, physiology, pathology, clinical medicine, and surgery. Includes extensive hospital rotations and hands-on patient care training.",
                duration="6 years",
                seats=50,
                requirements="A in Biology, Chemistry, Physics, and Mathematics. KCSE mean grade A- or equivalent. Pass medical entrance exam and interview."
            ),
            Course(
                title="Bachelor of Pharmacy",
                name="Pharmacy",
                description="Study pharmaceutical sciences, drug formulation, pharmacology, clinical pharmacy, and patient counseling. Prepare for careers in hospital pharmacies, pharmaceutical industry, and research.",
                duration="5 years",
                seats=40,
                requirements="A in Chemistry, Biology, and Mathematics/Physics. KCSE mean grade B+ or equivalent."
            ),
            Course(
                title="Bachelor of Laws (LLB)",
                name="Law",
                description="Comprehensive legal education covering constitutional law, criminal law, contract law, international law, and legal practice. Moot court sessions and internship opportunities at law firms.",
                duration="4 years",
                seats=60,
                requirements="B+ in English and any humanities subject. KCSE mean grade B+ or equivalent. Strong analytical and communication skills."
            ),
            Course(
                title="Bachelor of Nursing",
                name="Nursing",
                description="Train to become a registered nurse with expertise in patient care, community health, midwifery, and nursing leadership. Clinical placements in leading hospitals and community health centers.",
                duration="4 years",
                seats=45,
                requirements="C+ in Biology, Chemistry, and English. KCSE mean grade C+ or equivalent. Compassionate and dedicated to healthcare."
            ),
            Course(
                title="Bachelor of Public Health",
                name="Public Health",
                description="Focus on epidemiology, health policy, environmental health, disease prevention, and community health promotion. Prepare for roles in government health departments, NGOs, and WHO.",
                duration="4 years",
                seats=35,
                requirements="C+ in Biology, Chemistry, and Mathematics/Geography. KCSE mean grade C+ or equivalent."
            ),
            Course(
                title="Bachelor of Biomedical Science",
                name="Biomedical Science",
                description="Study human biology, medical microbiology, hematology, immunology, and laboratory diagnostics. Foundation for medical research, diagnostic labs, and further medical studies.",
                duration="4 years",
                seats=30,
                requirements="B in Biology, Chemistry, and Physics/Mathematics. KCSE mean grade B or equivalent."
            ),
            Course(
                title="Bachelor of Civil Engineering",
                name="Civil Engineering",
                description="Design and construct infrastructure including roads, bridges, buildings, water systems, and transportation networks. Includes site visits, CAD training, and structural analysis projects.",
                duration="5 years",
                seats=40,
                requirements="B+ in Mathematics, Physics, and Chemistry. KCSE mean grade B+ or equivalent. Strong problem-solving skills."
            ),
            Course(
                title="Bachelor of Electrical & Electronic Engineering",
                name="Electrical Engineering",
                description="Study power systems, circuit design, telecommunications, control systems, and renewable energy. Hands-on labs and industry internships with leading engineering firms.",
                duration="5 years",
                seats=35,
                requirements="B+ in Mathematics, Physics, and Chemistry. KCSE mean grade B+ or equivalent."
            ),
            Course(
                title="Bachelor of Mechanical Engineering",
                name="Mechanical Engineering",
                description="Learn thermodynamics, fluid mechanics, machine design, manufacturing processes, and robotics. Practical workshops and industry partnerships for real-world experience.",
                duration="5 years",
                seats=35,
                requirements="B+ in Mathematics, Physics, and Chemistry. KCSE mean grade B+ or equivalent."
            ),
            Course(
                title="Bachelor of Computer Engineering",
                name="Computer Engineering",
                description="Combine hardware and software engineering. Study digital systems, embedded systems, computer architecture, networking, and IoT. Build real computing systems in labs.",
                duration="5 years",
                seats=30,
                requirements="B+ in Mathematics, Physics, and Chemistry/Computer Studies. KCSE mean grade B+ or equivalent."
            ),
            Course(
                title="Bachelor of Business Administration",
                name="Business Administration",
                description="Comprehensive business education covering management, finance, marketing, entrepreneurship, and strategic planning. Case studies and internships with top companies.",
                duration="4 years",
                seats=80,
                requirements="C+ in Mathematics and English. KCSE mean grade C+ or equivalent."
            ),
            Course(
                title="Bachelor of Economics & Statistics",
                name="Economics",
                description="Study microeconomics, macroeconomics, econometrics, financial markets, and data analysis. Prepare for careers in banking, government policy, and international organizations.",
                duration="4 years",
                seats=50,
                requirements="B in Mathematics and English. KCSE mean grade B or equivalent."
            ),
            Course(
                title="Bachelor of Education (Science)",
                name="Education - Science",
                description="Train to become a high school science teacher. Specialize in Biology, Chemistry, Physics, or Mathematics. Includes teaching practice in partner schools.",
                duration="4 years",
                seats=40,
                requirements="C+ in two teaching subjects and English. KCSE mean grade C+ or equivalent. Passion for teaching."
            ),
            Course(
                title="Bachelor of Education (Arts)",
                name="Education - Arts",
                description="Prepare to teach English, History, Geography, Kiswahili, or Religious Studies. Pedagogy training, classroom management, and extensive teaching practice.",
                duration="4 years",
                seats=40,
                requirements="C+ in two teaching subjects and English. KCSE mean grade C+ or equivalent."
            ),
            Course(
                title="Bachelor of Information Technology",
                name="Information Technology",
                description="Software development, database management, cybersecurity, cloud computing, and IT project management. Industry certifications and internship opportunities.",
                duration="4 years",
                seats=50,
                requirements="C+ in Mathematics and any science subject. KCSE mean grade C+ or equivalent."
            ),
            Course(
                title="Bachelor of Computer Science",
                name="Computer Science",
                description="Deep dive into algorithms, data structures, artificial intelligence, machine learning, and software engineering. Research projects and hackathons.",
                duration="4 years",
                seats=40,
                requirements="B in Mathematics and Physics/Computer Studies. KCSE mean grade B or equivalent."
            ),
            Course(
                title="Bachelor of Agriculture",
                name="Agriculture",
                description="Crop science, animal husbandry, agricultural economics, soil science, and sustainable farming. Field work at university farms and agricultural research centers.",
                duration="4 years",
                seats=35,
                requirements="C+ in Biology, Chemistry, and Mathematics/Agriculture. KCSE mean grade C+ or equivalent."
            ),
            Course(
                title="Bachelor of Environmental Science",
                name="Environmental Science",
                description="Climate change, conservation biology, environmental policy, pollution control, and sustainable development. Field trips to national parks and conservation areas.",
                duration="4 years",
                seats=30,
                requirements="C+ in Biology, Chemistry, and Geography/Mathematics. KCSE mean grade C+ or equivalent."
            ),
            Course(
                title="Bachelor of Architecture",
                name="Architecture",
                description="Design theory, building technology, structural systems, urban planning, and sustainable design. Studio-based learning with design projects and site visits.",
                duration="5 years",
                seats=25,
                requirements="B+ in Mathematics, Physics, and any art subject. KCSE mean grade B+ or equivalent. Portfolio submission required."
            ),
            Course(
                title="Bachelor of Quantity Surveying",
                name="Quantity Surveying",
                description="Construction cost estimation, project management, contract law, and building economics. Prepare for careers in construction management and consultancy.",
                duration="4 years",
                seats=30,
                requirements="B in Mathematics, Physics, and English. KCSE mean grade B or equivalent."
            ),
            Course(
                title="Bachelor of Journalism & Media Studies",
                name="Journalism",
                description="News reporting, broadcast journalism, digital media, investigative journalism, and media ethics. Internships with leading media houses and practical newsroom experience.",
                duration="4 years",
                seats=35,
                requirements="B in English and any humanities subject. KCSE mean grade B or equivalent. Writing portfolio encouraged."
            ),
            Course(
                title="Bachelor of International Relations",
                name="International Relations",
                description="Diplomacy, global politics, international law, conflict resolution, and development studies. Prepare for careers in foreign service, NGOs, and international organizations.",
                duration="4 years",
                seats=40,
                requirements="B in English and History/Geography. KCSE mean grade B or equivalent."
            ),
            Course(
                title="Bachelor of Psychology",
                name="Psychology",
                description="Clinical psychology, counseling, developmental psychology, research methods, and mental health. Practicum in hospitals and counseling centers.",
                duration="4 years",
                seats=35,
                requirements="B in Biology and English. KCSE mean grade B or equivalent. Empathy and interpersonal skills."
            ),
            Course(
                title="Bachelor of Social Work",
                name="Social Work",
                description="Community development, child welfare, social policy, counseling, and case management. Field placements in social service agencies and community organizations.",
                duration="4 years",
                seats=30,
                requirements="C+ in English and any humanities subject. KCSE mean grade C+ or equivalent. Passion for helping communities."
            ),
        ]
        
        for course in courses:
            db.add(course)
        
        school_info = db.query(SchoolInfo).first()
        if not school_info:
            school_info = SchoolInfo(
                about="Sunshine School is a premier university in Nairobi offering world-class education in medicine, engineering, law, business, and the sciences. Established in 2010, we have produced over 5,000 graduates who are leaders in healthcare, technology, governance, and industry across Africa and beyond. Our state-of-the-art facilities, renowned faculty, and strong industry partnerships ensure our students receive practical, career-ready education.",
                mission="To cultivate academic excellence, innovation, and ethical leadership through transformative education that empowers students to solve real-world challenges and advance societal progress.",
                achievements="Top 10 University in East Africa 2024, 95% Graduate Employment Rate, 50+ International Research Partnerships, 200+ Full-time PhD Faculty, 5,000+ Alumni Worldwide",
                address="123 University Way, Nairobi, Kenya",
                phone="+254 700 000 000",
                email="admissions@sunshineschool.ac.ke"
            )
            db.add(school_info)
        
        admin = db.query(User).filter(User.email == "admin@sunshineschool.ac.ke").first()
        if not admin:
            admin = User(
                email="admin@sunshineschool.ac.ke",
                hashed_password=get_password_hash("admin123"),
                full_name="System Administrator",
                is_admin=True
            )
            db.add(admin)
            print("Created admin user: admin@sunshineschool.ac.ke / admin123")
        
        db.commit()
        print(f"Successfully seeded {len(courses)} courses!")
        print("School info created.")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()