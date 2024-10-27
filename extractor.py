import json, pandas as pd

with open('product.json', 'r') as f:
    data = json.load(f)
    datos = data['allVariants'][0]['attributesRaw']

for item in datos: 
    if item['name'] == "custom_attributes":
        elemento = item['value']['es-CR']
        
        elemento_diccionario = json.loads(elemento)        

diccionario_final = {}   

for atributo, valor in elemento_diccionario.items():
    
    if atributo in ('allergens', 'sku', 'vegan', 'kosher', 'organic', 'vegetarian', 'gluten_free', 'lactose_free', 'package_quantity', 'Unit_size', 'net_weight'): 
        diccionario_final[atributo] = valor['value']        

print(diccionario_final)

allergens = diccionario_final['allergens']
allergens_list = []
#ciclo recolector de allergens.
for allergen in allergens: 
    print(allergen['name'])
    allergens_list.append(allergen['name'])

print(allergens_list)

diccionario_final['allergens'] = allergens_list
print(diccionario_final)

df = pd.DataFrame.from_dict(diccionario_final)
df.to_excel('resultado.xlsx', index=False)

print("Archivo listo en resultado.xlsx")