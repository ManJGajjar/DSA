# 01 — Sorting Algorithms

Sorting is the foundation. Every major algorithm course starts here because it teaches you to think about **comparisons, swaps, recursion, and divide-and-conquer** — patterns that appear everywhere.

---

## Algorithms Covered

| File | Algorithm | Time (avg) | Space | Stable? |
|------|-----------|------------|-------|---------|
| `bubble_sort.py` | Bubble Sort | O(n²) | O(1) | ✅ Yes |
| `selection_sort.py` | Selection Sort | O(n²) | O(1) | ❌ No |
| `insertion_sort.py` | Insertion Sort | O(n²) | O(1) | ✅ Yes |
| `merge_sort.py` | Merge Sort | O(n log n) | O(n) | ✅ Yes |
| `quick_sort.py` | Quick Sort | O(n log n) | O(log n) | ❌ No |

---

## Visual Intuition

### Bubble Sort
Repeatedly compares adjacent elements and swaps them if out of order.
The largest element "bubbles up" to the end each pass.

```
Pass 1:  [5, 3, 8, 1] → [3, 5, 1, 8]
Pass 2:  [3, 5, 1, 8] → [3, 1, 5, 8]
Pass 3:  [3, 1, 5, 8] → [1, 3, 5, 8]  ✓
```

### Merge Sort
Divide the array in half repeatedly until single elements,
then merge sorted halves back together.

```
        [38, 27, 43, 3]
       /               \
  [38, 27]           [43, 3]
  /      \           /     \
[38]    [27]       [43]    [3]
  \      /           \     /
  [27, 38]           [3, 43]
       \               /
        [3, 27, 38, 43]  ✓
```

### Quick Sort
Pick a pivot. Put smaller elements left, larger right. Recurse.

```
pivot = 3
[3, 6, 8, 10, 1, 2, 1]
 ↓
[1, 2, 1] | [3] | [6, 8, 10]
    ↓                ↓
 sorted           sorted
```

---

## Key Takeaways

- **Use Insertion Sort** for nearly-sorted small arrays — it's O(n) best case
- **Use Merge Sort** when you need guaranteed O(n log n) and stability matters
- **Use Quick Sort** in practice — fastest in-place sort on average, used by most standard libraries
- Never use Bubble/Selection in production — they exist to teach comparison logic
