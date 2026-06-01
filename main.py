from datetime import datetime

class StudySession:
    def __init__(self):
        self.sessions = []
        self.next_session_id = 1

    def add_session(self, subject, date, duration):
        try:
            # Validate date format (YYYY-MM-DD)
            datetime.strptime(date, "%Y-%m-%d")
            session = {
                "sessionID": self.next_session_id,
                "subject": subject.strip(),
                "duration": int(duration),
                "date": date
            }
            if not all([session["subject"], session["duration"] > 0]):
                return False, "Invalid subject or duration (must be positive number)"
            self.sessions.append(session)
            self.next_session_id += 1
            return True, f"Session added successfully! Session ID: {session['sessionID']}"
        except ValueError as e:
            return False, f"Validation error: {str(e)}. Date must be YYYY-MM-DD and duration an integer"

    def view_session(self, session_id=None):
        if not self.sessions:
            return False, "No study sessions recorded yet"
        if session_id:
            for sess in self.sessions:
                if sess["sessionID"] == session_id:
                    return True, (f"Session Details:\nID: {sess['sessionID']}\nSubject: {sess['subject']}\n"
                                  f"Duration (mins): {sess['duration']}\nDate: {sess['date']}")
            return False, "Session ID not found"
        else:
            output = "All Study Sessions:\n"
            for sess in self.sessions:
                output += f"ID: {sess['sessionID']} | Subject: {sess['subject']} | Date: {sess['date']}\n"
            return True, output

    def edit_session(self, session_id, new_subject=None, new_date=None, new_duration=None):
        for sess in self.sessions:
            if sess["sessionID"] == session_id:
                try:
                    if new_subject:
                        sess["subject"] = new_subject.strip()
                    if new_date:
                        datetime.strptime(new_date, "%Y-%m-%d")
                        sess["date"] = new_date
                    if new_duration:
                        sess["duration"] = int(new_duration)
                        if sess["duration"] <= 0:
                            return False, "Duration must be a positive integer"
                    return True, "Session updated successfully"
                except ValueError as e:
                    return False, f"Invalid input: {str(e)}. Date format YYYY-MM-DD"
        return False, "Session ID not found"

    def get_session_by_id(self, session_id):
        for sess in self.sessions:
            if sess["sessionID"] == session_id:
                return sess
        return None


class Deliverable:
    def __init__(self, study_session):
        self.deliverables = []
        self.next_deliverable_id = 1
        self.study_session = study_session  # Link to StudySession class

    def add_deliverable(self, session_id, task_name, submission_date, status):
        session = self.study_session.get_session_by_id(session_id)
        if not session:
            return False, "Associated study session not found"
        try:
            datetime.strptime(submission_date, "%Y-%m-%d")
            deliverable = {
                "deliverableID": self.next_deliverable_id,
                "sessionID": session_id,
                "taskName": task_name.strip(),
                "submissionDate": submission_date,
                "status": status.strip().capitalize()
            }
            if not all([deliverable["taskName"], deliverable["status"]]):
                return False, "Task name and status cannot be empty"
            self.deliverables.append(deliverable)
            self.next_deliverable_id += 1
            return True, f"Deliverable added! ID: {deliverable['deliverableID']}"
        except ValueError as e:
            return False, f"Validation error: {str(e)}. Date format YYYY-MM-DD"

    def update_status(self, deliverable_id, new_status):
        for deliv in self.deliverables:
            if deliv["deliverableID"] == deliverable_id:
                deliv["status"] = new_status.strip().capitalize()
                return True, "Deliverable status updated"
        return False, "Deliverable ID not found"

    def view_deliverable(self, session_id=None):
        if not self.deliverables:
            return False, "No deliverables recorded yet"
        if session_id:
            output = f"Deliverables for Session ID {session_id}:\n"
            found = False
            for deliv in self.deliverables:
                if deliv["sessionID"] == session_id:
                    output += (f"ID: {deliv['deliverableID']} | Task: {deliv['taskName']}\n"
                               f"Submission Date: {deliv['submissionDate']} | Status: {deliv['status']}\n")
                    found = True
            return (True, output) if found else (False, "No deliverables found for this session ID")
        else:
            output = "All Deliverables:\n"
            for deliv in self.deliverables:
                output += (f"ID: {deliv['deliverableID']} | Session ID: {deliv['sessionID']} | Task: {deliv['taskName']}\n"
                           f"Submission Date: {deliv['submissionDate']} | Status: {deliv['status']}\n")
            return True, output


class ProgressTracker:
    def __init__(self, study_session, deliverable):
        self.progress_records = []
        self.study_session = study_session
        self.deliverable = deliverable

    def calculate_progress(self, topic_name):
        # Get all sessions and deliverables related to the topic/subject
        related_sessions = [s for s in self.study_session.sessions if s["subject"].lower() == topic_name.lower()]
        if not related_sessions:
            return False, "No sessions found for this topic/subject"
        related_delivs = [d for d in self.deliverable.deliverables if any(s["sessionID"] == d["sessionID"] for s in related_sessions)]
        total_delivs = len(related_delivs)
        completed_delivs = len([d for d in related_delivs if d["status"].lower() == "completed"])
        progress_percent = (completed_delivs / total_delivs) * 100 if total_delivs > 0 else 0.0
        completion_status = "Completed" if progress_percent == 100 else "In Progress" if progress_percent > 0 else "Not Started"
        
        # Save or update progress record
        existing = next((p for p in self.progress_records if p["topicName"].lower() == topic_name.lower()), None)
        if existing:
            existing["progressPercentage"] = round(progress_percent, 2)
            existing["completionStatus"] = completion_status
        else:
            self.progress_records.append({
                "topicName": topic_name.strip().capitalize(),
                "progressPercentage": round(progress_percent, 2),
                "completionStatus": completion_status
            })
        return True, (progress_percent, completion_status, total_delivs, completed_delivs)

    def update_progress(self, topic_name, new_percent=None, new_status=None):
        record = next((p for p in self.progress_records if p["topicName"].lower() == topic_name.lower()), None)
        if not record:
            return False, "No progress record found for this topic"
        try:
            if new_percent is not None:
                new_percent = float(new_percent)
                if not 0 <= new_percent <= 100:
                    return False, "Progress percentage must be between 0 and 100"
                record["progressPercentage"] = round(new_percent, 2)
            if new_status:
                record["completionStatus"] = new_status.strip().capitalize()
            return True, "Progress record updated"
        except ValueError:
            return False, "Progress percentage must be a number"

    def generate_report(self, topic_name=None):
        if not self.progress_records:
            return False, "No progress records available to generate report"
        if topic_name:
            record = next((p for p in self.progress_records if p["topicName"].lower() == topic_name.lower()), None)
            if not record:
                return False, "Topic not found in progress records"
            report = f"PROGRESS REPORT - {record['topicName']}\n"
            report += f"Progress Percentage: {record['progressPercentage']}%\n"
            report += f"Completion Status: {record['completionStatus']}\n"
            return True, report
        else:
            report = "OVERALL PROGRESS REPORT\n"
            for rec in self.progress_records:
                report += f"\nTopic: {rec['topicName']}\n"
                report += f"Progress: {rec['progressPercentage']}%\n"
                report += f"Status: {rec['completionStatus']}\n"
            return True, report


# Interactive Console Interface
def main():
    print(" ==============STUDY SESSION TRACKER=============== ")
    
    # Initialize system components
    study_sess = StudySession()
    deliverable = Deliverable(study_sess)
    progress_tracker = ProgressTracker(study_sess, deliverable)

    while True:
        print("1. Track Study Session ")
        print("2. Input Session Deliverable")
        print("3. Track Progress per Topic ")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            print("\n--- TRACK STUDY SESSION ---")
            sub_choice = input("Select action:\n1. Add New Session\n2. View Sessions\n3. Edit Session\nEnter choice (1-3): ").strip()
            if sub_choice == "1":
                subject = input("Enter subject/topic: ")
                date = input("Enter session date (YYYY-MM-DD): ")
                duration = input("Enter session duration (minutes): ")
                success, msg = study_sess.add_session(subject, date, duration)
                print(f"\n{'SUCCESS:' if success else 'ERROR:'} {msg}")
            elif sub_choice == "2":
                sess_id = input("Enter session ID to view (leave blank for all): ").strip()
                sess_id = int(sess_id) if sess_id else None
                success, msg = study_sess.view_session(sess_id)
                print(f"\n{'RESULTS:' if success else 'ERROR:'} {msg}")
            elif sub_choice == "3":
                sess_id = input("Enter session ID to edit: ").strip()
                if not sess_id.isdigit():
                    print("ERROR: Session ID must be a number")
                    continue
                sess_id = int(sess_id)
                new_sub = input("Enter new subject (leave blank to keep current): ")
                new_date = input("Enter new date (YYYY-MM-DD, leave blank to keep current): ")
                new_dur = input("Enter new duration (minutes, leave blank to keep current): ")
                success, msg = study_sess.edit_session(sess_id, new_sub or None, new_date or None, new_dur or None)
                print(f"\n{'SUCCESS:' if success else 'ERROR:'} {msg}")
            else:
                print("Invalid sub-choice. Please try again.")

        elif choice == "2":
            print("\n--- INPUT SESSION DELIVERABLE ---")
            sub_choice = input("Select action:\n1. Add New Deliverable\n2. Update Deliverable Status\n3. View Deliverables\nEnter choice (1-3): ").strip()
            if sub_choice == "1":
                sess_id = input("Enter associated session ID: ").strip()
                if not sess_id.isdigit():
                    print("ERROR: Session ID must be a number")
                    continue
                sess_id = int(sess_id)
                task = input("Enter task name/description: ")
                sub_date = input("Enter submission date (YYYY-MM-DD): ")
                status = input("Enter current status (e.g., Pending, Completed): ")
                success, msg = deliverable.add_deliverable(sess_id, task, sub_date, status)
                print(f"\n{'SUCCESS:' if success else 'ERROR:'} {msg}")
            elif sub_choice == "2":
                deliv_id = input("Enter deliverable ID to update: ").strip()
                if not deliv_id.isdigit():
                    print("ERROR: Deliverable ID must be a number")
                    continue
                deliv_id = int(deliv_id)
                new_status = input("Enter new status: ")
                success, msg = deliverable.update_status(deliv_id, new_status)
                print(f"\n{'SUCCESS:' if success else 'ERROR:'} {msg}")
            elif sub_choice == "3":
                sess_id = input("Enter session ID to view deliverables (leave blank for all): ").strip()
                sess_id = int(sess_id) if sess_id.isdigit() else None
                success, msg = deliverable.view_deliverable(sess_id)
                print(f"\n{'RESULTS:' if success else 'ERROR:'} {msg}")
            else:
                print("Invalid sub-choice. Please try again.")

        elif choice == "3":
            print("\n--- PROGRESS TRACKING PER TOPIC ---")
            sub_choice = input("Select action:\n1. Calculate Progress\n2. Update Progress\n3. Generate Report\nEnter choice (1-3): ").strip()
            if sub_choice == "1":
                topic = input("Enter topic/subject to calculate progress: ")
                success, data = progress_tracker.calculate_progress(topic)
                if success:
                    percent, status, total, completed = data
                    print(f"\nPROGRESS FOR {topic.upper()}:")
                    print(f"Total Deliverables: {total} | Completed: {completed}")
                    print(f"Progress Percentage: {round(percent, 2)}%")
                    print(f"Completion Status: {status}")
                else:
                    print(f"ERROR: {data}")
            elif sub_choice == "2":
                topic = input("Enter topic to update progress: ")
                new_percent = input("Enter new progress percentage (0-100, leave blank to skip): ").strip()
                new_status = input("Enter new completion status (leave blank to skip): ")
                success, msg = progress_tracker.update_progress(topic, new_percent or None, new_status or None)
                print(f"\n{'SUCCESS:' if success else 'ERROR:'} {msg}")
            elif sub_choice == "3":
                topic = input("Enter topic for report (leave blank for overall report): ").strip()
                success, report = progress_tracker.generate_report(topic or None)
                print(f"\n{'--- REPORT ---' if success else 'ERROR:'}")
                print(report)
            else:
                print("Invalid sub-choice. Please try again.")

        elif choice == "4":
            print("\nThank you!  youre success.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
