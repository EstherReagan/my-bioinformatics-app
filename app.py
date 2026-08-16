import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Bio-Quantum AI Suite",
    page_icon="🧬",
    layout="wide"
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🧬 Bio-Quantum AI")
app_mode = st.sidebar.radio(
    "Select System Engine:",
    ["1. Genomics & Bioinformatics", "2. Biochemistry & Drug Discovery", "3. Biomedical AI Image Scanner"]
)

st.sidebar.info("💡 No-Code Operator Mode: This web platform runs live data analysis entirely in the cloud.")

# ==========================================
# MODULE 1: GENOMICS & BIOINFORMATICS
# ==========================================
if app_mode == "1. Genomics & Bioinformatics":
    st.title("🧬 Genomics & Bioinformatics Parsing Engine")
    st.write("Analyze raw FASTA/DNA sequences, calculate thermal GC-content stability, and map transcription sequences.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📥 Input Genetic Configuration")
        default_dna = "ATGCGATCGATCGATCGATCGATCGATCGCGGCTATATATGCGCGTATCGCGTA"
        dna_input = st.text_area("Enter Raw DNA Sequence (A, T, C, G)", default_dna, height=150).upper().strip()
        
        invalid_chars = [char for char in dna_input if char not in "ATCGN"]
        if invalid_chars:
            st.error(f"⚠️ Invalid characters detected: {set(invalid_chars)}")
        else:
            dna_seq = Seq(dna_input)
            mrna_seq = dna_seq.transcribe()
            protein_seq = dna_seq.translate()
            gc_val = gc_fraction(dna_seq) * 100
            st.success("✅ Sequence successfully parsed!")

    with col2:
        st.subheader("📊 Primary Sequence Metrics")
        if not invalid_chars:
            m1, m2 = st.columns(2)
            m1.metric("Total Base Pairs", len(dna_input))
            m2.metric("GC-Content Stability", f"{gc_val:.2f}%")
            
            st.markdown("**Transcribed mRNA Sequence:**")
            st.code(str(mrna_seq), language="text")
            
            st.markdown("**Translated Amino Acid Peptide Chain:**")
            st.code(str(protein_seq), language="text")

    if not invalid_chars:
        st.subheader("📈 Nucleotide Frequency Distribution")
        counts = {"Adenine (A)": dna_input.count("A"), "Thymine (T)": dna_input.count("T"), 
                  "Cytosine (C)": dna_input.count("C"), "Guanine (G)": dna_input.count("G")}
        df_counts = pd.DataFrame(list(counts.items()), columns=["Nucleotide", "Count"])
        fig = px.bar(df_counts, x="Nucleotide", y="Count", color="Nucleotide")
        st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MODULE 2: BIOCHEMISTRY & DRUG DISCOVERY
# ==========================================
elif app_mode == "2. Biochemistry & Drug Discovery":
    st.title("🧪 Biochemistry De Novo Drug Design Tool")
    st.write("Calculate Lipinski's Rule of 5 properties to screen small molecules for chemical bioavailability.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🧪 Select Target Pipeline Profile")
        target_disease = st.selectbox("Select Disease Target Vector", ["Oncology (Kinase Inhibitor)", "Neurology", "Antiviral"])
        
        mol_weight = st.slider("Molecular Weight (Da)", 100.0, 800.0, 350.0, step=10.0)
        log_p = st.slider("Octanol-Water Partition Coefficient (LogP)", -2.0, 7.0, 2.5, step=0.1)
        h_donors = st.slider("Hydrogen Bond Donors", 0, 12, 3)
        h_acceptors = st.slider("Hydrogen Bond Acceptors", 0, 20, 6)
        
    with col2:
        st.subheader("⚖️ Lipinski's Rule of 5 Evaluation")
        
        w_fail = mol_weight > 500
        p_fail = log_p > 5
        d_fail = h_donors > 5
        a_fail = h_acceptors > 10
        total_violations = sum([w_fail, p_fail, d_fail, a_fail])
        
        st.write(f"**Molecular Weight (< 500 Da):** {'❌ Fail' if w_fail else '✅ Pass'} ({mol_weight} Da)")
        st.write(f"**LogP Partition (< 5):** {'❌ Fail' if p_fail else '✅ Pass'} ({log_p})")
        st.write(f"**H-Bond Donors (≤ 5):** {'❌ Fail' if d_fail else '✅ Pass'} ({h_donors})")
        st.write(f"**H-Bond Acceptors (≤ 10):** {'❌ Fail' if a_fail else '✅ Pass'} ({h_acceptors})")
        
        if total_violations <= 1:
            st.success(f"🎉 Drug Candidate Viable! Total Violations: {total_violations}.")
        else:
            st.error(f"⚠️ Low Oral Bioavailability Risk! Total Violations: {total_violations}.")

    st.subheader("📊 Molecular Structural Fingerprint Radar")
    categories = ['Mol Weight', 'LogP', 'H-Bond Donors', 'H-Bond Acceptors']
    values = [mol_weight/100, log_p + 2, h_donors, h_acceptors]
    
    fig = go.Figure(data=go.Scatterpolar(r=values, theta=categories, fill='toself'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MODULE 3: BIOMEDICAL AI IMAGE SCANNER
# ==========================================
elif app_mode == "3. Biomedical AI Image Scanner":
    st.title("📡 Biomedical AI & Healthcare Imaging Suite")
    st.write("Simulates a computer-vision neural network highlighting deep structural tissue density spikes or anomalies.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🖼️ Diagnostic Loading Dock")
        scan_type = st.selectbox("Select Diagnostics Domain", ["MRI Scan", "CT Scan", "Ultrasound Matrix Array"])
        noise_level = st.slider("Neural Network Signal Noise Filter", 0.0, 1.0, 0.2)
        scan_trigger = st.button("🚀 Execute AI Automated Tissue Segmentation")
        
    with col2:
        st.subheader("📡 Neural Processing Viewport")
        
        np.random.seed(42)
        grid_size = 50
        x = np.linspace(-3, 3, grid_size)
        y = np.linspace(-3, 3, grid_size)
        X, Y = np.meshgrid(x, y)
        
        healthy_tissue = np.exp(- (X**2 + Y**2) / 4)
        anomaly_spike = 1.5 * np.exp(- ((X - 0.8)**2 + (Y - 0.7)**2) / 0.3)
        raw_signal = healthy_tissue + anomaly_spike + (np.random.randn(grid_size, grid_size) * noise_level)
        
        if scan_trigger:
            with st.spinner("Running AI computer vision matrix evaluations..."):
                segmented_ai_layer = np.where(raw_signal > 1.1, 2.0, raw_signal)
                fig = px.imshow(segmented_ai_layer, color_continuous_scale="Jet")
                st.plotly_chart(fig, use_container_width=True)
                st.info("🎯 AI Diagnostics Alert Vector: Cluster detected. High-intensity density spikes indicate localized tissue anomalies.")
        else:
            fig = px.imshow(raw_signal, color_continuous_scale="Viridis")
            st.plotly_chart(fig, use_container_width=True)
