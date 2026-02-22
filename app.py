from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    portfolio_data = {
        "name": "Douglas Ferreira",
        "role": "Engenheiro de Software Full-Stack",
        "headline": "Arquitetura de Software Robusta para Negócios Escaláveis.",
        "subheadline": "10 anos de experiência transformando requisitos complexos em soluções digitais de alta performance com Python, PHP e Node.js.",
        "about": """Com uma década de atuação no mercado de tecnologia, construí minha carreira fundamentada na entrega de valor real através da engenharia de software. Não escrevo apenas código; projeto ecossistemas digitais.
        
        Minha trajetória como Engenheiro Full-Stack me permitiu dominar todo o ciclo de vida do desenvolvimento, desde a concepção da arquitetura até o deploy em produção. Especialista em ambientes complexos, combino a robustez do PHP e Python com a versatilidade do Node.js para criar sistemas que são, acima de tudo, seguros, performáticos e sustentáveis a longo prazo.
        
        Atualmente, meu foco está em arquitetura de software, garantindo que as decisões técnicas de hoje sustentem o crescimento do negócio amanhã.""",
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
            "linkedin": "linkedin.com/in/douglasferreira",
            "github": "github.com/douglasferreira"
        }
    }
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
