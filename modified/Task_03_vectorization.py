import numpy as np
import timeit
# Modified: Increased dataset size to 5,000,000 samples, higher latency range (10-
500 ms),
# and added logarithmic + trigonometric jitter metric evaluation
rng = np.random.default_rng(99)
latency_ms = rng.uniform(10, 500, 5_000_000)
def loop_version():
metrics = []
for value in latency_ms:
sec = value / 1000.0
metrics.append((sec ** 2) + np.log1p(sec))
return metrics
def vectorized_version():
sec = latency_ms / 1000.0
return (sec ** 2) + np.log1p(sec)
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
result = vectorized_version()
print("First five combined jitter metrics:", np.round(result[:5], 6))
print(f"Mean metric across 5M samples: {np.mean(result):.6f}")
print(f"Loop time (5M): {loop_time:.4f} s")
print(f"Vectorized time (5M): {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")