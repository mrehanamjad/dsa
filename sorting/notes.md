# Sorting Algorithms

## 🧠 What is **Selection Sort**?

**Selection Sort** is a simple sorting algorithm that sorts an array by **repeatedly selecting the smallest (or largest) element** from the unsorted part and putting it in the correct position in the sorted part.

---

## 🔄 **How it works (Step-by-Step)**

Let’s say we have this array:

```
[5, 2, 8, 1, 3]
```

### Step 1:

* Find the **smallest element** in the entire array → `1`
* Swap it with the **first element**
* Array becomes → `[1, 2, 8, 5, 3]`

### Step 2:

* Now look at the remaining **unsorted part** `[2, 8, 5, 3]`
* Smallest element is `2`
* Swap with itself (no change)
* Array → `[1, 2, 8, 5, 3]`

### Step 3:

* Next unsorted part → `[8, 5, 3]`
* Smallest element is `3`
* Swap with `8`
* Array → `[1, 2, 3, 5, 8]`

Now the array is sorted ✅

---

## ⚙️ **Algorithm (in steps)**

1. Loop from index `0` to `n-1`
2. Assume the current index is the smallest
3. Compare it with the rest of the array
4. If a smaller element is found → update smallest index
5. After inner loop ends → swap smallest element with the current one
6. Repeat until the whole array is sorted

---

## 💻 **Python Code**

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # swap
    return arr

# Example
nums = [5, 2, 8, 1, 3]
print(selection_sort(nums))
```

**Output:**

```
[1, 2, 3, 5, 8]
```

---

## ⏱️ **Complexity Analysis**

| Type               | Complexity | Explanation                        |
| ------------------ | ---------- | ---------------------------------- |
| **Time (Best)**    | O(n²)      | Still compares all pairs           |
| **Time (Worst)**   | O(n²)      | Nested loops                       |
| **Time (Average)** | O(n²)      | Same                               |
| **Space**          | O(1)       | In-place sorting (no extra memory) |
| **Stable?**        | ❌ No       | May change order of equal elements |

---

## ✅ **Key Points**

* Easy to understand and implement.
* Inefficient for large datasets.
* Good for small arrays or when memory usage matters.
* Does fewer swaps than bubble sort.

---

Would you like me to show a **visual step-by-step diagram** of selection sort on a sample array (like `[64, 25, 12, 22, 11]`)?


