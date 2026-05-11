from urllib.parse import urlparse


def extract_features(url):
    features = {}

    features["url_length"] = len(url)

    features["dot_count"] = url.count(".")

    features["has_https"] = 1 if url.startswith("https") else 0

    features["has_at_symbol"] = 1 if "@" in url else 0

    return features
