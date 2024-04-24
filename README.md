# INSURANCE COMPANY
Una compañía de seguros tiene sistemas de administración de pólizas heredados y plataformas de análisis independientes para la ciencia de datos. La replicación de datos en entornos de análisis es manual. Esto da como resultado análisis limitados a instantáneas obsoletas. Los cambios en los precios de las políticas tardan demasiado en reflejar las nuevas tendencias. Y los problemas de calidad de los datos son comunes.
La falta de acceso a datos en tiempo real restringe gravemente la capacidad de la aseguradora para detectar fraude, ajustar los modelos de riesgo y optimizar las experiencias de los clientes. Por ejemplo, el análisis de reclamaciones se limita a lotes mensuales en lugar de aprovechar la información actualizada al minuto. El equipo de fijación de precios tampoco puede ajustar las tarifas rápidamente en función de los patrones de pérdidas emergentes. La empresa necesita una arquitectura mejorada para ofrecer acceso unificado a datos tanto para transacciones como para análisis.
La solución implica crear microservicios orientados a capacidades de seguros, como administración de pólizas y procesamiento de reclamos. Estos proporcionan API en tiempo real para datos de pólizas/reclamaciones protegidos por una puerta de enlace. Un lago de datos en la nube consume estos datos para realizar análisis avanzados. Este enfoque descompone los sistemas existentes a lo largo del tiempo en servicios enfocados y desacoplados que brindan acceso a datos en tiempo real a través de API bien definidas. Hay algunas especificaciones:
▪ Desarrollar microservicios para administración de pólizas, cálculo de precios, gestión de reclamos.
▪ Exponer datos de pólizas y reclamos a través de API en tiempo real detrás de una puerta de enlace.
▪ Ingerir datos de API en un lago de datos en la nube para realizar análisis.
▪ Aplicar aprendizaje automático e IA a los datos consolidados.

## Gestión de Cotización Microservicio
El Microservicio de Gestión de Cotizaciones es una parte esencial dentro de la arquitectura mejorada propuesta para la compañía de seguros. Este servicio está diseñado para agilizar y automatizar el proceso de generación de cotizaciones de seguros, ofreciendo una solución eficiente y precisa tanto para los clientes como para el equipo interno.
### Introducción

#### Funcionalidades Principales:
1. **Generación de Cotizaciones:**
El microservicio facilita la generación de cotizaciones de seguros basadas en la información proporcionada por el cliente. Utilizando algoritmos avanzados, calcula primas de seguro precisas y adaptables a los parámetros ingresados, asegurando una estimación acorde a las necesidades y circunstancias individuales.

2. **Validación de Información:**
Para garantizar la exactitud de las cotizaciones, el sistema valida la información del cliente y la política, asegurando que se generen cotizaciones precisas y confiables. Esta validación se realiza en tiempo real, evitando errores y garantizando una experiencia sin contratiempos para el usuario.

#### Tecnologías y Herramientas:
**Lenguaje de Programación:**
El microservicio está desarrollado en Python, un lenguaje de programación versátil y ampliamente utilizado en el ámbito de la ciencia de datos y el desarrollo de aplicaciones web.

**Frameworks:**
Se utiliza FastAPI, un moderno y rápido framework de Python para la creación de APIs web. FastAPI ofrece un rendimiento excepcional y una documentación automática interactiva, lo que facilita el desarrollo y la depuración de APIs.

**Base de Datos:**
Para almacenar las cotizaciones generadas y la información relacionada, se emplea MongoDB Atlas, una base de datos NoSQL en la nube altamente escalable y flexible. MongoDB Atlas proporciona un entorno seguro y eficiente para la gestión de datos, permitiendo un almacenamiento y recuperación rápidos y confiables.

#### API:
El microservicio expone endpoints a través de una API, permitiendo la integración con otros sistemas y facilitando el acceso a las funcionalidades de generación de cotizaciones de manera programática.

- **Endpoint para Generar Cotizaciones**: Permite a los clientes y otros servicios solicitar la generación de cotizaciones de seguros.

Con el Microservicio de Gestión de Cotizaciones, la compañía de seguros puede ofrecer un proceso ágil, eficiente y preciso para la generación de cotizaciones de seguros, mejorando significativamente la experiencia del cliente y optimizando las operaciones internas.

### Diagrama de Clases
[![ClassDiagram](https://github.com/ISCODEVUTB/SA-InsuranceCompany_1p24/blob/81aa8431bf97f69a5adda52a8b04b285e6c3eed0/gestion_cotizaciones_microservicio/img/classes.png "ClassDiagram")](https://github.com/ISCODEVUTB/SA-InsuranceCompany_1p24/blob/81aa8431bf97f69a5adda52a8b04b285e6c3eed0/gestion_cotizaciones_microservicio/img/classes.png "ClassDiagram")



