def chunk_text(pages, chunk_size=500):
    chunks = []

    for page in pages:

        # ✅ Handle dictionary case
        if isinstance(page, dict):
            text = page.get("text", "")

        # ✅ Handle string case
        elif isinstance(page, str):
            text = page

        # ✅ Handle list case (important fix)
        elif isinstance(page, list):
            text = " ".join([str(p) for p in page])

        else:
            text = str(page)

        # Split into chunks
        for i in range(0, len(text), chunk_size):
            chunks.append(text[i:i + chunk_size])

    return chunks