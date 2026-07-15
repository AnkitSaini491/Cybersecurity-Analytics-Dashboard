import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# CYBERSECURITY DATA USING PANDAS
# ==========================================

security = {
    "Month": [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ],

    "Threats": [45,52,60,75,68,82,90,88,96,105,110,120],

    "Malware": [8,10,12,15,13,18,20,19,22,24,25,28],

    "FailedLogins": [120,140,165,180,210,235,250,245,270,290,310,340],

    "NetworkTraffic": [250,270,290,320,340,360,390,410,430,450,470,500],

    "CriticalAlerts": [2,3,4,5,4,6,7,8,8,9,10,11],

    "BlockedAttacks": [30,35,40,50,48,55,60,63,67,70,75,82],

    "SecurityScore": [92,91,90,89,90,88,87,88,86,85,84,83]
}

df = pd.DataFrame(security)

# ==========================================
# KPI VALUES
# ==========================================

total_threats = df["Threats"].sum()

total_malware = df["Malware"].sum()

total_failed = df["FailedLogins"].sum()

total_blocked = df["BlockedAttacks"].sum()

total_alerts = df["CriticalAlerts"].sum()

avg_security = df["SecurityScore"].mean()

# ==========================================
# DARK THEME
# ==========================================

plt.style.use("dark_background")

fig = plt.figure(figsize=(20,12))

fig.patch.set_facecolor("#101820")

fig.suptitle(
    "CYBERSECURITY ANALYTICS DASHBOARD",
    fontsize=26,
    fontweight="bold",
    color="white",
    y=0.98
)

# ==========================================
# KPI CARDS
# ==========================================

plt.figtext(
    0.02,0.89,
    f"Threats\n{total_threats}",
    fontsize=14,
    bbox=dict(facecolor="#e74c3c",boxstyle="round,pad=0.7")
)

plt.figtext(
    0.18,0.89,
    f"Malware\n{total_malware}",
    fontsize=14,
    bbox=dict(facecolor="#9b59b6",boxstyle="round,pad=0.7")
)

plt.figtext(
    0.34,0.89,
    f"Failed Logins\n{total_failed}",
    fontsize=14,
    bbox=dict(facecolor="#3498db",boxstyle="round,pad=0.7")
)

plt.figtext(
    0.50,0.89,
    f"Blocked Attacks\n{total_blocked}",
    fontsize=14,
    bbox=dict(facecolor="#27ae60",boxstyle="round,pad=0.7")
)

plt.figtext(
    0.66,0.89,
    f"Critical Alerts\n{total_alerts}",
    fontsize=14,
    bbox=dict(facecolor="#f39c12",boxstyle="round,pad=0.7")
)

plt.figtext(
    0.82,0.89,
    f"Security Score\n{avg_security:.1f}%",
    fontsize=14,
    bbox=dict(facecolor="#16a085",boxstyle="round,pad=0.7")
)

# ==========================================
# CHART 1 - THREAT TREND
# ==========================================

ax1 = plt.subplot(3,2,1)

ax1.plot(
    df["Month"],
    df["Threats"],
    marker="o",
    linewidth=3,
    color="red"
)

ax1.fill_between(
    df["Month"],
    df["Threats"],
    color="red",
    alpha=0.30
)

ax1.set_title("Threat Detection Trend")
ax1.set_ylabel("Threats")
ax1.grid(alpha=0.3)
ax1.tick_params(axis="x", rotation=45)
# ==========================================
# CHART 2 - MALWARE DETECTION
# ==========================================

ax2 = plt.subplot(3,2,2)

ax2.bar(
    df["Month"],
    df["Malware"],
    color="purple"
)

ax2.set_title("Malware Detection")
ax2.set_ylabel("Detected Malware")
ax2.grid(alpha=0.3)
ax2.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 3 - FAILED LOGIN ATTEMPTS
# ==========================================

ax3 = plt.subplot(3,2,3)

ax3.plot(
    df["Month"],
    df["FailedLogins"],
    marker="o",
    linewidth=3,
    color="orange"
)

ax3.fill_between(
    df["Month"],
    df["FailedLogins"],
    color="orange",
    alpha=0.30
)

ax3.set_title("Failed Login Attempts")
ax3.set_ylabel("Attempts")
ax3.grid(alpha=0.3)
ax3.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 4 - CRITICAL ALERTS
# ==========================================

ax4 = plt.subplot(3,2,4)

ax4.bar(
    df["Month"],
    df["CriticalAlerts"],
    color="red"
)

ax4.set_title("Critical Security Alerts")
ax4.set_ylabel("Alerts")
ax4.grid(alpha=0.3)
ax4.tick_params(axis="x", rotation=45)


# ==========================================
# CHART 5 - THREAT DISTRIBUTION
# ==========================================

ax5 = plt.subplot(3,2,5)

threat_data = [
    df["Threats"].sum(),
    df["Malware"].sum(),
    df["BlockedAttacks"].sum()
]

labels = [
    "Threats",
    "Malware",
    "Blocked"
]

colors = [
    "#ff4d4d",
    "#9b59b6",
    "#2ecc71"
]

ax5.pie(
    threat_data,
    labels=labels,
    autopct="%1.1f%%",
    colors=colors,
    startangle=90
)

ax5.set_title("Threat Distribution")


# ==========================================
# CHART 6 - NETWORK TRAFFIC
# ==========================================

ax6 = plt.subplot(3,2,6)

ax6.plot(
    df["Month"],
    df["NetworkTraffic"],
    marker="o",
    linewidth=3,
    color="cyan"
)

ax6.fill_between(
    df["Month"],
    df["NetworkTraffic"],
    color="cyan",
    alpha=0.30
)

ax6.set_title("Network Traffic")
ax6.set_ylabel("Traffic (GB)")
ax6.grid(alpha=0.3)
ax6.tick_params(axis="x", rotation=45)

# ==========================================
# CHART 7 - SECURITY SCORE TREND
# ==========================================

plt.figure(figsize=(10,5))
plt.style.use("dark_background")

plt.plot(
    df["Month"],
    df["SecurityScore"],
    marker="o",
    linewidth=3,
    color="lime"
)

plt.fill_between(
    df["Month"],
    df["SecurityScore"],
    color="lime",
    alpha=0.30
)

plt.title("Security Score Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Security Score (%)")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# DEVICE RISK ANALYSIS
# ==========================================

device_data = {
    "Device": ["Servers","Workstations","Laptops","Mobiles","IoT"],
    "Threats": [42,35,28,18,12]
}

device_df = pd.DataFrame(device_data)

plt.figure(figsize=(8,5))
plt.style.use("dark_background")

plt.bar(
    device_df["Device"],
    device_df["Threats"],
    color="tomato"
)

plt.title("Device Risk Analysis")
plt.ylabel("Detected Threats")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# COUNTRY-WISE ATTACKS
# ==========================================

country_data = {
    "Country":[
        "USA",
        "China",
        "Russia",
        "India",
        "Germany",
        "Brazil"
    ],

    "Attacks":[
        320,
        280,
        260,
        210,
        170,
        150
    ]
}

country_df = pd.DataFrame(country_data)

plt.figure(figsize=(9,5))
plt.style.use("dark_background")

plt.barh(
    country_df["Country"],
    country_df["Attacks"],
    color="cyan"
)

plt.title("Country-wise Attack Analysis")
plt.xlabel("Detected Attacks")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()


# ==========================================
# ATTACK SEVERITY
# ==========================================

severity = {
    "Severity":["Critical","High","Medium","Low"],
    "Count":[42,95,180,320]
}

severity_df = pd.DataFrame(severity)

plt.figure(figsize=(7,7))
plt.style.use("dark_background")

plt.pie(
    severity_df["Count"],
    labels=severity_df["Severity"],
    autopct="%1.1f%%",
    startangle=90,
    colors=[
        "#ff0000",
        "#ff8c00",
        "#ffd700",
        "#32cd32"
    ]
)

plt.title("Attack Severity Distribution")

plt.tight_layout()
plt.show()


# ==========================================
# SECURITY SUMMARY
# ==========================================

print("="*60)
print("CYBERSECURITY ANALYTICS SUMMARY")
print("="*60)

print(f"Total Threats          : {total_threats}")
print(f"Blocked Attacks        : {total_blocked}")
print(f"Malware Detected       : {total_malware}")
print(f"Failed Logins          : {total_failed}")
print(f"Critical Alerts        : {total_alerts}")
print(f"Average Security Score : {avg_security:.2f}%")

print("="*60)


# ==========================================
# SAVE DASHBOARD
# ==========================================

fig.savefig(
    "cybersecurity_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDashboard saved as cybersecurity_dashboard.png")


# ==========================================
# PROJECT INFO
# ==========================================

print("\nProject Name : Cybersecurity Analytics Dashboard")
print("Technology   : Python | Pandas | Matplotlib")
print("Status       : Dashboard Generated Successfully")


# ==========================================
# FOOTER
# ==========================================

plt.figtext(
    0.30,
    0.02,
    "Developed using Python | Pandas | Matplotlib",
    fontsize=11,
    color="white"
)

plt.show()
