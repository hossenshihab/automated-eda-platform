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

st.sidebar.header("📁 Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Choose a CSV file",
    type=["csv"],
)

if uploaded_file is None:
    st.info("Please upload a CSV file to begin.")
    st.stop()

st.sidebar.divider()

st.sidebar.header("🧭 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Analysis",
        "Visualization",
        "Cleaning",
        "AI Insights",
    ],
)

# Load dataframe
df = load_dataset(uploaded_file)

profiler = DatasetProfiler(df)
analyzer = DatasetAnalyzer(df)
insights = DatasetInsights(df)
cleaner = DataCleaner(df)
visualizer = DataVisualizer(df)

st.success("Dataset uploaded successfully!")

st.sidebar.divider()

st.sidebar.header("📋 Dataset Info")

st.sidebar.write(f"**Rows:** {df.shape[0]}")
st.sidebar.write(f"**Columns:** {df.shape[1]}")
st.sidebar.write(f"**Missing:** {int(df.isnull().sum().sum())}")
st.sidebar.write(f"**Duplicates:** {int(df.duplicated().sum())}")

if page == "Overview":

    st.divider()

    st.header("Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

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
            width="stretch",
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
elif page == "Analysis":

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
        width="stretch",
    )

    categorical = analyzer.categorical_summary()

    if not categorical.empty:
        st.subheader("Categorical Summary")

        st.dataframe(
            categorical,
            width="stretch",
        )

    missing = analyzer.missing_summary()

    if not missing.empty:
        st.subheader("Missing Value Summary")

        st.dataframe(
            missing,
            width="stretch",
        )

    st.subheader("Duplicate Summary")

    st.dataframe(
        analyzer.duplicate_summary(),
        width="stretch",
    )

    st.subheader("Correlation Matrix")

    st.dataframe(
        analyzer.correlation_matrix(),
        width="stretch",
    )

elif page == "Visualization":
    st.divider()

    st.header("Interactive Visualization")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

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
            width="stretch",
        )

    elif plot_type == "Box Plot":

        column = st.selectbox(
            "Select Numeric Column",
            numeric_columns,
        )

        fig = visualizer.boxplot(column)

        st.plotly_chart(
            fig,
            width="stretch",
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
            width="stretch",
        )

    elif plot_type == "Distribution Plot":

        column = st.selectbox(
            "Column",
            numeric_columns,
        )

        fig = visualizer.distribution_plot(column)

        st.plotly_chart(
            fig,
            width="stretch",
        )

    elif plot_type == "Violin Plot":

        column = st.selectbox(
            "Column",
            numeric_columns,
        )

        fig = visualizer.violin_plot(column)

        st.plotly_chart(
            fig,
            width="stretch",
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
            width="stretch",
        )

    elif plot_type == "Bar Chart":

        column = st.selectbox(
            "Column",
            df.columns.tolist(),
        )

        fig = visualizer.bar_chart(column)

        st.plotly_chart(
            fig,
            width="stretch",
        )

    elif plot_type == "Pie Chart":

        column = st.selectbox(
            "Column",
            df.columns.tolist(),
        )

        fig = visualizer.pie_chart(column)

        st.plotly_chart(
            fig,
            width="stretch",
        )

    elif plot_type == "Correlation Heatmap":

        fig = visualizer.correlation_heatmap()

        st.plotly_chart(
            fig,
            width="stretch",
        )

    elif plot_type == "Missing Values Chart":

        fig = visualizer.missing_values_chart()

        st.plotly_chart(
            fig,
            width="stretch",
        )

elif page == "Cleaning":
    st.divider()

    st.header("🧹 Data Cleaning Dashboard")

    clean_option = st.selectbox(
        "Select Cleaning Operation",
        [
            "Fill Missing (Mean)",
            "Fill Missing (Median)",
            "Fill Missing (Mode)",
            "Drop Missing Rows",
            "Remove Duplicates",
            "Encode Categorical",
            "Standard Scaling",
            "Min-Max Scaling",
            "Drop Columns",
        ],
    )

    selected_columns = []

    if clean_option == "Drop Columns":
        selected_columns = st.multiselect(
            "Select Columns",
            df.columns.tolist(),
        )

    # Initialize session state

    if "cleaned_df" not in st.session_state:
        st.session_state.cleaned_df = None

    # Apply cleaning

    if st.button("Apply Cleaning"):

        # Always start from the original uploaded dataset
        cleaner = DataCleaner(df)

        if clean_option == "Fill Missing (Mean)":
            cleaner.fill_missing_mean()

        elif clean_option == "Fill Missing (Median)":
            cleaner.fill_missing_median()

        elif clean_option == "Fill Missing (Mode)":
            cleaner.fill_missing_mode()

        elif clean_option == "Drop Missing Rows":
            cleaner.drop_missing()

        elif clean_option == "Remove Duplicates":
            cleaner.remove_duplicates()

        elif clean_option == "Encode Categorical":
            cleaner.encode_categorical()

        elif clean_option == "Standard Scaling":
            cleaner.standardize_numeric()

        elif clean_option == "Min-Max Scaling":
            cleaner.minmax_scale()

        elif clean_option == "Drop Columns":
            cleaner.drop_columns(selected_columns)

        # Save cleaned dataframe in session state
        st.session_state.cleaned_df = cleaner.get_clean_data()

    # Show cleaned dataset (if available)

    if st.session_state.cleaned_df is not None:

        st.success("Cleaning completed successfully!")

        st.subheader("Cleaned Dataset Preview")

        st.dataframe(
            st.session_state.cleaned_df,
            width="stretch",
        )

        st.download_button(
            label="⬇ Download Cleaned CSV",
            data=st.session_state.cleaned_df.to_csv(index=False),
            file_name="cleaned_dataset.csv",
            mime="text/csv",
        )

elif page == "AI Insights":

    st.divider()

    st.header("🧠 AI Dataset Insights")

    report = insights.generate_report()

    overall = report["Overall Recommendation"]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Readiness Score",
            overall["Readiness Score"],
        )

    with col2:
        st.metric(
            "Dataset Status",
            overall["Status"],
        )

    st.divider()

    st.subheader("✅ Overall Recommendations")

    for recommendation in overall["Recommendations"]:
        st.success(recommendation)

        st.subheader("🟡 Missing Value Insights")

    missing = report["Missing Value Insights"]

    if len(missing) == 0:
        st.success("No missing values detected.")

    else:

        for item in missing:

            st.warning(f"""
         **{item['Column']}**

         Missing Values: **{item['Missing Count']}**

         Missing Percentage: **{item['Missing (%)']}%**

         Recommendation:

         {item['Recommendation']}
         """)

    st.subheader("🔵 Duplicate Rows")

    duplicate = report["Duplicate Insights"]

    st.info(f"""
    Duplicate Rows: **{duplicate['Duplicate Rows']}**

    Recommendation: **{duplicate['Recommendation']}**
    """)

    st.subheader("🔴 Outlier Detection")

    outliers = report["Outlier Insights"]

    outlier_df = pd.DataFrame(outliers)

    outlier_df = outlier_df[
    outlier_df["Outliers"] > 0
    ]

    if outlier_df.empty:

        st.success(
            "No significant outliers detected."
        )

    else:

        st.dataframe(
            outlier_df,
            width="stretch",
        )


    st.subheader("🟣 Correlation Insights")

    correlation = report["Correlation Insights"]

    for item in correlation:

        st.info(
            item["Recommendation"]
        )
