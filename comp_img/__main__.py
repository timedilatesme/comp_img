from . import BaseClass, base_function  # pragma: no cover


def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m comp_img` and `$ comp_img `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    print("Executing main function")
    base = BaseClass()
    print(base.base_method())
    print(base_function())
    print("End of main function")


if __name__ == "__main__":  # pragma: no cover
    main()
