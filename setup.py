from setuptools import setup, find_packages

setup(
    name="pylint-inspect-stack",  # Name of your package
    version="0.1.0",  # Initial version
    description="A custom pylint plugin to warn against the usage of inspect.stack().",
    long_description=open("README.md").read(),  # Use the README file for detailed description
    long_description_content_type="text/markdown",  # Specify the README format
    url="https://github.com/mujeeb91/pylint-inspect-stack",  # GitHub repo link
    author="Mujeeb",
    author_email="mujeeb91@hotmail.com",  # Your email address
    license="MIT",
    packages=find_packages(),
    install_requires=["pylint"],
    entry_points={
        "pylint.plugins": [
            "inspect_stack_checker = pylint_inspect_stack.inspect_stack_checker",
        ],
    },
    python_requires=">=3.12",
)
