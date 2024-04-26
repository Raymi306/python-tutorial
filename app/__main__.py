"""Module for building and build-time QA of the python tutorial codeblocks"""
import inspect
import json
from os import makedirs
import sys

from app.codeblocks import get_func_body
from app.pages import first_steps, first_projects, variables, classes, error_handling
from app.qa import CodeblocksTester, BuildTestFailure


PAGE_MODULES = (
     first_steps,
     first_projects,
     variables,
     classes,
     error_handling,
)

OUTPUT_DIR = "dist"


def run_build_checks():
    """QA for build process"""
    testers = (CodeblocksTester(PAGE_MODULES),)
    fail = False
    for tester in testers:
        try:
            tester.test()
        except BuildTestFailure:
            fail = True
    if fail:
        sys.exit(1)


def main():
    """
    Perform all of the actions necessary to output the python tutorial codeblocks
    """
    print()
    run_build_checks()
    print()
    makedirs(OUTPUT_DIR, exist_ok=True)
    with open(f'{OUTPUT_DIR}/codeblocks.json', 'w', encoding='utf-8') as f:
        codeblock_map = {}
        for module in PAGE_MODULES:
            nonlocals = getattr(module, "NONLOCALS", ())
            print(f"extracting from {module.__name__}:")
            for member_name, member in inspect.getmembers(module, inspect.isfunction):
                if member_name not in nonlocals:
                    print("    ", member_name)
                    codeblock_map[member_name] = get_func_body(member)
        json.dump(codeblock_map, f)


if __name__ == '__main__':
    main()
