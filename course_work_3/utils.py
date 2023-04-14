import os
import json

PATH = os.path.join("operations.json")


def read_json():
    """
    Считывает файл по пути PATH, и преобразует формат JSON в объект Python
    :return: возвращает информацию из файла формата JSON в виде объекта Python
    """
    with open(PATH, "r", encoding="utf8") as data:
        return json.load(data)


def filter_executed(data: list):
    """
    Отсеивает невыполненные операции
    :param data: список, содержащий словари с информацией об операциях
    :return: список словарей, содержащих информацию только об исполненных операциях
    """
    ret_val = [data[i] for i in range(len(data)) if data[i].get("state") == "EXECUTED"]
    return ret_val


def sort_date(data: list):
    """
    Выполняет сортировку словарей по дате
    :param data: список словарей содержащих информацию об операциях
    :return: отсортированный список словарей, содержащий информацию об операциях
    """
    data.sort(key=lambda x: x["date"])
    return data
