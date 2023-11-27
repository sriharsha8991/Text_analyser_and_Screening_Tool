import yake
# Initialize YAKE keyword extractor
kw_extractor = yake.KeywordExtractor()

def extract_keywords(text, max_num_keywords=3):
    yake_extractor = yake.KeywordExtractor(top=max_num_keywords)
    keywords = yake_extractor.extract_keywords(text)
    return ", ".join([kw for kw, _ in keywords])