import numpy as np
# Real-world case: Estimate the probability that a 3-phase software/infrastructure
# deployment exceeds a 45-day contractual deadline when phase durations are
uncertain.
# Assumptions: Phase 1 ~ Triangular(10, 14, 20) days, Phase 2 ~ Normal(18, 3) days,
# Phase 3 ~ Uniform(8, 14) days; N = 250,000 Monte Carlo trials.
rng = np.random.default_rng(2026)
N = 250_000
deadline_days = 45.0
phase1 = rng.triangular(10.0, 14.0, 20.0, N)
phase2 = rng.normal(18.0, 3.0, N)
phase3 = rng.uniform(8.0, 14.0, N)
total_duration = phase1 + phase2 + phase3
prob_late = np.mean(total_duration > deadline_days)
p95_duration = np.percentile(total_duration, 95)
print(f"Mean project duration: {np.mean(total_duration):.2f} days")
print(f"Probability of missing 45d SLA: {prob_late:.2%}")
print(f"95th-percentile schedule bound: {p95_duration:.2f} days")