# Django-setuptest
import setuptest

class TestSuite(setuptest.setuptest.SetupTestSuite):

    def resolve_packages(self):
        packages = super(TestSuite, self).resolve_packages()
        if 'test_app' not in packages:
            packages.append('test_app')
        return packages
