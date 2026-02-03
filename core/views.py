from django.shortcuts import render


def home(request):
    context = {
        'name': 'Anesh Meghwar',
        'role': 'Python Developer & Instructor',
        'summary': 'Recent BSCS Graduate and Data Science Intern at 10Pearls. Experienced in building web applications with Django and mentoring aspiring developers. Passionate about solving real-world problems using AI and modern web technologies.',

        'social_links': {
            'linkedin': 'https://www.linkedin.com/in/anesh-meghwar/',
            'email': 'mailto:aneshrathorel@gmail.com',
            'phone': 'tel:+923431135155',
            # Add your GitHub if you have one, or keep it empty
            'github': '#'
        },

        # --- 1. QUALIFICATION (EDUCATION) ---
        'education': [
            {
                'degree': 'Bachelor of Science in Computer Science (BSCS)',
                'school': 'University of Sindh, Jamshoro',
                'year': 'Graduated Dec 2025',
                'desc': 'Core Coursework: Data Structures, Artificial Intelligence, Machine Learning, Software Engineering, and OOP.'
            },
            {
                'degree': 'Diploma of Associate Engineering (DAE) - Mechanical',
                'school': 'GPI Mithi',
                'year': '2019 - 2022',
                'desc': 'Award: Completed via Engro / Thar Foundation Scholarship.'
            }
        ],

        # --- 2. EXPERIENCE ---
        'experience': [
            {
                'role': 'Data Science Intern',
                'company': '10Pearls',
                'year': 'Dec 2025 - Present',
                'desc': 'Applying modern data science techniques and clean coding standards. Bridging the gap between complex technical concepts and practical solutions.'
            },
            {
                'role': 'Python Developer & Instructor',
                'company': 'Thar Institute of Technology',
                'year': 'Jan 2026 - Present',
                'desc': 'Instructing students on Python fundamentals (OOP, Loops). Developing curriculum for web development modules and mentoring aspiring developers.'
            },
            {
                'role': 'Capstone Project Coordinator',
                'company': 'IMCS Jamshoro',
                'year': '2025',
                'desc': 'Facilitated communication between academic teams and industry partners to align project goals.'
            }
        ],

        # --- 3. PROJECTS ---
        'projects': [
            {
                'name': 'Plant Disease Detection (LeafDoctor AI)',
                'tech': 'Python, TensorFlow, CNN, Flutter',
                'year': 'Mar 2025',
                'desc': 'Cross-platform mobile app to detect crop diseases with high accuracy using MobileNetV3 Small.'
            },
            {
                'name': 'WhatsApp Clone',
                'tech': 'Flutter, Dart',
                'year': '2024',
                'desc': 'Built a functional messaging UI with real-time navigation and state management.'
            },
            {
                'name': 'E-commerce Web Application',
                'tech': 'Django, SQLite, Bootstrap, HTML/CSS',
                'year': '2024',
                'desc': 'A full-stack web application featuring product management and dynamic content.'
            }
        ],

        # --- 4. CERTIFICATIONS ---
        'certifications': [
            'Machine Learning - Stanford Online (Coursera)',
            'TensorFlow for AI, ML, and Deep Learning - DeepLearning.AI',
            'AI for Everyone - Andrew Ng',
            'Mobile App Development with Flutter',
            'Python for Data Science',
            'Django for Beginners'
        ],

        # --- 5. SKILLS ---
        'skills': [
            'Python', 'Django', 'TensorFlow', 'Keras', 'CNN',
            'Flutter', 'Dart', 'OOP', 'Data Structures', 'Git/GitHub'
        ]
    }
    return render(request, 'core/home.html', context)