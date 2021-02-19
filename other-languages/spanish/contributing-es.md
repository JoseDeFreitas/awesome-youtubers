# Guía para contribuidores

Por favor, lee el [código de conducta](../../code-of-conduct.md).

Añade solo YouTubers que sean **increíbles**. *"Después de todo, se trata de calidad, no de cantidad"*. [¿Qué es increíble?](https://github.com/sindresorhus/awesome/blob/main/awesome.md#only-awesome-is-awesome)

<details>
  <summary>Guía para usuarios nuevos en GitHub</summary>
  <ol>
    <li>Ve al archivo <a href="https://github.com/JoseDeFreitas/awesome-youtubers/blob/main/readme.md">readme.md</a> en este repositorio.</li>
    <li>Haz click en el botón "edit" (el que tiene un ícono de un lapiz).</li>
    <li>Añade al nuevo YouTuber (siguiendo el formato especificado abajo y de último en la sección correspondiente) y haz click en "Commit".</li>
    <li>Haz click en el botón verde "Create pull request", llena la plantilla y haz click de nuevo en el botón verde "Create pull request".</li>
    <p>Eso es todo... ¡qué fácil!</p>
  </ol>
</details>

## Añade al YouTuber siguiendo este formato

```html
[<img align="left" height="94px" width="94px" alt="Avatar del canal" src="LINK_AL_AVATAR_DEL_CANAL"/>](LINK_A_LA_PÁGINA_PRINCIPAL_DEL_CANAL)

[**NOMBRE_DEL_CANAL**](LINK_A_LA_PÁGINA_PRINCIPAL_DEL_CANAL) [<img height="16px" width="16px" alt="Badge for verified YouTube channels" src="../../media/badge-verified.svg" title="Es un canal de YouTube verificado"/>](../../badges.md#verified-youtube-channel) [<img height="16px" width="16px" alt="Badge for youtubers that upload videos weekly" src="../../media/badge-weekly.svg" title="Sube videos semanales"/>](../../badges.md#weekly-video-upload) \
Contenido sobre: EJEMPLO, EJEMPLO, EJEMPLO \
Playlists destacadas: `LISTA DE REPRODUCCIÓN 1`, `LISTA DE REPRODUCCIÓN 2`, `LISTA DE REPRODUCCIÓN 3`, `LISTA DE REPRODUCCIÓN 4`. \
<br/>
```

<details>
  <summary>Ejemplo:</summary>

[<img align="left" height="94px" width="94px" alt="Avatar del canal GitHub" src="https://yt3.ggpht.com/a/AATXAJzVBGU-QyENevFp8etYX1iEak8Y7KEjUPsucWAvAA=s100-c-k-c0xffffffff-no-rj-mo"/>](https://www.youtube.com/user/github)

[**GitHub**](https://www.youtube.com/user/github) [<img height="16px" width="16px" alt="Badge for youtubers that upload videos weekly" src="../../media/badge-weekly.svg" title="Uploads videos weekly"/>](../../badges.md#weekly-video-upload) \
Contenido sobre: Código abierto, Seguridad, Desarrollo de aplicaciones \
Playlists destacadas: `Open Source Friday`, `GitHub Satellite 2020 - Work`, `Public Roadmap`, `GitHub Artic Code Vault`.
</details>

**Edita solo las palabras que están en MAYÚSCULAS. No modifiques las otras cosas. Abajo están las consideraciones.**

- En el ejemplo puedes ver que el YouTuber tiene dos insignias (la insignia de canal verificado y la de subir un video semanal). Si el canal no cumple con alguno de estos requisitos, remueve la insignia. Más información en el archivo [badges.md](../../badges.md).
- Si la sección "Playlists destacadas" tiene menos de 124 caracteres, añade un símbolo `\` y una etiqueta `<br/>` en la línea de abajo. Si no es el caso, no lo hagas.
- Presta atención a los demás símbolos: puntos, comas, asteriscos, etc. Algunos de ellos son usados por el [awesome YouTubers linter](../../linter/).
- Antes de abrir la pull request asegúrate de que la disposición se ve bien.

## Crea la pull request siguiendo este formato

*Aparece automáticamente cuando creas la pull request.*

```markdown
- **Nombre del YouTuber:**
- **¿De qué trata el canal? (ej: desarrollo web, diseño, ...)**:
- **¿En cuál sección está el canal? (si creaste una sección, por favor especifica el porqué)**:
- **¿Por qué consideras que el YouTuber se merece un puesto en esta lista? *¿Qué lo hace increíble?***:
```

<details>
  <summary>Ejemplo:</summary>

- **Nombre del YouTuber**: GitHub
- **¿De qué trata el canal? (ej: desarrollo web, diseño, ...)**: Plataforma de desarrollo de software para guardar repositorios.
- **¿En cuál sección está el canal? (si creaste una sección, por favor especifica el porqué)**: Código abierto.
- **¿Por qué consideras que el YouTuber se merece un puesto en esta lista? *¿Qué lo hace increíble?***: El YouTuber sube videos cada día con tutoriales generales de tecnología. Estos tutoriales incluyen: asegurando tu organización, encontrando vulnerabilidades, usando GitHub actions y demás. También tiene geniales listas de reproducción en donde puedes encontrar charlas de profesionales que te enseñan sobre diferentes tópicos.
</details>
