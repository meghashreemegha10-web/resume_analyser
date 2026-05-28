const SKILL_INFO = {
  "python": {
    title: "Python",
    icon: "🐍",
    demand: "Very High",
    demandColor: "#10b981",
    description: "Python is the world's most popular programming language for data science, machine learning, automation, and backend development. It has a rich ecosystem of libraries like NumPy, Pandas, TensorFlow, and FastAPI.",
    why_matters: "Python is required in 70%+ of AI/ML and data engineering job postings. It's the gateway to machine learning, data analysis, and modern backend APIs.",
    projects: "AI Voice Assistant, Automatic File Organizer, Web Scraper for Jobs",
    resources: [
      { label: "Official Python Docs", url: "https://docs.python.org/3/" },
      { label: "Real Python Tutorials", url: "https://realpython.com" },
      { label: "Python on freeCodeCamp", url: "https://www.freecodecamp.org/learn/scientific-computing-with-python/" }
    ]
  },
  "java": {
    title: "Java",
    icon: "☕",
    demand: "High",
    demandColor: "#f59e0b",
    description: "Java is a widely used enterprise language known for its stability, performance, and cross-platform capabilities. It powers large-scale backend systems, Android apps, and enterprise applications.",
    why_matters: "Java is a staple in enterprise software, banking systems, and Android development. Strong Java skills are valued in large corporations and financial institutions.",
    projects: "School Management System, Android Fitness Tracker, Multi-threaded Chat Application",
    resources: [
      { label: "Oracle Java Docs", url: "https://docs.oracle.com/en/java/" },
      { label: "Java on Codecademy", url: "https://www.codecademy.com/learn/learn-java" }
    ]
  },
  "react": {
    title: "React",
    icon: "⚛️",
    demand: "Very High",
    demandColor: "#10b981",
    description: "React is a JavaScript library by Meta for building fast, interactive user interfaces. It uses a component-based architecture and virtual DOM for optimal rendering performance.",
    why_matters: "React dominates frontend development. Most modern web applications are built with React or React-based frameworks like Next.js.",
    projects: "SaaS Dashboard UI, E-commerce Storefront, Real-time Collaborative Task Board",
    resources: [
      { label: "React Official Docs", url: "https://react.dev" },
      { label: "The Odin Project (React)", url: "https://www.theodinproject.com/paths/full-stack-javascript/courses/react" }
    ]
  },
  "aws": {
    title: "Amazon Web Services (AWS)",
    icon: "☁️",
    demand: "Very High",
    demandColor: "#10b981",
    description: "AWS is the world's leading cloud platform offering 200+ services including compute (EC2), storage (S3), AI/ML services, and serverless functions (Lambda).",
    why_matters: "Cloud experience, especially AWS, is now expected in most senior engineering roles. AWS certification significantly boosts career prospects.",
    projects: "Serverless Image Resizer (S3 + Lambda), CI/CD Pipeline on AWS, Auto-Scaling Web App",
    resources: [
      { label: "AWS Training & Certification", url: "https://aws.amazon.com/training/" },
      { label: "AWS on freeCodeCamp (YouTube)", url: "https://www.youtube.com/watch?v=ulprqHHWlng" }
    ]
  },
  "docker": {
    title: "Docker",
    icon: "🐳",
    demand: "High",
    demandColor: "#f59e0b",
    description: "Docker is a containerization platform that packages applications and their dependencies into portable containers. It ensures consistent environments from development to production.",
    why_matters: "Docker is a fundamental DevOps skill. Without containerization knowledge, deploying modern microservices and cloud-native applications is nearly impossible.",
    projects: "Multi-container Flask + PostgreSQL Stack, Dockerized CI/CD workflow, Microservice Cluster local setup",
    resources: [
      { label: "Docker Official Docs", url: "https://docs.docker.com" },
      { label: "Docker Tutorial for Beginners (YouTube)", url: "https://www.youtube.com/watch?v=3c-iBn73dDE" }
    ]
  },
  "kubernetes": {
    title: "Kubernetes",
    icon: "🚢",
    demand: "Very High",
    demandColor: "#10b981",
    description: "Kubernetes (K8s) is an open-source container orchestration system that automates deployment, scaling, and management of containerized applications.",
    why_matters: "Kubernetes is the industry standard for managing containerized workloads at scale. It's essential for DevOps, SRE, and cloud engineering roles.",
    projects: "Self-Healing App Deployment with Ingress Controller, Local K8s Cluster via Minikube, GitOps Pipeline with ArgoCD",
    resources: [
      { label: "Kubernetes Official Docs", url: "https://kubernetes.io/docs/home/" },
      { label: "Kubernetes on freeCodeCamp", url: "https://www.freecodecamp.org/news/the-kubernetes-handbook/" }
    ]
  },
  "sql": {
    title: "SQL",
    icon: "🗄️",
    demand: "High",
    demandColor: "#f59e0b",
    description: "SQL (Structured Query Language) is the universal language for querying and manipulating relational databases. It is used to extract, filter, aggregate, and transform data.",
    why_matters: "SQL is required in almost every data-related role — data analyst, data engineer, backend developer, and business intelligence. It's a foundational skill.",
    projects: "Database Schema Design for Library, Complex Sales Queries Report Dashboard, SQL Data Analytics Project",
    resources: [
      { label: "SQLZoo Interactive Tutorials", url: "https://sqlzoo.net" },
      { label: "Mode SQL Tutorial", url: "https://mode.com/sql-tutorial/" }
    ]
  },
  "fastapi": {
    title: "FastAPI",
    icon: "⚡",
    demand: "Very High",
    demandColor: "#10b981",
    description: "FastAPI is a modern, high-performance Python web framework for building APIs. It is based on standard Python type hints and is one of the fastest Python frameworks available.",
    why_matters: "FastAPI is rapidly becoming the preferred framework for building ML-powered APIs and microservices in Python. It's production-ready and developer-friendly.",
    projects: "Secure User Auth Backend REST API, Real-time Chat API (Websockets), Machine Learning Model Hosting Endpoint",
    resources: [
      { label: "FastAPI Official Docs", url: "https://fastapi.tiangolo.com" },
      { label: "FastAPI Tutorial (YouTube)", url: "https://www.youtube.com/watch?v=0sOvCWFmrtA" }
    ]
  },
  "machine learning": {
    title: "Machine Learning",
    icon: "🤖",
    demand: "Extremely High",
    demandColor: "#6366f1",
    description: "Machine Learning is a branch of AI that enables systems to learn and improve from experience. It includes supervised/unsupervised learning, neural networks, and model training pipelines.",
    why_matters: "ML is among the highest-paying and fastest-growing fields in tech. Companies across every industry are investing heavily in ML talent.",
    projects: "House Price Predictor (Regression), Customer Segmentation (K-Means Clustering), Image Classifier (CNN)",
    resources: [
      { label: "Google ML Crash Course", url: "https://developers.google.com/machine-learning/crash-course" },
      { label: "fast.ai Practical Deep Learning", url: "https://www.fast.ai" }
    ]
  },
  "nlp": {
    title: "Natural Language Processing (NLP)",
    icon: "🗣️",
    demand: "Extremely High",
    demandColor: "#6366f1",
    description: "NLP is the subfield of AI focused on enabling computers to understand, interpret, and generate human language. It powers chatbots, sentiment analysis, translation, and resume parsers like this one.",
    why_matters: "With the rise of LLMs and generative AI, NLP expertise is among the most sought-after skills in the AI industry right now.",
    projects: "PDF Resume Parser, Fine-tuned Sentiment Classifier on Tweets, Intent Recognition Chatbot",
    resources: [
      { label: "HuggingFace NLP Course", url: "https://huggingface.co/learn/nlp-course" },
      { label: "spaCy 101", url: "https://spacy.io/usage/spacy-101" }
    ]
  },
  "ai": {
    title: "Artificial Intelligence",
    icon: "🧠",
    demand: "Extremely High",
    demandColor: "#6366f1",
    description: "AI is the broad field of computer science focused on building systems that simulate human intelligence. It encompasses ML, NLP, computer vision, robotics, and generative AI.",
    why_matters: "AI is reshaping every industry. Having AI knowledge — even at a conceptual level — differentiates candidates significantly in today's job market.",
    projects: "Chess playing AI Agent, Generative AI Text summarizer, Autonomous Line Follower Robot",
    resources: [
      { label: "Elements of AI (Free Course)", url: "https://www.elementsofai.com" },
      { label: "Stanford AI Course (CS221)", url: "https://ai.stanford.edu/courses/" }
    ]
  },
  "communication": {
    title: "Communication",
    icon: "💬",
    demand: "High",
    demandColor: "#f59e0b",
    description: "Effective communication encompasses written, verbal, and presentation skills. It includes the ability to convey technical concepts to non-technical stakeholders clearly and concisely.",
    why_matters: "Technical skills get you hired; communication skills get you promoted. Hiring managers rate communication as one of the top soft skills they look for.",
    projects: "Technical Documentation Wiki, Interactive Product Pitch Presentation, Tech Blog / Tutorial Series writer",
    resources: [
      { label: "Coursera: Communication Skills", url: "https://www.coursera.org/learn/wharton-communication-skills" },
      { label: "Toastmasters International", url: "https://www.toastmasters.org" }
    ]
  },
  "leadership": {
    title: "Leadership",
    icon: "🏆",
    demand: "High",
    demandColor: "#f59e0b",
    description: "Leadership involves guiding teams, making decisions, managing projects, mentoring others, and driving initiatives to completion. It is demonstrated through results and people management.",
    why_matters: "Leadership skills are essential for senior roles, tech leads, and management tracks. Even individual contributors are expected to show leadership on projects.",
    projects: "Open Source Project Maintainer, Hackathon Team Lead, Student Club Founder & Leader",
    resources: [
      { label: "Harvard Leadership Principles", url: "https://online.hbs.edu/courses/leadership-principles/" },
      { label: "Manager's Handbook (Notion)", url: "https://themanagershandbook.com" }
    ]
  },
  "project management": {
    title: "Project Management",
    icon: "📋",
    demand: "Medium-High",
    demandColor: "#f59e0b",
    description: "Project management involves planning, executing, and closing projects on time and within budget. It includes scope management, risk assessment, stakeholder communication, and resource allocation.",
    why_matters: "Organizations need people who can own deliverables end-to-end. PMP certification or demonstrated PM experience adds significant value to any engineering profile.",
    projects: "Agile Sprint Planner Web Application, Kanban board tool Integration, Risk Assessment Audit Report",
    resources: [
      { label: "PMI Project Management Basics", url: "https://www.pmi.org/learning/training-development/online-courses" },
      { label: "Google PM Certificate", url: "https://grow.google/certificates/project-management/" }
    ]
  },
  "agile": {
    title: "Agile Methodology",
    icon: "🔄",
    demand: "Medium-High",
    demandColor: "#f59e0b",
    description: "Agile is an iterative software development methodology that emphasizes collaboration, flexibility, and delivering working software in short cycles called sprints.",
    why_matters: "Agile is the standard way software teams operate. Understanding Agile ceremonies (standups, retrospectives, sprint planning) is expected in most tech roles.",
    projects: "Jira-like Task Management System, Sprint Burndown Chart Calculator, Agile Team Retrospective board",
    resources: [
      { label: "Agile Manifesto", url: "https://agilemanifesto.org" },
      { label: "Atlassian Agile Guide", url: "https://www.atlassian.com/agile" }
    ]
  },
  "scrum": {
    title: "Scrum",
    icon: "🏉",
    demand: "Medium",
    demandColor: "#64748b",
    description: "Scrum is a specific Agile framework that organizes work into fixed-length sprints (usually 2 weeks), with defined roles (Scrum Master, Product Owner, Dev Team) and ceremonies.",
    why_matters: "Most software teams use Scrum as their delivery framework. Knowing Scrum roles, artifacts, and ceremonies makes you immediately productive on any team.",
    projects: "Planning Poker Tool for estimation, Scrum Velocity Tracker, Scrum Board web interface",
    resources: [
      { label: "Scrum Guide (Official)", url: "https://scrumguides.org" },
      { label: "Scrum.org Learning Path", url: "https://www.scrum.org/pathway/scrum-master/" }
    ]
  },
  "mongodb": {
    title: "MongoDB",
    icon: "🍃",
    demand: "High",
    demandColor: "#f59e0b",
    description: "MongoDB is a leading document-oriented NoSQL database that stores data in flexible JSON-like documents. It is built for scaling, high availability, and handling unstructured data easily.",
    why_matters: "MongoDB is a key part of the popular MERN/MEAN stack. Knowing NoSQL is crucial when building modern web apps that require flexible, dynamic schemas and high performance.",
    projects: "Product Catalog Management API, Real-Time Analytics Dashboard, Social Media Post Repository",
    resources: [
      { label: "MongoDB University (Free Courses)", url: "https://learn.mongodb.com" },
      { label: "MongoDB Official Docs", url: "https://www.mongodb.com/docs/" }
    ]
  },
  "cache": {
    title: "Caching (Redis / Memcached)",
    icon: "⚡",
    demand: "High",
    demandColor: "#f59e0b",
    description: "Caching is the process of storing copies of data in a high-speed data storage layer (like Redis or Memcached) to serve future requests faster instead of querying slower database backends.",
    why_matters: "Caching is vital for optimizing application speed and reducing backend load. Hiring managers look for caching experience to verify you can build scalable, high-performance systems.",
    projects: "Session Store microservice with Redis, API Rate Limiter middleware, Database Query Caching Wrapper",
    resources: [
      { label: "Redis University", url: "https://university.redis.io" },
      { label: "Introduction to Caching", url: "https://aws.amazon.com/caching/" }
    ]
  }
};

// ─── Modal Elements ───
const modal = document.getElementById('skill-modal');
const modalTitle = document.getElementById('modal-title');
const modalIcon = document.getElementById('modal-icon');
const modalDemand = document.getElementById('modal-demand');
const modalDesc = document.getElementById('modal-desc');
const modalWhy = document.getElementById('modal-why');
const modalProjects = document.getElementById('modal-projects');
const modalResources = document.getElementById('modal-resources');
const modalClose = document.getElementById('modal-close');
const modalOverlay = document.getElementById('modal-overlay');

function openSkillModal(skillKey) {
  const info = SKILL_INFO[skillKey.toLowerCase()];
  if (!info) return;

  modalIcon.textContent = info.icon;
  modalTitle.textContent = info.title;
  modalDemand.textContent = `Market Demand: ${info.demand}`;
  modalDemand.style.color = info.demandColor;
  modalDesc.textContent = info.description;
  modalWhy.textContent = info.why_matters;
  modalProjects.textContent = info.projects || "No specific projects registered.";

  modalResources.innerHTML = '';
  info.resources.forEach(r => {
    const a = document.createElement('a');
    a.href = r.url;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    a.textContent = '→ ' + r.label;
    a.className = 'resource-link';
    modalResources.appendChild(a);
  });

  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeSkillModal() {
  modal.classList.remove('open');
  document.body.style.overflow = '';
}

if (modalClose) modalClose.addEventListener('click', closeSkillModal);
if (modalOverlay) modalOverlay.addEventListener('click', closeSkillModal);
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeSkillModal(); });

// Attach click handlers to all skill badges
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-skill]').forEach(badge => {
    badge.style.cursor = 'pointer';
    badge.addEventListener('click', () => openSkillModal(badge.dataset.skill));
  });
});
