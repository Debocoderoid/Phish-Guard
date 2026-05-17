from urllib.parse import urlparse
import re
import ipaddress


suspicious_words = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "banking",
    "confirm"
]

suspicious_tlds = {
    "xyz",
    "top",
    "gq",
    "fit",
    "tk",
    "ml",
    "ga",
    "cf",
    "cc",
    "loan"
}

shorteners = {
    "bit.ly",
    "tinyurl.com",
    "goo.gl"
}


def count_letters(text):
    return sum(c.isalpha() for c in text)


def longest_token_length(tokens):
    if not tokens:
        return 0

    return max(len(token) for token in tokens)


def count_actual_symbols(text, exclude_dots=False):
    if exclude_dots:
        return sum(not c.isalnum() and c != "." for c in text)

    return sum(not c.isalnum() for c in text)


def character_continuity_rate(text):
    if len(text) <= 1:
        return 0

    repeated = sum(
        1 for i in range(1, len(text))
        if text[i] == text[i - 1]
    )

    return repeated / len(text)


def has_ip_address(domain):
    try:
        ipaddress.ip_address(domain)
        return 1

    except:
        return 0


def extract_features(url):

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)

    domain = (
        parsed.netloc
        if parsed.netloc
        else parsed.path.split("/")[0]
    )

    path = (
        parsed.path
        if parsed.netloc
        else "/".join(parsed.path.split("/")[1:])
    )

    query = parsed.query

    domain_tokens = [
        token
        for token in domain.split(".")
        if token
    ]

    path_tokens = [
        token
        for token in path.split("/")
        if token
    ]

    tld = (
        domain.split(".")[-1].lower()
        if "." in domain
        else ""
    )

    features = {}

    features["url_length"] = len(url)
    features["domain_length"] = len(domain)
    features["path_length"] = len(path)

    features["subdir_length"] = sum(
        len(token) for token in path_tokens
    )

    features["domain_token_count"] = len(domain_tokens)

    features["longest_path_token_length"] = longest_token_length(
        path_tokens
    )

    features["dot_count"] = url.count(".")
    features["hyphen_count"] = url.count("-")

    features["host_letter_count"] = count_letters(domain)

    features["arg_domain_ratio"] = (
        len(query) / len(domain)
        if len(domain) > 0
        else 0
    )

    features["domain_url_ratio"] = (
        len(domain) / len(url)
        if len(url) > 0
        else 0
    )

    features["path_domain_ratio"] = (
        len(path) / len(domain)
        if len(domain) > 0
        else 0
    )

    features["path_url_ratio"] = (
        len(path) / len(url)
        if len(url) > 0
        else 0
    )

    features["character_continuity_rate"] = (
        character_continuity_rate(url)
    )

    features["symbol_count_domain"] = (
        count_actual_symbols(domain, exclude_dots=True)
    )

    features["has_login"] = int(
        "login" in url.lower()
    )

    features["has_verify"] = int(
        "verify" in url.lower()
        or "update" in url.lower()
    )

    features["has_at_symbol"] = int(
        "@" in url
    )

    features["has_ip"] = has_ip_address(domain)

    features["is_suspicious_tld"] = int(
        tld in suspicious_tlds
    )

    features["is_secure"] = int(
        url.lower().startswith("https")
    )

    features["digit_count"] = sum(
        c.isdigit() for c in url
    )

    features["subdomain_count"] = max(
        len(domain_tokens) - 2,
        0
    )

    features["uses_shortener"] = int(
        domain in shorteners
    )

    features["suspicious_word_count"] = sum(
        word in url.lower()
        for word in suspicious_words
    )

    return features