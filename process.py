# Librerias
import pandas as pd
import numpy as np
import os
from datetime import *
import seaborn as sns
import shutil
pd.options.display.max_columns = None # Muestre todas las columns de un dataframe
#---------------------------------------------------------------------------------#

# Función que calcula las variables historicas #

def process_saldos_pendientes(num=int):
    print('INICIO PROCESS')
    print('='*120)
    time1 = datetime.now()
    
    # Ruta carpeta con archivos
    ruta_archivos = "C:/Users/Aleja/OneDrive/Escritorio/Icesi/I Semestre/Gestión estrategica/AlmanaConsultory/AlmanaConsultory/Información/saldos-pendientes/"
    
    # Archivos a utilizar
    dirs = os.listdir(ruta_archivos) # Listado de archivos en una carpeta
    dirs = dirs[-num:] # Filtrando solo para los ultimos 12 meses
    dirs = [ruta_archivos + x for x in dirs]
    print('Archivos a cargar: ',dirs)
    print('-'*120)
    
    # Cargando archivo según el parametro que se le indique
    if num == 1:
        df = pd.read_excel(dirs[-1], dtype={'Cliente':str, 'Nro. docto. cruce':str})
    else:
        df = [pd.read_excel(i) for i in dirs]
        df = pd.concat(df, axis=0)
    
    # Limpieza de datos
    df.drop_duplicates(subset=['Nro. docto. cruce'], keep='last', inplace=True) # Se eliminan duplicados dado que por ley la factura debe de ser unica y que en los casos duplicados se identificaron dos escenarios: 1.) una prorroga de vencimiento (se conservo la mas actualizada) 2.) facturas con una fecha de compra en los ultimos días del mes por lo cual sigue estando vigente al siguiente mes
    df['conteo'] = 1
    print('Dimension base inicial:',df.shape)
    print('Facturas duplicadas base inicial:',df[df.duplicated(subset=['Nro. docto. cruce'], keep=False)].shape[0])
    print('-'*120)
    # filtro para quedarnos solo con facturas iniciadas por F7Y
    df['tipo_factura'] = df['Nro. docto. cruce'].apply(lambda x: x[:3]) # Crando variables para el filtro
    print('Distribucion por tipo_factura: ',df['tipo_factura'].value_counts(dropna=False)) # distribucion por tipo_factura
    print('-'*120)
    df = df[df['tipo_factura']=='F7Y'] # Aplicando el filtro
    print('Dimension base F7Y: ', df.shape)
    print('-'*120)
    
    # Agrupando por cliente
    df_agrup = df.groupby('Cliente').agg({'Dias vencidos':'max', 'conteo':'count', 'Totalx COP':['sum','mean'], 'Cupo de crédito':'max'}).reset_index()
    df_agrup.columns = df_agrup.columns.map('_'.join).str.strip('_') 
    df_agrup['porcentaje_uso_cupo'] = (df_agrup['Totalx COP_sum']/df_agrup['Cupo de crédito_max'])*100
    df_agrup = df_agrup.astype({'Cliente':str, 'Dias vencidos_max':int, 'conteo_count':int, 'Totalx COP_sum':float,'Totalx COP_mean':float, 
                                'Cupo de crédito_max':float, 'porcentaje_uso_cupo':float})
    # Renombrando columnas
    if num == 1:
        nombre = 'corte'
    else:
        nombre = str(num)+'m'

    df_agrup.rename(columns={'Cliente':'nit','Dias vencidos_max':'mora_max_'+nombre,'conteo_count':'num_facturas_'+nombre,
                             'Totalx COP_sum':'valor_facturas_'+nombre,'Totalx COP_mean':'prom_facturas_'+nombre,'Cupo de crédito_max':'cupo_max_'+nombre,
                             'porcentaje_uso_cupo':'porcentaje_uso_cupo_'+nombre}, inplace=True)
    print('Dimension base final agrupada por clientes',df_agrup.shape)
    
    time2 = datetime.now()
    print('Tiempo de ejecución: ', time2 - time1)
    return df_agrup

# Funcion que calcula el comportamiento moroso del clientes según la historia de 12 meses
def process_comportamiento_moroso():
    print('INICIO PROCESS')
    print('='*120)
    time1 = datetime.now()
    
    # Ruta carpeta con archivos
    ruta_archivos = "C:/Users/Aleja/OneDrive/Escritorio/Icesi/I Semestre/Gestión estrategica/AlmanaConsultory/AlmanaConsultory/Información/saldos-pendientes/"
    
    # Archivos a utilizar
    dirs = os.listdir(ruta_archivos) # Listado de archivos en una carpeta
    dirs = dirs[-12:] # Filtrando solo para los ultimos 12 meses
    dirs = [ruta_archivos + x for x in dirs]
    print('Archivos utilizados: ',dirs)
    print('-'*120)
    
    # Creando carpeta temporal
    if os.path.exists('Salidas-temporales') == True:
        shutil.rmtree('Salidas-temporales')
    os.mkdir('Salidas-temporales')
    
    # Cargando archivos
    for i in dirs:
        df = pd.read_excel(i, dtype={'Cliente':str, 'Nro. docto. cruce':str})
        # Limpieza de datos
        df.drop_duplicates(subset=['Nro. docto. cruce'], keep='last', inplace=True) # Se eliminan duplicados dado que por ley la factura debe de ser unica y que en los casos duplicados se identificaron dos escenarios: 1.) una prorroga de vencimiento (se conservo la mas actualizada) 2.) facturas con una fecha de compra en los ultimos días del mes por lo cual sigue estando vigente al siguiente mes
        print('Dimension base inicial:',df.shape)
        print('Facturas duplicadas base inicial:',df[df.duplicated(subset=['Nro. docto. cruce'], keep=False)].shape[0])
        print('-'*120)
        # filtro para quedarnos solo con facturas iniciadas por F7Y
        df['tipo_factura'] = df['Nro. docto. cruce'].apply(lambda x: x[:3]) # Crando variables para el filtro
        print('Distribucion por tipo_factura: ',df['tipo_factura'].value_counts(dropna=False)) # distribucion por tipo_factura
        print('-'*120)
        df = df[df['tipo_factura']=='F7Y'] # Aplicando el filtro
        print('Dimension base F7Y: ', df.shape)
        print('-'*120)
        # Agrupando por cliente
        df_agrup = df.groupby('Cliente').agg({'Dias vencidos':'max'}).reset_index()
        df_agrup.rename(columns={'Cliente':'nit','Dias vencidos':'mora_max_'+i[-11:-5]}, inplace=True)
        # Guardando en carpeta temporal
        df_agrup.to_csv(os.getcwd()+'//Salidas-temporales//'+i[-11:-5]+'.csv', sep='|', index=False)
        del df
        
    # Archivos temporales
    dirs = os.listdir(os.getcwd()+'//Salidas-temporales//') # Listado de archivos en una carpeta
    dirs = [os.getcwd()+'//Salidas-temporales//' + x for x in dirs]
    
    # Llamando archivos y uniendo en un solo dataframe
    df = pd.read_csv(dirs[0], sep='|')
    df['nit'] = df['nit'].astype(str)
    for i in dirs[1:]:
        d = pd.read_csv(i, sep='|')
        d['nit'] = d['nit'].astype(str)
        print('Archivos temporales a unir:')
        print(i)
        print('-'*120)
        df = pd.merge(df, d, how='outer', on='nit')
    # Borrando carpeta
    shutil.rmtree('Salidas-temporales')
    print('Dimension base unificada: ', df.shape)
    df.fillna(0, inplace=True)
    #Creando variables nuevas
    df['count_semestre1'] = df[df.iloc[:, 1:7] != 0].count(axis=1)
    df['suma_semestre1'] = df[df.iloc[:, 1:7] != 0].sum(axis=1)
    df['count_semestre2'] = df[df.iloc[:, 7:13] != 0].count(axis=1)
    df['suma_semestre2'] = df[df.iloc[:, 7:13] != 0].sum(axis=1)
    
    # Creando variable de interes
    condiciones = [(df['suma_semestre1']==0)&(df['suma_semestre2']==0),
                   (df['count_semestre1']+df['count_semestre2'])>=7,
                   (df['count_semestre1']>df['count_semestre2'])&(df['suma_semestre1']>df['suma_semestre2']),
                   (df['count_semestre1']<df['count_semestre2'])&(df['suma_semestre1']<df['suma_semestre2'])]
    # Definir las decisiones correspondientes para cada condición
    decisiones = ['sano','constante','decreciente','incremental']
    # Usar np.select para crear la nueva columna de decisión
    df['comportamiento_moroso'] = np.select(condiciones, decisiones, default='intermitente')
    print('Distribucion de los comportamiento')
    print(df['comportamiento_moroso'].value_counts(dropna=False))
    df = pd.get_dummies(df, columns=['comportamiento_moroso'], dtype=int)
    print('-'*120)
    print('Dimension base final: ',df.shape)
    print('Clientes duplicados: ', df[df.duplicated(subset=['nit'])].shape[0])
    
    time2 = datetime.now()
    print('Tiempo de ejecución: ', time2 - time1)
    return df

# Funcion para calcular el comportamiento de pago
def process_comportamiento_pago():
    print('INICIO PROCESS')
    print('='*120)
    time1 = datetime.now()
    
    # Ruta archivo
    ruta_archivos = "C:/Users/Aleja/OneDrive/Escritorio/Icesi/I Semestre/Gestión estrategica/AlmanaConsultory/AlmanaConsultory/Información/pagos/"
    
    # Archivo a cargar
    dirs = os.listdir(ruta_archivos) # Listado de archivos en una carpeta
    dirs = dirs[:1] # Filtrando solo para los ultimos 12 meses
    dirs = [ruta_archivos + x for x in dirs]
    print('Archivo a cargar:',dirs)
    print('-'*120)
    
    # Cargando archivo
    df = pd.read_csv(dirs[-1], sep=';', dtype={'Tercero movto.':str})
    print('Dimension base inicial: ',df.shape)
    print('-'*120)
    
    # Limpiando archivo
    df = df[['Tercero movto.','Fecha','Fecha vcto. sa.']]
    df['Fecha'] = pd.to_datetime(df['Fecha'], format="%d/%m/%Y") 
    df['Fecha vcto. sa.'] = pd.to_datetime(df['Fecha vcto. sa.'], format="%d/%m/%Y")
    
    # Creando variable de interes
    condiciones = [((df['Fecha'] - df['Fecha vcto. sa.']).dt.days)<0,
                ((df['Fecha'] - df['Fecha vcto. sa.']).dt.days)==0,
                (((df['Fecha'] - df['Fecha vcto. sa.']).dt.days)>0)&(((df['Fecha'] - df['Fecha vcto. sa.']).dt.days)<=5),
                ((df['Fecha'] - df['Fecha vcto. sa.']).dt.days)>5]
    # Definir las decisiones correspondientes para cada condición
    decisiones = ['pronto_pago','dia_pago','olvido_pago','moroso_pago']
    # Usar np.select para crear la nueva columna de decisión
    df['comportamiento'] = np.select(condiciones, decisiones, default='revisar')
    df['conteo'] = 1
    
    # pivot table
    df_pivot = pd.pivot_table(df, values='conteo', index=['Tercero movto.'],columns=['comportamiento'], aggfunc="count").reset_index()
    df_pivot.fillna(0,inplace=True)
    df_pivot.rename(columns={'Tercero movto.':'nit'}, inplace=True)
    df_pivot['comportamiento_pago'] = df_pivot.iloc[:, 1:].idxmax(axis=1)
    print('Dimension base pivoteada',df_pivot.shape)
    print('-'*120)
    print(df_pivot['comportamiento_pago'].value_counts(dropna=False))
    df_pivot = pd.get_dummies(df_pivot, columns=['comportamiento_pago'], dtype=int)
    print('-'*120)
    
    time2 = datetime.now()
    print('Tiempo de ejecución: ', time2 - time1)
    return df_pivot