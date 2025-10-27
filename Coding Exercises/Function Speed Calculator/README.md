---

# ⏱️ Function Speed Calculator (Python Decorator Example)

This simple Python script demonstrates how to use **decorators** to measure and display the **execution time** of functions. It’s a great example for learning Python’s decorator syntax and how to time code performance.

---

## 📜 Code Overview

The program defines a custom decorator `speed_calc_decorator()` that measures how long a given function takes to run.
It then applies this decorator to two functions — one **fast** and one **slow** — to compare their speeds.

```python
import time
current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970

def speed_calc_decorator(function):
    start = current_time
    function()
    end = time.time()
    diff = end - start
    print(f'{function.__name__} run speed: {diff}s\n')
    return function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()
```

---

## ⚙️ How It Works

1. **`speed_calc_decorator()`**

   * Records the time before and after running the target function.
   * Calculates the difference and prints how long it took.

2. **Decorators (@ syntax)**

   * Used to "wrap" functions, allowing additional behavior (like timing) without modifying the function itself.

3. **Test Functions**

   * `fast_function()` — loops a million times.
   * `slow_function()` — loops ten million times.
   * The output shows that the slow function takes longer.

---

## 🧠 Key Concepts Demonstrated

* **Python Decorators**
* **Function Wrapping**
* **Timing Code Execution**
* **Code Profiling Basics**

---

## 💡 Example Output

```
1730050847.321044  # current Unix timestamp
fast_function run speed: 0.037s

slow_function run speed: 0.338s
```

*(Your exact times will vary depending on your system.)*

---

## 🚀 How to Run

1. Clone this repo:

   ```bash
   git clone https://github.com/your-username/function-speed-decorator.git
   cd function-speed-decorator
   ```

2. Run the script:

   ```bash
   python speed_calculator.py
   ```

---

## 🧩 Possible Improvements

* Fix the decorator to calculate start time **inside** the decorator call instead of using `current_time`.
* Return the function’s result from the decorator.
* Format output times for better readability.

---

## 📚 Learn More

* [Python Decorators — Official Docs](https://docs.python.org/3/glossary.html#term-decorator)
* [Real Python: Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

---
