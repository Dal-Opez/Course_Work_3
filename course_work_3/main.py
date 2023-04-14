from utils import read_json, filter_executed, sort_date, print_info, LAST_OPERATIONS_CNT
from operation import Operation


def main():
    data = sort_date(filter_executed(read_json()))
    data.reverse()
    op_list = [Operation(data[i].get("date"), data[i].get("operationAmount"), data[i].get("description"),
                         data[i].get("from"), data[i].get("to")) for i in range(LAST_OPERATIONS_CNT)]
    print_info(op_list)


main()
