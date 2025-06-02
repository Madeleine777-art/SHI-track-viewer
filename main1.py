import streamlit as st

# Page settings
st.set_page_config(page_title="Recrystallisation Dynamics of Swift Heavy Ion Tracks in Single Crystal YIG", layout="centered")


# Global CSS styles
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: Arial, sans-serif !important;
            background-color: #0d1b2a;
            color: #ffffff;
            font-size: 1.15rem;
        }

        .main-title {
            text-align: center;
            font-size: 2.2em;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 0.8em;
        }

        .section-title {
            font-size: 1.6em;
            font-weight: bold;
            color: #90caf9;
            margin-top: 2em;
            margin-bottom: 0.4em;
        }

        .toc-button {
            display: block;
            background-color: #2c3e50;    /* dark gray */
            color: #f9a825;               /* golden yellow */
            padding: 0.6em 1em;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 0.4em;
            text-decoration: none;
            transition: background-color 0.2s, color 0.2s;
        }
        .toc-button:hover {
            background-color: #f9a825;    /* golden yellow */
            color: #2c3e50;               /* dark gray */
        }
            
        .joke-box {
            background: #1976d2;
            color: white;
            border-radius: 18px;
            padding: 1.3em 1.7em;
            margin-top: 1.5em;
            font-size: 1.4rem;
            text-align: center;
        }

        .contact-box {
            background: #ffffff;
            color: #222;
            border-radius: 18px;
            padding: 1.7em 2.5em;
            margin: 2.2em auto;
            font-size: 1.15rem;
            max-width: 560px;
            box-shadow: 0 4px 28px 0 rgba(44,62,80,0.10);
            border: 1.2px solid #e0e6ed;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("<div class='main-title'>Studying Recrystallisation Dynamics of Swift Heavy Ion Tracks in Single Crystal Y<sub>3</sub>Fe<sub>5</sub>O<sub>12</sub> (YIG)</div>", unsafe_allow_html=True)

# Table of Contents with anchor buttons
st.markdown("### 📚 Table of Contents")
toc_items = {
    "Introduction": "intro",
    "Experimental Procedure": "exp",
    "Data and Results": "results",
    "Conclusion": "conclusion",
    "References": "refs",
    "Joke (just for fun!)": "joke",
    "Contact Details": "contact"
}
for label, anchor in toc_items.items():
    st.markdown(f"<a class='toc-button' href='#{anchor}'>{label}</a>", unsafe_allow_html=True)

# Scroll Targets + Content
# Introduction
st.markdown('<div id="intro" class="section-title">Introduction</div>', unsafe_allow_html=True)

# 1) SHI description with ref 1
st.markdown("""
<div style="text-align: justify; margin-bottom: 1.5em;">
Swift heavy ions (SHIs) are high-energy particles characterised by their mass and energy exceeding 10 amu and 1 MeV/amu, respectively. SHIs are naturally present in nuclear fission processes as well as in cosmic radiation, but can also be produced artificially at large accelerator facilities. They are used to simulate the conditions in nuclear reactors by mimicking fission fragment effects since their mass-energy combinations are similar to those found in fission fragments and cosmic rays. When a SHI propagates within a material, it will transfer energy over nanometric distances through dense ionisation that can result in transient or permanent structural modifications. The SHI will transfer energy primarily to the target electrons in a material (referred to as delta electrons), over timescales of the order of ~10⁻¹⁵ s. These delta electrons are ejected outward in a radial manner within a few ångströms around the ion’s trajectory. These excited electrons eventually transfer energy to the lattice through electron-phonon coupling, which could result in localised melting and fast quenching over ~10⁻¹² s¹.
</div>
""", unsafe_allow_html=True)

# 2) Centered Fig. 1 + caption
st.image("SHIprocessandevery.png", use_container_width=True)
st.markdown("""
<div style="text-align: center; margin-bottom: 1.5em;">
<b>Fig. 1.</b> Schematic of a sample irradiated by SHIs, with emphasis on the sequence of interactions and corresponding energy transfer timescales.
</div>
""", unsafe_allow_html=True)

# 3) YIG track morphology + motivation with ref 2
st.markdown("""
<div style="text-align: justify; margin-bottom: 1.5em;">
Numerous studies have shown that when Yttrium iron garnet (YIG, Y₃Fe₅O₁₂) is subjected to SHI irradiation, it tends to form continuous, cylindrical amorphous tracks². These ion tracks are visible with transmission electron microscopy (TEM) and have been widely studied. However, the recrystallisation dynamics of these ion tracks under in-situ thermal annealing remain unexplored. These tracks are underdense relative to the surrounding matrix, leading to stresses around the track periphery. Studying the crystallisation dynamics in real time could reveal any dependence of the recovery rate on crystallographic orientation and stress state (through local specimen thickness, nearby/overlapping tracks, mechanical anisotropy of the crystal and temperature-induced bending of the lamella). YIG is an excellent candidate for these studies since it has a well-known cubic crystal structure, strong resistance to electron beam damage—an essential characteristic for prolonged in-situ TEM experiments—and good thermal stability. The properties of YIG at room temperature are tabulated in Table 1.
</div>
""", unsafe_allow_html=True)

# 4) Table 1 heading with refs 3⁴
st.markdown("""
**Table 1**  
Properties of Yttrium Iron Garnet at room temperature<sup>3,4</sup>
""", unsafe_allow_html=True)

# 5) Table markup
st.markdown("""
<table style="width:100%; border-collapse: collapse; font-size: 1.05rem;">
  <tr style="background-color:#444; color:white;">
    <th style="text-align:left; padding: 8px;">Properties</th>
    <th style="text-align:left; padding: 8px;">Value</th>
  </tr>
  <tr><td style="padding: 6px;">Chemical composition</td><td style="padding: 6px;">Y₃Fe₅O₁₂</td></tr>
  <tr style="background-color:#2c2c2c;"><td style="padding: 6px;">Crystal structure</td><td style="padding: 6px;">Cubic Ia3̅d</td></tr>
  <tr><td style="padding: 6px;">Lattice constant</td><td style="padding: 6px;">12.376 Å ± 0.004 Å</td></tr>
  <tr style="background-color:#2c2c2c;"><td style="padding: 6px;">Thermal expansion coefficient</td><td style="padding: 6px;">1.04 × 10⁻⁵ K⁻¹</td></tr>
  <tr><td style="padding: 6px;">Thermal conductivity</td><td style="padding: 6px;">7.4 W/mK</td></tr>
  <tr style="background-color:#2c2c2c;"><td style="padding: 6px;">Density</td><td style="padding: 6px;">5.17 g/cm³</td></tr>
  <tr><td style="padding: 6px;">Curie temperature</td><td style="padding: 6px;">~560 K</td></tr>
  <tr style="background-color:#2c2c2c;"><td style="padding: 6px;">Melting point</td><td style="padding: 6px;">1828 K</td></tr>
</table>
""", unsafe_allow_html=True)

# 6) Closing motivation paragraph
st.markdown("""
<div style="text-align: justify; margin-top: 1em;">
This work aims to directly observe and quantify ion track recrystallisation in single-crystal YIG using in-situ TEM, identify key factors affecting track recovery including heating conditions and beam exposure, optimise sample preparation using focused ion beam (FIB) techniques and streamline data analysis via Python scripts, with the goal of establishing a robust framework for studying real-time defect evolution in irradiated crystals and providing insights into structure recovery processes relevant in both materials and nuclear research.
</div>
""", unsafe_allow_html=True)

#Experimental procedure
st.markdown('<div id="exp" class="section-title"> Experimental Procedure</div>', unsafe_allow_html=True)

# 1) Irradiation & imaging details
st.markdown("""
<div style="text-align: justify; margin-bottom: 1.5em;">
Single crystal (111) YIG was irradiated at room temperature using 167 MeV Xe ions (Sₑ ≈ 24.9 keV/nm near the surface) to a fluence of 2×10¹¹ cm⁻² at the Joint Institute for Nuclear Research (JINR) in Dubna, Russia. Lamellae were extracted from the irradiated bulk (~1 µm below the irradiated surface) using FIB lift-out in an FEI Helios Nanolab 650 and mounted on Si₃N₄ MEMS heating chips (DENS Solutions Wildfire). Imaging was performed in BF TEM mode on a JEOL ARM 200F at 200 keV and recorded on a Quantum Detectors MerlinEM detector (256×256 px, 10 ms/frame, 2×12-bit, continuous mode). The experimental workflow is shown in Fig. 2.
</div>
""", unsafe_allow_html=True)

# 2) Fig. 2 + caption (with non-breaking spans)
st.image("expflow.png", use_container_width=True)
st.markdown("""
<div style="text-align: center; margin-bottom: 1.5em;">
<b>Fig. 2.</b> Experimental workflow for in-situ TEM analysis, (1) ion milling, (2) FIB lift-out, (3) MEMS chip mounting followed by final thinning, (4) TEM specimen holder loading, and (5) insertion into TEM. (6) BF TEM images before <span style="white-space:nowrap;">~823&nbsp;K, 39&nbsp;s</span> and after recrystallisation <span style="white-space:nowrap;">~823&nbsp;K, 60.85&nbsp;s</span>. The dark band (bend contour) indicates stress-induced sample bending and deviation from the initial zone-axis alignment.
</div>
""", unsafe_allow_html=True)

# 3) GUI description
st.markdown("""
<div style="text-align: justify; margin-bottom: 1.5em;">
To overcome the synchronisation challenge between imaging and heating systems on separate PCs, a custom Python-based graphical user interface (EMGUI) was developed. This tool triggers both systems simultaneously—minimising temporal misalignment and ensuring each frame maps to the correct temperature. The GUI also provides real-time acquisition monitoring, parameter setup, and automated data storage. A screenshot is shown in Fig. 3.
</div>
""", unsafe_allow_html=True)

# 4) Fig. 3 + caption
st.image("GUI.png", use_container_width=True)
st.markdown("""
<div style="text-align: center; margin-bottom: 1.5em;">
<b>Fig. 3.</b> EMGUI interface for MerlinEM camera and heating-holder control.</div>
""", unsafe_allow_html=True)

# Data and Results Section
# --- Results Section ---
st.markdown('<div id="results" class="section-title"> Data and Results</div>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: justify; margin-bottom: 1.5em;">
Bright-field (BF) TEM imaging, in-situ thermal annealing, and feature tracking tools were combined to obtain visual and quantitative information regarding recrystallisation. Fig. 4 shows the initial characterisation of the irradiated YIG sample before annealing.
</div>
""", unsafe_allow_html=True)

# Fig. 4
st.image("BFimageQR.png", use_container_width=True)
st.markdown("""
<div style="text-align: center; margin-bottom: 1.5em;">
<strong>Fig. 4.</strong> Plan view BF TEM micrographs of single crystal YIG irradiated with 167 MeV Xe ions to a fluence of 2×10¹¹ cm⁻². (A) Shows high-density ion tracks as bright circular features across the lamella. The upper-right region shows no tracks due to local amorphisation from FIB thinning, while tracks remain well-defined even in thicker crystalline areas. (B) shows a [111] aligned BF view of the region marked by the red square in (A), isolated and overlapping amorphous tracks are clearly distinguished from the strongly diffracting crystalline surroundings. (C) is an FFT of (B), confirming [111] zone axis alignment, and (D) is a thickness map (EELS log-ratio method), where the black square denotes the field of view shown in (A), showing an average thickness of <span style="white-space:nowrap;">51.2&nbsp;±&nbsp;23.0&nbsp;nm</span> within the red square corresponding to the region in (B). The Si₃N₄ support films surrounding the YIG sample is saturated to emphasise the sample thickness.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: justify; margin-bottom: 1.5em;">
The resulting time series of images was corrected for the camera gain response and temporally binned by a factor of 5 to reduce noise. The stack was aligned using a Sobel filter to correct for sample drift during heating. Each frame was labelled with the corresponding time and temperature values and is shown in Fig. 5 below. Please press “play” to view the recrystallisation behaviour over time.
</div>
""", unsafe_allow_html=True)

# Fig. 5
st.video("processed_with_scalebar.mp4")
st.markdown("""
<div style="text-align: center; margin-bottom: 1.5em;">
<strong>Fig. 5.</strong> Dynamic evolution of SHI track recrystallisation in single‐crystal YIG. Aligned BF TEM frames of a YIG specimen irradiated with 167 MeV Xe ions, annotated with elapsed time (s) and temperature (<span style="white-space:nowrap;">773–823&nbsp;K</span>), captured by a high-speed camera. Track diameter reveals insignificant recrystallisation at about <span style="white-space:nowrap;">773&nbsp;K</span> and progressive decrease at <span style="white-space:nowrap;">823&nbsp;K</span>, indicating recrystallisation.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: justify; margin-bottom: 1.5em;">
The MIPAR MATLAB package was used to segment the resulting images. Due to sample drift during heating, a consistent field of view was not maintained throughout the experiment. TrackPy was used to track individual features across all the frames in which they were detected. The various tracks were classified into three groups, namely early-stage tracks (0–34 s) which represents the features visible before the field of view shift, late-stage tracks (~36–58 s) which represents the features visible after drift stabilised, and the full-duration tracks (0–56 s) which represents the tracks consistently visible throughout the heating profile. Large temperature adjustments lead to significant thermal expansion, causing specimen drift and bending. Near zone axis imaging is preferable from a contrast point of view. It is therefore desirable to pre-heat the specimen prior to final zone axis alignment and focusing so that the resultant change in field of view, focus and specimen tilt due to the final temperature increase is within acceptable limits. 773 K was identified as a suitable intermediate temperature where track annealing was slow enough to allow for final alignment before excessive track shrinkage occurred. Fig.6 shows the equivalent circle diameter DEC, defined as in Eq. (1).
</div>
""", unsafe_allow_html=True)

# Equation
st.latex(r"""D_{EC} = 2 \sqrt{\frac{A}{\pi}}\quad\hspace{1cm}(1)""")

st.markdown("""
<div style="text-align: justify; margin-bottom: 1.5em;">
where <em>A</em> is the cross-sectional track area, plotted as a function of temperature and time for the three groups (A–C), along with a zoomed-in view (D) of the final recrystallisation stage.
</div>
""", unsafe_allow_html=True)

# Fig. 6 panels
cols = st.columns(4)
with cols[0]:
    st.markdown("**A**")
    st.image("panel1_500s.png", use_container_width=True)
with cols[1]:
    st.markdown("**B**")
    st.image("panel2_550s.png", use_container_width=True)
with cols[2]:
    st.markdown("**C**")
    st.image("panel3_all.png", use_container_width=True)
with cols[3]:
    st.markdown("**D**")
    st.image("panel4_zoomed_47_57s.png", use_container_width=True)

st.markdown("""
<div style="text-align: center; margin-bottom: 1.5em;">
<b>Fig. 6.<b> (A) Tracks visible from 0–35 s during the temperature ramp from <span style="white-space:nowrap;">773–823&nbsp;K</span> show only a small reduction in <em>D<sub>EC</sub></em>. (B) Tracks visible from 35.2–55.2 s under constant temperature at <span style="white-space:nowrap;">823&nbsp;K</span> show rapid recrystallisation from the decreasing trend. (C) Full-duration tracks exhibit a similar trend, confirming recrystallisation. The data between 33–35 s was unreliable due to image blur caused by rapid specimen shift to recenter the field of view. (D) A magnified view of (C) highlighting the time window between 47 and ~56 s, where the recrystallisation rate rapidly increases.
</div>
""", unsafe_allow_html=True)

# Conclusion
st.markdown('<div id="conclusion" class="section-title"> Conclusion</div>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align: justify;">
In-situ annealing enabled direct TEM observation of SHI track recrystallisation in single-crystal YIG with millisecond temporal resolution. Limited recrystallisation was observed below 773 K, and most tracks began to recrystallise only once the temperature reached 823 K. Maintaining 823 K resulted in full recrystallisation within about 35 s with a significant increase in track shrinkage rate after 30 s. The integration of a high-speed camera with precise thermal control enabled millisecond-resolved frame-by-frame monitoring of structural recovery. Despite challenges from thermal drift and contrast variations, the obtained results suggest that such experiments can indeed supply reliable data on annealing dynamics in irradiated materials. While the presented results are limited to equivalent circle diameter, any number of additional parameters (e.g. eccentricity, perimeter, orientation, etc.) may be extracted from the segmented dataset.
</div>
""", unsafe_allow_html=True)

# --- References Section ---
st.markdown('<div id="refs" class="section-title"> <span style="color:red;">References:</span></div>', unsafe_allow_html=True)

st.markdown("""
<sup>1</sup> Lang, M.; Flyura Djurabekova; Medvedev, N.; Toulemonde, M.; Trautmann, C.Fundamental Phenomena and Applications of Swift Heavy Ion Irradiations. <em>Elsevier eBooks</em> 2020, 485–516. DOI: 10.1016/B978-0-12-803581-8.11644-3.

<br><sup>2</sup> Costantini, J.-M.; Desvignes, J. M.; Toulemonde, M.<em>Journal of Applied Physics</em> 2000, 87 (9), 4164–4174. DOI: 10.1063/1.373047.

<br><sup>3</sup> Mitra, A.Structural and Magnetic Properties of YIG Thin Films and Interfacial Origin of Magnetisation Suppression. Ph.D. Dissertation, University of Leeds School of Physics and Astronomy, 2017, pp. 8–11. <em>https://etheses.whiterose.ac.uk/id/eprint/18696/1/Arpita%20Mitra_FinalThesis.pdf</em> (accessed April 2025).

<br><sup>4</sup> Ferrisphere Inc.<em>Properties of YIG and GaYIG</em>.<em>https://www.ferrisphere.com/wp-content/uploads/2021/05/Properties-of-YIG-and-GaYIG-Sheet1-1.pdf</em> (accessed April 2025).
""", unsafe_allow_html=True)

# Joke Section
st.markdown('<div id="joke" class="section-title"> Joke (just for fun!)</div>', unsafe_allow_html=True)
st.markdown("""
<div class="joke-box">
    Why did the swift heavy ion refuse to apologise to the crystal?<br><br>
    <strong>Because it said, "I'm just passing through—damage is my ion-tent!"</strong>
</div>
""", unsafe_allow_html=True)
st.caption("<div style='text-align:center;'>If you laughed, you’re a scientist. If you groaned... you’re normal.</div>", unsafe_allow_html=True)

# Contact Details
st.markdown('<div id="contact" class="section-title">📬 Contact Details</div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-box">
    <div style="font-size:1.4em; font-weight:800; color:#1b3a57;">Madeleine Badenhorst</div>
    <div style="margin-top: 0.4em;">
        MSc Candidate, Department of Physics<br>
        Nelson Mandela University, Centre for HRTEM
    </div>
    <div style="margin-top: 0.5em;">
        <b>Email:</b> <a href="mailto:s223108049@mandela.ac.za" style="color:#1565c0;">s223108049@mandela.ac.za</a>
    </div>
    <div style="margin-top:0.8em; font-style:italic; color:#1b3a57;">
        If you have advice, feedback, or just want to chat SHIs, come find me at the conference or email!
    </div>
</div>
""", unsafe_allow_html=True)