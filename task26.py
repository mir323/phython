text = input()

cost_per_symbol_kopecks = 40

total_cost_kopecks = len(text) * cost_per_symbol_kopecks

rubles = total_cost_kopecks // 100
kopecks = total_cost_kopecks% 100

print(f"{rubles} р. {kopecks} коп.")
