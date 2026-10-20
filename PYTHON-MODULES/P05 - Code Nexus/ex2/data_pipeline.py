#!/usr/bin/env python3


from abc import ABC, abstractmethod
from typing import Any, List, Union, Tuple, Protocol
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


class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...


class CSVExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        csv_line = ",".join(value for _, value in data)
        print(f"CSV Output:\n{csv_line}")


class JSONExportPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        entries = ", ".join(
            f'"item_{rank}": "{value}"' for rank, value in data
        )
        print(f"JSON Output:\n{{{entries}}}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            data_to_export = []
            for _ in range(nb):
                if len(processor.data_queue) > 0:
                    data_to_export.append(processor.output())
            if data_to_export:
                plugin.process_output(data_to_export)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    stream = DataStream()
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
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
    print("\nSend 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(3, csv_plugin)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    test_data_2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]
    print("\nSend another batch of data:", test_data_2)
    stream.process_stream(test_data_2)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(5, json_plugin)
    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
