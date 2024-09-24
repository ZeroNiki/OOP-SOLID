# OOP Tasks for Junior python (With solid)

[RU README](https://github.com/ZeroNiki/OOP-SOLID/blob/main/README_RU.md)

This is a repository for solving OOP problems following the SOLID principles

## Install

Clone repository:

```bash
git clone https://github.com/ZeroNiki/OOP-SOLID.git

cd OOP-SOLID
```

## Usage

See output

```bash
python start.py
```

Usage Example in `src/main.py`

## OOP

Sure! Let’s explore the principles of OOP using just one example: **Task Management**.

### Example: Task Management

We'll define a simple task management system where we can create tasks and manage them.

#### 1. Encapsulation

**Definition:** Encapsulation is the mechanism of hiding the internal state of an object and providing methods to interact with it.

**Code Example:**
The `Task` class encapsulates properties of a task, such as `title`, `description`, and `status`, and provides methods to interact with these properties.

```python
class Task:
    def __init__(self, title, description, status="open"):
        self._title = title
        self._description = description
        self._status = status  # Status can be changed through a method

    def mark_as_completed(self):
        self._status = "completed"
```

**Explanation:** Here, the internal attributes of the task are prefixed with an underscore (e.g., `_title`, `_status`), indicating that they should not be accessed directly from outside the class. Instead, methods like `mark_as_completed` are provided to modify the status safely.

#### 2. Inheritance

**Definition:** Inheritance allows creating a new class based on an existing class, inheriting its properties and methods.

**Code Example:**
We can create subclasses for different types of tasks, such as `UrgentTask`, which inherits from `Task`.

```python
class UrgentTask(Task):
    def __init__(self, title, description):
        super().__init__(title, description, status="urgent")
```

**Explanation:** The `UrgentTask` class extends the `Task` class, adding a specific type of task without duplicating the code. It inherits the `mark_as_completed` method and any other functionality defined in the `Task` class.

#### 3. Polymorphism

**Definition:** Polymorphism allows using different classes through a single interface.

**Code Example:**
We can create a function that displays a task, which can accept both `Task` and `UrgentTask` objects.

```python
def display_task(task: Task):
    print(f"Title: {task._title}, Status: {task._status}")
```

**Explanation:** The `display_task` function can accept any object of type `Task` or its subclasses, allowing for flexibility in how tasks are represented and displayed. This is useful for handling different task types without needing to know their specific class.

#### 4. Abstraction

**Definition:** Abstraction allows highlighting important characteristics of an object while hiding unnecessary details.

**Code Example:**
The `TaskManager` class can manage tasks without needing to know the details of each task's implementation.

```python
class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, task: Task):
        self._tasks.append(task)

    def display_all_tasks(self):
        for task in self._tasks:
            display_task(task)
```

**Explanation:** The `TaskManager` class provides a high-level interface for managing tasks, such as adding and displaying them, without exposing the internal details of how tasks are stored or manipulated. This helps users of `TaskManager` focus on its functionality rather than the implementation of tasks.

## SOLID

The SOLID principles are a set of five fundamental principles of object-oriented design that help create more understandable, flexible, and maintainable systems. Let's look at each of these principles using examples from the above tasks.

### 1. S - Single Responsibility Principle

**Definition:** Each class should have only one responsibility, and that responsibility should be completely encapsulated within the class.

**Example:**
In the task management task, the `Task` class is responsible only for representing a task, while the `TaskManager` class is responsible for managing a collection of tasks. This way, if the way we want to manage tasks changes (e.g. adding more operations), we can change the `TaskManager` without affecting the `Task`.

```python
class Task:
  def __init__(self, title, description, status="open", due_date=None):
    self.title = title
    self.description = description
    self.status = status
    self.due_date = due_date

class TaskManager:
  def __init__(self):
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)
```

### 2. O — Open/Closed Principle

**Definition:** Classes should be open for extension, but closed for modification.

**Example:**
In calculator, if we want to add new operations (like exponentiation), we can create a new class `Power` that inherits from `Operation` without changing the code of `Calculator` class itself.

```python
class Power(Operation):
  def execute(self, a, b):
    return a ** b

class Calculator:
  def __init__(self):
    self.operations = {
      '+': Add(),
      '-': Subtract(),
      '*': Multiply(),
      '/': Divide(),
      '**': Power() # New operation
    }
```

### 3. L — Liskov Substitution Principle

**Definition:** Objects of a subclass should be interchangeable with objects of a superclass without changing the desired properties of the program.

**Example:**
In calculator, all operations (e.g. `Add`, `Subtract`, `Multiply`, `Divide`) implement the `Operation` interface. This allows you to use any operations in the `Calculator` class without checking which operation is passed.

```python
class Operation:
  def execute(self, a, b):
    raise NotImplementedError

class Add(Operation):
  def execute(self, a, b):
    return a + b
```

### 4. I — Interface Segregation Principle

**Definition:** Clients should not depend on interfaces they do not use.

**Example:**
Let's imagine that in the user management task we create different interfaces for user management, such as `UserCreation`, `UserRetrieval`, etc. This will avoid situations where a class implementing one interface is forced to implement unnecessary methods.

```python
class UserCreation:
  def create_user(self, name, email):
    pass

class UserRetrieval:
  def get_user(self, user_id):
    pass
```

### 5. D — Dependency Inversion Principle

**Definition:** Top-level modules should not depend on lower-level modules. Both types of modules should depend on abstractions.

**Example:**
In an order management system, `OrderManager` might depend on an abstraction representing the source of order storage (such as a database or file system), rather than on the concrete class implementing that storage.

```python
class OrderRepository:
  def save_order(self, order):
    pass

class OrderManager:
  def __init__(self, repository: OrderRepository):
    self.repository = repository

def add_order(self, order):
  self.repository.save_order(order)
```
