class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
            return("value must be a string")
        self._value = val

    # -------------------------
    # Sentence-type checkers
    # -------------------------
    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    # -------------------------
    # Count sentences
    # -------------------------
    def count_sentences(self):
        # Replace sentence-ending punctuation with a period
        cleaned = self.value
        for mark in ["!", "?"]:
            cleaned = cleaned.replace(mark, ".")

        # Split on periods
        parts = cleaned.split(".")

        # Filter out empty and whitespace-only parts
        sentences = [p for p in parts if p.strip()]

        return len(sentences)
