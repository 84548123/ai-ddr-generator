def retrieve_context(db, query):
    return db.similarity_search(query, k=5)