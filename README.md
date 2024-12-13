# AlmanaConsultory

Este proyecto es parte de  **Proyecto Gestión Estrategica 2024-2** curso de la maestría en Ciencia de Datos, Universidad Icesi, Cali Colombia. 

#### -- Status del Proyecto: [Completed]

#### Miembros:

|Nombre     |  Email   | 
|---------|-----------------|
|[Alejandro Pérez Lugo](https://github.com/AlejoPerez98)(@AlejoPerez98)| 1144102059@u.icesi.edu.co |
|[Nathaly Henao Lugo](https://github.com/Nathalyhl)(@Nathalyhl)| 1143994336@u.icesi.edu.co |
|[Mauricio Guzman](https://github.com/MguzmanA)(@MguzmanA)| Mauroguzman15@gmail.com |


## Contacto
* No dudes en ponerte en contacto con el jefe de equipo o el instructor si tienes alguna pregunta o estás interesado en colaborar.

## Introducción del proyecto/Objetivo
El objetivo de este proyecto es proporcionar herramientas que permitan resolver una problemática clave del negocio. En este caso específico, se busca desarrollar un modelo que reduzca la probabilidad de impago por parte de los clientes del Banco W.

### Partner
This section should be added when there's a partner institution 
* [Universidad Icesi](https://www.icesi.edu.co/)
* [Website for group]()

### Methods Used
* Análisis exploratorio
* Arbol de decisión
* XGBoost
* Creación funciones
* PCA

### Tecnologías
* Python
* Visual Studio Code
* Git Hub 

## Descripción del proyecto

En la gestión de los créditos del área de postventa de una ensambladora de motocicletas y comercializadora de partes y repuestos, se observa un problema creciente relacionado con la cartera del canal tradicional. La empresa atiende a diversos tipos de clientes, desde pequeños comerciantes hasta grandes empresas consolidadas en el mercado del sector de los repuestos. Como requisito inicial para que estos clientes entren a ser parte de este canal se exige un historial de compras al contado que permite evaluar el comportamiento del cliente, posteriormente, se otorga un cupo de crédito que utilizan para realizar sus compras a un plazo por lo general de 30 días.
Cada una de las ventas tiene un plazo de pago y cuando pasa este, sus facturas pasan a cartera vencida, bloqueando automáticamente su capacidad de realizar nuevas compras a crédito y despacho de artículos pendientes. En los últimos meses, la cartera vencida ha tenido un incremento lo cual ha generado un impacto negativo en el flujo de caja de la empresa, deteriorando su liquidez y complicando la operatividad financiera.

Una de las posibles causas, es que el asesor de ventas no alcanza a abarcar la totalidad de clientes para realizar las visitas de cobro de cartera, ya que cada miembro del equipo comercial gestiona entre 100 y 120 clientes, lo que hace esta función cada vez más complicada a través de un seguimiento manual, generando actividades complejas y poco eficientes. Dado lo anterior, desde el área de postventa, se quiere gestionar la implementación de estrategias proactivas para mitigar el riesgo de impago.

Por tanto, el objetivo principal será desarrollar un modelo predictivo que permita identificar, con antelación, los clientes que tienen alta probabilidad de caer en cartera vencida durante el mes siguiente. Esto permitirá automatizar y fortalecer los controles de cartera, optimizar las acciones de recuperación y facilitar la gestión del equipo comercial. De esta manera, se busca no solo reducir la cartera vencida, sino también mejorar la sostenibilidad financiera de la empresa.

### Problema

La gestión de créditos debe ser considerada como una actividad riesgosa y clave en la gestión de fondos dados los efectos en la liquidez y la solvencia de la empresa, por lo tanto, un riesgo en el que se incurre es el riego crediticio, este supone la probabilidad de impago en los compromisos adquiridos por los clientes por falta de liquidez, lo que traerá a la empresa implicaciones sobre su flujo de caja, recuperación de cartera y estabilidad económica. Se requiere de una solución que permita disminuir el riesgo crediticio.

### Objetivo general

Establecer un modelo que permita mejorar la toma de decisiones en la gestión del crédito.

### Objetivos específicos

* Disminuir la colocación de pedidos incobrables.
* Estandarizar el proceso de asignación de créditos a clientes.

## Análisis de causas

* La información de ​cartera  sólo se envía cada 15 días a los asesores.
* La información no le llega a la persona indicada para tramitar el pago.
* Sólo se hace seguimiento a facturas vencidas.​
* El primer cobro recae en el Asesor comercial, el cual no logra llegar a todos sus clientes.​

## Estado del arte

Los modelos de Credit Scoring son herramientas utilizadas por las entidades financieras para evaluar la probabilidad de que un cliente no pague un crédito. Estos modelos analizan variables como el historial crediticio, la situación económica, el comportamiento de pago y datos demográficos. Los métodos más comunes incluyen la regresión logística, árbole, técnicas XGBoost. Estos modelos permiten a las decisiones más informadas sobre a quién otorgar créditos y en qué condiciones.

Algunos de los autores más conocidos en el desarrollo de modelos de Credit Scoring incluyen:
	
#### Modelo de Credit scoring para instituciones de microfinanzas en el marco de Basilea ii

Empresas en general deben tener procesos que permitan medir y gestionar el riesgo de crédito, apoyándose en los principios de Basilea, para los autores la mejor solución es tener un modelo de Credit Scoring que permita medir la probabilidad de impago de los créditos a otorgar, se basan en un modelo de regresión logística binaria, que buscará predecir si el cliente posee solvencia económica para pagar el compromiso adquirido o no tendrá solvencia para el pago.

El modelo selecciona las variables independientes más significativas para explicar el comportamiento crediticio y utiliza la regresión logística binaria, que está intrínsecamente ligada al concepto de odds mediante la transformación logit(log(p/(1-p))). Esta transformación linealiza la relación entre las variables independientes y la probabilidad de impago. Por otro lado, β_0+β_1 x_1+⋯+β_n x_n corresponde a la combinación lineal de las variables independientes, que se utiliza para calcular el logit y, posteriormente, las probabilidades de impago.

La gestión del modelo permite clasificar a los nuevos clientes dada las variables independientes, por último, se destaca la importancia de agregar variables macroeconómicas y características del cliente, para mejorar la precisión de la predicción.

    1. Principios Básicos para una supervisión bancaria eficaz.
    2. Principios de Basilea.

Este artículo tiene como objetivo brindar los lineamientos básicos que se deben seguir los bancos y/o entidades crediticias para reducir la probabilidad de quiebra, se define la importancia del riesgo del crédito como principio número 17, este principio expone en primera medida las reglas del juego de la entidad y/o banco, su apetito por el riesgo, perfil de riesgo, la situación macroeconómica y de los mercados.

Esta definición permitirá identificar, cuantificar, evaluar, vigilar, informar y controlar o mitigar el riesgo de crédito, se hace énfasis en que se tengan los procesos de todo el ciclo de vida del crédito desde su colocación hasta la gestión continua de préstamos e inversiones.

#### Análisis de riesgo crediticio, propuesta del modelo credit scoring

Se muestra la brecha que existe a nivel de información entre los bancos y demás entidades o empresas que brinden un crédito, partiendo del riesgo en que incurren estas entidades al brindar estos créditos, esta brecha de información financiera les permitiría definir:

	Políticas de ventas, inversiones y condiciones de pago.
	Identificar y gestionar el riesgo de incobrables.
	Establecer las acciones que permitan asegurar la recuperación de los fondos invertidos en cuentas por cobrar.

A su vez, se destaca la importancia de que estas entidades posean una metodología de evaluación crediticia, en pro de mejorar la gestión del crédito, minimizando su riesgo. Se diseño un modelo de Credit Scoring para evaluar a cada nuevo crédito a otorgar, para esto se gestionó la una matriz con ponderaciones construida con variables escogidas por expertos en el tema, así se logró estandarizar una matriz que tiene en cuenta tanto variables cuantitativas como cualitativas brindándoles un peso específico.

#### Desarrollo de un score de riesgo financiero con xgboost para evaluación de crédito fintec

Este proyecto desarrolla un modelo de XGBoost para estimar el score de crédito de clientes de una empresa Fintech, utilizando datos sociodemográficos, laborales y de comportamiento financiero. El proceso de entrenamiento incluyó la eliminación de outliers y la reducción de dimensionalidad mediante PCA Robusta, además de optimizar los hiperparámetros mediante simulación Montecarlo para evitar el sobreajuste y mejorar el rendimiento. A pesar de los desafíos relacionados con la calidad de los datos y los sesgos, el modelo predice eficazmente el impago, especialmente en scores bajos.

El modelo propone una solución robusta y adaptable para predecir el comportamiento de pago de clientes a corto, mediano y largo plazo, alineado con las necesidades del sector Fintech. Se utilizó validación cruzada y métricas como la *Matriz de Confusión* y el *Estadístico Kolmogorov-Smirnov (KS)* para asegurar la fiabilidad del modelo, además de considerar la integración de nuevas fuentes de datos y técnicas avanzadas de machine learning para mejorar su precisión.

## Datos

En el presente análisis se busca identificar las variables explicativas del vencimiento de clientes en la cartera, utilizando para ello la creación de variables sintéticas y el análisis de correlación. El objetivo principal es entender los factores que inciden en el incumplimiento de pagos, generando información que permita tomar decisiones estratégicas para la gestión de la cartera.

## Datos Base

Se cuenta con dos bases de datos principales:

	Facturas de ventas: Información relacionada con las transacciones realizadas por los clientes.
	Clientes: Datos demográficos y características específicas de los clientes registrados.

## Creación de Variables Sintéticas

A partir de los datos disponibles, se han diseñado variables sintéticas que explican el comportamiento de pago de los clientes, específicamente relacionadas con el vencimiento. Estas variables son:

	Mora máxima a corte: Número máximo de días de atraso acumulados por el cliente hasta la fecha de corte.
	Valor de facturas a corte: Suma de los valores pendientes de pago hasta la fecha de corte.
	Promedio de facturas a corte: Valor promedio de las facturas registradas hasta la fecha de corte.
	Porcentaje de uso del cupo a corte: Relación entre el monto utilizado y el cupo total asignado al cliente, expresado en porcentaje.
	Mora máxima en 12 meses: Mayor cantidad de días de atraso acumulados por el cliente en el último año.

Estas variables han sido definidas para reflejar comportamientos históricos y actuales que puedan estar vinculados al incumplimiento de los clientes.

#### Cálculo de Variables por Temporalidad

Con el fin de analizar tendencias y patrones en el comportamiento de pago de los clientes, se desarrollaron funciones para calcular las variables mencionadas en cuatro rangos temporales: Un mes, tres meses, seis y doce meses a corte. Este análisis temporal permitirá identificar si los clientes muestran señales de incumplimiento recurrentes.

#### Análisis de Correlación

Para determinar las variables que tienen mayor influencia sobre el vencimiento de clientes, se seleccionaron las variables con una correlación superior al 70%, de aquí salen 16 variables.

De igual forma, se gestiona un arbol de decisión para determinar de estas 16 variables cuáles son las más importantes, el arbol tiene cómo umbrales un promedio de importancia de las variables, de aquí quedan cómo

   1. Valor facturas a corte
	2. Promedio facturas a corte
    3. Porcentaje uso a corte
    4. Mora máxima a 12m

### Modelos

Posteriormente, se implementan modelos de aprendizaje no supervisado, como árboles de clasificación y XGBoost, con el objetivo de clasificar a los clientes según su vencimiento. Para la evaluación de los modelos, se utiliza la curva ROC, lo que permite identificar el punto óptimo y ajustar los valores de los hiperparámetros de manera iterativa.