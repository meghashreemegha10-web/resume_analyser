import re
from typing import List, Dict
from pydantic import BaseModel

try:
    import spacy
except ImportError:
    spacy = None

# Mock database of market needs - In a real app this would come from an API or DB
MARKET_NEEDS = {
    "python": 10, "java": 8, "react": 9, "aws": 9, "docker": 8,
    "kubernetes": 9, "communication": 7, "leadership": 8, "sql": 8,
    "fastapi": 9, "machine learning": 10, "nlp": 10, "ai": 10,
    "project management": 7, "agile": 7, "scrum": 6,
    "mongodb": 8, "cache": 7
}

CATEGORIES = {
    "technical": ["python", "java", "react", "aws", "docker", "kubernetes", "sql", "fastapi", "machine learning", "nlp", "ai", "mongodb", "cache"],
    "soft": ["communication", "leadership"],
    "methodology": ["project management", "agile", "scrum"]
}

SECTION_KEYWORDS = {
    "experience": ["experience", "employment", "work history", "professional history", "work experience", "professional experience"],
    "education": ["education", "academic", "academics", "educational background", "qualification", "qualifications"],
    "skills": ["skills", "technical skills", "skills & expertise", "core competencies", "technologies"],
    "projects": ["projects", "personal projects", "academic projects", "key projects", "portfolio"]
}

ACTION_VERBS = {
    "led", "managed", "developed", "built", "designed", "created", "optimized",
    "improved", "implemented", "delivered", "coordinated", "analyzed", "architected",
    "spearheaded", "accelerated", "engineered", "established", "formulated",
    "generated", "initiated", "launched", "maximized", "reduced", "upgraded"
}

class AnalysisResult(BaseModel):
    score: int
    found_skills: List[str]
    missing_critical_skills: List[str]
    summary: str
    skills_score: int
    structure_score: int
    experience_score: int
    readability_score: int
    sections_found: List[str]
    sections_missing: List[str]
    action_verb_count: int
    estimated_years: int
    feedback_notes: List[str]

class ResumeAnalyzer:
    def __init__(self):
        self.nlp = None
        if spacy:
            try:
                self.nlp = spacy.load("en_core_web_sm")
            except Exception as e:
                print(f"Warning: spacy model not found or error loading: {e}. Fallback to blank model.")
                try:
                    self.nlp = spacy.blank("en")
                except:
                    self.nlp = None
        else:
            print("Warning: spacy not installed. Using simple regex matching.")

    def analyze(self, text: str) -> AnalysisResult:
        text_lower = text.lower()
        found_skills = []
        
        # 1. Skill Extraction
        for skill in MARKET_NEEDS.keys():
            if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
                found_skills.append(skill)
        
        found_by_cat = {cat: [] for cat in CATEGORIES}
        for skill in found_skills:
            for cat, list_skills in CATEGORIES.items():
                if skill in list_skills:
                    found_by_cat[cat].append(skill)
        
        tech_pts = min(25, len(found_by_cat["technical"]) * 5)
        soft_pts = min(8, len(found_by_cat["soft"]) * 4)
        method_pts = min(7, len(found_by_cat["methodology"]) * 4)
        skills_score = tech_pts + soft_pts + method_pts

        # 2. Section Detection
        sections_found = []
        for section, kw_list in SECTION_KEYWORDS.items():
            pattern = r'(?m)^\s*(?:' + '|'.join(re.escape(kw) for kw in kw_list) + r')\s*$'
            if re.search(pattern, text_lower, re.IGNORECASE | re.MULTILINE):
                sections_found.append(section)
        
        sections_missing = [s for s in SECTION_KEYWORDS.keys() if s not in sections_found]
        structure_score = len(sections_found) * 5

        # 3. Action Verbs Count
        action_verb_occurrences = 0
        for verb in ACTION_VERBS:
            action_verb_occurrences += len(re.findall(r'\b' + re.escape(verb) + r'\b', text_lower))
        
        # 4. Experience Years Estimation
        import datetime
        current_year = datetime.datetime.now().year
        range_pattern = r'\b(19[89]\d|20[0-2]\d)\s*(?:\-|–|—|to)\s*(Present|Current|19[89]\d|20[0-2]\d)\b'
        ranges = re.findall(range_pattern, text, re.IGNORECASE)

        parsed_ranges = []
        for start_year, end_val in ranges:
            start = int(start_year)
            if end_val.lower() in ["present", "current"]:
                end = current_year
            else:
                try:
                    end = int(end_val)
                except ValueError:
                    end = start
            if end >= start:
                parsed_ranges.append((start, end))
        
        estimated_years = 0
        if parsed_ranges:
            parsed_ranges.sort(key=lambda x: x[0])
            merged = [parsed_ranges[0]]
            for current in parsed_ranges[1:]:
                prev = merged[-1]
                if current[0] <= prev[1]:
                    merged[-1] = (prev[0], max(prev[1], current[1]))
                else:
                    merged.append(current)
            estimated_years = sum(end - start for start, end in merged)
            if estimated_years == 0 and len(parsed_ranges) > 0:
                estimated_years = len(merged)

        # Parse direct year mentions (e.g. "5 years of experience")
        exp_mention = re.search(r'\b(\d+)\s*(?:\+\s*)?years?\b(?:\s+of\s+experience)?', text_lower)
        if exp_mention:
            mentioned_years = int(exp_mention.group(1))
            estimated_years = max(estimated_years, mentioned_years)

        exp_pts = 0
        if estimated_years >= 6:
            exp_pts = 15
        elif estimated_years >= 3:
            exp_pts = 10
        elif estimated_years >= 1:
            exp_pts = 5
            
        verb_pts = 0
        if action_verb_occurrences >= 8:
            verb_pts = 10
        elif action_verb_occurrences >= 4:
            verb_pts = 8
        elif action_verb_occurrences >= 1:
            verb_pts = 5
            
        experience_score = exp_pts + verb_pts

        # 5. Readability & Formatting
        words = text_lower.split()
        word_count = len(words)
        
        has_contact = 0
        if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text):
            has_contact += 3
        if re.search(r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b', text):
            has_contact += 2

        readability_score = 0
        if 300 <= word_count <= 1000:
            readability_score += 10
        elif 150 <= word_count <= 1500:
            readability_score += 6
        else:
            readability_score += 2
            
        readability_score += has_contact

        # Total Calculation
        score = skills_score + structure_score + experience_score + readability_score
        score = min(100, max(10, score))

        # Generate Feedback Notes
        feedback_notes = []
        if sections_missing:
            feedback_notes.append(f"Missing essential resume sections: {', '.join(sections_missing).title()}.")
        if action_verb_occurrences < 4:
            feedback_notes.append("Your resume has low action verb density. Describe accomplishments using verbs like 'led', 'developed', or 'optimized'.")
        if estimated_years == 0:
            feedback_notes.append("No professional timeline could be parsed. List dates (e.g. '2021 - 2024') for previous work or projects.")
        if word_count < 250:
            feedback_notes.append("The resume is very brief. Expand on your projects, work roles, and achievements.")
        elif word_count > 1200:
            feedback_notes.append("The resume is quite long. Consider condensing it to be more concise and scannable.")
        if has_contact < 5:
            feedback_notes.append("Ensure your email and phone number are clearly visible in the contact section.")
        if len(found_by_cat["technical"]) < 3:
            feedback_notes.append("Consider adding more high-demand technical skills matching your field (e.g. Python, AWS, Docker).")
        if not found_by_cat["soft"] or not found_by_cat["methodology"]:
            feedback_notes.append("Include methodology or soft skills (e.g. Agile, Scrum, Communication) to show balanced professional capability.")

        # Suggest specific project recommendations based on detected skill gaps
        missing_skills = [
            s for s, w in sorted(MARKET_NEEDS.items(), key=lambda x: x[1], reverse=True)
            if s not in found_skills
        ][:5]

        PROJECT_RECOMMENDATIONS_DB = {
            "python": "Build a command-line tool or a web scraper using BeautifulSoup to fetch and clean job post details.",
            "java": "Develop a multi-threaded client-server chat application or a school management API with Spring Boot.",
            "react": "Build a responsive SaaS layout dashboard using modern React components and mock data metrics.",
            "aws": "Create a serverless pipeline that resizes images dynamically using AWS Lambda triggers and S3 buckets.",
            "docker": "Dockerize a Python/FastAPI backend application and hook it up to a PostgreSQL database container using Docker Compose.",
            "kubernetes": "Configure a local microservices application and deploy it to Kubernetes (Minikube) using Ingress resource routing.",
            "sql": "Design a relational database schema for an e-commerce database and write complex subqueries to aggregate sales reporting data.",
            "fastapi": "Create a RESTful API complete with JWT cookie-based session login authentication and automated API docs.",
            "machine learning": "Build a housing market price predictor model using Scikit-Learn regression or a customer segment group cluster.",
            "nlp": "Build a resume parser tool or sentiment classifier model on user reviews using spaCy or HuggingFace pipelines.",
            "ai": "Develop a game-playing agent using Minimax/reinforcement learning or a pipeline using generative LLM text completion.",
            "project management": "Draft an interactive project Gantt chart layout tracking dependencies, resources, and critical path milestones.",
            "agile": "Construct a Kanban board interface tracking ticket cycles (To Do, In Progress, In Review, Done).",
            "scrum": "Simulate and track team metrics like sprint velocity and burndown progress statistics in a structured table format.",
            "mongodb": "Build a document-based data repository API showcasing nested arrays, aggregation queries, and dynamic schemas.",
            "cache": "Implement an in-memory caching middleware layer using Redis/Memcached to cache database response payloads."
        }

        recommended_projects = []
        for ms in missing_skills:
            if ms in PROJECT_RECOMMENDATIONS_DB:
                recommended_projects.append(f"To bridge the gap in '{ms.upper()}', consider building: {PROJECT_RECOMMENDATIONS_DB[ms]}")

        if recommended_projects:
            feedback_notes.append("💡 Project Suggestions to improve your match score:\n" + "\n".join(f"- {proj}" for proj in recommended_projects[:3]))

        summary = f"Detected {len(found_skills)} market skills. "
        if score >= 80:
            summary += "Excellent profile with strong structural completeness and skill alignment."
        elif score >= 50:
            summary += "Good profile. Address the missing sections and expand on key skills to improve match rating."
        else:
            summary += "Low match rating. Review formatting, add structural headers, and integrate high-impact skills."

        return AnalysisResult(
            score=score,
            found_skills=found_skills,
            missing_critical_skills=missing_skills,
            summary=summary,
            skills_score=skills_score,
            structure_score=structure_score,
            experience_score=experience_score,
            readability_score=readability_score,
            sections_found=sections_found,
            sections_missing=sections_missing,
            action_verb_count=action_verb_occurrences,
            estimated_years=estimated_years,
            feedback_notes=feedback_notes
        )
