import pytest
from pypi_domains_extractor.main import getPypiDomains

def test_getPypiDomains_length():
    domains = getPypiDomains()
    assert len(domains) == 2

def test_getPypiDomains_contains_pypi():
    domains = getPypiDomains()
    assert "https://pypi.org/" in domains

def test_getPypiDomains_contains_test_pypi():
    domains = getPypiDomains()
    assert "https://test.pypi.org/" in domains
