import hashlib
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


class Privacidad:
    def __init__(self):
        pass

    def _obtener_salt(self):
        # Obtener el salt del archivo .env
        salt = os.environ.get("SALT")
        if salt is None:
            raise ValueError("No se encontró la variable de entorno 'SALT' en el archivo .env")
        return salt.encode()
    
    def generar_clave(self):
        # Generar una clave simétrica utilizando Fernet
        return Fernet.generate_key()
    
    def generar_par_claves(self):
        # Generar una clave privada
        clave_privada = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        # Generar la clave pública correspondiente
        clave_publica = clave_privada.public_key()
        return clave_publica, clave_privada

    def cifrar_nombre_asimetrico(self, nombre, clave_publica):
        nombre_codificado = nombre.encode()
        nombre_cifrado = clave_publica.encrypt(
            nombre_codificado,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return nombre_cifrado

    def descifrar_nombre_asimetrico(self, nombre_cifrado, clave_privada):
        nombre_descifrado = clave_privada.decrypt(
            nombre_cifrado,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return nombre_descifrado.decode()

    def cifrar_nombre(self, nombre, clave):
        # Crear una instancia de Fernet con la clave proporcionada
        f = Fernet(clave)
        # Codificar el nombre y cifrarlo
        nombre_codificado = nombre.encode()
        nombre_cifrado = f.encrypt(nombre_codificado)
        return nombre_cifrado

    def descifrar_nombre(self, nombre_cifrado, clave):
        # Crear una instancia de Fernet con la clave proporcionada
        f = Fernet(clave)
        # Descifrar y decodificar el nombre
        nombre_descifrado = f.decrypt(nombre_cifrado)
        nombre_original = nombre_descifrado.decode()
        return nombre_original
    
    def generar_salt(self, longitud=16):
        # Retorna un salt aleatorio con la longitud especificada
        return os.urandom(longitud)
    
    def hash_nombre_apellido(self, nombre, apellido):
        # Concatenar nombre y apellido
        nombre_completo = nombre + " " + apellido
        # Codificar el nombre completo para prepararlo para el hashing
        nombre_completo_codificado = nombre_completo.encode()
        # Crear el hash usando SHA-256
        hash_objeto = hashlib.sha256(nombre_completo_codificado)
        # Obtener el valor hash hexadecimal
        hash_hex = hash_objeto.hexdigest()
        return hash_hex
    
    def hash_md5nombre_apellido(self, nombre, apellido):
        # Concatenar nombre y apellido
        nombre_completo = nombre + " " + apellido
        # Codificar el nombre completo para prepararlo para el hashing
        nombre_completo_codificado = nombre_completo.encode()
        # md5
        hash_objeto_md5 = hashlib.md5(nombre_completo_codificado)
        # Obtener el valor hash hexadecimal
        hash_hex = hash_objeto_md5.hexdigest()
        return hash_hex
    
    
    def hash_con_salt(self, nombre, apellido):
        nombre_completo = nombre + " " + apellido
        nombre_completo_codificado = nombre_completo.encode()
        salt = self.generar_salt()
        entrada_con_salt = nombre_completo_codificado + salt
        hash_objeto = hashlib.sha256(entrada_con_salt)
        hash_hex = hash_objeto.hexdigest()
        return hash_hex
    

    
anonimizador_cifrador = Privacidad()

nombre_anonimizado_sha256 = anonimizador_cifrador.hash_nombre_apellido("Carlos", "Garcia")
nombre_anonimizado_md5 = anonimizador_cifrador.hash_md5nombre_apellido("Carlos", "Garcia")
nombre_anonimizado_con_salt = anonimizador_cifrador.hash_con_salt("Carlos", "Garcia")

print("Nombre anonimizado con SHA-256:", nombre_anonimizado_sha256)
print("Nombre anonimizado con MD5:", nombre_anonimizado_md5)
print("Nombre anonimizado con salt:", nombre_anonimizado_con_salt)

# Generar clave Fernet
clave_fernet = anonimizador_cifrador.generar_clave()

# Cifrar y descifrar un nombre con Fernet
nombre_original = "Carlos Garcia"
nombre_cifrado = anonimizador_cifrador.cifrar_nombre(nombre_original, clave_fernet)
nombre_descifrado = anonimizador_cifrador.descifrar_nombre(nombre_cifrado, clave_fernet)

print("Nombre Original:", nombre_original)
print("Nombre Cifrado:", nombre_cifrado)
print("Nombre Descifrado:", nombre_descifrado)

# Generar par de claves RSA
clave_publica, clave_privada = anonimizador_cifrador.generar_par_claves()

# Cifrar y descifrar un nombre con RSA
nombre_original = "Carlos Garcia"
nombre_cifrado = anonimizador_cifrador.cifrar_nombre_asimetrico(nombre_original, clave_publica)
nombre_descifrado = anonimizador_cifrador.descifrar_nombre_asimetrico(nombre_cifrado, clave_privada)

print("Nombre Original:", nombre_original)
print("Nombre Cifrado:", nombre_cifrado)
print("Nombre Descifrado:", nombre_descifrado)


