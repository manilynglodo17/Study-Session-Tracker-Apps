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
## How to Run
1. Requirements
Python 3.x
2. Clone this repository:
   ```bash
   git clone https://github.com/chvzdn/dally.git

## Navigate to the project folder:
  ```bash
  cd Study Session Tracker 
  ```

Run the Application:
  ```bash
  python main.py
  ```

Running Tests
Run automated tests using pytest: 
```bash
py -m pytest -v
```
Or run all tests in the tests folder:
```bash
pytest tests/
```

 Export Report
Inside the application:
1. Go to the Report tab
2. Click Export Report
3. Output file will be saved as:
```
report.txt
```

Author 
Developed as a school project by:
Manilyn Glodo ([GitHub Profile of Glodo](https://github.com/chvzdn))
Elaysa Golde ([GitHub Profile of elaysa](

In Partial Fulfillment of the Requirements for the Subject CC103 Computer Programming 2 Under the Course of Bachelor of Science in Information Technology at Sorsogon State University Bulan Campus. With the Supervision of our Professor John Mark Gabrentina.



Features

•Feature 1 – Track Study Session

Allows students to log a study session by entering the subject, topic, date, start time, and end time. The system automatically calculates the total duration and saves the session record.

•Feature 2 – Input Session Deliverable

Allows students to attach a specific task, assignment, or output to a saved session. Students can set a due date and update the deliverable status to Completed when finished.

•Feature 3 – Progress Tracking by Topic

Aggregates all sessions and deliverables under a topic and displays a percentage-based progress report with a 



