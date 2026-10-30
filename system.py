"""
Job In India
AI Job Matching & Recommendation System

Algorithm:
    TF-IDF Vectorization + Cosine Similarity

Input:
    Candidate profile + list of jobs

Output:
    Ranked jobs with match percentage and explanation
"""

from __future__ import annotations

import re
from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# TEXT UTILITIES
# ============================================================

def clean_text(text: str) -> str:
    """
    Clean text before sending it to the ML model.
    """
    if not text:
        return ""

    text = str(text).lower()

    # Remove special characters
    text = re.sub(r"[^a-z0-9+#.\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def normalize_skills(skills: Any) -> list[str]:
    """
    Convert different skill formats into a clean list.

    Supports:
        "Python, Java, SQL"
        ["Python", "Java", "SQL"]
    """

    if skills is None:
        return []

    if isinstance(skills, list):
        values = skills
    else:
        values = re.split(r"[,;|]", str(skills))

    result = []

    for skill in values:
        skill = clean_text(skill)

        if skill:
            result.append(skill)

    return list(dict.fromkeys(result))


# ============================================================
# CANDIDATE PROFILE
# ============================================================

def build_candidate_text(candidate: dict) -> str:
    """
    Convert candidate information into one ML text document.
    """

    name = candidate.get("name", "")
    education = candidate.get("education", "")
    experience = candidate.get("experience", "")
    skills = normalize_skills(candidate.get("skills", []))
    interests = candidate.get("interests", "")

    text = f"""
    {name}
    {education}
    {experience}
    {' '.join(skills)}
    {interests}
    """

    return clean_text(text)


# ============================================================
# JOB DOCUMENT
# ============================================================

def build_job_text(job: dict) -> str:
    """
    Convert a job into one ML document.
    """

    title = job.get("title", "")
    company = job.get("company", "")
    location = job.get("location", "")
    description = job.get("description", "")
    skills = normalize_skills(job.get("skills", []))

    text = f"""
    {title}
    {company}
    {location}
    {description}
    {' '.join(skills)}
    """

    return clean_text(text)


# ============================================================
# SKILL MATCHING
# ============================================================

def calculate_skill_match(
    candidate_skills: list[str],
    job_skills: list[str]
) -> tuple[float, list[str], list[str]]:
    """
    Calculate explicit skill overlap.

    Returns:
        skill_match_percentage
        matched_skills
        missing_skills
    """

    candidate_set = {
        clean_text(skill)
        for skill in candidate_skills
        if clean_text(skill)
    }

    job_set = {
        clean_text(skill)
        for skill in job_skills
        if clean_text(skill)
    }

    if not job_set:
        return 0.0, [], []

    matched = sorted(candidate_set.intersection(job_set))
    missing = sorted(job_set - candidate_set)

    percentage = (len(matched) / len(job_set)) * 100

    return round(percentage, 2), matched, missing


# ============================================================
# MATCH SCORE
# ============================================================

def calculate_match_score(
    cosine_score: float,
    skill_score: float
) -> float:
    """
    Final score.

    Weight:
        60% semantic similarity
        40% explicit skill match
    """

    final_score = (
        (cosine_score * 100) * 0.60
        + skill_score * 0.40
    )

    return round(min(final_score, 100), 2)


# ============================================================
# EXPLANATION
# ============================================================

def generate_reason(
    score: float,
    matched_skills: list[str],
    missing_skills: list[str]
) -> str:

    if score >= 80:
        level = "Excellent match"
    elif score >= 65:
        level = "Strong match"
    elif score >= 50:
        level = "Moderate match"
    else:
        level = "Low match"

    if matched_skills:
        matched_text = ", ".join(matched_skills[:5])
        reason = f"{level}. Matching skills: {matched_text}."
    else:
        reason = f"{level}. Limited direct skill overlap."

    if missing_skills:
        missing_text = ", ".join(missing_skills[:4])
        reason += f" Skills to improve: {missing_text}."

    return reason


# ============================================================
# JOB RECOMMENDATION ENGINE
# ============================================================

def recommend_jobs(
    candidate: dict,
    jobs: list[dict],
    top_n: int = 10
) -> list[dict]:

    if not jobs:
        return []

    candidate_text = build_candidate_text(candidate)

    if not candidate_text:
        return []

    job_texts = [
        build_job_text(job)
        for job in jobs
    ]

    documents = [candidate_text] + job_texts

    # --------------------------------------------------------
    # TF-IDF
    # --------------------------------------------------------

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),
        max_features=5000
    )

    matrix = vectorizer.fit_transform(documents)

    candidate_vector = matrix[0]
    job_vectors = matrix[1:]

    similarities = cosine_similarity(
        candidate_vector,
        job_vectors
    )[0]

    candidate_skills = normalize_skills(
        candidate.get("skills", [])
    )

    recommendations = []

    for index, job in enumerate(jobs):

        job_skills = normalize_skills(
            job.get("skills", [])
        )

        skill_score, matched_skills, missing_skills = (
            calculate_skill_match(
                candidate_skills,
                job_skills
            )
        )

        cosine_score = float(similarities[index])

        final_score = calculate_match_score(
            cosine_score,
            skill_score
        )

        result = dict(job)

        result["match_score"] = final_score
        result["semantic_similarity"] = round(
            cosine_score * 100,
            2
        )
        result["skill_match"] = skill_score
        result["matched_skills"] = matched_skills
        result["missing_skills"] = missing_skills

        result["reason"] = generate_reason(
            final_score,
            matched_skills,
            missing_skills
        )

        recommendations.append(result)

    # Highest score first
    recommendations.sort(
        key=lambda x: x["match_score"],
        reverse=True
    )

    return recommendations[:top_n]


# ============================================================
# SAMPLE DATA
# ============================================================

if __name__ == "__main__":

    candidate = {
        "name": "Harshit Tripathi",

        "education": (
            "B.Tech Computer Science "
            "Artificial Intelligence and Machine Learning"
        ),

        "experience": (
            "Student developer working on web development "
            "and machine learning projects"
        ),

        "skills": [
            "Python",
            "Machine Learning",
            "Artificial Intelligence",
            "Pandas",
            "NumPy",
            "Scikit Learn",
            "PHP",
            "MySQL",
            "JavaScript",
            "React",
            "Node.js"
        ],

        "interests": (
            "AI ML software development web development "
            "data science"
        )
    }

    jobs = [

        {
            "id": 1,
            "title": "Machine Learning Intern",

            "company": "TechVision India",

            "location": "Bangalore",

            "skills": [
                "Python",
                "Machine Learning",
                "Pandas",
                "NumPy",
                "Scikit Learn"
            ],

            "description": """
                Work on machine learning models,
                data preprocessing, model evaluation,
                Python development and AI projects.
            """
        },

        {
            "id": 2,
            "title": "PHP Backend Developer",

            "company": "Digital Solutions",

            "location": "Remote",

            "skills": [
                "PHP",
                "MySQL",
                "JavaScript",
                "REST API"
            ],

            "description": """
                Develop backend applications using PHP
                and MySQL. Build APIs and database-driven
                web applications.
            """
        },

        {
            "id": 3,
            "title": "Frontend React Developer",

            "company": "Startup Labs",

            "location": "Pune",

            "skills": [
                "React",
                "JavaScript",
                "HTML",
                "CSS"
            ],

            "description": """
                Build modern responsive web applications
                using React and JavaScript.
            """
        },

        {
            "id": 4,
            "title": "Data Analyst Intern",

            "company": "Analytics India",

            "location": "Hyderabad",

            "skills": [
                "Python",
                "Pandas",
                "NumPy",
                "SQL",
                "Data Analysis"
            ],

            "description": """
                Analyze datasets using Python, Pandas
                and SQL. Create reports and derive
                business insights from data.
            """
        },

        {
            "id": 5,
            "title": "Java Developer",

            "company": "Enterprise Systems",

            "location": "Delhi",

            "skills": [
                "Java",
                "Spring Boot",
                "SQL",
                "REST API"
            ],

            "description": """
                Develop enterprise backend applications
                using Java and Spring Boot.
            """
        }
    ]

    print("\n")
    print("=" * 70)
    print("       JOB IN INDIA - AI JOB RECOMMENDATION SYSTEM")
    print("=" * 70)

    recommendations = recommend_jobs(
        candidate,
        jobs,
        top_n=5
    )

    print()

    for rank, job in enumerate(recommendations, start=1):

        print("-" * 70)

        print(f"#{rank}  {job['title']}")
        print(f"Company      : {job['company']}")
        print(f"Location     : {job['location']}")
        print(f"Match Score  : {job['match_score']}%")
        print(
            f"Skill Match  : {job['skill_match']}%"
        )
        print(
            f"Semantic     : {job['semantic_similarity']}%"
        )

        print(
            "Matched      : "
            + (
                ", ".join(job["matched_skills"])
                if job["matched_skills"]
                else "None"
            )
        )

        print(
            "Missing      : "
            + (
                ", ".join(job["missing_skills"])
                if job["missing_skills"]
                else "None"
            )
        )

        print(f"Why          : {job['reason']}")

    print("-" * 70)
    print() 