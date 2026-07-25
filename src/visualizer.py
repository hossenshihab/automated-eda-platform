"""
Visualization module.

Provides interactive Plotly visualizations for exploratory
data analysis (EDA).
"""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class DataVisualizer:
    """
    Interactive visualization toolkit for pandas DataFrames.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()

    # =====================================================
    # Private Helper Methods
    # =====================================================

    def _validate_column(self, column: str) -> None:
        """Check whether a column exists."""

        if column not in self.df.columns:
            raise ValueError(
                f"Column '{column}' does not exist.\n"
                f"Available columns: {list(self.df.columns)}"
            )

    def _validate_numeric(self, column: str) -> None:
        """Ensure a column is numeric."""

        self._validate_column(column)

        if not pd.api.types.is_numeric_dtype(self.df[column]):
            raise TypeError(
                f"Column '{column}' is not numeric."
            )

    def _apply_layout(
        self,
        fig: go.Figure,
        title: str,
    ) -> go.Figure:
        """Apply a consistent layout."""

        fig.update_layout(
            title={
                "text": title,
                "x": 0.5,
                "xanchor": "center",
            },
            template="plotly_white",
            height=600,
            width=950,
            font=dict(
                family="Arial",
                size=14,
            ),
            title_font_size=22,
            legend_title_text="",
            margin=dict(
                l=50,
                r=50,
                t=80,
                b=50,
            ),
        )

        return fig

    # =====================================================
    # Histogram
    # =====================================================

    def histogram(
        self,
        column: str,
        bins: int = 30,
    ) -> go.Figure:

        self._validate_numeric(column)

        fig = px.histogram(
            self.df,
            x=column,
            nbins=bins,
            marginal="box",
        )

        return self._apply_layout(
            fig,
            f"Histogram of {column}",
        )

    # =====================================================
    # Boxplot
    # =====================================================

    def boxplot(
        self,
        column: str,
    ) -> go.Figure:

        self._validate_numeric(column)

        fig = px.box(
            self.df,
            y=column,
            points="outliers",
        )

        return self._apply_layout(
            fig,
            f"Boxplot of {column}",
        )

    # =====================================================
    # Scatter Plot
    # =====================================================

    def scatter_plot(
        self,
        x: str,
        y: str,
        color: str | None = None,
    ) -> go.Figure:

        self._validate_numeric(x)
        self._validate_numeric(y)

        if color is not None:
            self._validate_column(color)

        fig = px.scatter(
            self.df,
            x=x,
            y=y,
            color=color,
        )

        return self._apply_layout(
            fig,
            f"{y} vs {x}",
        )

    # =====================================================
    # Line Plot
    # =====================================================

    def line_plot(
        self,
        x: str,
        y: str,
    ) -> go.Figure:

        self._validate_column(x)
        self._validate_numeric(y)

        fig = px.line(
            self.df,
            x=x,
            y=y,
        )

        return self._apply_layout(
            fig,
            f"{y} over {x}",
        )

    # =====================================================
    # Bar Chart
    # =====================================================

    def bar_chart(
        self,
        column: str,
    ) -> go.Figure:

        self._validate_column(column)

        counts = (
            self.df[column]
            .value_counts()
            .reset_index()
        )

        counts.columns = [column, "Count"]

        fig = px.bar(
            counts,
            x=column,
            y="Count",
            text="Count",
        )

        fig.update_traces(textposition="outside")

        return self._apply_layout(
            fig,
            f"{column} Distribution",
        )

    # =====================================================
    # Pie Chart
    # =====================================================

    def pie_chart(
        self,
        column: str,
    ) -> go.Figure:

        self._validate_column(column)

        counts = (
            self.df[column]
            .value_counts()
            .reset_index()
        )

        counts.columns = [column, "Count"]

        fig = px.pie(
            counts,
            names=column,
            values="Count",
            hole=0.35,
        )

        return self._apply_layout(
            fig,
            f"{column} Distribution",
        )

    # =====================================================
    # Correlation Heatmap
    # =====================================================

    def correlation_heatmap(self) -> go.Figure:

        corr = self.df.corr(numeric_only=True)

        fig = px.imshow(
            corr,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            aspect="auto",
        )

        return self._apply_layout(
            fig,
            "Correlation Heatmap",
        )

    # =====================================================
    # Missing Values Chart
    # =====================================================

    def missing_values_chart(self) -> go.Figure:

        missing = (
            self.df.isna()
            .sum()
            .sort_values(ascending=False)
        )

        missing = missing[missing > 0]

        fig = px.bar(
            x=missing.index,
            y=missing.values,
            labels={
                "x": "Columns",
                "y": "Missing Values",
            },
            text=missing.values,
        )

        fig.update_traces(textposition="outside")

        return self._apply_layout(
            fig,
            "Missing Values by Column",
        )

    # =====================================================
    # Violin Plot
    # =====================================================

    def violin_plot(
        self,
        column: str,
    ) -> go.Figure:

        self._validate_numeric(column)

        fig = px.violin(
            self.df,
            y=column,
            box=True,
            points="outliers",
        )

        return self._apply_layout(
            fig,
            f"Violin Plot of {column}",
        )

    # =====================================================
    # Distribution Plot
    # =====================================================

    def distribution_plot(
        self,
        column: str,
    ) -> go.Figure:

        self._validate_numeric(column)

        fig = px.histogram(
            self.df,
            x=column,
            marginal="violin",
            nbins=30,
        )

        return self._apply_layout(
            fig,
            f"Distribution of {column}",
        )

    # =====================================================
    # Save Figure
    # =====================================================

    def save_html(
        self,
        fig: go.Figure,
        filename: str,
    ) -> None:

        fig.write_html(filename)

    def save_png(
        self,
        fig: go.Figure,
        filename: str,
    ) -> None:
        """
        Requires:
            pip install kaleido
        """

        fig.write_image(filename)