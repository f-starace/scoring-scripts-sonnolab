from typing import List
import numpy as np
from math import sqrt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd

# for plot representation
from plotly.graph_objects import Figure
import plotly.graph_objects as go
from typing import Optional


import statsmodels.api as sm
from patsy import dmatrix
import statsmodels.formula.api as smf



class Linear:
    def __init__(
        self,
        df: pd.DataFrame,
        X: List[str],
        y: str,
        fit_intercept: bool = True,
        copy_X: bool = True,
        test_size: int = 0,
        random_state: Optional[int] = None,
        label: Optional[str] = None,
    ):
        X = df[X].values
        y = df[y].values

        self.X = X
        self.y = y
        self.test_size = test_size
        self.label = label

        if self.test_size:
            # we split the df into a training and testing set
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=self.test_size, random_state=random_state
            )
        else:
            # we use the entire dataset as training set
            self.X_train, self.y_train = X, y

        self.model = LinearRegression(fit_intercept=fit_intercept, copy_X=copy_X).fit(
            self.X_train, self.y_train
        )
        self.calc_train_metrics()
        self.calc_test_metrics()

    def calc_train_metrics(self) -> None:
        """ """
        pred_train = self.model.predict(self.X_train)
        self.r_sq_train = self.model.score(self.X_train, self.y_train)
        self.rmse_train = mean_squared_error(self.y_train, pred_train, squared=False)

    def calc_test_metrics(self) -> None:
        """ """
        if not self.test_size:
            return None

        pred_test = self.model.predict(self.X_test)
        self.r_sq_test = self.model.score(self.X_test, self.y_test)
        self.rmse_test = mean_squared_error(self.y_test, pred_test, squared=False)

    def result(self) -> dict:
        result = {}
        result["model"] = {
            "intercept": self.model.intercept_,
            "coef": list(self.model.coef_),
            "type": "linear",
        }
        result["train"] = {
            "r_sq": self.r_sq_train,
            "rmse": self.rmse_train,
        }

        if self.test_size == 0:
            result["test"] = None
            return result

        result["test"] = {
            "r_sq": self.r_sq_test,
            "rmse": self.rmse_test,
        }
        return result

    def plot(self, figure: Figure) -> Figure:
        X_range = np.linspace(self.X.min(), self.X.max(), 100)
        y_range = self.model.predict(X_range.reshape(-1, 1))

        regression_line = go.Scatter(
            x=X_range,
            y=y_range,
            name=f"Linear Regression" if not self.label else self.label,
        )

        if self.test_size:
            train_markers = go.Scatter(
                x=self.X_train.squeeze(), y=self.y_train, mode="markers", name="train"
            )
            test_markers = go.Scatter(
                x=self.X_test.squeeze(), y=self.y_test, mode="markers", name="test"
            )
            figure.add_traces([regression_line, train_markers, test_markers])
        else:
            figure.add_traces(regression_line)

        return figure

