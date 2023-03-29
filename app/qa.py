"""Testers and test helpers for QA of tutorial"""
from abc import ABC, abstractmethod
import asyncio
from dataclasses import dataclass, field
import doctest

import aiohttp


class BuildTestFailure(BaseException):
    """Custom exception to indicate a build test failure"""


@dataclass(frozen=True)
class BuildTestResult:
    """Helper class to represent a build test result"""
    passed: bool
    output: list[str] = field(default_factory=list)


# pylint: disable=too-few-public-methods
class BuildTest(ABC):
    """Abstract class to build tests upon"""
    name = ''

    @abstractmethod
    def _test(self):
        """
        Children implement me
        Perform actions to ensure quality of tutorial
        """
        raise NotImplementedError

    def test(self):
        """Universal test logic"""
        test_result = self._test()
        print(f'\nTesting {self.name or self}')

        if not test_result.passed:  # only take action on failures
            print('  - Fail!')
            if test_result.output:
                print('Output:')
                for line in test_result.output:
                    print(f'  {line}')
            raise BuildTestFailure()
        print('  - Pass')


class CodeblocksTester(BuildTest):
    """Make sure the templated codeblocks do what the tutorial claims"""
    name = 'Codeblocks'

    def _test(self):
        from app.templates import codeblocks  # pylint: disable=import-outside-toplevel
        failure_count, _ = doctest.testmod(
                codeblocks,
                verbose=None,
                report=False
                )
        return BuildTestResult(not bool(failure_count))


class LinkTester(BuildTest):
    """Make sure all templated links are alive"""

    name = 'Links'
    def __init__(self, concurrency=16, ignore_internal_links=False):
        """
        Semaphore limits number of concurrent requests for performance
        Is still nonblocking"""
        self.concurrency = concurrency
        self.ignore_internal_links = ignore_internal_links

    @staticmethod
    async def fetch(session, url, lock):
        """Locked async HTTP GET"""
        async with lock:
            return await session.get(url)

    async def get_failures(self, links):
        """
        Send GET requests for link in links, return responses of requests
        which do not return 200 OK.
        """
        async with aiohttp.ClientSession() as session:
            lock = asyncio.Semaphore(self.concurrency)
            responses = await asyncio.gather(
                *[self.fetch(session, url, lock) for url in links]
            )
            failures = [r for r in responses if r.status != 200]
            return failures

    def _test(self):
        from app.templates.links import links  # pylint: disable=import-outside-toplevel

        def strip_fragment_identifiers(link):
            return link.split('#')[0]

        if self.ignore_internal_links:
            links = set(
                strip_fragment_identifiers(link) for template_var, link in links.items()
                if not template_var.startswith('int')
            )
        else:
            links = set(strip_fragment_identifiers(link) for link in links.values())

        fails = asyncio.run(self.get_failures(links))
        return BuildTestResult(
            not bool(fails),
            [f'{fail.url}: {fail.status}' for fail in fails]
        )


class UnresolvedTemplateVariablesTester(BuildTest):
    """Make sure all variables in the template have a match in context"""
    name = 'Unresolved Variables'

    def __init__(self, env, ctx):
        self.env = env
        self.ctx = ctx
        super().__init__()

    def _test(self):
        # pylint: disable=import-outside-toplevel
        from jinja2 import meta

        from app.templates import TEMPLATES
        # pylint: enable=import-outside-toplevel

        passed = True
        output = []
        for template in TEMPLATES:
            ast = self.env.parse(self.env.get_template(template).render())
            vars_in_template = meta.find_undeclared_variables(ast)
            if mismatch := vars_in_template.difference(set(self.ctx.keys())):
                passed = False
                output.append(f'{template}: {mismatch}')
        return BuildTestResult(passed, output)
# pylint: enable=too-few-public-methods
