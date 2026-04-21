from pyscript import document


class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name.strip()
        self.section = section.strip()
        self.favorite_subject = favorite_subject.strip()

    def introduce(self):
        return f"{self.name} ({self.section}) - {self.favorite_subject}"


# Initial data
classmates = [
    Classmate("Megan Skiendiel", "Bestie 3", "Singer"),
    Classmate("Lola Tung", "Bestie 2", "Actress"),
    Classmate("Hudson Williams", "Madman", "Actor"),
    Classmate("Laufey Jonsdottir", "Madwoman", "Singer"),
    Classmate("Alysa Liu", "Bestie 1", "Figure Skater")
]


def add_classmate(event):
    name_input = document.getElementById("name")
    section_input = document.getElementById("section")
    subject_input = document.getElementById("subject")

    name = name_input.value
    section = section_input.value
    subject = subject_input.value

    if not name or not section or not subject:
        alert("Please fill in all fields!")
        return

    new_student = Classmate(name, section, subject)
    classmates.append(new_student)

    name_input.value = ""
    section_input.value = ""
    subject_input.value = ""

    show_classmates(None)


def show_classmates(event):
    output = document.getElementById("output")
    output.innerHTML = ""

    for student in classmates:
        li = document.createElement("li")
        li.className = "list-group-item"
        li.innerText = student.introduce()
        output.appendChild(li)