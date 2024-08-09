import os
import csv
import re


def get_markdown_files(directory):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files


def extract_concept_blocks(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        concept_blocks = re.findall(
            r"---\s*\*\*_[Cc]oncept_\*\*\s*(.*?)\s*---", content, re.DOTALL
        )
        return concept_blocks


def test_extract_concept_blocks():
    file_path = "/home/jinheonyoon/workspace/ml/Machine_Learning.md"
    concept_blocks = extract_concept_blocks(file_path)
    print(concept_blocks)
    # save to markdown file
    with open("concept_blocks.md", "w", encoding="utf-8") as file:
        for block in concept_blocks:
            file.write(f"{block}\n\n")


def extract_all_concept_blocks(directory):
    all_concept_blocks = []
    markdown_files = get_markdown_files(directory)
    for file_path in markdown_files:
        concept_blocks = extract_concept_blocks(file_path)
        all_concept_blocks.extend(concept_blocks)
    return all_concept_blocks


def process_text(text):
    pattern = r"- \*\*([\s\S]*?)\*\* : ([\s\S]*?) : ([\s\S]*?)(?=\n- \*\*|\Z)"

    matches = re.findall(pattern, text)

    data = []
    for match in matches:
        concept = match[0].strip()
        description = match[1].strip()
        tags = match[2].strip()
        data.append([concept, description, tags])

    return data


def write_csv(data, filename="output.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)


# Main function


def main():
    # Directory containing markdown files
    markdown_directory = "content"

    # Extract all concept blocks from the directory
    all_concept_blocks = extract_all_concept_blocks(markdown_directory)

    # Print each concept block
    #    for idx, block in enumerate(all_concept_blocks):
    #    print(f"Concept Block {idx + 1}:\n{block}\n")

    all_concept_blocks = extract_all_concept_blocks(markdown_directory)

    data = []
    for block in all_concept_blocks:
        data.extend(process_text(block))

    write_csv(data, "output_test.csv")

    print("\n\n".join(all_concept_blocks))


if __name__ == "__main__":
    main()
    # test_extract_concept_blocks()
