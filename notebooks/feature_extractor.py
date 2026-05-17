from urllib.parse import urlparse
import re

def count_letters(text):
    """
    Count alphabetic characters.
    """
    return sum(c.isalpha() for c in text)


def longest_token_length(tokens):
    """
    Find longest token length in list.
    """
    if not tokens:
        return 0

    return max(len(token) for token in tokens)


def count_symbols(text):
    """
    Count non-alphanumeric characters.
    """
    return sum(not c.isalnum() for c in text)


def character_continuity_rate(text):
    """
    Approximation of CharacterContinuityRate.

    Measures repeated consecutive characters.
    """

    if len(text) <= 1:
        return 0

    repeated = 0

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            repeated += 1

    return repeated / len(text)


def extract_features(url):
    """
    Extract ONLY the 15 selected features
    used during retraining.
    """

    parsed = urlparse(url)

    domain = parsed.netloc
    path = parsed.path
    query = parsed.query

    domain_tokens = [token for token in domain.split(".") if token]

    path_tokens = [token for token in path.split("/") if token]

    tld = domain.split(".")[-1] if "." in domain else ""

    features = {}

    features["domain_token_count"] = len(domain_tokens)

    features["LongestPathTokenLength"] = longest_token_length(path_tokens)

    features["argDomanRatio"] = len(query) / len(domain) if len(domain) > 0 else 0

    features["domainUrlRatio"] = len(domain) / len(url) if len(url) > 0 else 0

    features["pathDomainRatio"] = len(path) / len(domain) if len(domain) > 0 else 0

    features["domainlength"] = len(domain)

    features["SymbolCount_Domain"] = count_symbols(domain)

    features["tld"] = len(tld)

    features["pathurlRatio"] = len(path) / len(url) if len(url) > 0 else 0

    features["NumberofDotsinURL"] = url.count(".")

    features["subDirLen"] = sum(len(token) for token in path_tokens)

    features["host_letter_count"] = count_letters(domain)

    features["CharacterContinuityRate"] = character_continuity_rate(url)

    features["pathLength"] = len(path)

    features["urlLen"] = len(url)
    
    features["has_login"] = int("login" in url.lower())
    
    features["has_verify"] = int("verify" in url.lower())
    
    features["hyphen_count"] = url.count("-")
    
    features["has_ip"] = int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)))

    return features