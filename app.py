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
    # Hero Segment
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
st.subheader("⚙️ Scaffold Optimization Sliders")target_disease = st.selectbox("Pipeline Indication Profiling", ["Oncology (Kinase Domain Pathway)", "CNS Neurology (BBB Target Vector)", "Immunology / Antiviral Blocker"])mol_weight = st.slider("Molecular Weight Footprint (Da)", 100.0, 800.0, 380.0, step=10.0)log_p = st.slider("Hydrophobicity Index (LogP Mapping)", -2.0, 7.0, 2.9, step=0.1)h_donors = st.slider("Reactive Hydrogen Donors", 0, 12, 2)h_acceptors = st.slider("Reactive Hydrogen Acceptors", 0, 20, 5)st.markdown("", unsafe_allowed_html=True)with col2:st.markdown("", unsafe_allowed_html=True)st.subheader("⚖️ Lipinski Filter Compliance Dashboard")w_fail = mol_weight > 500p_fail = log_p > 5d_fail = h_donors > 5a_fail = h_acceptors > 10total_violations = sum([w_fail, p_fail, d_fail, a_fail])c_a, c_b = st.columns(2)with c_a:st.write(f"Mass Boundary (<500 Da): {'❌ Over Limit' if w_fail else '✅ Nominal'} ({mol_weight} Da)")st.write(f"Partition Scale (<5 LogP): {'❌ High Risk' if p_fail else '✅ Nominal'} ({log_p})")with c_b:st.write(f"H-Donors (≤5 States): {'❌ Over Limit' if d_fail else '✅ Nominal'} ({h_donors})")st.write(f"H-Acceptors (≤10 States): {'❌ Over Limit' if a_fail else '✅ Nominal'} ({h_acceptors})")st.write("---")if total_violations <= 1:st.success(f"🎉 Lead Asset Cleared! Compliance Violations: {total_violations}. Structural oral bioavailability is highly favorable.")else:st.error(f"⚠️ Formulation Risk Flagged. Total Compliance Violations: {total_violations}. Synthetic engineering alterations advised.")st.markdown("", unsafe_allowed_html=True)st.write("")st.markdown("", unsafe_allowed_html=True)st.subheader("📊 Multi-Dimensional Structural Radar Signature")categories = ['Mass Profile', 'Hydrophobicity', 'H-Bond Donors', 'H-Bond Acceptors']values = [mol_weight/100, log_p + 2, h_donors, h_acceptors]fig = go.Figure(data=go.Scatterpolar(r=values, theta=categories, fill='toself', line=dict(color='#2563EB')))fig.update_layout(polar=dict(radialaxis=dict(visible=True, gridcolor='#334155')),template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False)st.plotly_chart(fig, use_container_width=True)st.markdown("", unsafe_allowed_html=True)==========================================PAGE 4: BIOMEDICAL AI IMAGE SCANNER==========================================elif app_page == "📡 Biomedical Neural Scanner":st.markdown("📡 Deep-Learning Computer Vision Image Engine", unsafe_allowed_html=True)st.markdown("Simulate localized object tracking maps across healthcare imaging arrays.", unsafe_allowed_html=True)col1, col2 = st.columns([1, 1.2])with col1:st.markdown("", unsafe_allowed_html=True)st.subheader("🖼️ Clinical File Setup")scan_type = st.selectbox("Modality Configuration", ["High-Field MRI (T2-Weighted)", "Volumetric CT Scan Slice", "Ultrasound Matrix Grid Array"])noise_level = st.slider("Input Signal Signal-to-Noise Ratio (SNR)", 0.0, 1.0, 0.15)scan_trigger = st.button("🚀 Boot Autonomous Segmentation Model")st.markdown("", unsafe_allowed_html=True)with col2:st.markdown("", unsafe_allowed_html=True)st.subheader("📡 Real-Time Matrix Inference Model")np.random.seed(42)grid_size = 50x = np.linspace(-3, 3, grid_size)y = np.linspace(-3, 3, grid_size)X, Y = np.meshgrid(x, y)healthy_tissue = np.exp(- (X2 + Y2) / 4)anomaly_spike = 1.6 * np.exp(- ((X - 0.7)**2 + (Y - 0.6)**2) / 0.25)raw_signal = healthy_tissue + anomaly_spike + (np.random.randn(grid_size, grid_size) * noise_level)if scan_trigger:with st.spinner("Executing convolutional element matrices..."):segmented_ai_layer = np.where(raw_signal > 1.1, 2.5, raw_signal)fig = px.imshow(segmented_ai_layer, color_continuous_scale="Viridis", template="plotly_dark")fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')st.plotly_chart(fig, use_container_width=True)st.info("🎯 Localization Complete: Target anomalous density structural variant isolated at quadrant marker vector [X:31, Y:29].")else:fig = px.imshow(raw_signal, color_continuous_scale="Magma", template="plotly_dark")fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')st.plotly_chart(fig, use_container_width=True)st.caption("Awaiting neural execution commands. Use the left dashboard dock activation control trigger.")st.markdown("", unsafe_allowed_html=True)==========================================PAGE 5: LICENSING & TIERS (PRICING)==========================================elif app_page == "💎 Licensing & Tiers":st.markdown("💎 Flexible Licensing for Global Science Teams", unsafe_allowed_html=True)st.markdown("Scale up your drug-discovery pipelines with secure, specialized processing hardware tiers.", unsafe_allowed_html=True)p1, p2, p3 = st.columns(3)with p1:st.markdown("""Academic Sandbox$0 /mo🧬 Base Genome Base-Pair Analysis🧪 4-Parameter Slider Access📡 Standard Heatmap Render Visuals🔒 Secure Database Storage API🚀 Cloud H100 Tensor Boosts""", unsafe_allowed_html=True)st.button("Activate Free Account Key", key="p1_btn", use_container_width=True)with p2:st.markdown("""MOST POPULARBioTech Professional$499 /mo🧬 Unlimited FASTA/DNA Compilations🧪 Extended Bioavailability Rules Analytics📡 Automated Real-Time Scan Isolations🔒 Dedicated Local Cloud Cluster Cache⚡ Priority Server Thread Scheduling""", unsafe_allowed_html=True)st.button("Launch 14-Day Enterprise Trial", key="p2_btn", type="primary", use_container_width=True)with p3:st.markdown("""Global Pharma TierCustom /quote🧬 Full Multi-Tenant Database Portals🧪 Direct AWS S3 Pipeline Relays📡 Complete Clinical Image Arrays Batching🔒 Regulatory HIPAA Compliance Isolation👑 24/7 Dedicated Infrastructure Support""", unsafe_allowed_html=True)st.button("Contact Strategic Relations", key="p3_btn", use_container_width=True
