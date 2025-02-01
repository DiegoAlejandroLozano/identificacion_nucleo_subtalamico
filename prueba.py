wavlist = ['cgau1', 'cmor', 'mexh']

def aplicar_cwt_y_guardar_imagen(nombre_trans:str,registro:np.ndarray,ruta:str,m:int):      
    nombre_imagen = os.path.join(ruta, f"Figura_{m}.png")
    
    # Escalas para la CWT
    scales = np.arange(1, 100)

    # Realizar la transformada continua de wavelet (CWT) 
    cwt, _ = pywt.cwt(registro, scales, nombre_trans)

    # Plotear el resultado
    plt.figure(figsize=(2.5,2.5))
    plt.imshow(np.abs(cwt), extent=[0, 0.1, scales[-1], scales[0]], aspect='auto', cmap='jet')
    plt.axis('off')
    plt.gca().set_position([0,0,1,1])
    plt.savefig(nombre_imagen, bbox_inches='tight', pad_inches=0)
    plt.close()

for transformada in wavlist:
    #Se genera las transformadas al conjunto de datos df_stn
    ruta_imagenes_stn = os.path.join("imagenes", transformada, "stn")    
    for i, registro in enumerate(df_stn.values):
        # Se itera sobre cada fila del DataFrame 'df_stn' junto con su índice,
        # utilizando 'enumerate' para obtener tanto el índice 'i' como el registro directamente
        aplicar_cwt_y_guardar_imagen(
            nombre_trans = transformada,
            registro     = registro,
            ruta         = ruta_imagenes_stn,
            m            = i
        )
    #Se genera las transformadas al conjunto de datos df_otras
    ruta_imagenes_otras = os.path.join("imagenes", transformada, "otras")    
    for i, registro in enumerate(df_otras.values):
        # Se itera sobre cada fila del DataFrame 'df_otras' junto con su índice,
        # utilizando 'enumerate' para obtener tanto el índice 'i' como el registro directamente
        aplicar_cwt_y_guardar_imagen(
            nombre_trans = transformada,
            registro     = registro,
            ruta         = ruta_imagenes_otras,
            m            = i
        )  