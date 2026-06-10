/* Gegow UI Global Styles - Philippines Tropical Theme */
:root {
    --gegow-primary: #008C99; /* Tropical water */
    --gegow-accent: #FF8F00; /* Sunset amber */
    --gegow-bg: #F5F7F2; /* Soft sand */
    --gegow-gradient-btn: linear-gradient(90deg, #FF8F00, #E65100);
    --gegow-glass: rgba(255, 255, 255, 0.75);
}

.glass-nav { 
    background: var(--gegow-glass); 
    backdrop-filter: blur(12px); 
    border-top: 1px solid rgba(255,255,255,0.4); 
}

.btn-gegow { 
    background: var(--gegow-gradient-btn); 
    border-radius: 12px; 
    color: white;
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(255,143,0,0.3); 
    transition: transform 0.2s ease;
}

.btn-gegow:active { transform: scale(0.95); }

.card-gradient-overlay { 
    background: linear-gradient(to top, rgba(0,25,35,0.8) 0%, transparent 100%); 
}

.wizard-step { 
    transition: opacity 0.3s ease-in-out; 
}