#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Union, List, Tuple
from collections import deque


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data_queue: deque[str] = deque()
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        if self.data_queue:
            return (
                self.rank - len(self.data_queue),
                self.data_queue.popleft(),
            )
        return (0, "")


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(self, data: Union[int, float, List[Union[int, float]]]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, (int, float)):
            self.data_queue.append(str(data))
            self.rank += 1
        else:
            for item in data:
                self.data_queue.append(str(item))
                self.rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, str):
            self.data_queue.append(data)
            self.rank += 1
        else:
            for item in data:
                self.data_queue.append(item)
                self.rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items()
                )
                for item in data
            )
        return False

    def ingest(
        self,
        data: Union[dict[str, str], List[dict[str, str]]],
    ) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, dict):
            log_entry = (
                f"{data.get('log_level', 'INFO')}: "
                f"{data.get('log_message', '')}"
            )
            self.data_queue.append(log_entry)
            self.rank += 1
        else:
            for item in data:
                log_entry = (
                    f"{item.get('log_level', 'INFO')}: "
                    f"{item.get('log_message', '')}"
                )
                self.data_queue.append(log_entry)
                self.rank += 1


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    print("Testing Numeric Processor...")
    numeric_proc = NumericProcessor()
    print("Trying to validate input '42':", numeric_proc.validate(42))
    print("Trying to validate input 'Hello':", numeric_proc.validate("Hello"))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_proc.ingest("foo")
    except Exception as e:
        print(f"Got exception: {e}")
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric_proc.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        rank, value = numeric_proc.output()
        print(f"Numeric value {rank}: {value}")

    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print("Trying to validate input '42':", text_proc.validate(42))
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text_proc.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    rank, value = text_proc.output()
    print(f"Text value {rank}: {value}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print("Trying to validate input 'Hello':", log_proc.validate("Hello"))
    log_data = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}
    ]
    print("Processing data:", log_data)
    log_proc.ingest(log_data)
    print("Extracting 2 values...")
    for i in range(2):
        rank, value = log_proc.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
