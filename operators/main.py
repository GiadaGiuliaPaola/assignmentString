# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line
spain_language = 'Castilian Spanish'
switzerland_language = 'Swiss German'
print(spain_language == switzerland_language)

spain_religion = 'Roman Catholic'
switzerland_religion = 'Roman Catholic'
print(spain_religion == switzerland_religion)

spain_capital = 'Madrid'
switzerland_capital = 'Bern'
print(len(spain_capital) != len(switzerland_capital))

spain_GDP = 10.7
switzerland_GDP = 5.2
print(switzerland_GDP > spain_GDP)

spain_population_growth = 0.13
switzerland_population_growth = 0.65
print((spain_population_growth and switzerland_population_growth) < 1)

spain_population_count = 47163418
switzerland_population_count = 8508698
print((spain_population_count or switzerland_population_count) > 10000000)
print((spain_population_count or switzerland_population_count) >= 10000000)

