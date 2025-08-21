import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

results_path = Path("results") / "bench_results.csv"
df = pd.read_csv(results_path, header=None,
                 names=["lang", "algorithm", "n", "repeats", "avg_ms"])

# Convert dtypes
df["n"] = pd.to_numeric(df["n"], errors="coerce")
df["avg_ms"] = pd.to_numeric(df["avg_ms"], errors="coerce")

# Chart 1: runtime vs n (linear scale), grouped by lang+algo
plt.figure()
for (lang, algo), g in df.groupby(["lang", "algorithm"]):
    g = g.sort_values("n")
    plt.plot(g["n"], g["avg_ms"], marker="o", label=f"{lang} - {algo}")
plt.xlabel("n")
plt.ylabel("Tiempo promedio (ms)")
plt.title("Tiempo de ejecución vs n (menor es mejor)")
plt.legend()
Path("results").mkdir(exist_ok=True, parents=True)
plt.savefig("results/runtime_by_lang_algo.png", bbox_inches="tight")
plt.close()

# Chart 2: runtime vs n (log scale Y)
plt.figure()
for (lang, algo), g in df.groupby(["lang", "algorithm"]):
    g = g.sort_values("n")
    plt.plot(g["n"], g["avg_ms"], marker="o", label=f"{lang} - {algo}")
plt.xlabel("n")
plt.ylabel("Tiempo promedio (ms) (escala log)")
plt.yscale("log")
plt.title("Tiempo de ejecución vs n (escala log)")
plt.legend()
plt.savefig("results/runtime_logscale.png", bbox_inches="tight")
plt.close()

print("Gráficas guardadas en results/")
