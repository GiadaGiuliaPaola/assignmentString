# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
print (f'Leek is {leek_price} euro per kilo.')

leek_order = 'leek 4'
leek_order.find('int')
number_order = leek_order[-1]
sum_total = int(number_order) * leek_price
print(sum_total)

broccoli_price = 2.34
broccoli_order =  'broccoli 1.6'
number_broccoli_order = broccoli_order[-3:]
sum_total_broccoli = float(number_broccoli_order) * broccoli_price
print(f'{number_broccoli_order}kg broccoli costs {round(sum_total_broccoli,2)}e')


