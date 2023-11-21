import os
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

BOT_NAME = os.environ["BOT_NAME"]


def construct_index(directory_data, directory_index, force_reload=False):
    # check if storage already exists
    if not os.path.exists(directory_index) or force_reload:
        print(f'Creating new index using {directory_data}')
        # load the documents and create the index
        documents = SimpleDirectoryReader(directory_data).load_data()
        index = VectorStoreIndex.from_documents(documents)
        # store it for later
        index.storage_context.persist(persist_dir=directory_index)
        print(f'Storing new index to {directory_index}')
    else:
        # load the existing index
        print(f'Loading existing index from {directory_index}')
        storage_context = StorageContext.from_defaults(persist_dir=directory_index)
        index = load_index_from_storage(storage_context)
    
    return index

def query(question, index):
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    return response

def ask(bot_name):
    index = construct_index(directory_data=f'data/{bot_name}', directory_index=f'storage/{bot_name}')
    while True:
        question = input("What do you want to know?")
        response = query(question=question, index=index)
        print(f"{bot_name} says: {response}")

if __name__ == '__main__':
    ask(BOT_NAME)