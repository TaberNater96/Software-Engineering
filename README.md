<div align="center">
  <h2><b>Software Engineering Projects and Challenges<b></h2>
</div>

&nbsp;

<details>
  <summary><b>Click Here To Navigate To Each Repository<b></summary>

  - [Race of the Robots](https://github.com/TaberNater96/Software-Engineering/tree/main/Race%20of%20the%20Robots)
  - [OOP - School Catalogue](https://github.com/TaberNater96/Software-Engineering/tree/main/Advanced%20Operations/OOP%20-%20School%20Catalogue)
  - [Unit Testing - Surfshop](https://github.com/TaberNater96/Software-Engineering/tree/main/Advanced%20Operations/Unit%20Testing%20-%20Surfshop)
  - [Iterator Objects - Student Rosters](https://github.com/TaberNater96/Software-Engineering/tree/main/Advanced%20Operations/Iterator%20Objects%20-%20Student%20Rosters)
  - [Weather API](https://github.com/TaberNater96/Software-Engineering/tree/main/SWE%20Challenges/Weather%20API)
</details>

&nbsp;

This software engineering repository serves as a comprehensive resource for understanding the intricacies of software development and system design. It emphasizes how software engineers play a crucial role in bridging the gap between advanced technological solutions and practical applications, making sophisticated systems accessible and enabling organizations to leverage modern software effectively.

Users exploring this repository are introduced to the techniques used in constructing robust and efficient software systems. The knowledge gained here spans a wide range of software engineering methodologies, from foundational concepts to advanced applications in database design, front-end development, and machine learning integration. This repository aims to guide learners through the development landscape with dynamic processes that delve into the core aspects of software performance and scalability.

The projects featured within this repository highlight best practices in both architectural design and code implementation, establishing a foundation for building scalable database pipelines, intuitive front-end experiences, and high-quality machine learning algorithms. Whether users are interested in the structural elegance of code or the precision of algorithmic efficiency, this repository offers a thorough understanding of software engineering. It combines creative insights with practical, example-driven knowledge, fostering independent exploration and demonstrating the essential role of software engineering in connecting advanced technology with real-world applications.

<div align="center">
  <h2>Quick Summaries (TLDR)</h2>
</div>

## Table of Contents
- [Race of the Robots](#race-of-the-robots)
- [OOP - School Catalogue](#oop-school-catalogue)
- [Unit Testing - Surfshop](#unit-testing-surfshop)
- [Iterator Objects - Student Rosters](#iterator-objects-student-rosters)

&nbsp;

<div id="race-of-the-robots" align="center">
  <h2>Race of the Robots</h2>
</div>

https://github.com/TaberNater96/Software-Engineering/assets/127979108/56ba790a-3e3d-4ecd-95f3-9ab8dd217fb5

![Robot Race Results](https://github.com/TaberNater96/Software-Engineering/assets/127979108/606d7fff-2380-430f-b3aa-8bc86e826496)

This project, assigned by Codecademy, was designed to command, track, and score bots in a relatively simple simulation in which the main goal was to have the bots traverse different mazes to reach a target. However this project takes that concept a step further by turning it into a race and has 6 different bots race against each other and record their performance. The entire concept behind the logic of this project is to demonstrate how dynamic python containers can be, they are much more than objects that can store data. Parameters are defined behind the scenes such as a "#" corresponding to a wall that the bot cannot pass within the given boundaries of the martix. This fully automated algorithm shows how relatively simple code can lead to a program that can learn from past mistakes and ultimately achieve a given goal. This project serves as a foundation for more complex algorithms that can traverse a restricted path of a martix until a path is found and the goal is achieved, making it an invaluable tool in the area of data mining.

<div id="oop-school-catalogue" align="center">
  <h2>OOP - School Catalogue</h2>
</div>

This project involves creating a digital school catalog for the New York City Department of Education to hold quick reference material for each school in the city. It uses Python classes and inheritance to create a parent class `School` and two child classes `PrimarySchool` and `HighSchool`. The `School` class includes properties for `name`, `level`, and `numberOfStudents`, with appropriate getters, a setter for `numberOfStudents`, and a `__repr__()` method for displaying school information. The `PrimarySchool` class adds a `pickupPolicy` property and a corresponding getter, while the `HighSchool` class adds a `sportsTeams` property and its getter, both overriding the `__repr__()` method to include their additional properties. This project showcases how inheritance allows specialized classes to share common properties and methods, making the code more modular and maintainable, serving as a foundation for building complex systems requiring organized data handling.

**Results:**

![OOP Results](https://github.com/TaberNater96/Software-Engineering/assets/127979108/ae042d62-b94e-4112-a64f-b6a9faee2ea4)

<div id="unit-testing-surfshop" align="center">
  <h2>Unit Testing - Surfshop</h2>
</div>

This Python project involves a test suite designed to assess the functionality of a shopping cart system for a surf shop, part of the Codecademy course work. Utilizing the **unittest** framework, it tests key features, including the addition of single and multiple surfboards to the cart, the application of local discounts, and the validation of checkout dates. The tests employ subtests to efficiently check multiple conditions and use exception handling to confirm proper error responses for invalid actions, such as adding too many surfboards or setting an inappropriate checkout date. This ensures that the surf shop's cart system operates correctly and handles various user actions and inputs effectively.

<div id="iterator-objects-student-rosters" align="center">
  <h2>Iterator Objects - Student Rosters</h2>
</div>

This project involves creating a digital school catalog and student roster system with a focus on iterator objects. The catalog includes classes for `School`, `PrimarySchool`, and `HighSchool`, inheriting from the `School` class, which has properties for `name`, `level`, and `numberOfStudents`, with appropriate getters, setters, and a `__repr__()` method. The `PrimarySchool` class adds a `pickupPolicy` property, and the `HighSchool` class includes a `sportsTeams` property, both with getters and overridden `__repr__()` methods. A key component is the `Roster` class, which manages a list of students and allows adding, removing, and iterating through students. By implementing the `__iter__()` and `__next__()` methods, the `Roster` class supports iteration, enabling seamless traversal through the list of students. The project is tested using the `unittest` framework to ensure that all classes and methods, especially the iterator functionality in the `Roster` class, work as expected. This demonstrates how iterator objects can enhance the flexibility and usability of a system designed for managing school and student information.

#### Class Structure and Properties Overview

| **Class**          | **Properties**                                               | **Methods**                                                                                                                                                    |
|--------------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **School**         | `name` (string), `level` (string), `numberOfStudents` (int)  | `get_name()`, `get_level()`, `get_number_of_students()`, `set_number_of_students(number)`, `__repr__()`                                                        |
| **PrimarySchool**  | Inherits `School` properties, `pickupPolicy` (string)        | `get_pickup_policy()`, `__repr__()`                                                                                                                            |
| **HighSchool**     | Inherits `School` properties, `sportsTeams` (list of strings)| `get_sports_teams()`, `__repr__()`                                                                                                                             |
| **Roster**         | `students` (list of strings)                                 | `add_student(student_name)`, `remove_student(student_name)`, `get_students()`, `__repr__()`, `__iter__()`, `__next__()`                                                                               |










