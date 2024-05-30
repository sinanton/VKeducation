import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    months = [datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%S').month for d in dates]
    return [m for m, c in Counter(months).most_common(n)]


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)