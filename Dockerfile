# docker build -t facturacion-db ./
# docker run -d --name facturacion-db-container -p 5433:5432 facturacion-db

FROM postgres:10.5
ENV POSTGRES_USER Ac1Q2ksADRSRERJ1vv1ot4WmLlddU8f1
ENV POSTGRES_PASSWORD i2eDhe9cGnQtdmDi30alhcb5Go9YzV9csSHyTGN5tJ6CmXjN7doLl4wvmLOh7X22
ENV POSTGRES_DB db_djfull