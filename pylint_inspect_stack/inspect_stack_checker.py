from pylint.checkers import BaseChecker

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

    def visit_call(self, node):
        """
        Check function calls for `stack()`.
        """
        inferred = next(node.func.infer(), None)
        if inferred and inferred.parent.name == "inspect" and inferred.name == "stack":
            self.add_message("inspect-stack", node=node)

# Register the checker with Pylint
def register(linter):
    linter.register_checker(InspectStackChecker(linter))
