import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Multi-Disciplinary Bio-Quantum AI Suite",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS STYLING ---
st.markdown("""
<style>
    .main-title { font-size: 32px; font-weight: bold; color: #2E5BFF; margin-bottom: 5px; }
    .sub-title { font-size: 16px; color: #666; margin-bottom: 25px; }
    .metric-card { background-color: #F8F9FA; padding: 15px; border-radius: 8px; border-left: 5px solid #2E5BFF; }
</style>
""", unsafe_allowed_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🧬 Bio-Quantum AI")
st.sidebar.markdown("---")
app_mode = st.sidebar.radio(
    "Select System Engine:",
    ["1. Genomics & Bioinformatics", "2. Biochemistry & Drug Discovery", "3. Biomedical AI Image Scanner"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **No-Code Operator Mode:** This web platform runs live data analysis and predictive simulations entirely in the cloud.")

# ==========================================
# MODULE 1: GENOMICS & BIOINFORMATICS
# ==========================================
if app_mode == "1. Genomics & Bioinformatics":
    st.markdown("<div class='main-title'>Genomics & Bioinformatics Parsing Engine</div>", unsafe_allowed_html=True)
    st.markdown("<div class='sub-title'>Analyze raw FASTA/DNA sequences, calculate thermal GC-content stability, and map transcription sequences.</div>", unsafe_allowed_html=True)
    
    col1, col2 = st.columns()
    
    with col1:
        st.subheader("📥 Input Genetic Configuration")
        default_dna = "ATGCGATCGATCGATCGATCGATCGATCGCGGCTATATATGCGCGTATCGCGTA"
        dna_input = st.text_area("Enter Raw DNA Sequence (A, T, C, G)", default_dna, height=150).upper().strip()
        
        # Validation
        invalid_chars = [char for char in dna_input if char not in "ATCGN"]
        if invalid_chars:
            st.error(f"⚠️ Invalid characters detected in sequence: {set(invalid_chars)}")
        else:
            # Calculations via BioPython
            dna_seq = Seq(dna_input)
            mrna_seq = dna_seq.transcribe()
            protein_seq = dna_seq.translate()
            gc_val = gc_fraction(dna_seq) * 100
            
            st.success("✅ Sequence successfully parsed!")

    with col2:
        st.subheader("📊 Primary Sequence Metrics")
        if not invalid_chars:
            m1, m2, m3 = st.columns(3)
            with m1:
                st.metric("Total Base Pairs", len(dna_input))
            with m2:
                st.metric("GC-Content Stability", f"{gc_val:.2f}%")
            with m3:
                st.metric("Molecular Weight approx", f"{len(dna_input) * 329.2:.1f} Da")
            
            # Sequence readouts
            st.markdown("**Transcribed mRNA Sequence:**")
            st.code(str(mrna_seq), language="text")
            
            st.markdown("**Translated Amino Acid Peptide Chain:**")
            st.code(str(protein_seq), language="text")

    if not invalid_chars:
        st.markdown("---")
        st.subheader("📈 Nucleotide Frequency Distribution")
        counts = {"Adenine (A)": dna_input.count("A"), "Thymine (T)": dna_input.count("T"), 
                  "Cytosine (C)": dna_input.count("C"), "Guanine (G)": dna_input.count("G")}
        df_counts = pd.DataFrame(list(counts.items()), columns=["Nucleotide", "Count"])
        fig = px.bar(df_counts, x="Nucleotide", y="Count", color="Nucleotide", title="Base Pair Allocation Graph")
        st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MODULE 2: BIOCHEMISTRY & DRUG DISCOVERY
# ==========================================
elif app_mode == "2. Biochemistry & Drug Discovery":
    st.markdown("<div class='main-title'>Biochemistry De Novo Drug Design Tool</div>", unsafe_allowed_html=True)
    st.markdown("<div class='sub-title'>Calculate Lipinski's Rule of 5 properties to screen small molecules for chemical bioavailability.</div>", unsafe_allowed_html=True)
    
    col1, col2 = st.columns()
    
    with col1:
        st.subheader("🧪 Select Target Pipeline Profile")
        target_disease = st.selectbox("Select Disease Target Vector", ["Oncology (Kinase Inhibitor)", "Neurology (Blood-Brain Barrier Crossing)", "Antiviral (Protease Binder)"])
        
        # Simulated molecular property selectors based on structural profiles
        st.markdown("**Adjust Chemical Scaffolding Parameters:**")
        mol_weight = st.slider("Molecular Weight (Da)", 100.0, 800.0, 350.0, step=10.0)
        log_p = st.slider("Octanol-Water Partition Coefficient (LogP)", -2.0, 7.0, 2.5, step=0.1)
        h_donors = st.slider("Hydrogen Bond Donors", 0, 12, 3)
        h_acceptors = st.slider("Hydrogen Bond Acceptors", 0, 20, 6)
        
    with col2:
        st.subheader("⚖️ Lipinski's Rule of 5 Evaluation")
        
        # Check Rules
        w_fail = mol_weight > 500
        p_fail = log_p > 5
        d_fail = h_donors > 5
        a_fail = h_acceptors > 10
        
        total_violations = sum([w_fail, p_fail, d_fail, a_fail])
        
        # Display checks
        st.markdown(f"**Molecular Weight (< 500 Da):** {'❌ Fail' if w_fail else '✅ Pass'} ({mol_weight} Da)")
        st.markdown(f"**LogP Partition (< 5):** {'❌ Fail' if p_fail else '✅ Pass'} ({log_p})")
        st.markdown(f"**H-Bond Donors (≤ 5):** {'❌ Fail' if d_fail else '✅ Pass'} ({h_donors})")
        st.markdown(f"**H-Bond Acceptors (≤ 10):** {'❌ Fail' if a_fail else '✅ Pass'} ({h_acceptors})")
        
        st.markdown("---")
        if total_violations <= 1:
            st.success(f"🎉 **Drug Candidate Viable!** Total Rule Violations: {total_violations}. This profile shows high structural bioavailability.")
        else:
            st.error(f"⚠️ **Low Oral Bioavailability Risk!** Total Rule Violations: {total_violations}. Structural alterations recommended.")

    # Molecular Profile Visualization
    st.markdown("---")
    st.subheader("📊 Molecular Structural Fingerprint Radar")
    
    categories = ['Mol Weight (Normalized)', 'LogP (Normalized)', 'H-Bond Donors', 'H-Bond Acceptors']
    values = [mol_weight/100, log_p + 2, h_donors, h_acceptors]
    
    fig = go.Figure(data=go.Scatterpolar(r=values, theta=categories, fill='toself', name='Molecule Property Map'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# MODULE 3: BIOMEDICAL AI IMAGE SCANNER
# ==========================================
elif app_mode == "3. Biomedical AI Image Scanner":
    st.markdown("<div class='main-title'>Biomedical AI & Healthcare Imaging Suite</div>", unsafe_allowed_html=True)
    st.markdown("<div class='sub-title'>Simulates a computer-vision neural network highlighting deep structural tissue density spikes or anomalies.</div>", unsafe_allowed_html=True)
    
    col1, col2 = st.columns()
    
    with col1:
        st.subheader("🖼️ Diagnostic Loading Dock")
        scan_type = st.selectbox("Select Diagnostics Domain", ["Magnetic Resonance Imaging (MRI)", "Computed Tomography (CT Scan)", "Ultrasound Matrix Array"])
        
        noise_level = st.slider("Neural Network Input Signal Noise Filter", 0.0, 1.0, 0.2)
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
                
                fig = px.imshow(
                    segmented_ai_layer, 
                    color_continuous_scale="Jet", 
                    title=f"AI Computer Vision Feedback Loop: {scan_type}"
                )
                st.plotly_chart(fig, use_container_width=True)
                st.info("🎯 **AI Diagnostics Alert Vector:** Cluster detected at coordinates [Row:32, Col:31]. High-intensity density spikes indicate localized tissue anomalies.")
        else:
            fig = px.imshow(raw_signal, color_continuous_scale="Viridis", title="Raw Unprocessed Matrix Grid Feed")
            st.plotly_chart(fig, use_container_width=True)
            st.write("Click 'Execute AI Automated Tissue Segmentation' on the left panel to simulate real-time neural mapping.")
