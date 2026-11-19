import matplotlib.pyplot as plt

# Constantes físicas
k = 8.99e9   # N·m²/C²
Q = 1.0      # 1 C

# Distâncias de 0,10 m até 1,00 m (passo de 0,01 m)
distancias = [0.10 + i * 0.01 for i in range(91)]
campos_eletricos = [k * abs(Q) / (r ** 2) for r in distancias]

plt.figure(figsize=(6, 4))
plt.plot(distancias, campos_eletricos, color="tab:blue", linewidth=2)
plt.title("Módulo do Campo Elétrico vs. Distância")
plt.xlabel("Distância r (m)")
plt.ylabel("Campo Elétrico E (N/C)")
plt.grid(True)
plt.tight_layout()
plt.savefig("campo_eletrico.png", dpi=150)
print("Gráfico salvo em campo_eletrico.png!")