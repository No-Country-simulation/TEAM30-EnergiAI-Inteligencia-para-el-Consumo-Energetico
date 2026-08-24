# Usar OpenJDK 21 como base
FROM eclipse-temurin:21-jdk-alpine

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el JAR generado al contenedor
COPY target/energiai-0.0.1-SNAPSHOT.jar app.jar

# Exponer puerto 8080 (Spring Boot default)
EXPOSE 8080

# Ejecutar la aplicación
ENTRYPOINT ["java", "-jar", "app.jar"]