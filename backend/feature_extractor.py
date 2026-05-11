# feature_extractor.py

from urllib.parse import urlparse


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

    # remove empty tokens
    domain_tokens = [token for token in domain.split(".") if token]

    path_tokens = [token for token in path.split("/") if token]

    # top-level domain
    tld = domain.split(".")[-1] if "." in domain else ""

    features = {}

    # =========================================================
    # 1. domain_token_count
    # =========================================================

    features["domain_token_count"] = len(domain_tokens)

    # =========================================================
    # 2. LongestPathTokenLength
    # =========================================================

    features["LongestPathTokenLength"] = longest_token_length(path_tokens)

    # =========================================================
    # 3. argDomanRatio
    # =========================================================

    features["argDomanRatio"] = len(query) / len(domain) if len(domain) > 0 else 0

    # =========================================================
    # 4. domainUrlRatio
    # =========================================================

    features["domainUrlRatio"] = len(domain) / len(url) if len(url) > 0 else 0

    # =========================================================
    # 5. pathDomainRatio
    # =========================================================

    features["pathDomainRatio"] = len(path) / len(domain) if len(domain) > 0 else 0

    # =========================================================
    # 6. domainlength
    # =========================================================

    features["domainlength"] = len(domain)

    # =========================================================
    # 7. SymbolCount_Domain
    # =========================================================

    features["SymbolCount_Domain"] = count_symbols(domain)

    # =========================================================
    # 8. tld
    # =========================================================

    features["tld"] = len(tld)

    # =========================================================
    # 9. pathurlRatio
    # =========================================================

    features["pathurlRatio"] = len(path) / len(url) if len(url) > 0 else 0

    # =========================================================
    # 10. NumberofDotsinURL
    # =========================================================

    features["NumberofDotsinURL"] = url.count(".")

    # =========================================================
    # 11. subDirLen
    # =========================================================

    features["subDirLen"] = sum(len(token) for token in path_tokens)

    # =========================================================
    # 12. host_letter_count
    # =========================================================

    features["host_letter_count"] = count_letters(domain)

    # =========================================================
    # 13. CharacterContinuityRate
    # =========================================================

    features["CharacterContinuityRate"] = character_continuity_rate(url)

    # =========================================================
    # 14. pathLength
    # =========================================================

    features["pathLength"] = len(path)

    # =========================================================
    # 15. urlLen
    # =========================================================

    features["urlLen"] = len(url)

    return features
