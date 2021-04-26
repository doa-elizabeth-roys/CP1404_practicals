from prac_06.programming_language import ProgrammingLanguage

def main():
    """Programming Languages and their details."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby._str_())
    print(python._str_())
    print(visual_basic._str_())



main()
