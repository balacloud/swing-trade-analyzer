# DBSCAN/Agglomerative Implementation Plan

> **Purpose:** Architectural plan for replacing KMeans with adaptive clustering
> **Scope:** Week 1 of S&R Improvement (2 hours estimated)
> **Status:** Planning Complete - Ready for Implementation

---

## 1. Current State Analysis

### Current Implementation: `_kmeans_sr()` (Lines 319-375)

```python
def _kmeans_sr(df: pd.DataFrame, cfg: SRConfig) -> Optional[Tuple[...]]
    # Problems:
    # 1. Fixed n_clusters=5 - arbitrary, not data-driven
    # 2. Fits on ALL high/low prices - noisy
    # 3. No pivot filtering - includes non-significant prices
    # 4. No touch-based scoring - all levels equal weight
```

**Current Weaknesses:**
| Issue | Impact | Priority |
|-------|--------|----------|
| Fixed 5 clusters | Missing natural price zones | Critical |
| No pivot detection | Including noise | High |
| No level scoring | Can't rank importance | Medium |

---

## 2. Proposed Architecture

### New Module: `_agglomerative_sr()`

**Design Principles:**
1. **Adaptive clustering** - Number of levels determined by data, not config
2. **Pivot-based input** - Only cluster significant price points
3. **ATR-based merge distance** - Volatility-adjusted thresholds
4. **Level scoring** - Rank by touch count + recency

### Class Diagram

```
SRConfig (existing)
├── merge_percent: float = 0.02      # NEW: 2% default
├── min_touches: int = 2              # NEW: Minimum touches for valid level
├── bars_for_pivot: int = 21          # NEW: Pivot detection window
└── (existing fields preserved)

compute_sr_levels()
├── _pivot_sr()                       # EXISTING: Keep as primary
├── _agglomerative_sr()               # NEW: Replace _kmeans_sr
│   ├── _detect_zigzag_pivots()       # NEW: ZigZag pivot detection
│   ├── _cluster_with_agglom()        # NEW: AgglomerativeClustering
│   └── _score_levels()               # NEW: Touch-based scoring
└── _volume_profile_sr()              # EXISTING: Keep as fallback
```

---

## 3. Implementation Details

### Step 1: Add ZigZag Pivot Detection

```python
def _detect_zigzag_pivots(
    df: pd.DataFrame,
    percent_delta: float = 0.05,  # 5% min change
    min_bars: int = 5
) -> Tuple[List[float], List[float]]:
    """
    Detect significant pivot highs and lows using ZigZag algorithm.

    Returns:
        (pivot_highs, pivot_lows) - Lists of significant price levels
    """
    # Use zigzag library or implement manually
    # Filter pivots by minimum bars between them
    pass
```

**Why ZigZag:**
- Filters noise (only significant swings)
- Adapts to volatility (percent-based)
- Standard TA approach (well-understood)

### Step 2: Replace KMeans with AgglomerativeClustering

```python
from sklearn.cluster import AgglomerativeClustering

def _cluster_with_agglom(
    pivot_prices: np.ndarray,
    merge_percent: float = 0.02,  # 2% of current price
    current_price: float = None
) -> List[float]:
    """
    Cluster pivot prices using AgglomerativeClustering.

    Key difference from KMeans:
    - No need to specify n_clusters
    - Uses distance threshold (merge_percent * current_price)
    - Hierarchical merging = more intuitive for price levels
    """
    if len(pivot_prices) < 2:
        return list(pivot_prices)

    # Calculate adaptive merge distance
    merge_distance = current_price * merge_percent

    # AgglomerativeClustering with distance_threshold
    clustering = AgglomerativeClustering(
        n_clusters=None,              # Let algorithm decide
        distance_threshold=merge_distance,
        linkage='average'             # Average linkage for price data
    )

    labels = clustering.fit_predict(pivot_prices.reshape(-1, 1))

    # Extract cluster centers using median (more robust)
    centers = []
    for label in set(labels):
        cluster_prices = pivot_prices[labels == label]
        centers.append(float(np.median(cluster_prices)))

    return sorted(centers)
```

**Parameters Explained:**
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| `n_clusters` | None | Let data determine count |
| `distance_threshold` | price * 0.02 | 2% bands (adjustable) |
| `linkage` | 'average' | Balance between single/complete |

### Step 3: Add Level Scoring

```python
def _score_levels(
    levels: List[float],
    df: pd.DataFrame,
    touch_threshold: float = 0.005  # 0.5% = "touch"
) -> List[Tuple[float, int]]:
    """
    Score levels by number of price touches.

    Returns:
        List of (level, score) tuples, sorted by score descending
    """
    scores = []
    for level in levels:
        # Count bars where high/low within threshold of level
        upper = level * (1 + touch_threshold)
        lower = level * (1 - touch_threshold)

        touches = ((df['high'] >= lower) & (df['high'] <= upper) |
                   (df['low'] >= lower) & (df['low'] <= upper)).sum()

        scores.append((level, int(touches)))

    # Sort by score descending
    return sorted(scores, key=lambda x: x[1], reverse=True)
```

---

## 4. Integration Plan

### Phase 1: Add New Functions (No Breaking Changes)

```python
# Add to support_resistance.py

# 1. New config fields
@dataclass
class SRConfig:
    # ... existing fields ...
    merge_percent: float = 0.02           # NEW
    zigzag_percent_delta: float = 0.05    # NEW
    min_touches_for_level: int = 2        # NEW

# 2. New private functions
def _detect_zigzag_pivots(...): ...
def _cluster_with_agglom(...): ...
def _score_levels(...): ...

# 3. New combined function
def _agglomerative_sr(df: pd.DataFrame, cfg: SRConfig) -> Optional[Tuple[...]]:
    """Replaces _kmeans_sr with adaptive clustering."""
    ...
```

### Phase 2: Update compute_sr_levels() Call Order

```python
def compute_sr_levels(df: pd.DataFrame, cfg: Optional[SRConfig] = None) -> SRLevels:
    # ... existing setup ...

    # 1) Pivot-based (primary - unchanged)
    if not high_vol:
        pivot_result = _pivot_sr(df, cfg)
        if pivot_result is not None:
            return SRLevels(method="pivot", ...)

    # 2) Agglomerative clustering (NEW - replaces KMeans)
    agglom_result = _agglomerative_sr(df, cfg)
    if agglom_result is not None:
        return SRLevels(method="agglomerative", ...)  # NEW method name

    # 3) Volume profile (fallback - unchanged)
    return SRLevels(method="volume_profile", ...)
```

### Phase 3: Deprecate _kmeans_sr()

```python
def _kmeans_sr(df: pd.DataFrame, cfg: SRConfig) -> Optional[Tuple[...]]:
    """
    DEPRECATED: Use _agglomerative_sr() instead.
    Kept for backward compatibility and A/B testing.
    """
    import warnings
    warnings.warn("_kmeans_sr is deprecated, use _agglomerative_sr", DeprecationWarning)
    # ... existing implementation ...
```

---

## 5. Testing Plan

### Unit Tests (Before Implementation)

```python
# tests/test_sr_agglomerative.py

def test_zigzag_detects_pivots():
    """ZigZag finds at least 2 pivots in trending data"""

def test_agglom_adapts_cluster_count():
    """Cluster count varies based on data, not fixed"""

def test_merge_percent_respects_threshold():
    """Levels within merge_percent are combined"""

def test_scoring_counts_touches():
    """Higher touch count = higher score"""
```

### Integration Tests

```python
def test_agglom_produces_valid_sr():
    """Full pipeline produces support < price < resistance"""

def test_agglom_handles_ath():
    """ATH stocks still get projected resistance"""

def test_agglom_performance():
    """Process 300 bars in < 100ms"""
```

### A/B Comparison

```python
def compare_kmeans_vs_agglom(tickers: List[str]):
    """
    Run both methods on same data, compare:
    - Number of levels detected
    - Level spacing (are they meaningful?)
    - Match with known S&R from TradingView
    """
```

---

## 6. Rollout Strategy

### Day 30 (Implementation)

1. Add new functions without changing existing flow
2. Add A/B test endpoint: `/api/sr/{ticker}?method=agglom`
3. Test on 5 stocks manually

### Day 31 (Validation)

1. Run A/B comparison on 30 stocks
2. Compare with TradingView S&R levels
3. Measure improvement in detection rate

### Day 32 (Switch)

1. If validation passes, make agglom the default
2. Keep KMeans as deprecated fallback
3. Update API response to include method used

---

## 7. Rollback Plan

If agglomerative performs worse:

```python
# In compute_sr_levels():
USE_AGGLOM = False  # Feature flag

if USE_AGGLOM:
    result = _agglomerative_sr(df, cfg)
else:
    result = _kmeans_sr(df, cfg)
```

---

## 8. Dependencies

### New Dependencies Required

```
# None - already have scikit-learn
# Optional: zigzag library for cleaner implementation
pip install zigzag  # Optional, can implement manually
```

### No Breaking Changes To

- API contracts (same response format)
- Frontend (no changes needed)
- Position sizing (uses same S&R output)

---

## 9. Success Metrics

| Metric | Current | Target | How to Measure |
|--------|---------|--------|----------------|
| Detection Rate | 80% | 87% | Test 30 stocks |
| ATH Success | 45% | 78% | Test 10 ATH stocks |
| Level Accuracy | Unknown | Compare with TV | Manual verification |
| Processing Time | ~50ms | <100ms | Benchmark |

---

## 10. Code Review Checklist

Before merging:

- [ ] All new functions have docstrings
- [ ] Type hints on all parameters
- [ ] Unit tests pass
- [ ] A/B comparison shows improvement
- [ ] No regressions in existing tests
- [ ] Feature flag allows rollback
- [ ] Performance within bounds

---

*Plan created: January 17, 2026*
*Estimated implementation: 2 hours*
*Ready for Day 30 development*
