import re
from datetime import datetime
from langchain.schema import Document

def extract_timestamp(log_entry):
    match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", log_entry)
    if match:
        return datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
    return None

def process_logs(file_path: str):
    with open(file_path, "r") as file:
        log_data = file.read()

    entries = re.split(r"(?=\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", log_data)
    documents = []
    for entry in entries:
        entry = entry.strip()
        if len(entry) > 10:
            ts = extract_timestamp(entry)
            if ts:
                documents.append(Document(page_content=entry, metadata={"timestamp": ts.isoformat()}))
    return documents
