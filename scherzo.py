import streamlit as st
import time

st.markdown(
    """
    <style>
    .stApp, [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://media.istockphoto.com/id/613318760/photo/various-herbs-and-spices-on-dark-wood-table.jpg?s=170667a&w=0&k=20&c=Ojh5nakZPndVfrlh2B3cz_MldcjnNBnzwAnqwGiOGiw=");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
if "loggato" not in st.session_state:
    st.session_state.loggato = False

if not st.session_state.loggato: 
   st.title("Corso di cucina avanzato")
   st.write("Inserisci i dati presenti sul tuo biglietto per accedere ai moduli.")

   st.divider()

   nome = st.text_input("Nome dello Studente")
   cognome = st.text_input("Cognome dello Studente")
   codice_coupon = st.text_input("Codice Coupon / ID Voucher")
   st.divider()   

   if st.button("CONVALIDA E RISCATTA CORSO", type="primary", use_container_width=True):
    
      if not nome or not cognome or not codice_coupon:
            st.error("⚠️ Compilare tutti i campi per verificare la validità nel database.")
      elif codice_coupon.upper() == "CUCINA2026": 
            with st.spinner("Verifica codice nel database in corso..."):
                time.sleep(2.5) 
            st.session_state.nome_studente = nome
            st.session_state.loggato = True
            st.rerun()
      else:
            st.error("❌ Codice Coupon non valido.")

else:
    st.title("🎓 Area Riservata Studente")
   
    st.write(f"Bentornato/a **{st.session_state.nome_studente}**. Il tuo piano di studi è attivo.")
    
    st.divider()
    
    st.subheader("📚 Corso Assegnato:")
    st.error("### **Master di Alta Cucina: Gestione avanzata e cottura dell'Acqua della Pasta**")
    
    st.divider()
    
    st.markdown("#### 📝 Moduli Didattici Disponibili:")
    with st.expander("Modulo 1: La termodinamica del pentolino (40 ore)"):
        st.write("- Studio approfondito del perché l'acqua non bolle mai se la fissi.")
        st.write("- Analisi chimica: il sale va messo prima o dopo? Teorie a confronto.")
        
    with st.expander("Modulo 2: Tecniche di sopravvivenza ai fornelli (60 ore)"):
        st.write("- Come non far bruciare l'acqua della pasta (Esercitazione pratica).")
        st.write("- Masterclass: distinguere un cucchiaio da una forchetta.")

    st.divider()

    # Il Bottone
    if st.button("🚀 AVVIA IL PRIMO WEBINAR", type="primary", use_container_width=True):
        with st.spinner("Connessione con il tutor in corso..."):
            time.sleep(2)
        emoji = "🧑‍🍳 🍕 🍝 🎂 🧑‍🍳 🍕 🍝 🎂 🧑‍🍳 🍕 🍝 🎂 🧑‍🍳 🧑‍🍳 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂🧑‍🍳 🍕 🍝 🎂"
        html_pioggia = f"""
        <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 9999; overflow: hidden;">
        <marquee direction="down" scrollamount="15" style="height: 100%; font-size: 50px;">
            {emoji} &nbsp;&nbsp;&nbsp;&nbsp; {emoji}
        </marquee>
        </div>
        """
        st.markdown(html_pioggia, unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: red; font-size: 65px;'>PAPOY</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: white; font-size: 22px;'>Da oggi in poi cucini tu</p>", unsafe_allow_html=True)
       
        if st.button("RIFAI 🔄"):
            st.session_state.loggato = False
            st.rerun()
