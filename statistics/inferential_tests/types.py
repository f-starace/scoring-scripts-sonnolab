from pydantic import BaseModel
from typing import List


class InferentialTest(BaseModel):
    name: str
    statistic: float
    pvalue: float
    meaningful: bool
    parametric: bool

class InferentialReport(BaseModel):
    tests: List[InferentialTest]
    total: int
    count: int
    nans: int