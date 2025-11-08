from app.agents.candidate_evaluation_agent import evaluate_candidate

candidate = '{"name": "John Doe", "email": "john@example.com", "phone": "123-456-7890", "education": "BSc Computer Science", "work_experience": 5, "skills": ["Java", "Spring Boot", "Microservices"], "certifications": ["None"]}'
jd = '{"min_work_experience": 5, "max_work_experience": 8, "skills": ["Java", "Spring Boot", "Microservices", "CI/CD", "Kubernetes", "Docker", "Jenkins", "GitLab CI", "GitHub Actions", "AWS", "GCP", "Azure", "Git", "RESTful APIs"]}'

result = evaluate_candidate(candidate, jd)
print('Evaluation Result:', result)
