import streamlit as st

st.title("Generador de informes radiológicos 🧠")

# =========================
# DICCIONARIOS
# =========================

higado = {
    "tamano": {
        "normal": "Hígado de tamaño conservado",
        "aumentado": "Hígado de tamaño incrementado",
        "disminuido": "Hígado de tamaño disminuido"
    },
    "contornos": {
        "regulares": "contornos regulares",
        "irregulares": "contornos irregulares"
    },
    "atenuacion": {
        "normal": "atenuación homogénea",
        "hipodensa": "disminución difusa de la atenuación",
        "hiperdensa": "aumento difuso de la atenuación"
    },
    "parenquima": {
        "normal": "parénquima homogéneo",
        "heterogeneo": "parénquima heterogéneo"
    },
    "lesiones": {
        "ninguna": "sin evidencias de lesiones focales ni difusas",
        "quistes": "con quistes hepáticos simples"
    },
    "vias_biliares": {
        "normal": "Vías biliares intrahepáticas no dilatadas."
    }
}

higado_lesion = {
    "tipo": {
        "quistica": "lesión quística",
        "solida": "lesión sólida",
        "mixta": "lesión de componente mixto"
    },
    "numero": {
        "unica": "lesión única",
        "multiples": "múltiples lesiones"
    },
    "bordes": {
        "definidos": "bordes bien definidos",
        "mal_definidos": "bordes mal definidos"
    }
}

vesicula = {

    "tamano": {
        "normal": "Vesícula biliar de tamaño conservado",
        "distendida": "Vesícula biliar distendida",
        "colapsada": "Vesícula biliar colapsada"
    },

    "pared": {
        "normal": "de paredes delgadas",
        "engrosada_difusa": "con engrosamiento parietal difuso",
        "engrosada_focal": "con engrosamiento parietal focal",
        "estratificada": "con engrosamiento parietal de aspecto estratificado",
        "irregular": "de contornos parietales irregulares",
        "discontinua": "con discontinuidad parietal",
        "calcificada": "con calcificación difusa de sus paredes"
    },

    "realce": {
        "normal": "",
        "aumentado": "con realce parietal aumentado tras contraste",
        "disminuido": "con disminución del realce parietal"
    },

    "contenido": {
        "homogeneo": "con contenido homogéneo",
        "heterogeneo": "con contenido denso heterogéneo",
        "litiasis": "con cálculos en su interior"
    },

    "cistico": {
        "no_visible": "",
        "normal": "",
        "obstruido": "con probable obstrucción del conducto cístico",
        "calculo": "con cálculo en el conducto cístico"
    },

    "perivesicular": {
        "normal": "",
        "inflamacion": "con cambios inflamatorios perivesiculares",
        "grasa": "con aumento de la densidad de la grasa perivesicular",
        "liquido": "con líquido perivesicular",
        "coleccion": "con colección perivesicular"
    },

    "lesiones": {
        "ninguna": "",
        "polipo": "con lesión polipoidea intraluminal",
        "masa": "con masa de densidad de partes blandas",
        "adenomiomatosis": "con engrosamiento parietal con pequeñas imágenes quísticas intramurales",
        "perdida_plano": "con pérdida del plano de clivaje con el hígado adyacente"
    },

    "gas": {
        "no": "",
        "lumen": "con gas en el lumen vesicular",
        "pared": "con gas en la pared vesicular",
        "mixto": "con gas en la pared y lumen vesicular"
    },

    "dispositivo": {
        "ninguno": "",
        "colecistostomia": "Se identifica catéter de colecistostomía"
    }
}

estomago = {

    "distension": {
        "adecuada": "Estómago adecuadamente distendido",
        "distendido": "Estómago distendido",
        "poco_distendido": "Estómago poco distendido",
        "colapsado": "Estómago colapsado"
    },

    "pared": {
        "normal": "paredes de grosor y morfología conservados",
        "engrosada_difusa": "engrosamiento parietal difuso",
        "engrosada_focal": "engrosamiento parietal focal",
        "irregular": "engrosamiento parietal de contornos irregulares"
    },

    "patron": {
        "normal": "",
        "estratificado": "con patrón estratificado",
        "homogeneo": "de aspecto homogéneo"
    },

    "realce": {
        "normal": "",
        "aumentado": "con aumento del realce tras contraste",
        "disminuido": "con disminución del realce tras contraste"
    },

    "contenido": {
        "vacio": "sin contenido significativo",
        "gas": "con contenido gaseoso",
        "liquido": "con contenido líquido",
        "mixto": "con contenido mixto (gas y líquido)",
        "material_denso": "con material hiperdenso en su interior"
    },

    "luz": {
        "normal": "luz de calibre conservado",
        "disminuida": "disminución del calibre luminal",
        "aumentada": "aumento del calibre luminal"
    },

    "perigastrico": {
        "normal": "",
        "estriacion": "con estriación de la grasa perigástrica",
        "liquido": "con líquido perigástrico",
        "gas": "con gas extraluminal perigástrico"
    },

    "lesiones": {
        "ninguna": "",
        "masa": "masa de densidad de partes blandas en la pared gástrica",
        "ulceracion": "imagen sugestiva de ulceración",
        "engrosamiento_focal": "engrosamiento focal de la pared"
    },

    "otros": {
        "ninguno": "",
        "sonda": "con sonda nasogástrica en su interior",
        "gastrectomia": "cambios postquirúrgicos compatibles con gastrectomía"
    }
}

bazo = {

    "tamano": {
        "normal": "Bazo de tamaño conservado",
        "aumentado": "Bazo aumentado de tamaño",
        "disminuido": "Bazo de tamaño disminuido",
        "atrofico": "Bazo atrófico"
    },

    "contornos": {
        "regulares": "de contornos regulares",
        "irregulares": "de contornos irregulares"
    },

    "parenquima": {
        "normal": "parénquima homogéneo",
        "heterogeneo": "parénquima heterogéneo",
        "hipodenso": "con áreas de menor atenuación",
        "hiperdenso": "con aumento de la atenuación"
    },

    "realce": {
        "normal": "realce homogéneo",
        "hipercaptante": "con áreas de mayor realce",
        "hipocaptante": "con áreas de menor realce"
    },

    "lesiones": {
        "ninguna": "",
        "quiste_simple": "lesión quística simple",
        "quiste_complejo": "lesión quística compleja",
        "solida": "lesión sólida",
        "hipodensa": "lesión hipodensa",
        "hipercaptante": "lesión hipercaptante",
        "hipocaptante": "lesión hipocaptante",
        "infarto": "área hipodensa de morfología triangular periférica",
        "coleccion": "colección esplénica"
    },

    "capsula": {
        "normal": "",
        "irregular": "con irregularidad de la cápsula esplénica",
        "discontinua": "con discontinuidad capsular"
    },

    "periesplenico": {
        "normal": "",
        "liquido": "con líquido libre periesplénico",
        "hemoperitoneo": "con líquido de alta densidad periesplénico",
        "coleccion": "con colección periesplénica"
    }
}

pancreas = {

    "tamano": {
        "normal": "Páncreas de tamaño conservado",
        "aumentado": "Páncreas aumentado de tamaño",
        "disminuido": "Páncreas disminuido de tamaño",
        "atrofico": "Páncreas atrófico"
    },

    "contornos": {
        "regulares": "de contornos regulares",
        "lobulados": "de contornos lobulados",
        "irregulares": "de contornos irregulares"
    },

    "parenquima": {
        "normal": "parénquima homogéneo",
        "heterogeneo": "parénquima heterogéneo",
        "hipodenso": "con disminución difusa de la atenuación",
        "graso": "con infiltración grasa del parénquima"
    },

    "realce": {
        "normal": "realce homogéneo tras contraste",
        "disminuido": "con áreas de menor realce",
        "aumentado": "con realce aumentado"
    },

    "lesiones": {
        "quistica": "lesión quística",
        "solida": "lesión sólida",
        "mixta": "lesión de componente mixto"
    },

    "localizacion": {
        "cabeza": "en la cabeza pancreática",
        "cuello": "en el cuello pancreático",
        "cuerpo": "en el cuerpo pancreático",
        "cola": "en la cola pancreática",
        "difusa": "de distribución difusa"
    },

    "conducto_principal": {
        "normal": "conducto pancreático principal no dilatado",
        "dilatado": "conducto pancreático principal dilatado",
        "irregular": "conducto pancreático principal de trayecto irregular",
        "corte_brusco": "interrupción abrupta del conducto pancreático"
    },

    "coledoco": {
        "normal": "colédoco intrapancreático de calibre conservado",
        "dilatado": "colédoco intrapancreático dilatado",
        "litiasis": "imagen hiperdensa en colédoco intrapancreático compatible con litiasis",
        "estenosis": "estrechamiento distal del colédoco intrapancreático",
        "doble_ducto": "dilatación concomitante del conducto pancreático y colédoco"
    },

    "peripancreatico": {
        "normal": "sin cambios inflamatorios peripancreáticos",
        "inflamacion": "estriación de la grasa peripancreática",
        "coleccion": "colecciones peripancreáticas",
        "necrosis": "colecciones heterogéneas sugestivas de necrosis",
        "gas": "colecciones con gas en su interior"
    }
}

asas_delgadas = {

    "calibre": {
        "normal": "Asas intestinales delgadas de calibre conservado",
        "dilatadas": "Asas intestinales delgadas dilatadas",
        "colapsadas": "Asas intestinales delgadas colapsadas",
        "oclusion": "Asas intestinales delgadas dilatadas con niveles hidroaéreos"
    },

    "pared": {
        "normal": "paredes finas y regulares",
        "engrosada": "con engrosamiento parietal",
        "irregular": "con contornos parietales irregulares",
        "ulcerada": "con discontinuidad de la mucosa"
    },

    "realce": {
        "normal": "realce parietal conservado",
        "hipercaptante": "con aumento del realce parietal",
        "hipocaptante": "con disminución del realce parietal"
    },

    "patron": {
        "normal": "",
        "estratificado": "de aspecto estratificado",
        "homogeneo": "de aspecto homogéneo",
        "edematoso": "de aspecto edematoso",
        "mucoso": "con predominio mucoso"
    },

    "contenido": {
        "gas": "contenido gaseoso",
        "liquido": "contenido líquido",
        "mixto": "contenido mixto",
        "material_denso": "material hiperdenso dependiente en la luz",
        "material_hipodenso": "material hipodenso dependiente en la luz"
    },

    "motilidad": {
        "normal": "",
        "disminuida": "con disminución del peristaltismo",
        "aumentada": "con aumento del peristaltismo"
    },

    "distension": {
        "normal": "",
        "focal": "distensión focal",
        "difusa": "distensión difusa"
    },

    "perienterico": {
        "normal": "sin alteraciones de la grasa perientérica",
        "estriacion": "con estriación de la grasa perientérica",
        "liquido": "con líquido libre perientérico",
        "gas": "con gas en la grasa perientérica",
        "adenopatias": "con adenopatías mesentéricas"
    },

    "localizacion": {
        "duodeno": "en duodeno",
        "yeyuno": "en yeyuno",
        "ileon": "en íleon",
        "difuso": "de distribución difusa"
    }
}

asas_gruesas = {

    # =========================
    # CALIBRE
    # =========================
    "calibre": {
        "normal": "Asas intestinales gruesas de calibre conservado",
        "dilatadas": "Asas intestinales gruesas dilatadas, con calibre máximo de (#) mm",
        "colapsadas": "Asas intestinales gruesas colapsadas"
    },

    # =========================
    # CONTENIDO
    # =========================
    "contenido": {
        "gas": "con contenido gaseoso",
        "heces": "con contenido fecaloideo",
        "liquido": "con contenido líquido",
        "mixto": "con contenido mixto (gas y material fecaloideo/líquido)",
        "material_denso": "con material hiperdenso en su luz"
    },

    # =========================
    # DISTRIBUCIÓN
    # =========================
    "distribucion": {
        "normal": "",
        "focal": "de compromiso focal",
        "difusa": "de compromiso difuso"
    },

    # =========================
    # PARED (MORFOLOGÍA)
    # =========================
    "pared": {
        "normal": "de paredes finas y regulares",
        "engrosada": "con engrosamiento parietal",
        "engrosada_difusa": "con engrosamiento parietal difuso",
        "engrosada_focal": "con engrosamiento parietal focal",
        "irregular": "de contornos parietales irregulares"
    },

    # =========================
    # PATRÓN / CARACTERÍSTICAS
    # =========================
    "patron": {
        "normal": "",
        "estratificado": "de aspecto estratificado",
        "homogeneo": "de aspecto homogéneo"
    },

    # =========================
    # REALCE
    # =========================
    "realce": {
        "normal": "",
        "hipercaptante": "con aumento del realce parietal tras contraste",
        "hipocaptante": "con disminución del realce parietal tras contraste"
    },

    # =========================
    # PERICOLÓNICO
    # =========================
    "pericolico": {
        "normal": "sin alteraciones de la grasa pericolónica",
        "estriacion": "con aumento de la densidad de la grasa pericolónica",
        "liquido": "con líquido libre pericolónico",
        "gas": "con presencia de gas extraluminal pericolónico"
    },

    # =========================
    # LESIONES
    # =========================
    "lesiones": {
        "ninguna": "",
        "masa": "masa de densidad de partes blandas en relación al colon",
        "engrosamiento_focal": "engrosamiento focal de la pared colónica",
        "diverticulos": "presencia de divertículos colónicos"
    },

    # =========================
    # LOCALIZACIÓN (CLAVE 🔥)
    # =========================
    "localizacion": {
        "ciego": "ciego",
        "colon_ascendente": "colon ascendente",
        "colon_transverso": "colon transverso",
        "colon_descendente": "colon descendente",
        "sigmoides": "colon sigmoides",
        "recto": "recto",
        "difuso": "de distribución difusa"
    },

    # =========================
    # RECTO
    # =========================
    "recto": {
        "normal": "Recto de calibre y paredes conservadas",
        "distendido": "Recto distendido",
        "pared_engrosada": "con engrosamiento parietal rectal",
        "contenido": "ampolla rectal con contenido fecaloideo"
    },

    # =========================
    # APÉNDICE
    # =========================
    "apendice": {
        "no_visible": "Apéndice no identificado",
        "normal": "Apéndice de calibre y paredes conservadas",
        "engrosado": "Apéndice aumentado de calibre",
        "pared_engrosada": "con engrosamiento parietal apendicular",
        "fecalito": "con imagen hiperdensa intraluminal (apendicolito)",
        "periapendicular": "con estriación de la grasa periapendicular",
        "liquido": "con líquido periapendicular"
    }
}

retroperitoneo = {
    "adenopatias": {
        "no": "sin adenopatías retroperitoneales",
        "si": "con adenopatías retroperitoneales",
        "voluminosas": "con adenopatías retroperitoneales aumentadas de tamaño",
        "conglomerado": "con conglomerados adenopáticos retroperitoneales"
    },
    "grasa": {
        "normal": "grasa retroperitoneal de densidad conservada",
        "estriacion": "con aumento de la densidad de la grasa retroperitoneal",
        "borramiento": "con borramiento de los planos grasos retroperitoneales"
    },
    "colecciones": {
        "no": "sin colecciones retroperitoneales",
        "liquida": "con colección líquida retroperitoneal",
        "compleja": "con colección retroperitoneal de densidad heterogénea",
        "absceso_like": "con colección con contenido líquido y gas en su interior"
    },
    "gas": {
        "no": "sin presencia de gas retroperitoneal",
        "si": "con presencia de gas en el espacio retroperitoneal"
    },
    "masas": {
        "no": "sin masas retroperitoneales",
        "si": "con masa retroperitoneal de densidad de partes blandas",
        "heterogenea": "con masa retroperitoneal de aspecto heterogéneo",
        "quistica": "con lesión quística retroperitoneal"
    },
    "vascular": {
        "normal": "vasos retroperitoneales de calibre y trayecto conservados",
        "dilatados": "vasos retroperitoneales dilatados",
        "estenosis": "con disminución focal del calibre vascular",
        "trombo": "con defecto de llenado intraluminal en (vaso) compatible con material trombótico",
        "calcificaciones": "con calcificaciones parietales vasculares"
    },
    "otros": {
        "normal": ""
    }
}

rinones_suprarrenales = {

    # =========================
    # TAMAÑO Y MORFOLOGÍA
    # =========================
    "tamano_morfologia": {
        "normal": "Ambos riñones de localización, tamaño y morfología conservados",
        "aumentados": "Riñones aumentados de tamaño",
        "disminuidos": "Riñones de tamaño disminuido",
        "asimetria": "Asimetría en el tamaño renal"
    },

    # =========================
    # PARENQUIMA
    # =========================
    "parenquima": {
        "normal": "parénquima homogéneo con adecuada diferenciación córtico-medular",
        "disminuida": "con disminución de la diferenciación córtico-medular",
        "heterogeneo": "parénquima renal de aspecto heterogéneo",
        "hipodenso": "parénquima renal con áreas hipodensas",
        "hipercaptante": "con áreas de mayor realce tras contraste",
        "hipocaptante": "con áreas de menor realce tras contraste",
        "adelgazado": "adelgazamiento del parénquima renal"
    },

    # =========================
    # LESIONES RENALES
    # =========================
    "lesiones": {
        "ninguna": "",
        "quistes_simples": "Se identifican quistes renales simples",
        "quistes_complejos": "Se identifican quistes renales de aspecto complejo",
        "masa": "Se identifica masa renal",
        "lesion_focal": "Se identifica lesión focal renal",
        "absceso": "Se identifica colección compatible con absceso renal"
    },

    # 🔥 DETALLE LESIONES
    "detalle_lesion": {
        "lado": ["derecho", "izquierdo", "bilateral"],
        "localizacion": ["polo_superior", "polo_medio", "polo_inferior"],
        "tamano": "de aproximadamente (#) mm"
    },

    # =========================
    # SENOS RENALES
    # =========================
    "senos": {
        "normal": "Senos renales homogéneos",
        "alterado": "Senos renales heterogéneos"
    },

    # =========================
    # SISTEMA COLECTOR
    # =========================
    "sistema_colector": {
        "normal": "",
        "dilatado_bilateral": "Dilatación pielocalicial y ureteral bilateral",
        "dilatado_derecho": "Dilatación pielocalicial y ureteral derecha",
        "dilatado_izquierdo": "Dilatación pielocalicial y ureteral izquierda"
    },

    # 🔥 GRADO (hidronefrosis)
    "grado_dilatacion": {
        "leve": "de grado leve",
        "moderado": "de grado moderado",
        "severo": "de grado severo"
    },

    # =========================
    # LITIASIS
    # =========================
    "litiasis": {
        "no": "No se evidencia litiasis",
        "renal": "Se identifican imágenes hiperdensas compatibles con litiasis renal",
        "ureteral": "Se identifican imágenes hiperdensas compatibles con litiasis ureteral"
    },

    # 🔥 DETALLE LITIASIS
    "detalle_litiasis": {
        "lado": ["derecho", "izquierdo"],
        "localizacion": ["pelvis", "calices", "ureter_proximal", "ureter_medio", "ureter_distal"],
        "tamano": "de aproximadamente (#) mm"
    },

    # =========================
    # CAMBIOS PERIRRENALES
    # =========================
    "perirrenal": {
        "normal": "Sin alteraciones de la grasa perirrenal",
        "estriacion": "Con estriación de la grasa perirrenal",
        "liquido": "Con líquido perirrenal",
        "coleccion": "Con colección perirrenal"
    },

    # =========================
    # SUPRARRENALES
    # =========================
    "suprarrenales": {
        "normal": "Glándulas suprarrenales de morfología conservada",
        "engrosadas": "Glándulas suprarrenales engrosadas",
        "nodulo": "Se identifica nódulo suprarrenal",
        "masa": "Se identifica masa suprarrenal",
        "hiperplasia": "Hiperplasia suprarrenal bilateral"
    },

    # 🔥 DETALLE SUPRARRENAL
    "detalle_suprarrenal": {
        "lado": ["derecha", "izquierda", "bilateral"],
        "tamano": "de aproximadamente (#) mm"
    }
}

vejiga = {
    "distension": {
        "distendida": "Vejiga distendida",
        "moderada": "Vejiga con repleción moderada",
        "colapsada": "Vejiga colapsada"
    },

    "pared": {
        "normal": "pared vesical de grosor conservado y contornos regulares",
        "engrosada_difusa": "engrosamiento difuso de la pared vesical",
        "engrosada_focal": "engrosamiento focal de la pared vesical",
        "irregular": "pared vesical de contornos irregulares",
        "trabeculada": "pared vesical de aspecto trabeculado",
        "calcificada": "calcificaciones parietales vesicales"
    },

    "realce": {
        "normal": "sin alteraciones del realce parietal",
        "aumentado": "con aumento del realce parietal tras contraste",
        "disminuido": "con disminución del realce parietal"
    },

    "contenido": {
        "homogeneo": "contenido vesical homogéneo",
        "hiperdenso": "contenido vesical hiperdenso",
        "heterogeneo": "contenido vesical heterogéneo",
        "nivel": "presencia de nivel líquido-líquido o líquido-material",
        "litiasis": "imagen hiperdensa dependiente compatible con litiasis vesical",
        "coagulos": "material intravesical compatible con coágulos"
    },

    "lesiones": {
        "ninguna": "sin lesiones intraluminales evidentes",
        "masa": "lesión de densidad de partes blandas en el interior vesical",
        "vegetante": "lesión intraluminal de aspecto vegetante",
        "nodular": "engrosamiento nodular de la pared vesical"
    },

    "perivesical": {
        "normal": "",
        "estriacion": "con aumento de la densidad de la grasa perivesical",
        "liquido": "con líquido perivesical",
        "coleccion": "con colección perivesical",
        "invasion": "con cambios sugestivos de invasión a la grasa perivesical"
    },

    "gas": {
        "no": "",
        "lumen": "con presencia de gas en el lumen vesical",
        "pared": "con gas en la pared vesical (enfisema vesical)",
        "mixto": "con gas en lumen y pared vesical"
    },

    "dispositivo": {
        "ninguno": "",
        "sonda": "con sonda vesical en adecuada posición"
    }
}

prostata = {
    "tamano": {
        "normal": "próstata de tamaño conservado",
        "aumentada": "próstata aumentada de tamaño, volumen aproximado (###) cc",
        "disminuida": "próstata de tamaño reducido"
    },
    "morfologia": {
        "normal": "de contornos regulares",
        "lobulada": "de contornos lobulados",
        "irregular": "de contornos irregulares",
        "protrusion_vesical": "con protrusión hacia la luz vesical"
    },
    "densidad": {
        "homogenea": "de densidad homogénea",
        "heterogenea": "de densidad heterogénea",
        "hipodensa": "con áreas hipodensas",
        "hiperdensa": "con focos hiperdensos"
    },
    "realce": {
        "normal": "realce homogéneo tras contraste",
        "heterogeneo": "realce heterogéneo tras contraste",
        "hipercaptante": "con áreas de mayor realce",
        "hipocaptante": "con áreas de menor realce"
    },
    "calcificaciones": {
        "no": "",
        "si": "con calcificaciones prostáticas"
    },
    "lesiones": {
        "ninguna": "sin lesiones focales evidentes",
        "nodulo": "imagen nodular prostática",
        "masa": "lesión de densidad de partes blandas en la próstata"
    }
}

utero = {
    "estado": {
        "normal": "Útero de aspecto y tamaños conservados",
        "no_visible": "Útero no caracterizado",
        "lateralizado": "Útero lateralizado"
    },
    "tamano_morfologia": {
        "normal": "útero de tamaño conservado y contornos regulares",
        "aumentado": "útero aumentado de tamaño",
        "disminuido": "útero de tamaño reducido",
        "atrofico": "útero atrófico",
        "irregular": "útero con contornos irregulares",
        "lobulado": "útero de contornos lobulados"
    },
    "contenido_cavitario": {
        "normal": "cavidad uterina sin contenido",
        "liquido": "cavidad uterina con líquido",
        "material_hiperdenso": "cavidad uterina con material hiperdenso dependiente",
        "material_heterogeneo": "cavidad uterina con contenido heterogéneo"
    },
    "paredes": {
        "normal": "paredes uterinas homogéneas",
        "engrosada": "pared uterina engrosada",
        "irregular": "pared uterina de contornos irregulares"
    },
    "lesiones": {
        "ninguna": "sin lesiones focales ni difusas",
        "masa_solida": "masa sólida de densidad de partes blandas",
        "masa_quistica": "lesión quística intrauterina o intramural",
        "calcificacion": "calcificación focal o difusa en el útero"
    },
    "adyacencias": {
        "normal": "sin alteraciones de tejidos adyacentes",
        "liquido": "líquido adyacente al útero",
        "masa": "masa adyacente al útero",
        "estriacion": "estriación de la grasa peritélica"
    }
}

adicionales = {
    "infeccioso": {
        "absceso": "colección compatible con absceso",
        "espondilodiscitis": "hallazgos compatibles con espondilodiscitis"
    },
    "liquido": {
        "presente": "presencia de líquido libre"
    },
    "trauma": {
        "trayecto": "trayecto traumático con cambios inflamatorios"
    },
    "oseo": {
        "degenerativos": "cambios degenerativos",
        "liticos": "lesiones óseas líticas"
    }
}

# =========================
# FUNCIONES
# =========================

def generar_higado(input_higado):

    texto = ""

    # =========================
    # TAMAÑO
    # =========================
    if input_higado["lhd"] > 155:
        tamano_final = "aumentado"
    else:
        tamano_final = input_higado["tamano"]

    texto += higado["tamano"][tamano_final]

    if input_higado["lhd"] > 0:
        texto += f". Lóbulo hepático derecho de {input_higado['lhd']} mm"

    # =========================
    # CONTORNOS
    # =========================
    texto += ", " + higado["contornos"][input_higado["contornos"]]

    # =========================
    # ATENUACIÓN + PARÉNQUIMA
    # =========================
    atenuacion = input_higado["atenuacion"]
    parenquima = input_higado["parenquima"]

    if atenuacion == "normal" and parenquima == "normal":
        texto += ", parénquima de atenuación homogénea"

    elif atenuacion == "hipodensa" and parenquima == "normal":
        texto += ", disminución difusa de la atenuación"

    elif atenuacion == "hiperdensa" and parenquima == "normal":
        texto += ", aumento difuso de la atenuación"

    elif parenquima == "heterogeneo":
        if atenuacion == "normal":
            texto += ", parénquima heterogéneo"
        elif atenuacion == "hipodensa":
            texto += ", parénquima heterogéneo con disminución difusa de la atenuación"
        else:
            texto += ", parénquima heterogéneo con aumento difuso de la atenuación"

    # =========================
    # LESIONES
    # =========================
    if input_higado.get("hay_lesion"):

        tipo = input_higado.get("tipo_lesion")
        bordes = input_higado.get("bordes")
        lesiones = input_higado.get("lesiones_lista", [])

        if len(lesiones) == 1:

            les = lesiones[0]

            texto += f", se identifica lesión {tipo} en segmento {les['segmento']}"

            if les["tam"] > 0:
                texto += f" de {les['tam']} mm"

            if les["uh"] != 0:
                texto += f" ({les['uh']} UH)"

            if bordes:
                texto += f", de bordes {bordes}"

        elif len(lesiones) > 1:

            texto += f", se identifican múltiples lesiones {tipo}"

            if bordes:
                texto += f", de bordes {bordes}"

            texto += ":"

            for i, les in enumerate(lesiones):
                texto += f" lesión {i+1} en segmento {les['segmento']}"

                if les["tam"] > 0:
                    texto += f" de {les['tam']} mm"

                if les["uh"] != 0:
                    texto += f" ({les['uh']} UH)"

                texto += ";"

        # 🔥 Hallazgos adicionales
        extra = input_higado.get("hallazgos_extra")
        if extra:
            texto += f" {extra}"

    else:
        texto += ", sin evidencias de lesiones focales ni difusas"

    # =========================
    # VÍAS BILIARES
    # =========================
    texto += ". " + higado["vias_biliares"]["normal"]

    return texto

def generar_vesicula(input_vesicula):

    texto = []

    # =========================
    # VESÍCULA
    # =========================
    linea = f"Vesícula biliar de tamaño {input_vesicula.get('tamano', 'no especificado')}, con pared {input_vesicula.get('pared', 'no especificada')} y realce {input_vesicula.get('realce', 'no especificado')}."
    texto.append(linea)

    # Solo mostrar grosor si es relevante (>0)
    grosor = input_vesicula.get("grosor_pared", 0)
    if grosor and grosor > 0:
        texto.append(f"Grosor parietal de {grosor} mm.")

    # =========================
    # CONTENIDO
    # =========================
    contenido = input_vesicula.get("contenido")
    if contenido:
        texto.append(f"Contenido {contenido}.")

    # =========================
    # CÍSTICO
    # =========================
    cistico = input_vesicula.get("cistico")
    if cistico and cistico != "no_visible":
        texto.append(f"Conducto cístico {cistico}.")

    # =========================
    # PARED FOCAL
    # =========================
    if input_vesicula.get("pared") == "engrosada_focal":
        ubicacion = input_vesicula.get("ubicacion_pared")
        if ubicacion:
            texto.append(f"Engrosamiento focal en {ubicacion}.")

    # =========================
    # LITIASIS
    # =========================
    if contenido == "litiasis":

        n = input_vesicula.get("n_calculos", 1)
        tam = input_vesicula.get("tam_calculo", 0)
        loc = input_vesicula.get("ubicacion_calculo")

        linea = f"Se identifican {n} cálculo(s) de hasta {tam} mm"

        if loc:
            linea += f", localizados en {loc}"

        texto.append(linea + ".")

    # =========================
    # PERIVESICULAR (CORREGIDO 🔥)
    # =========================
    perivesicular = input_vesicula.get("perivesicular")

    if perivesicular and perivesicular != "normal":

        if perivesicular == "inflamacion":
            texto.append("Cambios perivesiculares inflamatorios.")

        elif perivesicular == "grasa":
            texto.append("Cambios con densificación de la grasa perivesicular.")

        elif perivesicular == "liquido":
            texto.append("Cambios con presencia de líquido perivesicular.")

        elif perivesicular == "coleccion":
            linea = "Se identifica colección perivesicular"

            if input_vesicula.get("gas_coleccion"):
                linea += " con presencia de gas"

            loc = input_vesicula.get("ubicacion_coleccion")
            if loc:
                linea += f", localizada en región {loc}"

            texto.append(linea + ".")

    # =========================
    # COLECCIÓN (solo si NO se mencionó antes)
    # =========================
    if input_vesicula.get("hay_coleccion"):

        linea = "Se identifica colección perivesicular"

        tam = input_vesicula.get("tam_coleccion")
        if tam:
            linea += f" de {tam}"

        loc = input_vesicula.get("ubicacion_coleccion")
        if loc:
            linea += f", localizada en región {loc}"

        if input_vesicula.get("gas_coleccion"):
            linea += " con presencia de gas"

        # 🔥 evitar duplicado: solo agregar si no ya se mencionó
        if "colección perivesicular" not in " ".join(texto):
            texto.append(linea + ".")

    # =========================
    # LESIONES
    # =========================
    lesiones = input_vesicula.get("lesiones", [])

    if lesiones:

        texto.append("Se identifican las siguientes lesiones:")

        for i, lesion in enumerate(lesiones, start=1):

            tipo = lesion.get("tipo", "no especificado")
            tam = lesion.get("tamaño", 0)

            linea = f"Lesión {i}: {tipo} de aproximadamente {tam} mm"

            texto.append(linea + ".")

    # =========================
    # DISPOSITIVO
    # =========================
    if input_vesicula.get("dispositivo") == "colecistostomia":

        linea = "Se observa colecistostomía"

        via = input_vesicula.get("via")
        if via:
            linea += f" con vía {via}"

        trayecto = input_vesicula.get("trayecto")
        if trayecto:
            linea += f" y trayecto {trayecto}"

        texto.append(linea + ".")

    # =========================
    # GAS
    # =========================
    gas = input_vesicula.get("gas")

    if gas and gas != "no":
        texto.append(f"Presencia de gas en {gas}.")

    # =========================
    # OUTPUT
    # =========================
    return " ".join(texto)

def generar_estomago(input_estomago):

    texto = ""

    # =========================
    # DISTENSIÓN
    # =========================
    dist = input_estomago["distension"]

    if dist == "adecuada":
        texto += "Estómago con adecuada distensión"
    elif dist == "distendido":
        texto += "Estómago distendido"
    elif dist == "poco_distendido":
        texto += "Estómago poco distendido"
    else:
        texto += "Estómago colapsado"

    # =========================
    # CONTENIDO
    # =========================
    contenido = input_estomago["contenido"]

    contenido_map = {
        "vacio": "sin contenido significativo",
        "gas": "con contenido gaseoso",
        "liquido": "con contenido líquido",
        "mixto": "con contenido mixto",
        "material_denso": "con material denso en su interior"
    }

    texto += ", " + contenido_map[contenido]

    # =========================
    # PARED
    # =========================
    pared = input_estomago["pared"]
    patron = input_estomago["patron"]
    realce = input_estomago["realce"]
    grosor = input_estomago["grosor"]

    if pared == "normal":
        texto += ", paredes de grosor y contornos conservados"
    else:
        texto += ", con alteración parietal"

        if pared == "engrosada_difusa":
            texto += " de tipo difuso"
        elif pared == "engrosada_focal":
            texto += " de tipo focal"
        elif pared == "irregular":
            texto += " de contornos irregulares"

        if grosor > 0:
            texto += f", con grosor de aproximadamente {grosor} mm"

        if patron != "normal":
            texto += f", de patrón {patron}"

        if realce != "normal":
            texto += f", con realce {realce}"

    # =========================
    # LESIONES (🔥 NUEVO)
    # =========================
    if input_estomago.get("hay_lesion"):

        lesiones = input_estomago.get("lesiones_lista", [])

        if len(lesiones) == 1:

            les = lesiones[0]

            texto += f", se identifica lesión tipo {les['tipo']} en {les['localizacion']}"

            if les["tamaño"] > 0:
                texto += f" de {les['tamaño']} mm"

            if les["tipo"] == "ulceracion":
                if les.get("profundidad"):
                    texto += f", de aspecto {les['profundidad']}"

                if les.get("complicacion") != "ninguna":
                    texto += f", asociada a {les['complicacion']}"

        elif len(lesiones) > 1:

            texto += ", se identifican múltiples lesiones:"

            for i, les in enumerate(lesiones):
                texto += f" lesión {i+1} tipo {les['tipo']} en {les['localizacion']}"

                if les["tamaño"] > 0:
                    texto += f" de {les['tamaño']} mm"

                if les["tipo"] == "ulceracion":
                    if les.get("profundidad"):
                        texto += f", {les['profundidad']}"

                    if les.get("complicacion") != "ninguna":
                        texto += f", con {les['complicacion']}"

                texto += ";"

    else:
        texto += ", sin lesiones evidentes"

    # =========================
    # LUZ
    # =========================
    luz_map = {
        "normal": "luz de calibre conservado",
        "disminuida": "disminución del calibre luminal",
        "aumentada": "aumento del calibre luminal"
    }

    texto += ", " + luz_map[input_estomago["luz"]]

    # =========================
    # PERIGÁSTRICO
    # =========================
    peri_map = {
        "normal": "sin alteraciones perigástricas",
        "estriacion": "con estriación de la grasa perigástrica",
        "liquido": "con líquido perigástrico",
        "gas": "con gas extraluminal perigástrico"
    }

    texto += ", " + peri_map[input_estomago["perigastrico"]]

    # =========================
    # OTROS
    # =========================
    otros = input_estomago["otros"]

    if otros == "sonda":
        texto += ", con sonda nasogástrica en su interior"
    elif otros == "gastrectomia":
        texto += ", cambios postquirúrgicos compatibles con gastrectomía"

    texto += "."

    return texto

def generar_bazo(input_bazo):

    texto = ""

    # =========================
    # GENERAL
    # =========================
    texto += bazo["tamano"][input_bazo["tamano"]]
    texto += ", " + bazo["contornos"][input_bazo["contornos"]]
    texto += ", " + bazo["parenquima"][input_bazo["parenquima"]]

    # REALCE (solo si no es normal)
    if input_bazo["realce"] != "normal":
        texto += ", " + bazo["realce"][input_bazo["realce"]]

    # =========================
    # LESIONES
    # =========================
    if input_bazo["hay_lesion"]:

        lista = input_bazo.get("lesiones_lista", [])

        if len(lista) == 1:
            l = lista[0]

            texto += ", se identifica "
            texto += bazo["lesiones"][l["tipo"]]

            # tamaño
            if l["tam"] > 0:
                texto += f" de {l['tam']} mm"

            # localización
            if l["localizacion"] != "difuso":
                texto += f" en {l['localizacion'].replace('_', ' ')}"

        elif len(lista) > 1:

            texto += ", se identifican múltiples lesiones esplénicas"

            for i, l in enumerate(lista):
                texto += f"; lesión {i+1}: "
                texto += bazo["lesiones"][l["tipo"]]

                if l["tam"] > 0:
                    texto += f" de {l['tam']} mm"

                if l["localizacion"] != "difuso":
                    texto += f" en {l['localizacion'].replace('_', ' ')}"

    else:
        texto += ", sin lesiones focales"

    # =========================
    # CÁPSULA
    # =========================
    if input_bazo["capsula"] != "normal":
        texto += ", " + bazo["capsula"][input_bazo["capsula"]]

    # =========================
    # PERIESPLÉNICO
    # =========================
    if input_bazo["periesplenico"] != "normal":
        texto += ", " + bazo["periesplenico"][input_bazo["periesplenico"]]

    # =========================
    # FINAL
    # =========================
    texto += "."

    return texto

def generar_pancreas(input_pancreas):

    texto = ""

    # =========================
    # TAMAÑO + CONTORNOS
    # =========================
    texto += pancreas["tamano"][input_pancreas["tamano"]]
    texto += ", " + pancreas["contornos"][input_pancreas["contornos"]]

    # =========================
    # PARÉNQUIMA + REALCE
    # =========================
    texto += ", " + pancreas["parenquima"][input_pancreas["parenquima"]]

    if input_pancreas["realce"] != "normal":
        texto += ", " + pancreas["realce"][input_pancreas["realce"]]

    # =========================
    # LESIONES 🔥
    # =========================
    if input_pancreas.get("hay_lesion"):

        lesiones = input_pancreas.get("lesiones_lista", [])

        if len(lesiones) == 1:

            les = lesiones[0]

            texto += f", se identifica {pancreas['lesiones'][les['tipo']]} "
            texto += pancreas["localizacion"][les["localizacion"]]

            if les["tam"] > 0:
                texto += f" de {les['tam']} mm"

            if les["uh"] != 0:
                texto += f" ({les['uh']} UH)"

        elif len(lesiones) > 1:

            texto += ", se identifican múltiples lesiones:"

            for i, les in enumerate(lesiones):

                texto += f" lesión {i+1} {les['tipo']} "
                texto += pancreas["localizacion"][les["localizacion"]]

                if les["tam"] > 0:
                    texto += f" de {les['tam']} mm"

                if les["uh"] != 0:
                    texto += f" ({les['uh']} UH)"

                texto += ";"

    else:
        texto += ", sin lesiones focales evidentes"

    # =========================
    # CONDUCTO PANCREÁTICO
    # =========================
    texto += ", " + pancreas["conducto_principal"][input_pancreas["conducto"]]

    # =========================
    # COLÉDOCO
    # =========================
    texto += ", " + pancreas["coledoco"][input_pancreas["coledoco"]]

    # =========================
    # PERIPANCREÁTICO
    # =========================
    if input_pancreas["peripancreatico"] != "normal":
        texto += ", " + pancreas["peripancreatico"][input_pancreas["peripancreatico"]]

    else:
        texto += ", sin cambios inflamatorios peripancreáticos"

    texto += "."

    return texto

def generar_asas_delgadas(input_asas):

    texto = ""

    # =========================
    # CALIBRE
    # =========================
    texto += asas_delgadas["calibre"][input_asas["calibre"]]

    # =========================
    # DISTENSIÓN
    # =========================
    if input_asas["distension"] != "normal":
        texto += ", " + asas_delgadas["distension"][input_asas["distension"]]

    # =========================
    # CONTENIDO
    # =========================
    texto += ", con " + asas_delgadas["contenido"][input_asas["contenido"]]

    # =========================
    # PARED
    # =========================
    if input_asas["pared"] != "normal":
        texto += ", " + asas_delgadas["pared"][input_asas["pared"]]

    # =========================
    # REALCE
    # =========================
    if input_asas["realce"] != "normal":
        texto += ", " + asas_delgadas["realce"][input_asas["realce"]]

    # =========================
    # PATRÓN
    # =========================
    if input_asas["patron"] != "normal":
        texto += ", " + asas_delgadas["patron"][input_asas["patron"]]

    # =========================
    # MOTILIDAD
    # =========================
    if input_asas["motilidad"] != "normal":
        texto += ", " + asas_delgadas["motilidad"][input_asas["motilidad"]]

    # =========================
    # PERIENTÉRICO
    # =========================
    if input_asas["perienterico"] != "normal":
        texto += ", " + asas_delgadas["perienterico"][input_asas["perienterico"]]
    else:
        texto += ", sin alteraciones de la grasa perientérica"

    # =========================
    # LOCALIZACIÓN
    # =========================
    if input_asas["localizacion"] != "difuso":
        texto += " " + asas_delgadas["localizacion"][input_asas["localizacion"]]

    # =========================
    # FINAL
    # =========================
    texto += "."

    return texto

def generar_asas_gruesas(input_asas_gruesas):

    partes = []

    # =========================
    # CALIBRE
    # =========================
    if input_asas_gruesas["calibre"] == "normal":
        partes.append("Asas intestinales gruesas de calibre conservado")
    elif input_asas_gruesas["calibre"] == "colapsadas":
        partes.append("Asas intestinales gruesas colapsadas")
    elif input_asas_gruesas["calibre"] == "dilatadas":
        if "calibre_mm" in input_asas_gruesas:
            partes.append(f"Asas intestinales gruesas dilatadas, con calibre máximo de {input_asas_gruesas['calibre_mm']} mm")
        else:
            partes.append("Asas intestinales gruesas dilatadas")

    # =========================
    # DISTRIBUCIÓN
    # =========================
    if input_asas_gruesas["distribucion"] != "normal":
        if input_asas_gruesas["distribucion"] == "focal":
            partes.append("de compromiso focal")
        elif input_asas_gruesas["distribucion"] == "difusa":
            partes.append("de compromiso difuso")

    # =========================
    # CONTENIDO
    # =========================
    contenido_map = {
        "gas": "con contenido gaseoso",
        "heces": "con contenido fecaloideo",
        "liquido": "con contenido líquido",
        "mixto": "con contenido mixto (gas y material fecaloideo/líquido)",
        "material_denso": "con material hiperdenso en su luz"
    }

    partes.append(contenido_map[input_asas_gruesas["contenido"]])

    # =========================
    # PARED
    # =========================
    pared_map = {
        "normal": "de paredes finas y regulares",
        "engrosada": "con engrosamiento parietal",
        "engrosada_difusa": "con engrosamiento parietal difuso",
        "engrosada_focal": "con engrosamiento parietal focal",
        "irregular": "de contornos parietales irregulares"
    }

    partes.append(pared_map[input_asas_gruesas["pared"]])

    # =========================
    # PATRÓN
    # =========================
    if input_asas_gruesas["patron"] == "estratificado":
        partes.append("de aspecto estratificado")
    elif input_asas_gruesas["patron"] == "homogeneo":
        partes.append("de aspecto homogéneo")

    # =========================
    # REALCE
    # =========================
    if input_asas_gruesas["realce"] == "hipercaptante":
        partes.append("con aumento del realce parietal tras contraste")
    elif input_asas_gruesas["realce"] == "hipocaptante":
        partes.append("con disminución del realce parietal tras contraste")

    # =========================
    # LOCALIZACIÓN GLOBAL
    # =========================
    if input_asas_gruesas["localizacion"] != "difuso":
        loc_map = {
            "ciego": "en ciego",
            "colon_ascendente": "en colon ascendente",
            "colon_transverso": "en colon transverso",
            "colon_descendente": "en colon descendente",
            "sigmoides": "en colon sigmoides",
            "recto": "en recto"
        }
        partes.append(loc_map[input_asas_gruesas["localizacion"]])

    # =========================
    # PERICOLÓNICO
    # =========================
    peri_map = {
        "normal": "sin alteraciones de la grasa pericolónica",
        "estriacion": "con aumento de la densidad de la grasa pericolónica",
        "liquido": "con líquido libre pericolónico",
        "gas": "con presencia de gas extraluminal pericolónico"
    }

    partes.append(peri_map[input_asas_gruesas["pericolico"]])

    # =========================
    # LESIONES
    # =========================
    if input_asas_gruesas.get("hay_lesion"):

        for lesion in input_asas_gruesas["lesiones_lista"]:

            texto_lesion = ""

            if lesion["tipo"] == "masa":
                texto_lesion = "Se identifica masa de densidad de partes blandas"
            elif lesion["tipo"] == "engrosamiento_focal":
                texto_lesion = "Se identifica engrosamiento focal de la pared colónica"
            elif lesion["tipo"] == "diverticulos":
                texto_lesion = "Se identifican divertículos colónicos"

            loc_map = {
                "ciego": "en ciego",
                "colon_ascendente": "en colon ascendente",
                "colon_transverso": "en colon transverso",
                "colon_descendente": "en colon descendente",
                "sigmoides": "en colon sigmoides",
                "recto": "en recto"
            }

            texto_lesion += " " + loc_map[lesion["localizacion"]]

            partes.append(texto_lesion)

    # =========================
    # RECTO
    # =========================
    recto_map = {
        "normal": "Recto de calibre y paredes conservadas",
        "distendido": "Recto distendido",
        "pared_engrosada": "Recto con engrosamiento parietal",
        "contenido": "Ampolla rectal con contenido fecaloideo"
    }

    partes.append(recto_map[input_asas_gruesas["recto"]])

    # =========================
    # APÉNDICE
    # =========================
    ap_map = {
        "no_visible": "Apéndice no identificado",
        "normal": "Apéndice de calibre y paredes conservadas",
        "engrosado": "Apéndice aumentado de calibre",
        "pared_engrosada": "Apéndice con engrosamiento parietal"
    }

    texto_apendice = ap_map[input_asas_gruesas["apendice"]]

    extras = input_asas_gruesas.get("hallazgos_apendice", [])

    extras_map = {
        "fecalito": "con apendicolito",
        "periapendicular": "con estriación de la grasa periapendicular",
        "liquido": "con líquido periapendicular"
    }

    for extra in extras:
        texto_apendice += " " + extras_map[extra]

    partes.append(texto_apendice)

    # =========================
    # RESULTADO FINAL
    # =========================
    texto_final = ", ".join(partes) + "."

    return texto_final

def generar_retroperitoneo(input_rp):

    partes = []

    # =========================
    # ADENOPATÍAS
    # =========================
    adeno_map = {
        "no": "Sin adenopatías retroperitoneales",
        "si": "Con adenopatías retroperitoneales",
        "voluminosas": "Con adenopatías retroperitoneales aumentadas de tamaño",
        "conglomerado": "Con conglomerados adenopáticos retroperitoneales"
    }

    texto_adeno = adeno_map[input_rp["adenopatias"]]

    if input_rp["adenopatias"] != "no" and "localizacion_adenopatias" in input_rp:
        loc_map = {
            "paraaorticas": "de localización paraaórtica",
            "interaortocava": "en región interaortocava",
            "paracava": "de localización paracava",
            "iliacas": "en cadenas ilíacas",
            "difusa": "de distribución difusa"
        }
        texto_adeno += " " + loc_map[input_rp["localizacion_adenopatias"]]

    partes.append(texto_adeno)

    # =========================
    # GRASA
    # =========================
    grasa_map = {
        "normal": "Grasa retroperitoneal de densidad conservada",
        "estriacion": "Con aumento de la densidad de la grasa retroperitoneal",
        "borramiento": "Con borramiento de los planos grasos retroperitoneales"
    }

    partes.append(grasa_map[input_rp["grasa"]])

    # =========================
    # COLECCIONES
    # =========================
    if input_rp["colecciones"] != "no":

        colec_map = {
            "liquida": "Se identifica colección líquida retroperitoneal",
            "compleja": "Se identifica colección retroperitoneal de densidad heterogénea",
            "absceso_like": "Se identifica colección con contenido líquido y gas en su interior"
        }

        texto_colec = colec_map[input_rp["colecciones"]]

        if "tam_coleccion" in input_rp:
            texto_colec += f" de aproximadamente {input_rp['tam_coleccion']} mm"

        if "loc_coleccion" in input_rp and input_rp["loc_coleccion"]:
            texto_colec += f", ubicada en {input_rp['loc_coleccion']}"

        partes.append(texto_colec)

    # =========================
    # MASAS
    # =========================
    if input_rp["masas"] != "no":

        masa_map = {
            "solida": "Se identifica masa retroperitoneal de densidad de partes blandas",
            "heterogenea": "Se identifica masa retroperitoneal de aspecto heterogéneo",
            "quistica": "Se identifica lesión quística retroperitoneal"
        }

        texto_masa = masa_map[input_rp["masas"]]

        if "tam_masa" in input_rp:
            texto_masa += f" de aproximadamente {input_rp['tam_masa']} mm"

        if "loc_masa" in input_rp and input_rp["loc_masa"]:
            texto_masa += f", ubicada en {input_rp['loc_masa']}"

        if input_rp.get("efecto_masa"):
            texto_masa += ", con efecto de masa sobre estructuras adyacentes"

        partes.append(texto_masa)

    # =========================
    # GAS
    # =========================
    gas_map = {
        "no": "Sin presencia de gas retroperitoneal",
        "si": "Con presencia de gas en el espacio retroperitoneal"
    }

    partes.append(gas_map[input_rp["gas"]])

    # =========================
    # VASCULAR
    # =========================
    vascular_map = {
        "normal": "Vasos retroperitoneales de calibre y trayecto conservados",
        "dilatados": "Vasos retroperitoneales dilatados",
        "estenosis": "Con disminución focal del calibre vascular",
        "trombo": "Con defecto de llenado intraluminal compatible con material trombótico",
        "calcificaciones": "Con calcificaciones parietales vasculares"
    }

    texto_vascular = vascular_map[input_rp["vascular"]]

    if input_rp["vascular"] in ["trombo", "estenosis"] and "vaso" in input_rp:
        vaso_map = {
            "aorta": " a nivel de la aorta",
            "vena_cava": " a nivel de la vena cava inferior",
            "iliacos": " en vasos ilíacos",
            "mesentericos": " en vasos mesentéricos"
        }
        texto_vascular += vaso_map[input_rp["vaso"]]

    partes.append(texto_vascular)

    # =========================
    # OTROS
    # =========================
    if input_rp.get("otros"):
        partes.append(input_rp["otros"])

    # =========================
    # RESULTADO FINAL
    # =========================
    texto_final = ", ".join(partes) + "."

    return texto_final

def generar_rinones_suprarrenales(input_rinon):
    
    texto = []

    # =========================
    # GENERAL
    # =========================
    texto.append(rinones_suprarrenales["tamano_morfologia"][input_rinon["tamano"]])

    if input_rinon["parenquima"] != "normal":
        texto.append(rinones_suprarrenales["parenquima"][input_rinon["parenquima"]])
    else:
        texto.append(rinones_suprarrenales["parenquima"]["normal"])

    # =========================
    # LESIONES
    # =========================
    if input_rinon.get("hay_lesion"):

        lesiones_txt = []

        for lesion in input_rinon.get("lesiones_lista", []):
            tipo = lesion["tipo"]
            lado = lesion["lado"]
            loc = lesion["localizacion"]
            tam = lesion["tam"]

            base = rinones_suprarrenales["lesiones"][tipo]

            detalle = f" {lado}, a nivel del {loc}, de aproximadamente {tam} mm"
            lesiones_txt.append(base + detalle)

        texto.append(". ".join(lesiones_txt))

    # =========================
    # SISTEMA COLECTOR
    # =========================
    sistema = input_rinon["sistema"]

    if sistema != "normal":
        txt_sistema = rinones_suprarrenales["sistema_colector"][sistema]

        if "grado" in input_rinon:
            txt_sistema += " " + rinones_suprarrenales["grado_dilatacion"][input_rinon["grado"]]

        texto.append(txt_sistema)

    # =========================
    # LITIASIS
    # =========================
    litiasis = input_rinon["litiasis"]

    if litiasis != "no":
        txt_lit = rinones_suprarrenales["litiasis"][litiasis]

        lado = input_rinon["lado_lit"]
        loc = input_rinon["loc_lit"]
        tam = input_rinon["tam_lit"]

        txt_lit += f" en {lado}, a nivel de {loc}, de aproximadamente {tam} mm"

        texto.append(txt_lit)
    else:
        texto.append(rinones_suprarrenales["litiasis"]["no"])

    # =========================
    # PERIRRENAL
    # =========================
    if input_rinon["perirrenal"] != "normal":
        texto.append(rinones_suprarrenales["perirrenal"][input_rinon["perirrenal"]])
    else:
        texto.append(rinones_suprarrenales["perirrenal"]["normal"])

    # =========================
    # SUPRARRENALES
    # =========================
    suprarrenales = input_rinon["suprarrenales"]

    txt_sup = rinones_suprarrenales["suprarrenales"][suprarrenales]

    if suprarrenales in ["nodulo", "masa"]:
        lado = input_rinon["lado_sup"]
        tam = input_rinon["tam_sup"]
        txt_sup += f" en la {lado}, de aproximadamente {tam} mm"

    texto.append(txt_sup)

    # =========================
    # OUTPUT FINAL
    # =========================
    return ". ".join(texto) + "."

def generar_vejiga(input_vejiga):

    texto = []

    # =========================
    # DISTENSIÓN
    # =========================
    texto.append(vejiga["distension"][input_vejiga["distension"]])

    # =========================
    # PARED
    # =========================
    texto.append(vejiga["pared"][input_vejiga["pared"]])

    # Realce (si no es normal)
    if input_vejiga["realce"] != "normal":
        texto.append(vejiga["realce"][input_vejiga["realce"]])

    # =========================
    # CONTENIDO
    # =========================
    texto.append(vejiga["contenido"][input_vejiga["contenido"]])

    # =========================
    # LESIONES
    # =========================
    if input_vejiga.get("hay_lesion"):

        tipo = input_vejiga["tipo_lesion"]
        loc = input_vejiga["localizacion"]
        tam = input_vejiga["tam_lesion"]

        txt_lesion = vejiga["lesiones"][tipo]
        txt_lesion += f" en {loc}, de aproximadamente {tam} mm"

        texto.append(txt_lesion)
    else:
        texto.append(vejiga["lesiones"]["ninguna"])

    # =========================
    # PERIVESICAL
    # =========================
    if input_vejiga["perivesical"] != "normal":
        texto.append(vejiga["perivesical"][input_vejiga["perivesical"]])

    # =========================
    # GAS
    # =========================
    if input_vejiga["gas"] != "no":
        texto.append(vejiga["gas"][input_vejiga["gas"]])

    # =========================
    # DISPOSITIVO
    # =========================
    if input_vejiga["dispositivo"] != "ninguno":
        texto.append(vejiga["dispositivo"][input_vejiga["dispositivo"]])

    # =========================
    # OUTPUT FINAL
    # =========================
    return ". ".join(texto) + "."

def generar_pelvis(input_pelvis):
    if input_pelvis["tipo"] == "prostata":
        return "Próstata " + prostata["estado"][input_pelvis["estado"]]
    else:
        return utero["estado"][input_pelvis["estado"]] + "."

def generar_pelvis(input_pelvis):

    texto = []

    sexo = input_pelvis["sexo"]

    # =========================
    # 🔵 PRÓSTATA
    # =========================
    if sexo == "masculino":

        # Tamaño
        tam = input_pelvis["tamano"]

        if tam == "aumentada":
            vol = input_pelvis.get("volumen", "")
            texto.append(f"Próstata aumentada de tamaño, con volumen aproximado de {vol} cc")
        else:
            texto.append(prostata["tamano"][tam])

        # Morfología
        texto.append(prostata["morfologia"][input_pelvis["morfologia"]])

        # Densidad
        texto.append(prostata["densidad"][input_pelvis["densidad"]])

        # Realce
        texto.append(prostata["realce"][input_pelvis["realce"]])

        # Calcificaciones
        if input_pelvis["calcificaciones"] == "si":
            texto.append(prostata["calcificaciones"]["si"])

        # Lesiones
        if input_pelvis["lesiones"] != "ninguna":
            texto.append(prostata["lesiones"][input_pelvis["lesiones"]])
        else:
            texto.append(prostata["lesiones"]["ninguna"])

    # =========================
    # 🟣 ÚTERO
    # =========================
    else:

        # Estado general
        texto.append(utero["estado"][input_pelvis["estado"]])

        # Tamaño / morfología
        texto.append(utero["tamano_morfologia"][input_pelvis["tamano_morfologia"]])

        # Contenido cavitario
        texto.append(utero["contenido_cavitario"][input_pelvis["contenido"]])

        # Paredes
        texto.append(utero["paredes"][input_pelvis["paredes"]])

        # Lesiones
        if input_pelvis["lesiones"] != "ninguna":
            texto.append(utero["lesiones"][input_pelvis["lesiones"]])
        else:
            texto.append(utero["lesiones"]["ninguna"])

        # Adyacencias
        if input_pelvis["adyacencias"] != "normal":
            texto.append(utero["adyacencias"][input_pelvis["adyacencias"]])

    # =========================
    # OUTPUT FINAL
    # =========================
    return ". ".join(texto) + "."

def generar_adicionales(input_adicionales):

    texto = []

    # =========================
    # INFECCIOSO
    # =========================
    for item in input_adicionales.get("infeccioso", []):
        texto.append(adicionales["infeccioso"][item])

    # =========================
    # LÍQUIDO
    # =========================
    if input_adicionales.get("liquido"):
        texto.append(adicionales["liquido"]["presente"])

    # =========================
    # TRAUMA
    # =========================
    if input_adicionales.get("trauma"):
        texto.append(adicionales["trauma"]["trayecto"])

    # =========================
    # ÓSEO
    # =========================
    for item in input_adicionales.get("oseo", []):
        texto.append(adicionales["oseo"][item])

    # =========================
    # OUTPUT FINAL
    # =========================
    if texto:
        return ". ".join(texto) + "."
    else:
        return ""

# =========================
# IMPORTS
# =========================
import requests
import os

# =========================
# SCORING HEPÁTICO
# =========================

def scoring_hepatico(input_higado: dict):

    scores = {
        "Hepatocarcinoma (HCC)": 0,
        "Metástasis hepáticas": 0,
        "Hemangioma hepático": 0,
        "Quistes hepáticos simples": 0,
        "Esteatosis hepática": 0
    }

    hallazgos_extra = input_higado.get("hallazgos_extra", "").lower()

    # DIFUSO
    if input_higado["atenuacion"] == "hipodensa":
        scores["Esteatosis hepática"] += 2

    if input_higado["parenquima"] == "heterogeneo":
        scores["Hepatocarcinoma (HCC)"] += 1
        scores["Metástasis hepáticas"] += 1

    if input_higado["contornos"] == "irregulares":
        scores["Hepatocarcinoma (HCC)"] += 2

    if input_higado["tamano"] == "aumentado":
        scores["Hepatocarcinoma (HCC)"] += 1
        scores["Metástasis hepáticas"] += 1

    # LESIONES
    if input_higado.get("hay_lesion"):

        lesiones = input_higado.get("lesiones_lista", [])
        n = len(lesiones)

        if n > 1:
            scores["Metástasis hepáticas"] += 4
        else:
            scores["Hepatocarcinoma (HCC)"] += 2

        for l in lesiones:

            tipo = l.get("tipo")
            bordes = l.get("bordes")
            tam = l.get("tam", 0)
            uh = l.get("uh", 0)

            if tipo == "quistica":
                scores["Quistes hepáticos simples"] += 3

            elif tipo == "solida":
                scores["Hepatocarcinoma (HCC)"] += 2
                scores["Metástasis hepáticas"] += 2
                scores["Hemangioma hepático"] += 1

            elif tipo == "mixta":
                scores["Hepatocarcinoma (HCC)"] += 2
                scores["Metástasis hepáticas"] += 2

            if bordes == "mal_definidos":
                scores["Metástasis hepáticas"] += 2
                scores["Hepatocarcinoma (HCC)"] += 2

            elif bordes == "definidos":
                scores["Hemangioma hepático"] += 2
                scores["Quistes hepáticos simples"] += 1

            if tam > 50:
                scores["Hepatocarcinoma (HCC)"] += 1

            if uh < 20:
                scores["Quistes hepáticos simples"] += 2

            if uh > 100:
                scores["Hepatocarcinoma (HCC)"] += 2
                scores["Metástasis hepáticas"] += 2
                scores["Hemangioma hepático"] += 1
                scores["Quistes hepáticos simples"] -= 2
            
            if 30 <= uh <= 70:
                scores["Hemangioma hepático"] += 2

            # PATRONES CLAVE
            if tipo == "quistica" and uh < 20 and bordes == "definidos":
                scores["Quistes hepáticos simples"] += 6
                scores["Hepatocarcinoma (HCC)"] -= 2
                scores["Metástasis hepáticas"] -= 2

            if "realce periférico" in hallazgos_extra:
                scores["Hemangioma hepático"] += 5
                scores["Hepatocarcinoma (HCC)"] -= 3
                scores["Metástasis hepáticas"] -= 2

            if tipo == "quistica" and uh > 50:
                scores["Quistes hepáticos simples"] -= 4
                scores["Hepatocarcinoma (HCC)"] += 2
                scores["Metástasis hepáticas"] += 2

            if tam <= 30 and bordes == "definidos":
                scores["Hemangioma hepático"] += 3
                scores["Hepatocarcinoma (HCC)"] -= 2
                scores["Metástasis hepáticas"] -= 1

    # evitar negativos
    scores = {k: max(0, v) for k, v in scores.items()}

    total = sum(scores.values())

    if total == 0:
        return []

    resultados = [
        {"dx": dx, "prob": round(score / total, 3)}
        for dx, score in scores.items() if score > 0
    ]

    resultados.sort(key=lambda x: x["prob"], reverse=True)

    return resultados[:3]

# =========================
# IA (MISTRAL)
# =========================
def generar_impresion_ia(input_higado: dict, diferenciales: list):

    API_URL = "https://router.huggingface.co/v1/chat/completions"

    import os

    HEADERS = {
        "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
        "Content-Type": "application/json"
    }

    dx_txt = "\n".join([
        f"- {d['dx']} ({d['prob']*100:.1f}%)"
        for d in diferenciales
    ])

    prompt = prompt = f"""
Actúa como radiólogo experto en TAC.

Datos clínicos estructurados:
- Número de lesiones: {len(input_higado.get("lesiones_lista", []))}
- Tipo de lesión: {input_higado.get("lesiones_lista", [{}])[0].get("tipo", "")}
- Tamaño: {input_higado.get("lesiones_lista", [{}])[0].get("tam", "")} mm
- UH: {input_higado.get("lesiones_lista", [{}])[0].get("uh", "")}

Diagnósticos diferenciales:
{dx_txt}

Instrucciones:
- NO inventes hallazgos
- NO cambies número de lesiones
- NO asumas baja densidad si UH es alto
- Usa lenguaje médico formal
- Máximo 4 líneas
- Usa términos: "sugestivo de", "compatible con", "no se descarta"
- Prioriza el diagnóstico más probable sin afirmarlo como definitivo

if len(lesiones_lista) == 1:
    contexto_lesiones = "lesión única"
else:
    contexto_lesiones = "lesiones múltiples"

Redacta la impresión diagnóstica:
"""

    payload = {
        "model": "Qwen/Qwen2.5-7B-Instruct",
        "messages": [
            {"role": "system", "content": "Eres un radiólogo experto."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 120
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=20)

        if response.status_code != 200:
            return f"Error IA: {response.text}"

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error conexión IA: {str(e)}"

# =========================
# STREAMLIT
# =========================

with st.expander("Hígado", expanded=False):

    # =========================
    # GENERAL
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        tamano = st.radio(
            "Tamaño",
            ["normal", "aumentado", "disminuido"],
            horizontal=True,
            key="higado_tamano"
        )

        contornos = st.radio(
            "Contornos",
            ["regulares", "irregulares"],
            horizontal=True,
            key="higado_contornos"
        )

    with col2:
        atenuacion = st.radio(
            "Atenuación",
            ["normal", "hipodensa", "hiperdensa"],
            horizontal=True,
            key="higado_atenuacion"
        )

        parenquima = st.radio(
            "Parénquima",
            ["normal", "heterogeneo"],
            horizontal=True,
            key="higado_parenquima"
        )

    # =========================
    # LESIONES
    # =========================
    st.markdown("##### Lesiones hepáticas")

    hay_lesion = st.checkbox("¿Se identifican lesiones?", key="higado_lesion")

    lesiones_lista = []

    if hay_lesion:

        n_lesiones = st.number_input(
            "Número de lesiones",
            min_value=1,
            max_value=5,
            step=1,
            key="higado_n_lesiones"
        )

        for i in range(n_lesiones):

            st.markdown(f"**Lesión {i+1}**")

            col1, col2 = st.columns(2)

            with col1:
                tipo = st.radio(
                    "Tipo",
                    ["quistica", "solida", "mixta"],
                    horizontal=True,
                    key=f"higado_tipo_{i}"
                )

            with col2:
                bordes = st.radio(
                    "Bordes",
                    ["definidos", "mal_definidos"],
                    horizontal=True,
                    key=f"higado_bordes_{i}"
                )

            col3, col4, col5 = st.columns(3)

            with col3:
                segmento = st.selectbox(
                    "Segmento",
                    ["I","II","III","IVa","IVb","V","VI","VII","VIII"],
                    key=f"higado_seg_{i}"
                )

            with col4:
                tam = st.number_input(
                    "Tamaño (mm)",
                    min_value=0,
                    step=1,
                    key=f"higado_tam_{i}"
                )

            with col5:
                uh = st.number_input(
                    "UH",
                    step=1,
                    key=f"higado_uh_{i}"
                )

            lesiones_lista.append({
                "tipo": tipo,
                "bordes": bordes,
                "segmento": segmento,
                "tam": tam,
                "uh": uh
            })

            st.divider()

        hallazgos_extra = st.text_area(
            "Hallazgos especiales",
            placeholder="Ej: realce periférico, necrosis central, calcificación...",
            key="higado_extra"
        )

    # =========================
    # MEDIDAS
    # =========================
    st.markdown("**Medidas:**")

    lhd = st.number_input(
        "Lóbulo hepático derecho (mm)",
        min_value=0,
        step=1,
        key="higado_lhd"
    )

    # =========================
    # INPUT FINAL
    # =========================
    input_higado = {
        "tamano": tamano,
        "contornos": contornos,
        "atenuacion": atenuacion,
        "parenquima": parenquima,
        "lhd": lhd,
        "hay_lesion": hay_lesion
    }

    if hay_lesion:
        input_higado.update({
            "lesiones_lista": lesiones_lista,
            "hallazgos_extra": hallazgos_extra
        })

    # =========================
    # ANÁLISIS
    # =========================
    if st.button("Analizar hígado", key="btn_higado"):

        # Validación lesiones
        if hay_lesion and len(lesiones_lista) == 0:
            st.warning("Debe ingresar al menos una lesión.")
            st.stop()

        # SCORING
        diferenciales = scoring_hepatico(input_higado)

        if not diferenciales:
            st.warning("No hay suficientes datos para generar diagnóstico.")
            st.stop()

        st.subheader("Diagnósticos diferenciales")
        for d in diferenciales:
            st.write(f"{d['dx']} - {d['prob']*100:.1f}%")

        # IA
        impresion = generar_impresion_ia(input_higado, diferenciales)

        st.subheader("Impresión diagnóstica")

        if "Error" in str(impresion):
            st.error(impresion)
        else:
            st.success(impresion)

with st.expander("Vesícula biliar", expanded=False):

    # =========================
    # FILA 1
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        tamano = st.radio(
            "Tamaño",
            ["normal", "distendida", "colapsada"],
            horizontal=True
        )

    with col2:
        pared = st.radio(
            "Pared",
            ["normal", "engrosada_difusa", "engrosada_focal", "estratificada", "irregular", "discontinua", "calcificada"],
            horizontal=True
        )

    with col3:
        realce = st.radio(
            "Realce",
            ["normal", "aumentado", "disminuido"],
            horizontal=True
        )

    # =========================
    # FILA 2
    # =========================
    col4, col5, col6 = st.columns(3)

    with col4:
        grosor_pared = st.number_input("Grosor (mm)", min_value=0.0, step=0.1)

    with col5:
        contenido = st.radio(
            "Contenido",
            ["homogeneo", "heterogeneo", "litiasis"],
            horizontal=True
        )

    with col6:
        cistico = st.radio(
            "Cístico",
            ["no_visible", "normal", "obstruido", "calculo"],
            horizontal=True
        )

    # =========================
    # UBICACIÓN DE PARED (SI FOCAL)
    # =========================
    if pared == "engrosada_focal":
        ubicacion_pared = st.selectbox(
            "Ubicación engrosamiento",
            ["fondo", "cuerpo", "cuello"]
        )

    # =========================
    # LITIASIS
    # =========================
    if contenido == "litiasis":
        col_l1, col_l2, col_l3 = st.columns(3)

        with col_l1:
            n_calculos = st.number_input("N°", min_value=1, step=1)

        with col_l2:
            tam_calculo = st.number_input("Tamaño (mm)", min_value=0, step=1)

        with col_l3:
            ubicacion_calculo = st.selectbox(
                "Ubicación",
                ["fondo", "cuerpo", "cuello"]
            )

    # =========================
    # PERIVESICULAR
    # =========================
    perivesicular = st.radio(
        "Perivesicular",
        ["normal", "inflamacion", "grasa", "liquido", "coleccion"],
        horizontal=True
    )

    # =========================
    # COLECCIÓN
    # =========================
    hay_coleccion = st.checkbox("Colección")

    if hay_coleccion:
        colc1, colc2, colc3 = st.columns(3)

        with colc1:
            tam_coleccion = st.text_input("Tamaño")

        with colc2:
            ubicacion_coleccion = st.selectbox(
                "Ubicación",
                ["perivesicular", "subhepatico"]
            )

        with colc3:
            gas_coleccion = st.checkbox("Gas")

    # =========================
    # LESIONES (CON NÚMERO 🔥)
    # =========================
    st.markdown("##### Lesiones")

    hay_lesion = st.checkbox("¿Se identifican lesiones?")

    lesiones_lista = []

    if hay_lesion:

        n_lesiones = st.number_input(
            "Número de lesiones",
            min_value=1,
            step=1
        )

        for i in range(n_lesiones):

            st.markdown(f"**Lesión {i+1}**")

            col1, col2 = st.columns(2)

            with col1:
                tipo = st.radio(
                    "Tipo",
                    ["polipo", "masa", "adenomiomatosis", "perdida_plano"],
                    key=f"vesicula_tipo_{i}"
                )

            with col2:
                tamaño = st.number_input(
                    "Tamaño (mm)",
                    min_value=0,
                    step=1,
                    key=f"vesicula_tam_{i}"
                )

            lesion = {
                "tipo": tipo,
                "tamaño": tamaño
            }

            st.divider()

            lesiones_lista.append(lesion)

    # =========================
    # GAS
    # =========================
    gas = st.radio("Gas", ["no", "lumen", "pared", "mixto"], horizontal=True)

    # =========================
    # DISPOSITIVO
    # =========================
    dispositivo = st.radio("Dispositivo", ["ninguno", "colecistostomia"], horizontal=True)

    if dispositivo == "colecistostomia":
        via = st.text_input("Vía")
        trayecto = st.radio("Trayecto", ["adecuado", "no adecuado"], horizontal=True)

    # =========================
    # INPUT FINAL
    # =========================
    input_vesicula = {
        "tamano": tamano,
        "pared": pared,
        "realce": realce,
        "grosor_pared": grosor_pared,
        "contenido": contenido,
        "cistico": cistico,
        "perivesicular": perivesicular,
        "hay_coleccion": hay_coleccion,
        "gas": gas,
        "dispositivo": dispositivo
    }

    if pared == "engrosada_focal":
        input_vesicula["ubicacion_pared"] = ubicacion_pared

    if contenido == "litiasis":
        input_vesicula.update({
            "n_calculos": n_calculos,
            "tam_calculo": tam_calculo,
            "ubicacion_calculo": ubicacion_calculo
        })

    if hay_coleccion:
        input_vesicula.update({
            "tam_coleccion": tam_coleccion,
            "ubicacion_coleccion": ubicacion_coleccion,
            "gas_coleccion": gas_coleccion
        })

    if hay_lesion:
        input_vesicula["lesiones"] = lesiones_lista

    if dispositivo == "colecistostomia":
        input_vesicula.update({
            "via": via,
            "trayecto": trayecto
        })

with st.expander("Estómago", expanded=False):

    # =========================
    # FILA 1
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        distension = st.radio(
            "Distensión",
            ["adecuada", "distendido", "poco_distendido", "colapsado"],
            horizontal=True,
            key="estomago_distension"
        )

    with col2:
        contenido = st.radio(
            "Contenido",
            ["vacio", "gas", "liquido", "mixto", "material_denso"],
            horizontal=True,
            key="estomago_contenido"
        )

    # =========================
    # PARED (INDEPENDIENTE)
    # =========================
    st.markdown("##### Pared gástrica")

    col3, col4 = st.columns(2)

    with col3:
        pared = st.radio(
            "Tipo de pared",
            ["normal", "engrosada_difusa", "engrosada_focal", "irregular"],
            horizontal=True,
            key="estomago_pared"
        )

        patron = st.radio(
            "Patrón",
            ["normal", "estratificado", "homogeneo"],
            horizontal=True,
            key="estomago_patron"
        )

    with col4:
        realce = st.radio(
            "Realce",
            ["normal", "aumentado", "disminuido"],
            horizontal=True,
            key="estomago_realce"
        )

        grosor = st.number_input(
            "Grosor parietal (mm)",
            min_value=0.0,
            step=0.1,
            key="estomago_grosor"
        )

    # =========================
    # LESIONES (INDEPENDIENTES)
    # =========================
    st.markdown("##### Lesiones")

    hay_lesion = st.checkbox("¿Se identifican lesiones en estómago?", key="estomago_hay_lesion")

    lesiones_lista = []

    if hay_lesion:

        n_lesiones = st.number_input(
            "Número de lesiones",
            min_value=1,
            max_value=5,
            step=1,
            key="estomago_n_lesiones"
        )

        for i in range(n_lesiones):

            st.markdown(f"**Lesión {i+1}**")

            col_l1, col_l2, col_l3 = st.columns(3)

            with col_l1:
                tipo = st.radio(
                    "Tipo de lesión",
                    ["masa", "ulceracion"],
                    horizontal=True,
                    key=f"estomago_tipo_{i}"
                )

            with col_l2:
                localizacion = st.selectbox(
                    "Localización",
                    ["cardias", "fundus", "cuerpo", "antro", "píloro"],
                    key=f"estomago_loc_{i}"
                )

            with col_l3:
                tamaño = st.number_input(
                    "Tamaño (mm)",
                    min_value=0,
                    step=1,
                    key=f"estomago_tam_{i}"
                )

            lesion_dict = {
                "tipo": tipo,
                "localizacion": localizacion,
                "tamaño": tamaño
            }

            # =========================
            # ÚLCERA
            # =========================
            if tipo == "ulceracion":

                col_u1, col_u2 = st.columns(2)

                with col_u1:
                    profundidad = st.radio(
                        "Profundidad",
                        ["superficial", "profunda"],
                        horizontal=True,
                        key=f"estomago_prof_{i}"
                    )

                with col_u2:
                    complicacion = st.radio(
                        "Complicación",
                        ["ninguna", "perforacion", "coleccion", "neumoperitoneo"],
                        horizontal=True,
                        key=f"estomago_comp_{i}"
                    )

                lesion_dict.update({
                    "profundidad": profundidad,
                    "complicacion": complicacion
                })

            st.divider()

            lesiones_lista.append(lesion_dict)

    # =========================
    # LUZ
    # =========================
    luz = st.radio(
        "Luz",
        ["normal", "disminuida", "aumentada"],
        horizontal=True,
        key="estomago_luz"
    )

    # =========================
    # PERIGÁSTRICO
    # =========================
    perigastrico = st.radio(
        "Cambios perigástricos",
        ["normal", "estriacion", "liquido", "gas"],
        horizontal=True,
        key="estomago_perigastrico"
    )

    # =========================
    # OTROS
    # =========================
    otros = st.radio(
        "Otros",
        ["ninguno", "sonda", "gastrectomia"],
        horizontal=True,
        key="estomago_otros"
    )

    # =========================
    # INPUT FINAL
    # =========================
    input_estomago = {
        "distension": distension,
        "contenido": contenido,
        "pared": pared,
        "patron": patron,
        "realce": realce,
        "grosor": grosor,
        "luz": luz,
        "perigastrico": perigastrico,
        "otros": otros,
        "hay_lesion": hay_lesion
    }

    if hay_lesion:
        input_estomago["lesiones_lista"] = lesiones_lista

with st.expander("Bazo", expanded=False):

    # =========================
    # GENERAL
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        tamano = st.radio(
            "Tamaño",
            ["normal", "aumentado", "disminuido", "atrofico"],
            horizontal=True,
            key="bazo_tamano"
        )

        contornos = st.radio(
            "Contornos",
            ["regulares", "irregulares"],
            horizontal=True,
            key="bazo_contornos"
        )

    with col2:
        parenquima = st.radio(
            "Parénquima",
            ["normal", "heterogeneo", "hipodenso", "hiperdenso"],
            horizontal=True,
            key="bazo_parenquima"
        )

        realce = st.radio(
            "Realce",
            ["normal", "hipercaptante", "hipocaptante"],
            horizontal=True,
            key="bazo_realce"
        )

    # =========================
    # LESIONES
    # =========================
    st.markdown("##### Lesiones")

    hay_lesion = st.checkbox(
        "¿Se identifican lesiones esplénicas?",
        key="bazo_hay_lesion"
    )

    lesiones_lista = []

    if hay_lesion:

        n_lesiones = st.number_input(
            "Número de lesiones",
            min_value=1,
            max_value=5,
            step=1,
            key="bazo_n_lesiones"
        )

        for i in range(n_lesiones):

            st.markdown(f"**Lesión {i+1}**")

            col3, col4 = st.columns(2)

            with col3:
                tipo = st.radio(
                    "Tipo",
                    ["quiste_simple", "quiste_complejo", "solida",
                     "hipodensa", "hipercaptante", "hipocaptante",
                     "infarto", "coleccion"],
                    key=f"bazo_tipo_{i}"
                )

            with col4:
                localizacion = st.radio(
                    "Localización",
                    ["polo_superior", "polo_inferior", "hilio", "difuso"],
                    horizontal=True,
                    key=f"bazo_loc_{i}"
                )

                tamaño = st.number_input(
                    "Tamaño (mm)",
                    min_value=0,
                    step=1,
                    key=f"bazo_tam_{i}"
                )

            lesiones_lista.append({
                "tipo": tipo,
                "localizacion": localizacion,
                "tam": tamaño
            })

    # =========================
    # CÁPSULA Y PERIESPLÉNICO
    # =========================
    col5, col6 = st.columns(2)

    with col5:
        capsula = st.radio(
            "Cápsula",
            ["normal", "irregular", "discontinua"],
            horizontal=True,
            key="bazo_capsula"
        )

    with col6:
        periesplenico = st.radio(
            "Periesplénico",
            ["normal", "liquido", "hemoperitoneo", "coleccion"],
            horizontal=True,
            key="bazo_peri"
        )

    # =========================
    # INPUT FINAL
    # =========================
    input_bazo = {
        "tamano": tamano,
        "contornos": contornos,
        "parenquima": parenquima,
        "realce": realce,
        "capsula": capsula,
        "periesplenico": periesplenico,
        "hay_lesion": hay_lesion
    }

    if hay_lesion:
        input_bazo["lesiones_lista"] = lesiones_lista

with st.expander("Páncreas", expanded=False):

    # =========================
    # GENERAL (COMPACTO)
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        tamano = st.radio(
            "Tamaño",
            ["normal", "aumentado", "disminuido", "atrofico"],
            horizontal=True,
            key="pancreas_tamano"
        )

    with col2:
        contornos = st.radio(
            "Contornos",
            ["regulares", "lobulados", "irregulares"],
            horizontal=True,
            key="pancreas_contornos"
        )

    with col3:
        parenquima = st.radio(
            "Parénquima",
            ["normal", "heterogeneo", "hipodenso", "graso"],
            horizontal=True,
            key="pancreas_parenquima"
        )

    # =========================
    # REALCE + CONDUCTOS
    # =========================
    col4, col5 = st.columns(2)

    with col4:
        realce = st.radio(
            "Realce",
            ["normal", "disminuido", "aumentado"],
            horizontal=True,
            key="pancreas_realce"
        )

    with col5:
        conducto = st.radio(
            "Conducto pancreático",
            ["normal", "dilatado", "irregular", "corte_brusco"],
            horizontal=True,
            key="pancreas_conducto"
        )

    col6, col7 = st.columns(2)

    with col6:
        coledoco = st.radio(
            "Colédoco",
            ["normal", "dilatado", "litiasis", "estenosis", "doble_ducto"],
            horizontal=True,
            key="pancreas_coledoco"
        )

    with col7:
        peripancreatico = st.radio(
            "Peripancreático",
            ["normal", "inflamacion", "coleccion", "necrosis", "gas"],
            horizontal=True,
            key="pancreas_peri"
        )

    # =========================
    # LESIONES 🔥
    # =========================
    st.markdown("##### Lesiones")

    hay_lesion = st.checkbox("¿Se identifican lesiones?", key="pancreas_hay_lesion")

    lesiones_lista = []

    if hay_lesion:

        n_lesiones = st.number_input(
            "Número de lesiones",
            min_value=1,
            max_value=5,
            step=1,
            key="pancreas_n_lesiones"
        )

        for i in range(n_lesiones):

            st.markdown(f"**Lesión {i+1}**")

            colL1, colL2, colL3, colL4 = st.columns([1,1,1,1])

            with colL1:
                tipo = st.radio(
                    "Tipo",
                    ["quistica", "solida", "mixta"],
                    key=f"pancreas_tipo_{i}"
                )

            with colL2:
                loc = st.selectbox(
                    "Ubicación",
                    ["cabeza", "cuello", "cuerpo", "cola"],
                    key=f"pancreas_loc_{i}"
                )

            with colL3:
                tam = st.number_input(
                    "Tamaño (mm)",
                    min_value=0,
                    step=1,
                    key=f"pancreas_tam_{i}"
                )

            with colL4:
                uh = st.number_input(
                    "UH",
                    step=1,
                    key=f"pancreas_uh_{i}"
                )

            lesiones_lista.append({
                "tipo": tipo,
                "localizacion": loc,
                "tam": tam,
                "uh": uh
            })

    # =========================
    # INPUT FINAL
    # =========================
    input_pancreas = {
        "tamano": tamano,
        "contornos": contornos,
        "parenquima": parenquima,
        "realce": realce,
        "conducto": conducto,
        "coledoco": coledoco,
        "peripancreatico": peripancreatico,
        "hay_lesion": hay_lesion
    }

    if hay_lesion:
        input_pancreas["lesiones_lista"] = lesiones_lista

with st.expander("Asas intestinales delgadas", expanded=False):

    # =========================
    # GENERAL
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        calibre = st.radio(
            "Calibre",
            ["normal", "dilatadas", "colapsadas", "oclusion"],
            horizontal=True,
            key="delgadas_calibre"
        )

    with col2:
        contenido = st.radio(
            "Contenido",
            ["gas", "liquido", "mixto", "material_denso", "material_hipodenso"],
            horizontal=True,
            key="delgadas_contenido"
        )

    with col3:
        distension = st.radio(
            "Distensión",
            ["normal", "focal", "difusa"],
            horizontal=True,
            key="delgadas_distension"
        )

    # =========================
    # PARED
    # =========================
    st.markdown("##### Pared")

    col4, col5, col6 = st.columns(3)

    with col4:
        pared = st.radio(
            "Tipo",
            ["normal", "engrosada", "irregular", "ulcerada"],
            horizontal=True,
            key="delgadas_pared"
        )

    with col5:
        realce = st.radio(
            "Realce",
            ["normal", "hipercaptante", "hipocaptante"],
            horizontal=True,
            key="delgadas_realce"
        )

    with col6:
        patron = st.radio(
            "Patrón",
            ["normal", "estratificado", "homogeneo", "edematoso", "mucoso"],
            horizontal=True,
            key="delgadas_patron"
        )

    # =========================
    # MOTILIDAD + PERIENTÉRICO
    # =========================
    col7, col8 = st.columns(2)

    with col7:
        motilidad = st.radio(
            "Motilidad",
            ["normal", "disminuida", "aumentada"],
            horizontal=True,
            key="delgadas_motilidad"
        )

    with col8:
        perienterico = st.radio(
            "Grasa perientérica",
            ["normal", "estriacion", "liquido", "gas", "adenopatias"],
            horizontal=True,
            key="delgadas_peri"
        )

    # =========================
    # LOCALIZACIÓN
    # =========================
    localizacion = st.radio(
        "Localización",
        ["difuso", "duodeno", "yeyuno", "ileon"],
        horizontal=True,
        key="delgadas_localizacion"
    )

    # =========================
    # INPUT FINAL
    # =========================
    input_asas_delgadas = {
        "calibre": calibre,
        "contenido": contenido,
        "distension": distension,
        "pared": pared,
        "realce": realce,
        "patron": patron,
        "motilidad": motilidad,
        "perienterico": perienterico,
        "localizacion": localizacion
    }

with st.expander("Asas intestinales gruesas", expanded=False):

    # =========================
    # GENERAL
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        calibre = st.radio(
            "Calibre",
            ["normal", "dilatadas", "colapsadas"],
            horizontal=True,
            key="gruesas_calibre"
        )

        if calibre == "dilatadas":
            calibre_mm = st.number_input(
                "Calibre máximo (mm)",
                min_value=0,
                step=1,
                key="gruesas_calibre_mm"
            )

    with col2:
        contenido = st.radio(
            "Contenido",
            ["gas", "heces", "liquido", "mixto", "material_denso"],
            horizontal=True,
            key="gruesas_contenido"
        )

    with col3:
        distribucion = st.radio(
            "Distribución",
            ["normal", "focal", "difusa"],
            horizontal=True,
            key="gruesas_distribucion"
        )

    # =========================
    # PARED
    # =========================
    st.markdown("##### Pared colónica")

    col4, col5, col6 = st.columns(3)

    with col4:
        pared = st.radio(
            "Tipo",
            ["normal", "engrosada", "engrosada_difusa", "engrosada_focal", "irregular"],
            horizontal=True,
            key="gruesas_pared"
        )

    with col5:
        patron = st.radio(
            "Patrón",
            ["normal", "estratificado", "homogeneo"],
            horizontal=True,
            key="gruesas_patron"
        )

    with col6:
        realce = st.radio(
            "Realce",
            ["normal", "hipercaptante", "hipocaptante"],
            horizontal=True,
            key="gruesas_realce"
        )

    # =========================
    # PERICOLÓNICO
    # =========================
    pericolico = st.radio(
        "Grasa pericolónica",
        ["normal", "estriacion", "liquido", "gas"],
        horizontal=True,
        key="gruesas_peri"
    )

    # =========================
    # LOCALIZACIÓN
    # =========================
    localizacion = st.radio(
        "Localización",
        ["difuso", "ciego", "colon_ascendente", "colon_transverso",
         "colon_descendente", "sigmoides", "recto"],
        horizontal=True,
        key="gruesas_localizacion"
    )

    # =========================
    # LESIONES
    # =========================
    st.markdown("##### Lesiones")

    hay_lesion = st.checkbox(
        "¿Se identifican lesiones?",
        key="gruesas_hay_lesion"
    )

    lesiones_lista = []

    if hay_lesion:

        n_lesiones = st.number_input(
            "Número de lesiones",
            min_value=1,
            max_value=5,
            step=1,
            key="gruesas_n_lesiones"
        )

        for i in range(n_lesiones):

            st.markdown(f"**Lesión {i+1}**")

            col7, col8 = st.columns(2)

            with col7:
                tipo = st.radio(
                    "Tipo",
                    ["masa", "engrosamiento_focal", "diverticulos"],
                    key=f"gruesas_tipo_{i}"
                )

            with col8:
                loc_lesion = st.radio(
                    "Localización",
                    ["ciego", "colon_ascendente", "colon_transverso",
                     "colon_descendente", "sigmoides", "recto"],
                    horizontal=True,
                    key=f"gruesas_loc_{i}"
                )

            lesiones_lista.append({
                "tipo": tipo,
                "localizacion": loc_lesion
            })

    # =========================
    # RECTO
    # =========================
    st.markdown("##### Recto")

    recto = st.radio(
        "Recto",
        ["normal", "distendido", "pared_engrosada", "contenido"],
        horizontal=True,
        key="gruesas_recto"
    )

    # =========================
    # APÉNDICE
    # =========================
    st.markdown("##### Apéndice")

    col9, col10 = st.columns(2)

    with col9:
        apendice = st.radio(
            "Estado",
            ["no_visible", "normal", "engrosado", "pared_engrosada"],
            horizontal=True,
            key="gruesas_apendice"
        )

    with col10:
        hallazgos_apendice = st.multiselect(
            "Hallazgos asociados",
            ["fecalito", "periapendicular", "liquido"],
            key="gruesas_apendice_extra"
        )

    # =========================
    # INPUT FINAL
    # =========================
    input_asas_gruesas = {
        "calibre": calibre,
        "contenido": contenido,
        "distribucion": distribucion,
        "pared": pared,
        "patron": patron,
        "realce": realce,
        "pericolico": pericolico,
        "localizacion": localizacion,
        "recto": recto,
        "apendice": apendice,
        "hallazgos_apendice": hallazgos_apendice,
        "hay_lesion": hay_lesion
    }

    if calibre == "dilatadas":
        input_asas_gruesas["calibre_mm"] = calibre_mm

    if hay_lesion:
        input_asas_gruesas["lesiones_lista"] = lesiones_lista

with st.expander("Retroperitoneo", expanded=False):

    # =========================
    # FILA 1
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        adenopatias = st.radio(
            "Adenopatías",
            ["no", "si", "voluminosas", "conglomerado"],
            horizontal=True,
            key="rp_adenopatias"
        )

    with col2:
        grasa = st.radio(
            "Grasa retroperitoneal",
            ["normal", "estriacion", "borramiento"],
            horizontal=True,
            key="rp_grasa"
        )

    # 🔥 LOCALIZACIÓN ADENOPATÍAS
    if adenopatias != "no":
        loc_adenopatias = st.selectbox(
            "Localización adenopatías",
            ["paraaorticas", "interaortocava", "paracava", "iliacas", "difusa"],
            key="rp_loc_adeno"
        )

    # =========================
    # FILA 2
    # =========================
    col3, col4 = st.columns(2)

    with col3:
        colecciones = st.radio(
            "Colecciones",
            ["no", "liquida", "compleja", "absceso_like"],
            horizontal=True,
            key="rp_colecciones"
        )

    with col4:
        masas = st.radio(
            "Masas",
            ["no", "solida", "heterogenea", "quistica"],
            horizontal=True,
            key="rp_masas"
        )

    # 🔥 DETALLE COLECCIÓN
    if colecciones != "no":

        col_c1, col_c2 = st.columns(2)

        with col_c1:
            tam_coleccion = st.number_input(
                "Tamaño colección (mm)",
                min_value=0,
                step=1,
                key="rp_tam_colec"
            )

        with col_c2:
            loc_coleccion = st.text_input(
                "Ubicación colección",
                placeholder="Ej: paraaórtica, psoas, etc.",
                key="rp_loc_colec"
            )

    # 🔥 DETALLE MASA
    if masas != "no":

        col_m1, col_m2 = st.columns(2)

        with col_m1:
            tam_masa = st.number_input(
                "Tamaño masa (mm)",
                min_value=0,
                step=1,
                key="rp_tam_masa"
            )

        with col_m2:
            loc_masa = st.text_input(
                "Ubicación masa",
                placeholder="Ej: retrocava, paraaórtica...",
                key="rp_loc_masa"
            )

        efecto_masa = st.checkbox(
            "Efecto de masa sobre estructuras adyacentes",
            key="rp_efecto_masa"
        )

    # =========================
    # FILA 3
    # =========================
    col5, col6 = st.columns(2)

    with col5:
        gas = st.radio(
            "Gas retroperitoneal",
            ["no", "si"],
            horizontal=True,
            key="rp_gas"
        )

    with col6:
        vascular = st.radio(
            "Compromiso vascular",
            ["normal", "dilatados", "estenosis", "trombo", "calcificaciones"],
            horizontal=True,
            key="rp_vascular"
        )

    # 🔥 ESPECIFICAR VASO
    if vascular in ["trombo", "estenosis"]:
        vaso = st.selectbox(
            "Vaso comprometido",
            ["aorta", "vena_cava", "iliacos", "mesentericos"],
            key="rp_vaso"
        )

    # =========================
    # OTROS
    # =========================
    otros = st.text_area(
        "Otros hallazgos",
        placeholder="Ej: fibrosis retroperitoneal, cambios postquirúrgicos...",
        key="rp_otros"
    )

    # =========================
    # INPUT FINAL
    # =========================
    input_retroperitoneo = {
        "adenopatias": adenopatias,
        "grasa": grasa,
        "colecciones": colecciones,
        "masas": masas,
        "gas": gas,
        "vascular": vascular,
        "otros": otros
    }

    # 🔥 opcionales
    if adenopatias != "no":
        input_retroperitoneo["localizacion_adenopatias"] = loc_adenopatias

    if colecciones != "no":
        input_retroperitoneo.update({
            "tam_coleccion": tam_coleccion,
            "loc_coleccion": loc_coleccion
        })

    if masas != "no":
        input_retroperitoneo.update({
            "tam_masa": tam_masa,
            "loc_masa": loc_masa,
            "efecto_masa": efecto_masa
        })

    if vascular in ["trombo", "estenosis"]:
        input_retroperitoneo["vaso"] = vaso

with st.expander("Riñones y suprarrenales", expanded=False):

    # =========================
    # GENERAL
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        tamano = st.radio(
            "Tamaño / morfología",
            ["normal", "aumentados", "disminuidos", "asimetria"],
            horizontal=True,
            key="rinon_tamano"
        )

    with col2:
        parenquima = st.radio(
            "Parénquima",
            ["normal", "disminuida", "heterogeneo", "hipodenso", "hipercaptante", "hipocaptante", "adelgazado"],
            horizontal=True,
            key="rinon_parenquima"
        )

    # =========================
    # LESIONES RENALES
    # =========================
    st.markdown("##### Lesiones renales")

    hay_lesion = st.checkbox("¿Lesión renal?", key="rinon_hay_lesion")

    lesiones_lista = []

    if hay_lesion:

        n_lesiones = st.number_input(
            "Número de lesiones",
            min_value=1,
            max_value=5,
            step=1,
            key="rinon_n_lesiones"
        )

        for i in range(n_lesiones):

            st.markdown(f"**Lesión {i+1}**")

            colL1, colL2, colL3 = st.columns(3)

            with colL1:
                tipo = st.radio(
                    "Tipo",
                    ["quistes_simples", "quistes_complejos", "masa", "lesion_focal", "absceso"],
                    key=f"rinon_tipo_{i}"
                )

            with colL2:
                lado = st.radio(
                    "Lado",
                    ["derecho", "izquierdo", "bilateral"],
                    key=f"rinon_lado_{i}"
                )

            with colL3:
                localizacion = st.radio(
                    "Ubicación",
                    ["polo_superior", "polo_medio", "polo_inferior"],
                    key=f"rinon_loc_{i}"
                )

            tam = st.number_input(
                "Tamaño (mm)",
                min_value=0,
                step=1,
                key=f"rinon_tam_{i}"
            )

            lesiones_lista.append({
                "tipo": tipo,
                "lado": lado,
                "localizacion": localizacion,
                "tam": tam
            })

    # =========================
    # SISTEMA COLECTOR
    # =========================
    st.markdown("##### Sistema colector")

    col3, col4 = st.columns(2)

    with col3:
        sistema = st.radio(
            "Estado",
            ["normal", "dilatado_bilateral", "dilatado_derecho", "dilatado_izquierdo"],
            horizontal=True,
            key="rinon_sistema"
        )

    with col4:
        if sistema != "normal":
            grado = st.radio(
                "Grado",
                ["leve", "moderado", "severo"],
                horizontal=True,
                key="rinon_grado"
            )

    litiasis = st.radio(
        "Litiasis",
        ["no", "renal", "ureteral"],
        horizontal=True,
        key="rinon_litiasis"
    )

    if litiasis != "no":

        col5, col6 = st.columns(2)

        with col5:
            lado_lit = st.radio(
                "Lado",
                ["derecho", "izquierdo"],
                key="rinon_lado_lit"
            )

        with col6:
            loc_lit = st.radio(
                "Ubicación",
                ["pelvis", "calices", "ureter_proximal", "ureter_medio", "ureter_distal"],
                key="rinon_loc_lit"
            )

        tam_lit = st.number_input(
            "Tamaño (mm)",
            min_value=0,
            step=1,
            key="rinon_tam_lit"
        )

    # =========================
    # PERIRRENAL
    # =========================
    perirrenal = st.radio(
        "Cambios perirrenales",
        ["normal", "estriacion", "liquido", "coleccion"],
        horizontal=True,
        key="rinon_perirrenal"
    )

    # =========================
    # SUPRARRENALES
    # =========================
    st.markdown("##### Suprarrenales")

    suprarrenales = st.radio(
        "Estado",
        ["normal", "engrosadas", "nodulo", "masa", "hiperplasia"],
        horizontal=True,
        key="suprarrenal_estado"
    )

    if suprarrenales in ["nodulo", "masa"]:

        col7, col8 = st.columns(2)

        with col7:
            lado_sup = st.radio(
                "Lado",
                ["derecha", "izquierda", "bilateral"],
                key="suprarrenal_lado"
            )

        with col8:
            tam_sup = st.number_input(
                "Tamaño (mm)",
                min_value=0,
                step=1,
                key="suprarrenal_tam"
            )

    # =========================
    # INPUT FINAL
    # =========================
    input_rinon = {
        "tamano": tamano,
        "parenquima": parenquima,
        "perirrenal": perirrenal,
        "litiasis": litiasis,
        "sistema": sistema,
        "suprarrenales": suprarrenales,
        "hay_lesion": hay_lesion
    }

    if hay_lesion:
        input_rinon["lesiones_lista"] = lesiones_lista

    if sistema != "normal":
        input_rinon["grado"] = grado

    if litiasis != "no":
        input_rinon.update({
            "lado_lit": lado_lit,
            "loc_lit": loc_lit,
            "tam_lit": tam_lit
        })

    if suprarrenales in ["nodulo", "masa"]:
        input_rinon.update({
            "lado_sup": lado_sup,
            "tam_sup": tam_sup
        })

with st.expander("Vejiga", expanded=False):

    # =========================
    # FILA 1
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        distension = st.radio(
            "Distensión",
            ["distendida", "moderada", "colapsada"],
            horizontal=True,
            key="vejiga_distension"
        )

    with col2:
        contenido = st.radio(
            "Contenido",
            ["homogeneo", "hiperdenso", "heterogeneo", "nivel", "litiasis", "coagulos"],
            horizontal=True,
            key="vejiga_contenido"
        )

    # =========================
    # PARED
    # =========================
    st.markdown("##### Pared vesical")

    col3, col4 = st.columns(2)

    with col3:
        pared = st.radio(
            "Tipo",
            ["normal", "engrosada_difusa", "engrosada_focal", "irregular", "trabeculada", "calcificada"],
            horizontal=True,
            key="vejiga_pared"
        )

    with col4:
        realce = st.radio(
            "Realce",
            ["normal", "aumentado", "disminuido"],
            horizontal=True,
            key="vejiga_realce"
        )

    # =========================
    # LESIONES
    # =========================
    st.markdown("##### Lesiones")

    hay_lesion = st.checkbox("¿Lesión vesical?", key="vejiga_hay_lesion")

    if hay_lesion:

        tipo_lesion = st.radio(
            "Tipo de lesión",
            ["masa", "vegetante", "nodular"],
            horizontal=True,
            key="vejiga_tipo_lesion"
        )

        col_l1, col_l2 = st.columns(2)

        with col_l1:
            localizacion = st.selectbox(
                "Localización",
                ["pared anterior", "pared posterior", "pared lateral derecha", "pared lateral izquierda", "difusa"],
                key="vejiga_localizacion"
            )

        with col_l2:
            tam_lesion = st.number_input(
                "Tamaño (mm)",
                min_value=0,
                step=1,
                key="vejiga_tam"
            )

    # =========================
    # PERIVESICAL + GAS
    # =========================
    col5, col6 = st.columns(2)

    with col5:
        perivesical = st.radio(
            "Cambios perivesicales",
            ["normal", "estriacion", "liquido", "coleccion", "invasion"],
            horizontal=True,
            key="vejiga_perivesical"
        )

    with col6:
        gas = st.radio(
            "Gas",
            ["no", "lumen", "pared", "mixto"],
            horizontal=True,
            key="vejiga_gas"
        )

    # =========================
    # DISPOSITIVO
    # =========================
    dispositivo = st.radio(
        "Dispositivo",
        ["ninguno", "sonda"],
        horizontal=True,
        key="vejiga_dispositivo"
    )

    # =========================
    # INPUT FINAL
    # =========================
    input_vejiga = {
        "distension": distension,
        "contenido": contenido,
        "pared": pared,
        "realce": realce,
        "perivesical": perivesical,
        "gas": gas,
        "dispositivo": dispositivo,
        "hay_lesion": hay_lesion
    }

    if hay_lesion:
        input_vejiga.update({
            "tipo_lesion": tipo_lesion,
            "localizacion": localizacion,
            "tam_lesion": tam_lesion
        })

with st.expander("Órganos pélvicos", expanded=False):

    # =========================
    # SELECCIÓN DE SEXO
    # =========================
    sexo = st.radio(
        "Sexo del paciente",
        ["masculino", "femenino"],
        horizontal=True,
        key="pelvis_sexo"
    )

    # =========================
    # 🔵 PRÓSTATA
    # =========================
    if sexo == "masculino":

        st.markdown("### Próstata")

        col1, col2 = st.columns(2)

        with col1:
            tamano = st.radio(
                "Tamaño",
                ["normal", "aumentada", "disminuida"],
                horizontal=True,
                key="prostata_tamano"
            )

            morfologia = st.radio(
                "Morfología",
                ["normal", "lobulada", "irregular", "protrusion_vesical"],
                horizontal=True,
                key="prostata_morfologia"
            )

        with col2:
            densidad = st.radio(
                "Densidad",
                ["homogenea", "heterogenea", "hipodensa", "hiperdensa"],
                horizontal=True,
                key="prostata_densidad"
            )

            realce = st.radio(
                "Realce",
                ["normal", "heterogeneo", "hipercaptante", "hipocaptante"],
                horizontal=True,
                key="prostata_realce"
            )

        # Volumen solo si aumentada
        if tamano == "aumentada":
            volumen = st.number_input(
                "Volumen prostático (cc)",
                min_value=0,
                step=1,
                key="prostata_volumen"
            )

        # Extras
        col3, col4 = st.columns(2)

        with col3:
            calcificaciones = st.radio(
                "Calcificaciones",
                ["no", "si"],
                horizontal=True,
                key="prostata_calcificaciones"
            )

        with col4:
            lesiones = st.radio(
                "Lesiones",
                ["ninguna", "nodulo", "masa"],
                horizontal=True,
                key="prostata_lesiones"
            )

        input_pelvis = {
            "sexo": sexo,
            "tamano": tamano,
            "morfologia": morfologia,
            "densidad": densidad,
            "realce": realce,
            "calcificaciones": calcificaciones,
            "lesiones": lesiones
        }

        if tamano == "aumentada":
            input_pelvis["volumen"] = volumen

    # =========================
    # 🟣 ÚTERO
    # =========================
    else:

        st.markdown("### Útero")

        col1, col2 = st.columns(2)

        with col1:
            estado = st.radio(
                "Estado",
                ["normal", "no_visible", "lateralizado"],
                horizontal=True,
                key="utero_estado"
            )

            tamano_morfologia = st.radio(
                "Tamaño / morfología",
                ["normal", "aumentado", "disminuido", "atrofico", "irregular", "lobulado"],
                horizontal=True,
                key="utero_tamano"
            )

        with col2:
            contenido = st.radio(
                "Contenido cavitario",
                ["normal", "liquido", "material_hiperdenso", "material_heterogeneo"],
                horizontal=True,
                key="utero_contenido"
            )

            paredes = st.radio(
                "Paredes",
                ["normal", "engrosada", "irregular"],
                horizontal=True,
                key="utero_paredes"
            )

        # Lesiones
        lesiones = st.radio(
            "Lesiones",
            ["ninguna", "masa_solida", "masa_quistica", "calcificacion"],
            horizontal=True,
            key="utero_lesiones"
        )

        # Adyacencias
        adyacencias = st.radio(
            "Adyacencias",
            ["normal", "liquido", "masa", "estriacion"],
            horizontal=True,
            key="utero_adyacencias"
        )

        input_pelvis = {
            "sexo": sexo,
            "estado": estado,
            "tamano_morfologia": tamano_morfologia,
            "contenido": contenido,
            "paredes": paredes,
            "lesiones": lesiones,
            "adyacencias": adyacencias
        }

with st.expander("Hallazgos adicionales", expanded=False):

    col1, col2 = st.columns(2)

    with col1:
        infeccioso = st.multiselect(
            "Infeccioso",
            ["absceso", "espondilodiscitis"],
            key="add_infeccioso"
        )

        liquido = st.checkbox(
            "Líquido libre",
            key="add_liquido"
        )

    with col2:
        trauma = st.checkbox(
            "Trayecto traumático",
            key="add_trauma"
        )

        oseo = st.multiselect(
            "Óseo",
            ["degenerativos", "liticos"],
            key="add_oseo"
        )

    # =========================
    # INPUT FINAL
    # =========================
    input_adicionales = {
        "infeccioso": infeccioso,
        "liquido": liquido,
        "trauma": trauma,
        "oseo": oseo
    }


# =========================
# BOTÓN FINAL
# =========================

if st.button("Generar informe"):

    texto_higado = generar_higado(input_higado)
    texto_vesicula = generar_vesicula(input_vesicula)
    texto_estomago = generar_estomago(input_estomago)
    texto_pancreas = generar_pancreas(input_pancreas)
    texto_bazo = generar_bazo(input_bazo)
    texto_asas_delgadas = generar_asas_delgadas(input_asas_delgadas)
    texto_asas_gruesas = generar_asas_gruesas(input_asas_gruesas)
    texto_retro = generar_retroperitoneo(input_retroperitoneo)
    texto_rinon = generar_rinones_suprarrenales(input_rinon)  # 🔥 NUEVO
    texto_vejiga = generar_vejiga(input_vejiga)
    texto_pelvis = generar_pelvis(input_pelvis)
    texto_adicionales = generar_adicionales(input_adicionales)

    st.subheader("Resultados:")

    # 🔥 ORDEN TIPO INFORME REAL
    st.write("**Hígado:**", texto_higado)
    st.write("**Vesícula biliar:**", texto_vesicula)
    st.write("**Estómago:**", texto_estomago)
    st.write("**Páncreas:**", texto_pancreas)
    st.write("**Bazo:**", texto_bazo)

    st.write("**Asas intestinales delgadas:**", texto_asas_delgadas)
    st.write("**Asas intestinales gruesas:**", texto_asas_gruesas)

    st.write("**Retroperitoneo:**", texto_retro)
    st.write("**Riñones y suprarrenales:**", texto_rinon)  # 🔥 AQUÍ VA

    st.write("**Vejiga:**", texto_vejiga)
    st.write("**Pelvis:**", texto_pelvis)

    st.write("**Hallazgos adicionales:**", texto_adicionales)