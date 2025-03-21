from datetime import datetime

from project import Project

FILENAME = "projects.txt"

def main():
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    
    while True:
        print("\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n"
              "- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save: ")
            save_projects(projects, filename)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            if input("Would you like to save to projects.txt? (y/n): ").lower() == "y":
                save_projects(projects, "projects.txt")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


def load_projects(filename):
    """Load projects."""
    projects = []
    with open(filename, "r") as file:
        file.readline()
        for line in file:
            parts = line.strip().split("\t")
            projects.append(Project(*parts))
    return projects

def display_projects(projects):
    """Display projects."""
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]
    print("\nIncomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")
    print("\nComplete projects:")
    for project in sorted(complete):
        print(f"  {project}")

def add_project(projects):
    """Add a new project."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))

def update_project(projects):
    """Update a project's completion and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_completion:
        project.completion_percentage = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)


def filter_projects_by_date(projects):
    """Filter projects by start date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > date]
    for project in sorted(filtered, key=lambda x: x.start_date):
        print(project)


def save_projects(projects, filename):
    """Save projects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
            
if __name__ == "__main__":
    main()
