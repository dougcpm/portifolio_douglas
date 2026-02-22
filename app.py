from flask import Flask, render_template
from datetime import datetime
import os

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
                "title": "Plataforma de Gestão de Eventos",
                "problem": "Organizações com processos manuais para inscrição, controle de participantes e emissão de certificados, gerando retrabalho e baixa visibilidade sobre a jornada do participante.",
                "description": "Sistema web para gestão completa de eventos presenciais e online, com módulos de inscrição, controle de lotes, check-in, emissão de certificados e comunicação com participantes em tempo real.",
                "tech_stack": ["PHP 8", "Laravel", "MySQL", "Redis"],
                "role": "Engenheiro de Software Full-Stack",
                "demo_url": "",
                "demo_credentials": ""
            },
            {
                "title": "Sistema de Gestão de Frotas",
                "problem": "Empresas com veículos e equipes em campo sem controle centralizado de rotas, manutenções e utilização, resultando em custos elevados e baixa previsibilidade operacional.",
                "description": "Aplicação voltada ao monitoramento de frotas, cadastro de veículos, controle de manutenções, acompanhamento de deslocamentos e indicadores operacionais para suporte à tomada de decisão.",
                "tech_stack": ["Node.js", "NestJS", "PostgreSQL", "Docker"],
                "role": "Engenheiro de Software Full-Stack",
                "demo_url": "",
                "demo_credentials": ""
            },
            {
                "title": "Plataforma de Identificação do Cidadão",
                "problem": "Órgãos públicos e instituições com dados de cidadãos fragmentados em múltiplos sistemas, dificultando validação cadastral, consulta de informações e acesso a serviços.",
                "description": "Plataforma centralizada para gestão e consulta de dados de cidadãos, com camadas de autenticação, trilhas de auditoria e integrações com sistemas legados para unificação das informações.",
                "tech_stack": ["Python", "Django REST Framework", "PostgreSQL", "Redis"],
                "role": "Arquiteto de Software",
                "demo_url": "",
                "demo_credentials": ""
            }
        ],
        "contact": {
            "email": "douglas@example.com",
            "linkedin": "https://www.linkedin.com/in/douglas-ferreira-879a115a",
            "github": "https://github.com/dougcpm"
        }
    }
    current_year = datetime.now().year
    return render_template('index.html', data=portfolio_data, current_year=current_year)

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)
