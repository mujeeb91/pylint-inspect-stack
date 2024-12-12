from pylint.checkers import BaseChecker
import astroid

class InspectStackChecker(BaseChecker):
    """
    A custom Pylint checker to warn when `inspect.stack()` is called.
    """

    name = "inspect-stack-checker"
    msgs = {
        "W0001": (
            "Avoid using `inspect.stack()` as it can have performance implications.",
            "inspect-stack",
            "Warns against using `inspect.stack()`.",
        ),
    }

    def __init__(self, linter=None):
        super().__init__(linter)
        self.aliases = {}  # Initialize aliases as a dictionary

    def visit_import(self, node):
        """
        Track imports like `import inspect` or `import inspect as foo`.
        """
        for name, alias in node.names:
            if name == "inspect":
                self.aliases[alias or name] = name  # Correct dictionary assignment

    def visit_importfrom(self, node):
        """
        Track imports like `from inspect import stack` or `from inspect import stack as foo`.
        """
        if node.modname == "inspect":
            for name, alias in node.names:
                if name == "stack":
                    self.aliases[alias or name] = "stack"  # Correct dictionary assignment

    def visit_call(self, node):
        """
        Check function calls for `inspect.stack()` or aliases like `foo.stack()`.
        """
        if isinstance(node.func, astroid.Attribute):
            # Handle cases like `inspect.stack()` or `foo.stack()`
            if (
                node.func.attrname == "stack"
                and isinstance(node.func.expr, astroid.Name)
                and node.func.expr.name in self.aliases
            ):
                self.add_message("inspect-stack", node=node)

        elif isinstance(node.func, astroid.Name):
            # Handle cases like `stack()` when imported directly
            if node.func.name in self.aliases and self.aliases[node.func.name] == "stack":
                self.add_message("inspect-stack", node=node)

# Register the checker with Pylint
def register(linter):
    linter.register_checker(InspectStackChecker(linter))
