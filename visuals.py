import streamlit as st
import plotly.express as px

# ==========================================
# 1. GLOBAL CSS INJECTION (Glassmorphism & Antigravity)
# ==========================================
def inject_global_css():
    """
    Injects custom CSS to override Streamlit's native styling.
    Features: Dark mode, glassmorphism, antigravity hover animations,
    styled input widgets, custom sidebar, and customized scrollbars.
    """
    custom_css = """
    <style>
        /* Hide Streamlit Default UI Headers and Footers */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stDeployButton {display:none;}
        
        /* App Background */
        .stApp {
            background-color: #0b0b0f;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(93, 63, 211, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(20, 184, 166, 0.05) 0%, transparent 40%),
                radial-gradient(circle at 50% 50%, #0b0b0f 0%, #050507 100%);
            color: #ffffff;
            font-family: 'Outfit', 'Inter', -apple-system, sans-serif;
        }

        /* Antigravity Floating Animation */
        @keyframes antigravity {
            0% { transform: translateY(0px); box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4); }
            50% { transform: translateY(-6px); box-shadow: 0 16px 40px 0 rgba(93, 63, 211, 0.15); }
            100% { transform: translateY(0px); box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4); }
        }

        /* Glassmorphism Card Base */
        .glass-card {
            background: rgba(18, 18, 26, 0.55);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 20px;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }

        .glass-card:hover {
            border: 1px solid rgba(139, 92, 246, 0.3);
            animation: antigravity 5s ease-in-out infinite;
        }

        /* Custom Metric Styling */
        .metric-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }
        .metric-label {
            font-size: 0.8rem;
            color: #9ca3af;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            font-weight: 700;
        }
        .metric-icon { 
            font-size: 1.3rem; 
            padding: 6px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.04);
        }
        .metric-value {
            font-size: 2.4rem;
            font-weight: 800;
            color: #ffffff;
            margin: 0;
            line-height: 1.1;
            letter-spacing: -0.5px;
            background: linear-gradient(135deg, #ffffff 60%, #a78bfa 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .metric-delta { font-size: 0.85rem; font-weight: 600; margin-top: 8px;}
        .delta-positive { color: #10b981; } /* Green */
        .delta-negative { color: #f43f5e; } /* Red */
        .delta-neutral { color: #9ca3af; }

        /* Empty State Styling */
        .empty-state {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 48px 24px;
            text-align: center;
            background: rgba(18, 18, 26, 0.25);
            border: 1px dashed rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            backdrop-filter: blur(8px);
        }
        .empty-icon { font-size: 3.5rem; opacity: 0.4; margin-bottom: 16px; filter: grayscale(100%); }
        .empty-title { font-size: 1.2rem; font-weight: 700; color: #ffffff; margin-bottom: 6px; }
        .empty-text { font-size: 0.9rem; color: #9ca3af; max-width: 320px; line-height: 1.4; }

        /* Custom Glassmorphism Input styling overrides */
        .stTextInput input, .stNumberInput input, .stTextArea textarea, .stSelectbox select {
            background-color: rgba(18, 18, 26, 0.7) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 12px !important;
            transition: all 0.2s ease !important;
        }
        .stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus {
            border-color: #8b5cf6 !important;
            box-shadow: 0 0 10px rgba(139, 92, 246, 0.25) !important;
        }

        /* Streamlit Button Overrides */
        div.stButton > button {
            background: rgba(255, 255, 255, 0.03) !important;
            color: #ffffff !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            border-radius: 12px !important;
            padding: 10px 20px !important;
            font-weight: 600 !important;
            transition: all 0.2s ease !important;
            width: 100%;
        }
        div.stButton > button:hover {
            background: rgba(139, 92, 246, 0.15) !important;
            border-color: #8b5cf6 !important;
            transform: translateY(-2px);
        }
        div.stButton > button:active {
            transform: translateY(0px);
        }

        /* Streamlit Primary Button Overrides */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #7c3aed 0%, #4f46e5 100%) !important;
            border: none !important;
            box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3) !important;
        }
        div.stButton > button[kind="primary"]:hover {
            box-shadow: 0 6px 20px rgba(124, 58, 237, 0.45) !important;
            filter: brightness(1.1);
        }

        /* Custom Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #08080c !important;
            border-right: 1px solid rgba(255, 255, 255, 0.06) !important;
        }
        section[data-testid="stSidebar"] .stButton > button {
            text-align: left !important;
            background: transparent !important;
            border: 1px solid transparent !important;
            padding: 8px 16px !important;
            margin-bottom: 4px !important;
        }
        section[data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(255, 255, 255, 0.03) !important;
            border-color: rgba(255, 255, 255, 0.08) !important;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0b0b0f;
        }
        ::-webkit-scrollbar-thumb {
            background: #1f1f2e;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #2e2e42;
        }

        /* Habit item row */
        .habit-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 16px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: 12px;
            margin-bottom: 8px;
        }

        /* Glow effects */
        .text-glow-purple {
            text-shadow: 0 0 10px rgba(139, 92, 246, 0.5);
        }
        .text-glow-teal {
            text-shadow: 0 0 10px rgba(20, 184, 166, 0.5);
        }

        /* Specific override for Back to Home button */
        .back-home-wrapper button {
            background: rgba(139, 92, 246, 0.06) !important;
            color: #a78bfa !important;
            border: 1px solid rgba(139, 92, 246, 0.3) !important;
            border-radius: 30px !important;
            padding: 8px 18px !important;
            font-size: 0.85rem !important;
            letter-spacing: 0.5px !important;
            box-shadow: 0 0 12px rgba(139, 92, 246, 0.08) !important;
            backdrop-filter: blur(8px) !important;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
            width: auto !important;
            display: inline-flex !important;
            align-items: center !important;
            justify-content: center !important;
            float: right;
        }
        .back-home-wrapper button:hover {
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(20, 184, 166, 0.15) 100%) !important;
            border-color: #14b8a6 !important;
            color: #ffffff !important;
            box-shadow: 0 0 18px rgba(20, 184, 166, 0.25) !important;
            transform: translateY(-2px) !important;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# ==========================================
# 2. CUSTOM METRICS (Replaces st.metric)
# ==========================================
def render_glass_metric(label, value, icon="⚡", delta=None, delta_text="vs yesterday", invert_colors=False):
    """
    Renders a premium glassmorphism metric card.
    invert_colors=True is useful for Screen Time or Bad Habits (where negative delta is good).
    """
    delta_html = ""
    if delta is not None:
        if delta > 0:
            color_class = "delta-negative" if invert_colors else "delta-positive"
            sign = "+"
        elif delta < 0:
            color_class = "delta-positive" if invert_colors else "delta-negative"
            sign = ""
        else:
            color_class = "delta-neutral"
            sign = ""
        
        delta_html = f'<div class="metric-delta {color_class}">{sign}{delta} {delta_text}</div>'

    html = f"""
    <div class="glass-card">
        <div class="metric-header">
            <span class="metric-label">{label}</span>
            <span class="metric-icon">{icon}</span>
        </div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# ==========================================
# 3. PLOTLY CHART WRAPPER (Replaces st.line_chart)
# ==========================================
def style_glass_fig(fig):
    """
    Strips gridlines, backgrounds, and native styling from a Plotly figure
    to make it seamlessly blend into the dark glassmorphism UI.
    """
    fig.update_layout(
        # Transparent backgrounds
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#9ca3af", family="sans-serif", size=11),
        margin=dict(l=15, r=15, t=30, b=15),
        # Premium hover tooltips
        hoverlabel=dict(
            bgcolor="rgba(18, 18, 26, 0.95)", 
            font_size=13, 
            font_color="#ffffff",
            font_family="sans-serif",
            bordercolor="rgba(139, 92, 246, 0.3)"
        ),
        legend=dict(
            orientation="h", 
            yanchor="bottom", 
            y=1.02, 
            xanchor="right", 
            x=1,
            font=dict(size=10)
        )
    )
    
    # Strip X axis grid and zero lines
    fig.update_xaxes(
        showgrid=False, 
        zeroline=False, 
        showline=False,
        tickcolor="rgba(255,255,255,0.08)",
        linecolor="rgba(255,255,255,0.08)"
    )
    
    # Keep subtle grid for comparison charts or strip for sparklines
    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.03)",
        zeroline=False, 
        showline=False,
        tickcolor="rgba(255,255,255,0.08)"
    )
    
    return fig

def style_sparkline_fig(fig):
    """Strips all axes and labels for a clean sparkline look."""
    fig = style_glass_fig(fig)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    fig.update_xaxes(showticklabels=False)
    return fig

# ==========================================
# 4. EMPTY STATES (Replaces st.warning)
# ==========================================
def render_empty_state(title="No Data Yet", message="Start logging your habits to see insights.", icon="📭"):
    """
    Renders a premium zero-state placeholder when a dataframe is empty.
    """
    html = f"""
    <div class="empty-state">
        <div class="empty-icon">{icon}</div>
        <div class="empty-title">{title}</div>
        <div class="empty-text">{message}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
