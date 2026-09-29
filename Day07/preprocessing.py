from sentence_transformers import SentenceTransformer
import chromadb
model = SentenceTransformer("all-MiniLM-L6-v2")
with open("ai_simple.txt","r") as file:
    text=file.read()
print(text)
print("No of characters:",len(text))
chunks=[]
chunk_size=25 #20,30,50
chunk_overlap=10 #5,15,30
step=chunk_size-chunk_overlap
for i in range(0,len(text),step):
    chunk=text[i:i+chunk_size] #(0,266,10) text[0:10]
    chunks.append(chunk) #text[10:20]
#print("No of chunks:",len(chunks))
#for i in range(len(chunks)): 
  #  print(f"Chunk{i} -> {chunks[i]}")

#Embeddings
embeddings = model.encode(chunks)
#print("Embeddings created successfully.")
#print("No of embeddinggs:", len(embeddings))
#print(embeddings[0])
print(embeddings.shape)

#Chroma db 
client = chromadb.Client()
collection = client.create_collection(name="My_documents")
print("Collection created successfully")
ids=[]
for i in range(len(chunks)):
    ids.append(str(i))
collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist()
)
print("No of items in the collections:", collection.count())
results = collection.get()
for i in range(len(results["ids"])):
    print(f"ID: {results['ids'][i]} -> Chunk: {results['documents'][i]}")
chunk1 = collection.get(ids=['0'])
print("Chunk 1")