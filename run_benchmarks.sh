#!/usr/bin/env bash
set -euo pipefail

# Ajuste aquí los parámetros del experimento
REPEATS=5
RECURSIVE_NS=(10 20 25 30 35)
ITERATIVE_NS=(100000 200000 500000 1000000)

mkdir -p results

CSV="results/bench_results.csv"
: > "$CSV"  # limpiar/crear

# 1) C++ (compilado)
if [ -x "cpp/fib" ]; then
  echo "[C++] ejecutable encontrado."
else
  echo "[C++] no se encontró ejecutable. Intentando compilar..."
  (cd cpp && make)
fi

echo "[C++] Recursivo..."
for n in "${RECURSIVE_NS[@]}"; do
  ./cpp/fib rec "$n" "$REPEATS" "$CSV"
done

echo "[C++] Iterativo..."
for n in "${ITERATIVE_NS[@]}"; do
  ./cpp/fib iter "$n" "$REPEATS" "$CSV"
done

# 2) Python (interpretado)
echo "[Python] Recursivo..."
for n in "${RECURSIVE_NS[@]}"; do
  python python/fib.py rec "$n" "$REPEATS" "$CSV"
done

echo "[Python] Iterativo..."
for n in "${ITERATIVE_NS[@]}"; do
  python python/fib.py iter "$n" "$REPEATS" "$CSV"
done

echo "Resultados en $CSV"
