import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

# --- PREMIUM PAGE & BRAND CONFIGURATION ---
st.set_page_config(
    page_title="HelixVanguard AI | Enterprise Bio-Computing Suite",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CORPORATE REBRANDING STYLES ---
st.markdown("""
<style>
    /* Global Brand Overrides */
    @import url('https://googleapis.com');
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hero Section Component */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 100%);
        padding: 60px 40px;
        border-radius: 16px;
        margin-bottom: 35px;
        border: 1px solid #312E81;
        text-align: center;
    }
    .hero-badge {
        background-color: #2563EB;
        color: white;
        padding: 6px 14px;
        border-radius: 50px;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 1px;
        text-transform: uppercase;
        display: inline-block;
        margin-bottom: 15px;
    }
    .hero-title {
        color: #FFFFFF;
        font-size: 42px;
        font-weight: 700;
        letter-spacing: -1px;
        margin-bottom: 10px;
    }
    .hero-subtitle {
        color: #94A3B8;
        font-size: 18px;
        max-width: 700px;
        margin: 0 auto 25px auto;
        line-height: 1.6;
    }
    
    /* Premium Feature Cards */
    .feature-card {
        background-color: #1E293B;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #334155;
        transition: transform 0.2s ease;
        height: 100%;
    }
    .feature-icon { font-size: 28px; margin-bottom: 15px; }
    .feature-title { color: #F8FAFC; font-size: 18px; font-weight: 600; margin-bottom: 8px; }
    .feature-desc { color: #94A3B8; font-size: 14px; line-height: 1.5; }
    
    /* Corporate Pricing Tables */
    .price-card {
        background-color: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 16px;
        padding: 30px;
        text-align: center;
    }
    .price-card.premium {
        border: 2px solid #2563EB;
        position: relative;
    }
    .price-badge {
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        background-color: #2563EB;
        color: white;
        padding: 3px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
    }
    .price-tier { color: #94A3B8; font-size: 14px; text-transform: uppercase; font-weight: 600; }
    .price-amt { color: #FFFFFF; font-size: 36px; font-weight: 700; margin: 15px 0; }
    .price-features { color: #CBD5E1; font-size: 14px; text-align: left; line-height: 2; margin: 20px 0; list-style-type: none; padding-left: 0;}
    
    /* Dashboard Utility Blocks */
    .dashboard-panel {
        background-color: #0F172A;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1E293B;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allowed_html=True)

# --- NAVIGATION SYSTEM ---
st.sidebar.markdown("<h2 style='color:#2563EB; font-weight:700; margin-bottom:0;'>HELIXVANGUARD</h2>", unsafe_allowed_html=True)
st.sidebar.markdown("<p style='color:#64748B; font-size:12px; text-transform:uppercase; letter-spacing:1px;'>AI Operating Core v4.1</p>", unsafe_allowed_html=True)
st.sidebar.markdown("---")

app_page = st.sidebar.radio(
    "Application Directory",
    ["🏢 Corporate Overview", "🧬 Genomics & Bioinformatics", "🧪 Biochemistry & Therapeutics", "📡 Biomedical Neural Scanner", "💎 Licensing & Tiers"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("⚙️ **Environment Profile**")
st.sidebar.caption("Secure TLS Endpoints Active • Node: Compute-S4")

# ==========================================
# PAGE 1: CORPORATE OVERVIEW (HOME)
# ==========================================
if app_page == "🏢 Corporate Overview":
    st.markdown("""
    <div class='hero-container'>
        <div class='hero-badge'>Next-Gen Deep Tech Platform</div>
        <div class='hero-title'>Accelerating Molecular Discovery via Quantum-AI</div>
        <div class='hero-subtitle'>An enterprise-grade orchestration workspace uniting predictive genomic workflows, autonomous structural biochemistry modeling, and computer-vision clinical asset segmentation.</div>
    </div>
    """, unsafe_allowed_html=True)
    
    st.markdown("### 🌐 Integrated Core Infrastructures")
    st.markdown("Select an analytical pipeline engine from the left navigation tree to run localized compute operations.")
    st.write("")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🧬</div>
            <div class='feature-title'>Genomics Core</div>
            <div class='feature-desc'>Automated FASTA manipulation engines providing localized GC-thermal profiling, instant transcription schemas, and complete single-nucleotide calculation trees.</div>
        </div>
        """, unsafe_allowed_html=True)
    with c2:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🧪</div>
            <div class='feature-title'>Biochemistry Pipeline</div>
            <div class='feature-desc'>Screen small-molecule chemical libraries using multi-parameter structural descriptors. Instantly flags ADME bioavailability risks via Lipinski rule constraints.</div>
        </div>
        """, unsafe_allowed_html=True)
    with c3:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>📡</div>
            <div class='feature-title'>Neural Imaging Scanner</div>
            <div class='feature-desc'>Simulates high-pass deep-learning neural network layers to isolate and identify microscopic architectural tissue anomalies within multi-dimensional imaging arrays.</div>
        </div>
        """, unsafe_allowed_html=True)

# ==========================================
# PAGE 2: GENOMICS & BIOINFORMATICS
# ==========================================
elif app_page == "🧬 Genomics & Bioinformatics":
    st.markdown("<h2 style='color:#FFFFFF; font-weight:700;'>🧬 Genomics & Bioinformatics Parsing Engine</h2>", unsafe_allowed_html=True)
    st.markdown("<p style='color:#94A3B8; margin-bottom:30px;'>Run continuous sequencing tasks, calculate base allocations, and export structural transcript mappings.</p>", unsafe_allowed_html=True)
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("<div class='dashboard-panel'>", unsafe_allowed_html=True)
        st.subheader("📥 Sequence Input Port")
        default_dna = "ATGCGATCGATCGATCGATCGATCGATCGCGGCTATATATGCGCGTATCGCGTA"
        dna_input = st.text_area("Raw Nucleotide Input Array (A, T, C, G)", default_dna, height=180).upper().strip()
        st.markdown("</div>", unsafe_allowed_html=True)
        
        invalid_chars = [char for char in dna_input if char not in "ATCGN"]
        if invalid_chars:
            st.error(f"⚠️ Vector Fault: Invalid characters localized in structure: {set(invalid_chars)}")
        else:
            dna_seq = Seq(dna_input)
            mrna_seq = dna_seq.transcribe()
            protein_seq = dna_seq.translate()
            gc_val = gc_fraction(dna_seq) * 100
            st.success("✅ Sequence successfully registered into cache memory.")

    with col2:
        if not invalid_chars:
            st.markdown("<div class='dashboard-panel'>", unsafe_allowed_html=True)
            st.subheader("📊 Pipeline Analytics Summary")
            
            m1, m2 = st.columns(2)
            m1.metric("Total Structural Bases", f"{len(dna_input)} bp")
            m2.metric("Thermal GC-Stability Profile", f"{gc_val:.2f}%")
            
            st.markdown("<br><b>Target Transcription Sequence (mRNA)</b>", unsafe_allowed_html=True)
            st.code(str(mrna_seq), language="text")
            
            st.markdown("<b>Translated Peptide Chain Configuration</b>", unsafe_allowed_html=True)
            st.code(str(protein_seq), language="text")
            st.markdown("</div>", unsafe_allowed_html=True)

    if not invalid_chars:
        st.write("")
        st.markdown("<div class='dashboard-panel'>", unsafe_allowed_html=True)
        st.subheader("📈 Nucleotide Frequency Visualization Matrix")
        counts = {"Adenine (A)": dna_input.count("A"), "Thymine (T)": dna_input.count("T"), 
                  "Cytosine (C)": dna_input.count("C"), "Guanine (G)": dna_input.count("G")}
        df_counts = pd.DataFrame(list(counts.items()), columns=["Base Pair Element", "Total Count"])
        fig = px.bar(df_counts, x="Base Pair Element", y="Total Count", color="Base Pair Element", 
                     template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Dark24)
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allowed_html=True)

# ==========================================
# PAGE 3: BIOCHEMISTRY & DRUG DISCOVERY
# ==========================================
elif app_page == "🧪 Biochemistry & Therapeutics":
    st.markdown("<h2 style='color:#FFFFFF; font-weight:700;'>🧪 Small-Molecule Lead Discovery Optimization</h2>", unsafe_allowed_html=True)
    st.markdown("<p style='color:#94A3B8; margin-bottom:30px;'>Isolate optimal pharmaceutical compounds by adjusting structural constraints against Lipinski rule filters.</p>", unsafe_allowed_html=True)
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("<div class='dashboard-panel'>", unsafe_allowed_html=True)
