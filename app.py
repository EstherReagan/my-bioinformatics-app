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

# --- NAVIGATION SYSTEM ---
st.sidebar.title("🧬 HELIXVANGUARD")
st.sidebar.caption("AI Operating Core v4.1")
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
    st.title("🚀 Accelerating Molecular Discovery via Quantum-AI")
    st.markdown("### **Enterprise-grade orchestration workspace uniting predictive genomic workflows, autonomous structural biochemistry modeling, and computer-vision clinical asset segmentation.**")
    st.markdown("---")
    
    st.subheader("🌐 Integrated Core Infrastructures")
    st.write("Select an analytical pipeline engine from the left navigation tree to run localized compute operations.")
    st.write("")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.markdown("### 🧬 Genomics Core")
            st.write("Automated FASTA manipulation engines providing localized GC-thermal profiling, instant transcription schemas, and complete single-nucleotide calculation trees.")
    with c2:
        with st.container(border=True):
            st.markdown("### 🧪 Biochemistry Pipeline")
            st.write("Screen small-molecule chemical libraries using multi-parameter structural descriptors. Instantly flags ADME bioavailability risks via Lipinski rule constraints.")
    with c3:
        with st.container(border=True):
            st.markdown("### 📡 Neural Imaging Scanner")
            st.write("Simulates high-pass deep-learning neural network layers to isolate and identify microscopic architectural tissue anomalies within multi-dimensional imaging arrays.")

# ==========================================
# PAGE 2: GENOMICS & BIOINFORMATICS
# ==========================================
elif app_page == "🧬 Genomics & Bioinformatics":
    st.title("🧬 Genomics & Bioinformatics Parsing Engine")
    st.write("Run continuous sequencing tasks, calculate base allocations, and export structural transcript mappings.")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        with st.container(border=True):
            st.subheader("📥 Sequence Input Port")
            default_dna = "ATGCGATCGATCGATCGATCGATCGATCGCGGCTATATATGCGCGTATCGCGTA"
            dna_input = st.text_area("Raw Nucleotide Input Array (A, T, C, G)", default_dna, height=180).upper().strip()
        
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
            with st.container(border=True):
                st.subheader("📊 Pipeline Analytics Summary")
                
                m1, m2 = st.columns(2)
                m1.metric("Total Structural Bases", f"{len(dna_input)} bp")
                m2.metric("Thermal GC-Stability Profile", f"{gc_val:.2f}%")
                
                st.markdown("<br><b>Target Transcription Sequence (mRNA)</b>", unsafe_allowed_html=True)
                st.code(str(mrna_seq), language="text")
                
                st.markdown("<b>Translated Peptide Chain Configuration</b>", unsafe_allowed_html=True)
                st.code(str(protein_seq), language="text")

    if not invalid_chars:
        st.write("")
        with st.container(border=True):
            st.subheader("📈 Nucleotide Frequency Visualization Matrix")
            counts = {"Adenine (A)": dna_input.count("A"), "Thymine (T)": dna_input.count("T"), 
                      "Cytosine (C)": dna_input.count("C"), "Guanine (G)": dna_input.count("G")}
            df_counts = pd.DataFrame(list(counts.items()), columns=["Base Pair Element", "Total Count"])
            fig = px.bar(df_counts, x="Base Pair Element", y="Total Count", color="Base Pair Element", 
                         template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)

# ==========================================
# PAGE 3: BIOCHEMISTRY & DRUG DISCOVERY
# ==========================================
elif app_page == "🧪 Biochemistry & Therapeutics":
    st.title("🧪 Small-Molecule Lead Discovery Optimization")
    st.write("Isolate optimal pharmaceutical compounds by adjusting structural constraints against Lipinski rule filters.")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        with st.container(border=True):
            st.subheader("⚙️ Scaffold Optimization Sliders")
            target_disease = st.selectbox("Pipeline Indication Profiling", ["Oncology (Kinase Domain Pathway)", "CNS Neurology (BBB Target Vector)", "Immunology / Antiviral Blocker"])
            
            mol_weight = st.slider("Molecular Weight Footprint (Da)", 100.0, 800.0, 380.0, step=10.0)
            log_p = st.slider("Hydrophobicity Index (LogP Mapping)", -2.0, 7.0, 2.9, step=0.1)
            h_donors = st.slider("Reactive Hydrogen Donors", 0, 12, 2)
            h_acceptors = st.slider("Reactive Hydrogen Acceptors", 0, 20, 5)
        
    with col2:
        with st.container(border=True):
            st.subheader("⚖️ Lipinski Filter Compliance Dashboard")
            
            w_fail = mol_weight > 500
            p_fail = log_p > 5
            d_fail = h_donors > 5
            a_fail = h_acceptors > 10
            total_violations = sum([w_fail, p_fail, d_fail, a_fail])
            
            c_a, c_b = st.columns(2)
            with c_a:
                st.write(f"**Mass Boundary (<500 Da):** {'❌ Over Limit' if w_fail else '✅ Nominal'} ({mol_weight} Da)")
                st.write(f"**Partition Scale (<5 LogP):** {'❌ High Risk' if p_fail else '✅ Nominal'} ({log_p})")
            with c_b:
                st.write(f"**H-Donors (≤5 States):** {'❌ Over Limit' if d_fail else '✅ Nominal'} ({h_donors})")
                st.write(f"**H-Acceptors (≤10 States):** {'❌ Over Limit' if a_fail else '✅ Nominal'} ({h_acceptors})")
            
            st.write("---")
            if total_violations <= 1:
                st.success(f"🎉 Lead Asset Cleared! Compliance Violations: {total_violations}. Structural oral bioavailability is highly favorable.")
            else:
                st.error(f"⚠️ Formulation Risk Flagged. Total Compliance Violations: {total_violations}. Synthetic engineering alterations advised.")

    st.write("")
    with st.container(border=True):
        st.subheader("📊 Multi-Dimensional Structural Radar Signature")
        categories = ['Mass Profile', 'Hydrophobicity', 'H-Bond Donors', 'H-Bond Acceptors']
        values = [mol_weight/100, log_p + 2, h_donors, h_acceptors]
        
        fig = go.Figure(data=go.Scatterpolar(r=values, theta=categories, fill='toself', line=dict(color='#2563EB')))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, gridcolor='#334155')), 
                          template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

# ==========================================
# PAGE 4: BIOMEDICAL AI IMAGE SCANNER
# ==========================================
elif app_page == "📡 Biomedical Neural Scanner":
    st.title("📡 Deep-Learning Computer Vision Image Engine")
    st.write("Simulate localized object tracking maps across healthcare imaging arrays.")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        with st.container(border=True):
            st.subheader("🖼️ Clinical File Setup")
            scan_type = st.selectbox("Modality Configuration", ["High-Field MRI (T2-Weighted)", "Volumetric CT Scan Slice", "Ultrasound Matrix Grid Array"])
            noise_level = st.slider("Input Signal Signal-to-Noise Ratio (SNR)", 0.0, 1.0, 0.15)
            scan_trigger = st.button("🚀 Boot Autonomous Segmentation Model")
        
    with col2:
        with st.container(border=True):
            st.subheader("📡 Real-Time Matrix Inference Model")
            
            np.random.seed(42)
            grid_size = 50
            x = np.linspace(-3, 3, grid_size)
            y = np.linspace(-3, 3, grid_size)
            X, Y = np.meshgrid(x, y)
            
            healthy_tissue = np.exp(- (X**2 + Y**2) / 4)
            anomaly_spike = 1.6 * np.exp(- ((X - 0.7)**2 + (Y - 0.6)**2) / 0.25)
            raw_signal = healthy_tissue + anomaly_spike + (np.random.randn(grid_size, grid_size) * noise_level)
            
            if scan_trigger:
                with st.spinner("Executing convolutional element matrices..."):
                    segmented_ai_layer = np.where(raw_signal > 1.1, 2.5, raw_signal)
