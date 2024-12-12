This package warns in case the stack method is called.

#### Case 1
```
import inspect
inspect.stack(*args) # should be a warning here
```

#### Case 2
```
from inspect import stack
stack(*args) # should be a warning here
```

#### Case 3
```
from inspect import stack as my_stack
my_stack(*args) # should be a warning here
```

#### Case 4
```
def stack():
    pass
stack() # should not be a warning here
```

#### Case 5
```
import inspect as foo
foo.stack() # should be a warning here
```

#### Case 6 (not yet handled)
```
from inspect import stack
foo = stack
foo() # should be a warning here
```

### How to use this in other projects
1. Create a file called .pylintrc (in the root directory) and paste this,
```
[MASTER]
load-plugins=pylint_inspect_stack.inspect_stack_checker
```
2. Install the package by running the following command,
```
pip install git+https://github.com/mujeeb91/pylint-inspect-stack.git
```
3. Run pylint
```
pylint script.py
```