import streamlit as st
import plotly.express as go
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="A Cure for the Common Company",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Data Definitions ---

# Data for the "Prescription" tab
prescription_data = {
    'W': {
        'title': 'Work Environment',
        'items': [
            '**Psychological Safety:** Creating an environment where employees feel safe to speak up.',
            '**Flexible Work:** Offering flexible schedules and locations to support work-life integration.',
            '**Manageable Workload:** Using data to ensure workloads are challenging but not overwhelming.',
            '**Physical Space:** Designing offices that support different work styles (collaboration, focus).'
        ]
    },
    'E': {
        'title': 'Emotional & Mental Health',
        'items': [
            '**Accessible Resources:** Easy, confidential access to EAPs, therapy, and coaching.',
            '**Stress Management:** Proactive training and tools for mindfulness and resilience.',
            '**Stigma Reduction:** Leadership-driven campaigns to normalize mental health conversations.',
            '**Digital Detox:** Establishing clear boundaries for after-hours communication.'
        ]
    },
    'L1': {
        'title': 'Leadership & Culture',
        'items': [
            '**Empathetic Management:** Training managers to lead with compassion and support.',
            '**Clear Communication:** Transparency from leadership about business goals and changes.',
            '**Values Alignment:** Ensuring company values are reflected in daily practices and decisions.',
            '**Recognition:** Building a culture of appreciation for effort and outcomes.'
        ]
    },
    'L2': {
        'title': 'Lifestyle & Physical Health',
        'items': [
            '**Preventative Care:** Incentives and access to regular health screenings.',
            '**Financial Well-being:** Providing resources for financial planning, debt management, and savings.',
            '**Nutrition & Exercise:** Subsidies or access to healthy food options and fitness opportunities.',
            '**Sleep Health:** Education and resources to improve sleep hygiene.'
        ]
    }
}

# Data for the "Analytics Lab" step-flow
analytics_steps_data = {
    '1. Diagnose': {
        'title': 'Diagnose: Where are we now?',
        'text': 'Use aggregate data to establish a baseline. This includes analyzing claims data (for physical health issues), EAP utilization (for mental health), pulse survey results (for engagement/burnout), and turnover/absenteeism rates. This identifies the specific "symptoms" in the workforce.'
    },
    '2. Personalize': {
        'title': 'Personalize: What does our workforce need?',
        'text': 'Move away from one-size-fits-all. Segment the workforce (e.g., by role, location, life stage) to understand unique needs. Data can reveal that new parents need flexible schedules, while remote workers need better digital connection tools. This allows for targeted, high-impact interventions.'
    },
    '3. Measure': {
        'title': 'Measure: Is the prescription working?',
        'text': 'Track KPIs to measure the effectiveness of interventions. This includes leading indicators (e.g., EAP usage up, well-being survey scores up) and lagging indicators (e.g., healthcare costs down, turnover down). This provides a clear ROI and allows for continuous improvement.'
    },
    '4. Predict': {
        'title': 'Predict: What challenges are next?',
        'text': 'Use analytics to identify populations at high risk for burnout, turnover, or health issues *before* they become critical. This allows leadership to proactively deploy resources, offer support, or adjust workloads, moving from a reactive to a truly preventative model.'
    }
}

# Data for the "Analytics Lab" impact chart
leading_data = {
    'labels': ['EAP Utilization', 'Well-being Scores', 'Program Engagement', 'Manager Support Scores'],
    'data': [40, 25, 30, 22]
}
lagging_data = {
    'labels': ['Productivity', 'Employee Retention', 'Absenteeism', 'Healthcare Costs'],
    'data': [18, 20, -15, -12]
}

# --- Header ---
st.title("A Cure for the Common Company")
st.caption("An Interactive Prescription for a Healthier Workforce")

# --- Main Tab Navigation ---
tab_diagnosis, tab_prescription, tab_analytics, tab_prognosis = st.tabs([
    "Diagnosis", "Prescription", "Analytics Lab", "Prognosis"
])

# --- Tab 1: Diagnosis ---
with tab_diagnosis:
    st.markdown("""
    This section explores the "why" behind the need for a new approach. Traditional, one-size-fits-all wellness programs are often ineffective because they treat symptoms, not root causes. The modern workforce is facing unprecedented levels of burnout, disengagement, and stress. Below, you can see the scale of the problem and the associated costs.
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("The Problem with Common Wellness")
        
        # Replicate stat cards with st.metric
        r1_col1, r1_col2 = st.columns(2)
        with r1_col1:
            st.metric(
                label="Failure Rate", 
                value="80%", 
                delta="of programs fail to show ROI", 
                delta_color="off"
            )
        with r1_col2:
            st.metric(
                label="Employee Needs", 
                value="55%", 
                delta="feel programs don't meet needs", 
                delta_color="off"
            )
        
        st.metric(
            label="Burnout Cost", 
            value="$190B", 
            delta="Annual U.S. healthcare spending", 
            delta_color="off"
        )

    with col2:
        st.subheader("Wellness Program Effectiveness")
        
        # Plotly Donut Chart (replaces Chart.js)
        fig_donut = go.Figure(data=[go.Pie(
            labels=['Ineffective or Unused', 'Meets Employee Needs'],
            values=[80, 20],
            hole=.4,
            marker_colors=['#f0f0f0', '#0d9488'] # Match original colors
        )])
        fig_donut.update_layout(
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
            margin=dict(t=0, b=0, l=0, r=0),
            height=300
        )
        st.plotly_chart(fig_donut, use_container_width=True)

# --- Tab 2: Prescription ---
with tab_prescription:
    st.markdown("""
    A "Cure for the Common Company" requires a holistic prescription, moving beyond gym memberships and apps. This framework focuses on four interconnected pillars that create a genuine culture of well-being. Click on each pillar below to see the specific interventions prescribed for each area.
    """)

    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("The WELL Prescription")

        # Initialize session state to track the active pillar
        if 'active_pillar' not in st.session_state:
            st.session_state.active_pillar = 'W'

        # 2x2 Button Grid
        # Use st.button and session state to manage selection
        r1_col1, r1_col2 = st.columns(2)
        with r1_col1:
            if st.button("W: Work Environment", use_container_width=True, type="primary" if st.session_state.active_pillar == 'W' else "secondary"):
                st.session_state.active_pillar = 'W'
        with r1_col2:
            if st.button("E: Emotional Health", use_container_width=True, type="primary" if st.session_state.active_pillar == 'E' else "secondary"):
                st.session_state.active_pillar = 'E'
        
        r2_col1, r2_col2 = st.columns(2)
        with r2_col1:
            if st.button("L: Leadership", use_container_width=True, type="primary" if st.session_state.active_pillar == 'L1' else "secondary"):
                st.session_state.active_pillar = 'L1'
        with r2_col2:
            if st.button("L: Lifestyle Health", use_container_width=True, type="primary" if st.session_state.active_pillar == 'L2' else "secondary"):
                st.session_state.active_pillar = 'L2'

    with col2:
        # Display details based on the active pillar in session state
        active_pillar_key = st.session_state.active_pillar
        details = prescription_data[active_pillar_key]
        
        with st.container(border=True): # Use border to create a content box
            st.subheader(details['title'])
            for item in details['items']:
                st.markdown(f"- {item}")

# --- Tab 3: Analytics Lab ---
with tab_analytics:
    st.markdown("""
    This is where data and analytics become the central nervous system of the well-being strategy. Instead of guessing, data allows organizations to move through a continuous cycle of improvement. This is not about surveillance; it's about understanding aggregate, anonymized data to provide better support. Explore the steps in the process and see the data-driven impact.
    """)
    
    st.subheader("The Data-Driven Well-Being Cycle")
    
    # Use st.radio for the step-flow, replacing JS buttons
    step_choice = st.radio(
        "Select a step to see details:",
        options=analytics_steps_data.keys(),
        horizontal=True,
        label_visibility="collapsed"
    )
    
    # Display details for the chosen step
    step_details = analytics_steps_data[step_choice]
    with st.container(border=True):
        st.markdown(f"**{step_details['title']}**")
        st.markdown(step_details['text'])

    st.divider()

    st.subheader("Visualizing the Impact")
    st.markdown("""
    Data helps measure both leading indicators (proactive measures) and lagging indicators (business outcomes). Use the filters below to see how a data-driven approach can affect key metrics.
    """)
    
    # Use st.radio for the chart filter, replacing JS buttons
    chart_filter = st.radio(
        "Select indicators:",
        options=["Leading Indicators", "Lagging Indicators"],
        horizontal=True
    )

    # Prepare data for the Plotly Bar Chart
    if chart_filter == "Leading Indicators":
        chart_data = leading_data
        color = '#0d9488'
        title = "Leading Indicators Improvement"
    else:
        chart_data = lagging_data
        color = '#0f766e'
        title = "Lagging Indicators Improvement/Reduction"

    fig_impact = go.Figure(data=[go.Bar(
        y=chart_data['labels'],
        x=chart_data['data'],
        orientation='h',
        marker_color=color
    )])
    fig_impact.update_layout(
        title_text=title,
        xaxis_title="Avg. % Improvement/Reduction",
        yaxis=dict(autorange="reversed"), # Puts first item at the top
        margin=dict(t=40, b=0, l=0, r=0)
    )
    st.plotly_chart(fig_impact, use_container_width=True)


# --- Tab 4: Prognosis ---
with tab_prognosis:
    st.markdown("""
    The prognosis for companies that adopt a holistic, data-driven well-being strategy is strong. This is not just a "nice-to-have" benefit; it is a core business imperative that drives resilience, innovation, and financial performance. The outcomes are a healthier workforce and a more robust, competitive organization.
    """)
    
    st.subheader("The Business Case for Well-Being")
    
    # Use st.metric in columns for the final stat cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Higher Productivity", 
            value="31%", 
            delta="in high well-being companies", 
            delta_color="off"
        )
    with col2:
        st.metric(
            label="Greater Resilience", 
            value="25%", 
            delta="in teams with supportive managers", 
            delta_color="off"
        )
    with col3:
        st.metric(
            label="Lower Turnover", 
            value="59%", 
            delta="for employees who feel cared for", 
            delta_color="off"
        )

    st.divider()

    with st.container(border=True):
        st.subheader("The Final Verdict")
        st.markdown("""
        A "Cure for the Common Company" means shifting from reactive, generic perks to a proactive, personalized, and data-informed strategy. By focusing on the root causes of burnout and disengagement across the four pillars—Work, Emotion, Leadership, and Lifestyle—organizations can build a resilient, healthy, and high-performing workforce. Analytics are the key to unlocking this potential, providing the insights needed to act effectively and measure what truly matters.
        """)