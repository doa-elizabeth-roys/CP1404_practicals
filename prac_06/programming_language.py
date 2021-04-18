class ProgrammingLanguage:
    """Programming Languages Comparison."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True / False if the programming language is dynamically typed or not."""
        return self.typing == "Dynamic"

    def _str_(self):
        """Return a string with following format."""
        return ("{}, {} Typing, Reflection ={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                             self.year))

# Loop through and print the names of all of the languages with dynamic typing
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
