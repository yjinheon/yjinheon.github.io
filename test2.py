import re
import csv


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


# Test text with newlines in various places
text = """- **Latency** : 네트워크 지연시간. 데이터 패킷이 한 지점에서 다른 지점으로 이동하는데 걸리는 시간.
두줄일 경우 데이터어떻게 뽑히는지 확인 : AWS | WEB
- **Throughput** : 단위 시간당 처리량. 웹 어플리케이션 성능지표로 쓰일 경우 보통 단위시간 당 처리하는 요청의 수. 데이터 전송률 : AWS | WEB
- **IOPS** : Input Output Operation Per Second. 초당 처리하는 IO의 개수로 보통 스토리지의 속도를 의미. 
스토리지의 Throughput은 IOPS로서 스토리지 성능을 대표한다. : AWS | WEB
- **Bandwidth** : 네트워크에서 특정 시간 내에 전송될 수 있는 데이터의 최대 용량을 의미 : AWS | 
WEB"""

data = process_text(text)
write_csv(data)

print("CSV file 'output.csv' has been created with actual newlines in cells.")
