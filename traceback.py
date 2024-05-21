import sys
import traceback

class CustomError(Exception):
    def __init__(self, message="An error occurred", *args):
        super().__init__(message, *args)
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        return self.notes

    def with_base_traceback(self):
        return self.with_traceback(sys.exc_info()[2])

try:
    raise ValueError
except ValueError:
    c = CustomError()
    c_n = c.add_note("this is a note")
    c_bt = c.with_base_traceback()
    print(c_n, c_bt)
    print(sys.exc_info())
    for _ in range(5):
        try:
            print(sys.exc_info()[_])
        except IndexError:
            continue
