from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)


def get_portfolio_content(lang):
    if lang == "en":
        return {
            "name": "Douglas Ferreira",
            "role": "Full-Stack Software Engineer",
            "headline": "Robust Software Architecture for Scalable Businesses.",
            "subheadline": "Software engineering focused on architecture, performance and sustainable business growth.",
            "about": """Software Engineer with over 15 years of experience leading and developing results-oriented technology solutions. My work is driven by generating real business value, aligning technical decisions with the organization's strategic goals.

Throughout my career, I have built strong experience as a Full-Stack Engineer, with end-to-end ownership of the development lifecycle — from architectural definition to delivery and production support. I design and build scalable, secure and high-performance systems using technologies such as PHP, Python and Node.js, always focused on operational efficiency and sustainable growth.

I currently focus on software architecture and technical standards definition, contributing to more robust, predictable and scalable environments. I continually seek to balance technical excellence, product vision and measurable business impact.""",
            "skills": {
                "hard": [
                    "Python (Django/Flask)",
                    "PHP (Laravel/Symfony)",
                    "Node.js (NestJS/Express)",
                    "PostgreSQL / MySQL",
                    "Redis / MongoDB",
                    "Docker / CI/CD",
                    "Microservices",
                    "Clean Architecture",
                ],
                "soft": [
                    "Technical Leadership",
                    "Mentoring",
                    "Clear Communication",
                    "Complex Troubleshooting",
                    "Business-Oriented Mindset",
                ],
            },
            "projects": [
                {
                    "title": "Event Management Platform",
                    "problem": "Organizations relying on manual processes for registrations, attendee control and certificate issuing, leading to rework and low visibility over the participant journey.",
                    "description": "Web platform for end-to-end management of in-person and online events, including registration, ticket batches, check-in, certificate issuing and real-time communication with participants.",
                    "tech_stack": ["Python", "Django REST Framework", "PostgreSQL", "Redis"],
                    "role": "Full-Stack Software Engineer",
                    "demo_url": "https://demo.eventos.example.com",
                    "demo_credentials": "User: demo@company.com | Password: events123",
                },
                {
                    "title": "Fleet Management System",
                    "problem": "Companies with vehicles and field teams lacking centralized control of routes, maintenance and utilization, resulting in higher costs and low operational predictability.",
                    "description": "System for monitoring fleets, registering vehicles, controlling maintenance, tracking trips and providing operational indicators to support decision-making.",
                    "tech_stack": ["Python", "Django REST Framework", "PostgreSQL", "Redis"],
                    "role": "Full-Stack Software Engineer",
                    "demo_url": "https://demo.frotas.example.com",
                    "demo_credentials": "User: demo@company.com | Password: fleet123",
                },
                {
                    "title": "Citizen Identification Platform",
                    "problem": "Public agencies and institutions with citizen data spread across multiple systems, making it difficult to validate records, query information and provide services.",
                    "description": "Centralized platform for managing and querying citizen data, with authentication layers, audit trails and integrations with legacy systems to unify information.",
                    "tech_stack": ["Python", "Django REST Framework", "PostgreSQL", "Redis"],
                    "role": "Full-Stack Software Engineer",
                    "demo_url": "https://demo.idcidadao.example.com",
                    "demo_credentials": "User: demo@agency.gov | Password: citizen123",
                },
            ],
            "contact": {
                "email": "douglas@example.com",
                "linkedin": "https://www.linkedin.com/in/douglas-ferreira-879a115a",
                "github": "https://github.com/dougcpm",
            },
        }

    return {
        "name": "Douglas Ferreira",
        "role": "Engenheiro de Software Full-Stack",
        "headline": "Arquitetura de Software Robusta para Negócios Escaláveis.",
        "subheadline": "Engenharia de software orientada à arquitetura, performance e crescimento sustentável do negócio.",
        "about": """Engenheiro de Software com mais de 15 anos de experiência liderando e desenvolvendo soluções tecnológicas orientadas a resultados. Minha atuação é guiada pela geração de valor para o negócio, alinhando decisões técnicas às metas estratégicas da organização.

Ao longo da carreira, consolidei forte experiência como Full-Stack, com domínio completo do ciclo de desenvolvimento — da definição arquitetural à entrega e sustentação em produção. Atuo na construção de sistemas escaláveis, seguros e de alta performance, utilizando tecnologias como PHP, Python e Node.js, sempre com foco em eficiência operacional e crescimento sustentável.

Atualmente, concentro meus esforços em arquitetura de software e definição de padrões técnicos, contribuindo para ambientes mais robustos, previsíveis e preparados para escalar. Busco continuamente equilibrar excelência técnica, visão de produto e impacto mensurável nos resultados do negócio.""",
        "skills": {
            "hard": [
                "Python (Django/Flask)",
                "PHP (Laravel/Symfony)",
                "Node.js (NestJS/Express)",
                "PostgreSQL / MySQL",
                "Redis / MongoDB",
                "Docker / CI/CD",
                "Microsserviços",
                "Clean Architecture",
            ],
            "soft": [
                "Liderança Técnica",
                "Mentoria",
                "Comunicação Assertiva",
                "Troubleshooting Complexo",
                "Visão de Negócio",
            ],
        },
        "projects": [
            {
                "title": "Plataforma de Gestão de Eventos",
                "problem": "Organizações com processos manuais para inscrição, controle de participantes e emissão de certificados, gerando retrabalho e baixa visibilidade sobre a jornada do participante.",
                "description": "Sistema web para gestão completa de eventos presenciais e online, com módulos de inscrição, controle de lotes, check-in, emissão de certificados e comunicação com participantes em tempo real.",
                "tech_stack": ["Python", "Django REST Framework", "PostgreSQL", "Redis"],
                "role": "Engenheiro de Software Full-Stack",
                "demo_url": "https://demo.eventos.example.com",
                "demo_credentials": "Usuário: demo@empresa.com | Senha: eventos123",
            },
            {
                "title": "Sistema de Gestão de Frotas",
                "problem": "Empresas com veículos e equipes em campo sem controle centralizado de rotas, manutenções e utilização, resultando em custos elevados e baixa previsibilidade operacional.",
                "description": "Aplicação voltada ao monitoramento de frotas, cadastro de veículos, controle de manutenções, acompanhamento de deslocamentos e indicadores operacionais para suporte à tomada de decisão.",
                "tech_stack": ["Python", "Django REST Framework", "PostgreSQL", "Redis"],
                "role": "Engenheiro de Software Full-Stack",
                "demo_url": "https://demo.frotas.example.com",
                "demo_credentials": "Usuário: demo@empresa.com | Senha: frota123",
            },
            {
                "title": "Plataforma de Identificação do Cidadão",
                "problem": "Órgãos públicos e instituições com dados de cidadãos fragmentados em múltiplos sistemas, dificultando validação cadastral, consulta de informações e acesso a serviços.",
                "description": "Plataforma centralizada para gestão e consulta de dados de cidadãos, com camadas de autenticação, trilhas de auditoria e integrações com sistemas legados para unificação das informações.",
                "tech_stack": ["Python", "Django REST Framework", "PostgreSQL", "Redis"],
                "role": "Engenheiro de Software Full-Stack",
                "demo_url": "https://demo.idcidadao.example.com",
                "demo_credentials": "Usuário: demo@org.gov | Senha: cidadao123",
            },
        ],
        "contact": {
            "email": "douglas@example.com",
            "linkedin": "https://www.linkedin.com/in/douglas-ferreira-879a115a",
            "github": "https://github.com/dougcpm",
        },
    }


def get_ui_strings(lang):
    if lang == "en":
        return {
            "nav_about": "About",
            "nav_skills": "Skills",
            "nav_projects": "Projects",
            "nav_contact": "Contact",
            "hero_primary_cta": "View Featured Projects",
            "hero_secondary_cta": "Get in Touch",
            "section_about": "About Me",
            "section_skills": "Technical Expertise",
            "section_projects": "Featured Projects",
            "section_contact_title": "Shall we build solutions that really deliver results?",
            "section_contact_subtitle": "I am available for strategic projects and complex challenges that require architectural vision, technical excellence and focus on sustainable growth.",
            "project_problem_label": "Problem",
            "project_solution_label": "Solution",
            "project_tech_stack_label": "Tech Stack",
            "project_demo_link": "Access Demo Environment",
            "project_demo_credentials": "Access credentials:",
        }

    return {
        "nav_about": "Sobre",
        "nav_skills": "Skills",
        "nav_projects": "Projetos",
        "nav_contact": "Contato",
        "hero_primary_cta": "Ver Projetos Selecionados",
        "hero_secondary_cta": "Entrar em Contato",
        "section_about": "Sobre Mim",
        "section_skills": "Expertise Técnica",
        "section_projects": "Projetos em Destaque",
        "section_contact_title": "Vamos construir soluções que realmente geram resultado?",
        "section_contact_subtitle": "Estou disponível para projetos estratégicos e desafios de alta complexidade que exijam visão arquitetural, excelência técnica e foco em crescimento sustentável.",
        "project_problem_label": "Problema",
        "project_solution_label": "Solução",
        "project_tech_stack_label": "Tech Stack",
        "project_demo_link": "Acessar Ambiente de Demonstração",
        "project_demo_credentials": "Credenciais de acesso:",
    }


@app.route("/")
def home():
    lang = request.args.get("lang", "pt")
    if lang not in ("pt", "en"):
        lang = "pt"
    portfolio_data = get_portfolio_content(lang)
    ui_strings = get_ui_strings(lang)
    current_year = datetime.now().year
    return render_template(
        "index.html",
        data=portfolio_data,
        current_year=current_year,
        lang=lang,
        ui=ui_strings,
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)
