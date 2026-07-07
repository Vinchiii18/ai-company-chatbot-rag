from app.services.knowledge_base_service import knowledge_base_service


def main():
    # Load the saved knowledge base
    knowledge_base_service.load(
        "knowledge/employee_handbook.json"
    )

    # Get all chunks
    chunks = knowledge_base_service.get_chunks()

    print(f"\nLoaded {len(chunks)} chunks.\n")

    # Print a preview of each chunk
    for index, chunk in enumerate(chunks, start=1):
        print("=" * 80)
        print(f"Chunk #{index}")
        print(chunk.text[:300])
        print()


if __name__ == "__main__":
    main()