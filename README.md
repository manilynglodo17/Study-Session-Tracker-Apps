 Study Session Tracker Apps

Study Session Tracker is a standalone Python application designed to help students efficiently organize their study sessions, track learning deliverables, and monitor academic progress per topic in one centralized system.


The application allows users to:

•Create and manage study sessions, including logging subject, topic, date, and duration.

•Attach deliverables (assignments, outputs, readings) to each study session and mark them as completed.

•Store and manage short notes or reminders related to each study session

•View a summarized progress report per topic that presents all sessions and deliverables in a structured format. The report can be exported to a .txt file.

Built with a clean command-line interface, the system emphasizes simplicity, usability, and accessibility. It operates entirely offline and follows a structured Input → Process → Output model, ensuring reliable performance without relying on external databases or internet connectivity.

Through this application, students can improve their time management, maintain study consistency, and increase academic efficiency by having all essential tracking tools in a single, easy-to-use platform.

OOP Concepts Used

This project demonstrates core Object-Oriented Programming principles:

•Encapsulation: Private attributes using _variable naming convention inside Study Session, Deliverable, and Progress Tracker classes.

•Abstraction: IOutputWriter and IInputReader interfaces define standard methods for input and output handling.

•Polymorphism: Screen Display and LogFileWriter both implement IOutputWriter, allowing the app to switch output targets without changing core logic.

•Modularity: Code is separated into models, services, interfaces, and tests folders for clean structure and maintainability.

Technologies Used

•Python (core programming language)

•Command-Line Interface (CLI) for user interaction

•File handling for saving and exporting session reports to .txt




 Project Structure

```
StudySessionTracker/
│
├── interfaces/
│   └── data_service.py
│
├── models/
│   └── session.py
│   └── deliverable.py
│   └── progress_tracker.py
│
├── services/
│   └── session_service.py
│   └── deliverable_service.py
│   └── progress_service.py
│
├── tests/
│   └── test_services.py
│
├── main.py
└── README.md
```

How to Run the Application

1.Clone the repository:
Git clone https://github.com/[RepositoryLink]
Cd StudySessionTracker
2.Run the application:
Python main.py
1.Run the testst
Py -m pytest -v

Features

•Feature 1 – Track Study Session

Allows students to log a study session by entering the subject, topic, date, start time, and end time. The system automatically calculates the total duration and saves the session record.

•Feature 2 – Input Session Deliverable

Allows students to attach a specific task, assignment, or output to a saved session. Students can set a due date and update the deliverable status to Completed when finished.

•Feature 3 – Progress Tracking by Topic

Aggregates all sessions and deliverables under a topic and displays a percentage-based progress report with a visual progress bar. The report can be exported to a .txt file.


 Authors

Golde, Elaysa L. — Project Lead, UI/UX Designer, Documentation Writer

GitHub: https://github.com/[GoldeGitHubUsername]

Glodo, Manilyn— Lead Developer, Database Manager

GitHub:https://github.com/manilynglodo17
Repository Link

https://github.com/[RepositoryLink]
 



