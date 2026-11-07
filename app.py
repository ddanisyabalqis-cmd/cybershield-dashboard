import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CYBERSHIELD",
    page_icon="🔐",
    layout="wide"
)

# TAJUK
st.title("🔐 CYBERSHIELD")
st.subheader("Student Cyber Risk Dashboard")

st.write(
    "Analysing students' cybersecurity awareness "
    "and promoting safer online habits."
)

# DATA SURVEY
data = {
    "Same Password": {"Yes": 13, "No": 24},
    "Suspicious Links": {"Yes": 4, "No": 32, "Sometimes": 1},
    "Personal Information": {"Yes": 3, "No": 34},
    "Public Wi-Fi": {
        "Yes": 12, "No": 19, "Sometimes": 2,
        "I do not use public Wi-Fi": 1,
        "Sometimes (capital S)": 1,
        "Almost everyday": 1,
        "Rarely": 1
    },
    "Two-Factor Authentication": {"Yes": 9, "No": 28},
    "Password Updates": {
        "Yes": 15, "No": 15, "Blank": 1,
        "More than once": 1, "When needed": 1,
        "Sometimes": 1, "Sometimes when bored": 1,
        "When forgotten": 1, "3 times a year": 1
    },
    "Phishing Awareness": {
        "Yes": 13, "No": 3, "Not sure": 20
    },
    "Weak Passwords": {"Yes": 5, "No": 32}
}

# MENU
page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Home",
        "Dashboard Overview",
        "Survey Analysis",
        "Risk Analysis",
        "Recommendations",
        "About CYBERSHIELD"
    ]
)

# HOME
if page == "Home":
    st.title("Welcome to CYBERSHIELD 🛡️")
    st.write(
        "A student-focused cybersecurity dashboard "
        "that analyses online safety habits."
    )

    st.info(
        "Our mission is to increase cybersecurity "
        "awareness among students."
    )

    st.subheader("Project Objectives")
    st.write("• Analyse cybersecurity awareness.")
    st.write("• Identify common online safety concerns.")
    st.write("• Provide useful security recommendations.")
    st.write("• Encourage safer digital behaviour.")

# DASHBOARD
elif page == "Dashboard Overview":
    st.header("📊 Dashboard Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Respondents", "37")
    c2.metric("No 2FA", "75.7%")
    c3.metric("Not Sure About Phishing", "55.6%")
    c4.metric("Reuse Passwords", "35.1%")

    st.subheader("Key Findings")

    st.write("• 28 students do not use 2FA.")
    st.write("• 20 students are unsure about phishing.")
    st.write("• 13 students reuse passwords.")
    st.write("• 5 students report using weak passwords.")

    st.caption(
        "Survey results are self-reported. "
        "Phishing awareness has 36 responses."
    )

# SURVEY ANALYSIS
elif page == "Survey Analysis":
    st.header("📈 Survey Analysis")

    for question, answers in data.items():
        st.subheader(question)

        chart_data = pd.DataFrame(
            list(answers.items()),
            columns=["Answer", "Count"]
        )

        st.bar_chart(
            chart_data.set_index("Answer")
        )

        st.dataframe(
            chart_data,
            hide_index=True,
            use_container_width=True
        )

    st.warning(
        "Public Wi-Fi and password-update answers "
        "contain mixed response formats. "
        "Interpret these results carefully."
    )

# RISK ANALYSIS
elif page == "Risk Analysis":
    st.header("🚨 Cybersecurity Priority Analysis")

    risk = pd.DataFrame({
        "Issue": [
            "No Two-Factor Authentication",
            "Not Sure About Phishing",
            "Same Password Reuse",
            "Weak Passwords"
        ],
        "Percentage": [75.7, 55.6, 35.1, 13.5],
        "Priority": [
            "High",
            "High",
            "Medium",
            "Low"
        ]
    })

    st.dataframe(
        risk,
        hide_index=True,
        use_container_width=True
    )

    st.bar_chart(
        risk.set_index("Issue")["Percentage"]
    )

    st.caption(
        "Priority levels are action priorities based "
        "on project thresholds, not validated individual "
        "cyber risk scores."
    )

# RECOMMENDATIONS
elif page == "Recommendations":
    st.header("🛡️ Security Recommendations")

    st.subheader("1. Use Strong Passwords")
    st.write("Create unique passwords for different accounts.")

    st.subheader("2. Enable Two-Factor Authentication")
    st.write("Add another layer of account protection.")

    st.subheader("3. Identify Phishing")
    st.write("Check links and senders before clicking.")

    st.subheader("4. Protect Personal Information")
    st.write("Avoid sharing sensitive information publicly.")

    st.subheader("5. Use Public Wi-Fi Carefully")
    st.write("Avoid accessing sensitive accounts on unsecured networks.")

# ABOUT
elif page == "About CYBERSHIELD":
    st.header("About Our Project")

    st.write(
        "CYBERSHIELD is a student cybersecurity "
        "awareness project developed to understand "
        "online safety habits."
    )

    st.subheader("Data Information")
    st.write("• 37 survey respondents.")
    st.write("• 8 cybersecurity survey questions.")
    st.write("• Results are based on self-reported answers.")
    st.write("• One missing response for phishing awareness.")

    st.info(
        "CYBERSHIELD is an educational awareness tool. "
        "It does not detect cyberattacks or measure "
        "individual students' actual security."
    )

# FOOTER
st.divider()
st.caption("CYBERSHIELD | Student Cyber Risk Dashboard")
