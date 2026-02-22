from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    portfolio_data = {
        "name": "Douglas Ferreira",
        "role": "Engenheiro de Software Full-Stack",
        "headline": "Arquitetura de Software Robusta para Negócios Escaláveis.",
        "subheadline": "Engenharia de software orientada à arquitetura, performance e crescimento sustentável do negócio.",
        "about": """Engenheiro de Software com mais de 10 anos de experiência liderando e desenvolvendo soluções tecnológicas orientadas a resultados. Minha atuação é guiada pela geração de valor para o negócio, alinhando decisões técnicas às metas estratégicas da organização.

Ao longo da carreira, consolidei forte experiência como Full-Stack, com domínio completo do ciclo de desenvolvimento — da definição arquitetural à entrega e sustentação em produção. Atuo na construção de sistemas escaláveis, seguros e de alta performance, utilizando tecnologias como PHP, Python e Node.js, sempre com foco em eficiência operacional e crescimento sustentável.

Atualmente, concentro meus esforços em arquitetura de software e definição de padrões técnicos, contribuindo para ambientes mais robustos, previsíveis e preparados para escalar. Busco continuamente equilibrar excelência técnica, visão de produto e impacto mensurável nos resultados do negócio.""",
        "skills": {
            "hard": [
                "Python (Django/Flask)", "PHP (Laravel/Symfony)", "Node.js (NestJS/Express)",
                "PostgreSQL / MySQL", "Redis / MongoDB", "Docker / CI/CD",
                "Microsserviços", "Clean Architecture"
            ],
            "soft": [
                "Liderança Técnica", "Mentoria", "Comunicação Assertiva",
                "Troubleshooting Complexo", "Visão de Negócio"
            ]
        },
        "projects": [
            {
                "title": "Sistema de Gestão ERP Corporativo (SaaS)",
                "description": "Migração de sistema legado monolítico para arquitetura de microsserviços, reduzindo custos de manutenção e tempo de resposta.",
                "tech_stack": ["Python", "PostgreSQL", "Docker", "React"],
                "role": "Arquiteto de Software Líder"
            },
            {
                "title": "API de Pagamentos High-Traffic",
                "description": "API RESTful capaz de processar milhares de transações simultâneas com segurança bancária e zero downtime.",
                "tech_stack": ["Node.js", "Redis", "MongoDB", "AWS Lambda"],
                "role": "Desenvolvedor Backend Senior"
            },
            {
                "title": "Portal de Análise de Dados Financeiros",
                "description": "Dashboard interativo com processamento de dados em background para tomada de decisão executiva.",
                "tech_stack": ["PHP 8 (Laravel)", "Vue.js", "MySQL"],
                "role": "Full-Stack Developer"
            }
        ],
        "contact": {
            "email": "douglas@example.com",
            "linkedin": "www.linkedin.com/in/douglas-ferreira-879a115a",
            "github": "github.com/dougcpm"
        }
    }
    current_year = datetime.now().year
    return render_template('index.html', data=portfolio_data, current_year=current_year)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
