# Full-Featured-Web-App-Django
## 📧 Configuración de Gmail para envío de emails en Django
### 1. Requisitos
- Tener una cuenta de Gmail.

- Tener activada la verificación en dos pasos (2FA) en esa cuenta.

### 2. Generar una contraseña de aplicación
- Ir a https://myaccount.google.com/security

- En la sección "Acceso a Google", activar Verificación en dos pasos si aún no está activada.

- Luego, entrar a https://myaccount.google.com/apppasswords

- Iniciar sesión si se solicita.

- En Seleccionar aplicación, elegir: Correo.

- En Seleccionar dispositivo, elegir: Otro, y nombrar (por ejemplo Django App).

- Hacer clic en Generar.

- Google mostrará una contraseña de 16 caracteres. Copiarla.

⚠️ Solo se puede ver la contraseña una vez. Si la perdés, deberás generar otra nueva.

### 3. Usar la contraseña en Django
Agregar las siguientes variables a tu archivo .env o a tu configuración:
```bash
EMAIL_USER=tu_correo@gmail.com
EMAIL_HOST_PASSWORD=la_contraseña_de_aplicación_generada
```

## 🔐 Cómo generar la `SECRET_KEY`
### ✅ ¿Cómo generar una nueva SECRET_KEY?
Opción recomendada (desde consola):
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 🗝️ Guardarla en tu .env:
```.env
SECRET_KEY=k+v$3z!61x)v6&$51w4bka=ap=ge9!7m(2j!8pzj*zwhz1r&$q
```
## Créditos
- https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
