#!/usr/bin/env python3


from abc import ABC, abstractmethod
from typing import Any, List, Union, Tuple
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


class DataStream:
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            routed = False
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    routed = True
                    break
            if not routed:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            class_name = processor.__class__.__name__
            remaining = len(processor.data_queue)
            total = processor.rank
            print(
                f"{class_name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print()
    print("Initialize Data Stream...")
    stream = DataStream()
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print()
    print("Registering Numeric Processor")
    stream.register_processor(NumericProcessor())
    test_data = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"]
    ]
    print("Send first batch of data on stream:", test_data)
    stream.process_stream(test_data)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nRegistering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    print("Send the same batch again")
    stream.process_stream(test_data)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        stream.processors[0].output()
    for _ in range(2):
        stream.processors[1].output()
    for _ in range(1):
        stream.processors[2].output()
    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
