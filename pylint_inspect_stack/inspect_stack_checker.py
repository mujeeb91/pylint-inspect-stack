from pylint.checkers import BaseChecker

class InspectStackChecker(BaseChecker):
    # Define the checker class
    name = "inspect-stack-checker"
    priority = -1  # Priority level for the checker
    msgs = {
        "W0001": (
            "Usage of stack() detected. Avoid using it.",
            "inspect-stack-used",
            "Triggered when stack() is found in the code.",
        ),
    }

    def __init__(self, linter=None):
        super().__init__(linter)
        # Tracks aliases of `inspect.stack`
        self.aliases = set()

    def visit_importfrom(self, node):
        """
        Track aliases in 'from inspect import stack as alias' or similar.
        """
        if node.modname == "inspect":
            for name, alias in node.names:
                if name == "stack":
                    # Track alias or name directly if no alias is used
                    self.aliases.add(alias or name)
    
    def visit_call(self, node):
        """
        Check for calls to `stack()` from inspect or any tracked alias.
        """
        try:
            func_name = node.func.as_string()
            if func_name == "inspect.stack" or func_name in self.aliases:
                self.add_message("W0001", node=node)
        except AttributeError:
            pass

# Register the checker with Pylint
def register(linter):
    linter.register_checker(InspectStackChecker(linter))
