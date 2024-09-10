import csv
import faker
import datetime
import random

# Crie uma instância do Faker com provedor de data e hora
fake = faker.Faker('pt_BR')
fake.providers.extend([faker.providers.date_time.datetime])

# Gera datas em ordem sequencial
start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 1, 31)

# Defina taxas de conversão para cada estágio do funil
organic_clicks_rate = 0.05  # 5% das impressões são convertidas em cliques orgânicos
paid_clicks_rate = 0.03  # 3% das impressões são convertidas em cliques pagos
local_clicks_rate = 0.02  # 2% das impressões são convertidas em cliques locais
interactions_rate = 0.2  # 20% dos cliques são convertidos em interações
opportunities_rate = 0.1  # 10% das interações se convertem em oportunidades
sales_rate = 0.05  # 5% das oportunidades são convertidas em vendas

with open('funil.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(['Data',
                        'Impressões',
                        'Clicks',
                        'Interações',
                        'Oportunidades',
                        'Vendas',
                        'Custos',
                        'Receita',
                        'Alcance'])

    current_date = start_date
    for _ in range(31):
        data = current_date.strftime('%Y-%m-%d')

        # Gerar impressões
        impressoes = fake.random_int(min=2000, max=200000)
         
        # Calcular alcance
        alcance = int(impressoes * 0.1)  # 10% das impressões

        # Calcular cliques
        organic_clicks = int(impressoes * organic_clicks_rate)
        paid_clicks = int(impressoes * paid_clicks_rate)
        local_clicks = int(impressoes * local_clicks_rate)
        total_clicks = organic_clicks + paid_clicks + local_clicks

        # Calcular interações
        interactions = int(total_clicks * interactions_rate)

        # Calcular oportunidades
        opportunities = int(interactions * opportunities_rate)

        # Calcular vendas
        sales = int(opportunities * sales_rate)

        # Gerar custos e receitas (com base em valores e suposições aleatórias)
        costs = fake.random_int(min=500, max=5000)
        revenue = sales * fake.random_int(min=100, max=500)  # Assuming average sale value between $100 and $500

        # Grava linha em CSV
        csv_writer.writerow([data,
                            impressoes,
                            total_clicks,
                            interactions,
                            opportunities,
                            sales,
                            costs,
                            revenue,
                            alcance])

        current_date += datetime.timedelta(days=1)
