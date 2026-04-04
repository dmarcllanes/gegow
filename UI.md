/* Gegow UI Global Styles */
:root {
    --gegow-primary: #006D77;
    --gegow-accent: #FF7043;
    --gegow-bg: #F1F1E6;
    --gegow-gradient-btn: linear-gradient(90deg, #FF7043, #F4511E);
    --gegow-glass: rgba(255, 255, 255, 0.7);
}

.glass-nav { 
    background: var(--gegow-glass); 
    backdrop-filter: blur(10px); 
    border-top: 1px solid rgba(255,255,255,0.3); 
}

.btn-gegow { 
    background: var(--gegow-gradient-btn); 
    border-radius: 12px; 
    color: white;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(255,112,67,0.3); 
    transition: transform 0.2s ease;
}

.btn-gegow:active { transform: scale(0.95); }

.card-gradient-overlay { 
    background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 100%); 
}

.wizard-step { 
    transition: opacity 0.3s ease-in-out; 
}