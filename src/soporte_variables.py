# VARIABLES PARA REGRESIÓN LINEAL (DATAFRAME SOCIO-ECONOMICO)

# primera selección de columnas
lista_columnas = ['country', 'Region', 'Population in thousands (2017)', 'GDP per capita (current US$)',
                   'Employment: Agriculture (% of employed)', 'Employment: Industry (% of employed)', 'Employment: Services (% of employed)', 'Population age distribution (0-14 / 60+ years, %)',
                    'International migrant stock (000/% of total pop.)', 'Education: Government expenditure (% of GDP)', 'Quality Of Life Index', 
                    'Purchasing Power Index', 'Safety Index', 'Cost of Living', 'Rent Index', 'Grocery Index', 'Restaurant Price Index', 'Adjusted net national income per capita (constant 2010 US$)',
                     'Consumer price index (2010 = 100)', 'Human capital index (HCI) (scale 0-1)', 'Inflation, consumer prices (annual %)', 'Urban population (% of total population)_y']

renombrado_columnas = {'population_in_thousands_(2017)': 'population_2017',
                       'gdp_per_capita_(current_us$)': 'gdp_per_capita',
                       'employment:_agriculture_(%_of_employed)': 'employment_agriculture',  
                        'employment:_industry_(%_of_employed)':  'employment_industry',
                        'employment:_services_(%_of_employed)': 'employment_services', 
                        'population_age_distribution_(0-14_/_60+_years,_%)': 'population_age_distribution_0_14_and_60_plus',
                        'international_migrant_stock_(000/%_of_total_pop.)': 'international_migrant_stock_000_and_percentage',
                        'education:_government_expenditure_(%_of_gdp)': 'education',
                        'adjusted_net_national_income_per_capita_(constant_2010_us$)': 'adjusted_net_national_income_per_capita_2010',
                        'consumer_price_index_(2010_=_100)' : 'consumer_price_index',
                        'human_capital_index_(hci)_(scale_0-1)': 'human_capital_index',
                        'inflation,_consumer_prices_(annual_%)': 'inflation',
                        'urban_population_(%_of_total_population)_y': 'urban_population'
                        }

paises_indice = ['Argentina',  'Australia',  'Austria',  'Belarus',  'Belgium',  'Bosnia and Herzegovina',  'Brazil',  'Bulgaria',  'Canada',  'Chile',  'China, Hong Kong SAR',
                'China',  'Colombia',  'Croatia', 'Cyprus', 'Czechia', 'Denmark', 'Egypt', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Indonesia',
                'Iran (Islamic Republic of)', 'Ireland', 'Israel', 'Italy', 'Japan', 'Jordan', 'Lebanon', 'Lithuania', 'Malaysia', 'Mexico', 'Netherlands', 'New Zealand',
                'Norway', 'Pakistan', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Republic of Korea', 'Romania', 'Russian Federation', 'Saudi Arabia', 'Serbia', 'Singapore',
                'Slovakia', 'Slovenia', 'South Africa', 'Spain', 'Sri Lanka', 'Sweden', 'Switzerland', 'Thailand', 'The former Yugoslav Republic of Macedonia', 'Turkey',
                'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'Venezuela (Bolivarian Republic of)', 'Vietnam']

lista_float = ['population_age_distribution_0_14', 'population_age_distribution_60_plus', 'international_migrant_stock_000', 'international_migrant_stock']

orden_regiones = ['NorthernAfrica', 'SouthernAsia', 'South-easternAsia', 'CentralAmerica', 'EasternEurope', 'SouthernAfrica', 'SouthernEurope', 'SouthAmerica', 'EasternAsia',
                  'WesternAsia', 'NorthernAmerica', 'Oceania', 'WesternEurope', 'NorthernEurope']



# VARIABLES PARA REGRESIÓN LOGÍSTICA (DATAFRAME AEROLINEA)

columnas_categoria = ["seat_comfort", "departure_arrival_time_convenient", "food_and_drink", "gate_location", "inflight_wifi_service", "inflight_entertainment", 
                      "online_support", "ease_of_online_booking", "onboard_service", "leg_room_service", "baggage_handling", "checkin_service", "cleanliness", 
                      "online_boarding"]
