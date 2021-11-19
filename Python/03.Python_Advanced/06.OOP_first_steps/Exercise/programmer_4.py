class Programmer:
    def __init__(self, name, language, skills):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"

        return f"{self.name} does not know {language}"

    def change_language(self, language, skills_needed):
        if self.skills >= skills_needed and self.language != language:
            old_language = self.language
            self.language = language
            return f"{self.name} switched from {old_language} to {self.language}"

        elif self.skills >= skills_needed and self.language == language:
            return f"{self.name} already knows {self.language}"

        return f"{self.name} needs {skills_needed - self.skills} more skills"