import argparse
import time
import csv

def fib_iter(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

def fib_rec(n: int) -> int:
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["iter", "rec"], help="iter or rec")
    parser.add_argument("n", type=int)
    parser.add_argument("repeats", type=int)
    parser.add_argument("csv_out")
    args = parser.parse_args()

    times_ms = []
    for _ in range(args.repeats):
        t0 = time.perf_counter()
        # volatile equivalent not needed in Python; just compute
        if args.mode == "iter":
            fib_iter(args.n)
        else:
            fib_rec(args.n)
        t1 = time.perf_counter()
        times_ms.append((t1 - t0) * 1000.0)

    avg = sum(times_ms) / len(times_ms)

    with open(args.csv_out, "a", newline="") as f:
        w = csv.writer(f)
        w.writerow(["interpreted_python",
                    "iterative" if args.mode == "iter" else "recursive",
                    args.n, args.repeats, f"{avg:.6f}"])

if __name__ == "__main__":
    main()
