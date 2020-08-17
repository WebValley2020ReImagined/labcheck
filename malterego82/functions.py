def pad(w1: str, w2: str, p: str, times: int = 1) -> str:
    """String padding leveraging on f-strings
    
    Paramenters
    -----------
    w1: str
        First word
    w2: str
        Second word
    p: str
        Padding character or string
        
    Returns
    -------
        The two strings w1 and w2 padded with p
    """
    return f"{w1}{p}{w2}"

