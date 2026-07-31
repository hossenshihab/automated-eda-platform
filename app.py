from src.data_loader import load_dataset
from src.profiler import DatasetProfiler
from src.analyzer import DatasetAnalyzer
from src.insights import DatasetInsights
from src.cleaner import DataCleaner
from src.visualizer import DataVisualizer
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Automated EDA Platform",
    page_icon="📊",
    layout="wide",
)

st.title("Automated EDA Platform")

st.markdown("""
Upload any CSV file to automatically analyze,
visualize and clean your dataset.
""")

uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"],
)

if uploaded_file is None:
    st.info("Please upload a CSV file to begin.")
    st.stop()

# Load dataframe
df = load_dataset(uploaded_file)

profiler = DatasetProfiler(df)
analyzer = DatasetAnalyzer(df)
insights = DatasetInsights(df)
cleaner = DataCleaner(df)
visualizer = DataVisualizer(df)

st.success("Dataset uploaded successfully!")

st.divider()

st.header("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Rows",
        df.shape[0],
    )

with col2:
    st.metric(
        "Columns",
        df.shape[1],
    )

with col3:
    st.metric(
        "Missing Values",
        int(df.isnull().sum().sum()),
    )

with col4:
    st.metric(
        "Duplicate Rows",
        int(df.duplicated().sum()),
    )

st.divider()

with st.expander(
    "Dataset Preview",
    expanded=True,
):
    st.dataframe(
        df,
        use_container_width=True,
    )

st.divider()

st.header("Dataset Health")

report = profiler.quality_report()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Quality Score",
        report["Score"],
    )

with col2:
    st.metric(
        "Grade",
        report["Grade"],
    )

st.divider()
st.header("Dataset Analysis")

summary = analyzer.dataset_summary()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Memory (MB)",
        summary["Memory Usage (MB)"],
    )

with col2:
    st.metric(
        "Numeric Columns",
        summary["Numeric Columns"],
    )

with col3:
    st.metric(
        "Categorical Columns",
        summary["Categorical Columns"],
    )

st.subheader("Numerical Summary")

st.dataframe(
    analyzer.numeric_summary(),
    use_container_width=True,
)

categorical = analyzer.categorical_summary()

if not categorical.empty:
    st.subheader("Categorical Summary")

    st.dataframe(
        categorical,
        use_container_width=True,
    )

missing = analyzer.missing_summary()

if not missing.empty:
    st.subheader("Missing Value Summary")

    st.dataframe(
        missing,
        use_container_width=True,
    )

st.subheader("Duplicate Summary")

st.dataframe(
    analyzer.duplicate_summary(),
    use_container_width=True,
)

st.subheader("Correlation Matrix")

st.dataframe(
    analyzer.correlation_matrix(),
    use_container_width=True,
)

st.divider()

st.header("Interactive Visualization")

numeric_columns = df.select_dtypes(
    include="number"
).columns.tolist()

categorical_columns = df.select_dtypes(exclude="number").columns.tolist()

plot_type = st.selectbox(
    "Select Visualization",
    [
        "Histogram",
        "Distribution Plot",
        "Box Plot",
        "Violin Plot",
        "Scatter Plot",
        "Line Plot",
        "Bar Chart",
        "Pie Chart",
        "Correlation Heatmap",
        "Missing Values Chart",
    ],
)

if plot_type == "Histogram":

    column = st.selectbox(
        "Select Numeric Column",
        numeric_columns,
    )

    fig = visualizer.histogram(column)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

elif plot_type == "Box Plot":

    column = st.selectbox(
        "Select Numeric Column",
        numeric_columns,
    )

    fig = visualizer.boxplot(column)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

elif plot_type == "Scatter Plot":

    col1, col2 = st.columns(2)

    with col1:
        x = st.selectbox(
            "X Axis",
            numeric_columns,
        )

    with col2:
        y = st.selectbox(
            "Y Axis",
            numeric_columns,
            index=1 if len(numeric_columns) > 1 else 0,
        )

    fig = visualizer.scatter_plot(
        x,
        y,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

elif plot_type == "Distribution Plot":

    column = st.selectbox(
        "Column",
        numeric_columns,
    )

    fig = visualizer.distribution_plot(column)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

elif plot_type == "Violin Plot":

    column = st.selectbox(
        "Column",
        numeric_columns,
    )

    fig = visualizer.violin_plot(column)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

elif plot_type == "Line Plot":

    default_index = 0

    if "DateTime" in df.columns:
        default_index = df.columns.get_loc("DateTime")

    col1, col2 = st.columns(2)

    with col1:
        x = st.selectbox(
            "X Axis",
            df.columns.tolist(),
            index=default_index,
        )

    with col2:
        y = st.selectbox(
            "Y Axis",
            numeric_columns,
        )

    fig = visualizer.line_plot(
        x,
        y,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

elif plot_type == "Bar Chart":

    column = st.selectbox(
        "Column",
        df.columns.tolist(),
    )

    fig = visualizer.bar_chart(column)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

elif plot_type == "Pie Chart":

    column = st.selectbox(
        "Column",
        df.columns.tolist(),
    )

    fig = visualizer.pie_chart(column)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

elif plot_type == "Correlation Heatmap":

    fig = visualizer.correlation_heatmap()

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

elif plot_type == "Missing Values Chart":

    fig = visualizer.missing_values_chart()

    st.plotly_chart(
        fig,
        use_container_width=True,
    )
