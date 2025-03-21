from project import Project

FILENAME = "projects.txt"

def main():
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")
    display_projects(projects)
    add_project(projects)
    display_projects(projects)


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
    for project in incomplete:
        print(f"  {project}")
    print("\nComplete projects:")
    for project in complete:
        print(f"  {project}")

def add_project(projects):
    """Add a new project."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))


if __name__ == "__main__":
    main()
