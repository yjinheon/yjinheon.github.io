import os
import csv
import re
import pandas as pd
import yaml


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


def extract_yaml_block(markdown_content):
    """
    Extracts the YAML front matter from the Markdown content.

    :param markdown_content: String, the full content of a Markdown file
    :return: Dictionary containing parsed YAML data
    """
    # Split the content based on '---' to separate the YAML block from the rest of the content
    parts = markdown_content.split("---")

    # Ensure the YAML block is present
    if len(parts) > 1:
        yaml_block = parts[1].strip()
        try:
            # Parse the YAML block into a Python dictionary
            parsed_yaml = yaml.safe_load(yaml_block)
            return parsed_yaml
        except yaml.YAMLError as e:
            print(f"Error parsing YAML: {e}")
            return None
    else:
        print("No YAML front matter found.")
        return None


def get_tags_as_string(yaml_data):
    tags = yaml_data.get("tags", [])
    return ";".join(tags)


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


def data_to_df(data):

    df = pd.DataFrame(data, columns=["concept", "description", "tags"])
    return df


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

    # Convert data to a pandas DataFrame
    df = data_to_df(data)
    print(df.head())

    # filter df by tags
    df = df[df["tags"].str.contains("AWS")]
    df = df.reset_index(drop=True)
    df.to_csv("output.csv", index=False)
    # print("\n\n".join(all_concept_blocks))
    # print all row of df
    for index, row in df.iterrows():
        print(row["concept"])
        print(row["description"])
        print(row["tags"])
        print("\n")


if __name__ == "__main__":
    main()
    # test_extract_concept_blocks()
